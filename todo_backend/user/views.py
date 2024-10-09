from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status,filters
from rest_framework.decorators import api_view,permission_classes
from .models import User,Task
import random
import string
from .serializers import UserSerializer,TaskSerializer
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password,check_password
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import timedelta
from rest_framework import generics,permissions
from .permissions import IsAuthenticatedUser  # Import the custom permission
from rest_framework.permissions import AllowAny

# Create your views here.
class UserViews:

    @staticmethod
    def generate_otp():
        return str(random.randint(100000,999999))

    @api_view(['GET'])
    @permission_classes([IsAuthenticatedUser])
    def getUser(req):
        user = req.user
        user_serializer = UserSerializer(user)
        return Response({"user":user_serializer.data})

    @api_view(['POST'])
    @permission_classes([AllowAny])
    def signup(req):
        require_fields = ['first_name','last_name','email','password']

        if not all(field in req.data for field in require_fields):
            return Response({"error":"first name, last name, email, password are required"},
                            status=status.HTTP_400_BAD_REQUEST)
        data = req.data
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        password = data.get('password')

        if User.objects.filter(email=email).exists():
            return Response({"error": "Email already exists"}, status=status.HTTP_400_BAD_REQUEST)
        user = User(
            email=email,
            password=make_password(password),
            first_name=first_name,
            last_name=last_name
            )
        # token_value = ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))
        # user.token_value = token_value
        user.save()

        otp  = UserViews.generate_otp()
        user.otp = otp
        user.save()
        
         # Send the OTP to the user's email
        send_mail(
            'OTP Verification',
            f'Your OTP for registration is: {otp}',
            'tandon.aryaman123@gmail.com',  # Replace with your sender email
            [email],  # Use the user's provided email
            fail_silently=False,
        )

     # Generate JWT token
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        serialized_user = UserSerializer(user)

        response =  Response({"user": serialized_user.data, "message": "User created check your email for user verification"}, status= status.HTTP_201_CREATED)

        access_token_expiry = timedelta(minutes=5)
        refresh_token_expiry = timedelta(days = 15)

        response.set_cookie(
            key='access_token',
            value=access_token,
            httponly=True,                # Prevents JavaScript access to the cookie
            expires=access_token_expiry,
            secure=True,       # Use True in production if using HTTPS
            samesite='Lax',         # It can be ('Lax', 'None', or 'Strict')
        )
        response.set_cookie(
        key='refresh_token',
        value=str(refresh),
        httponly=True,
        expires=refresh_token_expiry,
        secure=True,
        samesite='Lax'
        )
        return response
    
    def email_is_verified(self):
        return self.is_email_verified
    

    @api_view(['POST'])
    def login(req):
        if "email" not in req.data or "password" not in req.data:
            return Response({"error": "Email & Password are required"}, status=status.HTTP_400_BAD_REQUEST)

        email = req.data["email"]
        password = req.data["password"]

        try:
            user = User.objects.get(email=email)

            # Check if the password is correct
            if not check_password(password,user.password):
                return Response({"error": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)

            # Check if the email is verified
            if not user.is_email_verified:
                return Response({"error": "Please verify your email before logging in."}, status=status.HTTP_403_FORBIDDEN)

            # Serialize the user data
            user_serializer = UserSerializer(user)

            # Generate access and refresh tokens
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            # Create the response object
            response = Response({
                "user": user_serializer.data,
                "message": "Logged in successfully",
            }, status=status.HTTP_200_OK)

            # Define token expiry times
            access_token_expiry = timedelta(minutes=15)
            refresh_token_expiry = timedelta(days=15)

            # Set cookies for access and refresh tokens
            response.set_cookie(
                key='access_token',
                value=access_token,
                httponly=True,                # Prevents JavaScript access to the cookie
                expires=access_token_expiry,
                secure=True,                   # Use True in production if using HTTPS
                samesite='Lax',                # It can be ('Lax', 'None', or 'Strict')
            )
            response.set_cookie(
                key='refresh_token',
                value=str(refresh),
                httponly=True,
                expires=refresh_token_expiry,
                secure=True,
                samesite='Lax'
            )

            return response

        except User.DoesNotExist:
            return Response({"error": "Invalid email or password"}, status=status.  HTTP_401_UNAUTHORIZED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @api_view(['POST'])
    def verify_otp(request):
        # Validate input data
        email = request.data.get("email")
        otp = request.data.get("otp")
    
        if not email or not otp:
            return Response({"error": "email and otp are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Get user by email
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error": "email does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        # Check if OTP is valid
        if otp != user.otp:
            return Response({"error": "otp is wrong"}, status=status.HTTP_400_BAD_REQUEST)

        # Mark email as verified and save user
        user.is_email_verified = True
        user.save()

        # Serialize and return user data
        user_serializer = UserSerializer(user)
        return Response({"user": user_serializer.data}, status=status.HTTP_200_OK)





class TaskViews:

    @api_view(['POST'])
    @permission_classes([IsAuthenticatedUser])
    def createTask(req):
        data = req.data
        # user_id = data.get('user_id')
        content = data.get('content')

        # if not user_id or not content:
        #     return Response({"error":"user_id and content are required"},status = status.HTTP_400_BAD_REQUEST)

        user = req.user
        
        task = Task(user = user,content=content)
        task.save()

        task_serializer = TaskSerializer(task)
        return Response({"task":task_serializer.data, "message":"Task created successfully"},status=status.HTTP_201_CREATED)

    @api_view(['PUT','PATCH'])
    def updateTask(req,task_id):   
        data = req.data
        content = data.get('content')
        is_complete = data.get('is_completed')

        try:
            task = Task.objects.get(id = task_id)
        except Task.DoesNotExist:
            return Response({"error":"Task does not exist"},status=status.HTTP_404_NOT_FOUND)

        if content:
            task.content = content
        if is_complete is not None:
            task.is_completed = is_complete
        task.save()

        task_serializer = TaskSerializer(task)
        return Response({"message":"Task updated successfully", "task":task_serializer.data},status=status.HTTP_200_OK)
    
    @api_view(['DELETE'])
    def deleteTask(req,task_id):
        try:
            task = Task.objects.get(id = task_id)
            task.delete()
            return Response({"message": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Task.DoesNotExist:
            return Response({"error":"Task does not exist"},status = status.HTTP_404_NOT_FOUND)

    @api_view(['GET'])
    def getTasks(req,user_id):
        try:
            user = User.objects.get(id = user_id)
            tasks = Task.objects.filter(user = user)     

            if not tasks:
                return Response({"message": "No tasks found for this user."}, status=status.HTTP_404_NOT_FOUND)

            task_serializer = TaskSerializer(tasks,many=True)
            return Response({"tasks": task_serializer.data}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)

# Generics from DRF
# class UserCreateView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permession_classes = [permissions.AllowAny]

        

