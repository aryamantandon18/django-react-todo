import { Button } from "../ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "../ui/card"
import { Input } from "../ui/input"
import { Separator } from "../ui/separator"
import { FaGithub } from "react-icons/fa"
import {FcGoogle} from "react-icons/fc"
import { useEffect, useState } from "react"
import { useAuth } from "@/context/context"
import axios from "axios"
import { server } from "@/main"
import Cookies from 'js-cookie';

export const SignUpCard =({setState})=>{
    const [email,setEmail] = useState("");
    const [password,setPassword] = useState("");
    const [confirmPassword,setConfirmPassword] = useState("");
    const [firstName,setFirstName] = useState("");
    const [lastName,setLastName] = useState("");
 
    const submitHandler = async(e)=>{
        e.preventDefault();
        const {data} = await axios.post(`${server}/api/signup/`,{first_name:firstName,last_name:lastName,email,password},{
            withCredentials:true,
            headers: {
                Authorization: Cookies.get('access_token'), // Set the Bearer token from the cookie
            },
    
        });
        console.log("Line 17 ", data);
    }
    useEffect(()=>{
        axios.get(`${server}/api/getUser/`,{
            withCredentials:true,
            headers:{
                'Content-Type' : 'application/json',
                'Authorization': 'Bearer' + Cookies.get('access_token')
            }
        })
        .then((res) => console.log(res))
        .catch((e) => console.log("Error:", e));
     }, []);

    return(
        <Card className="w-full h-full p-8">
            <CardHeader className="px-0 pt-0">
                <CardTitle className="text-2xl">Sign Up to Continue</CardTitle>
                <CardDescription>
                Use you email or another service to continue
            </CardDescription> 
            </CardHeader>
            
            <CardContent className="space-y-5 px-0 pb-0">
            <form className="space-y-2.5" onSubmit={submitHandler}>
                <div className="flex space-x-0.5">
                <Input
                className="flex-1"
                disabled={false}
                value={firstName}
                onChange={(e)=>setFirstName(e.target.value)}
                placeholder="First Name"
                type="text"
                required
                />
                <Input
                className="flex-1"
                disabled={false}
                value={lastName}
                onChange={(e)=>setLastName(e.target.value)}
                placeholder="Last Name"
                type="text"
                required
                />                    

                </div>

                <Input
                disabled={false}
                value={email}
                onChange={(e)=>setEmail(e.target.value) }
                placeholder="Email"
                type="email"
                required
                />
                <Input
                disabled={false}
                value={password}
                onChange={(e)=>{setPassword(e.target.value)}}
                placeholder="Password"
                type="password"
                required
                />
                 <Input
                disabled={false}
                value={confirmPassword}
                onChange={(e)=>{setConfirmPassword(e.target.value)}}
                placeholder="Confirm Password"
                type="password"
                required
                />
                <Button type="submit" className="w-full" size="lg" disabled={false}>
                    Continue
                </Button>
            </form> 
            <Separator/>
            <div className="flex flex-col gap-y-2.5">
                <Button
                onClick={()=>{}}
                variant="outline"
                className="w-full relative"
                size="lg"
                >
                    <FcGoogle className="size-5 absolute top-2.5 left-2.5" /> 
                    Continue with Google 
                </Button>
                <Button
                onClick={()=>{}}
                variant="outline"
                className="w-full relative"
                size="lg"
                >
                    <FaGithub className="size-5 absolute top-2.5 left-2.5" /> 
                    Continue with Github 
                </Button>
            </div>
            <p className="text-xs text-muted-foreground">
                Already have an account? <span className="text-sky-700 hover:underline cursor-pointer" onClick={() => setState("Login")}>Login In</span>
            </p>
            </CardContent>
            
        </Card>
    )
}