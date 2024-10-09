from django.db import models

# User model
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Consider using Django's authentication system for password management
    date_joined = models.DateTimeField(auto_now_add=True)
    # token_value = models.CharField(max_length=1000, null=True)
    otp = models.CharField(max_length=6, null=True, blank=True)
    is_email_verified = models.BooleanField(default=False)
    image = models.ImageField(upload_to='static/profile_images/', blank=True, null=True) 

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Task model
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    content = models.TextField()  # Task description or content
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Task for {self.user.first_name} - {'Completed' if self.is_completed else 'Incomplete'} - Body - {self.content[0:50]}"
