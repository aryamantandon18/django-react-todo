import { Button } from "../ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "../ui/card"
import { Input } from "../ui/input"
import { Separator } from "../ui/separator"
import { FaGithub } from "react-icons/fa"
import {FcGoogle} from "react-icons/fc"
import { useState } from "react"
import { useAuth } from "@/context/context"

export const LoginInCard =({setState})=>{
    const [email,setEmail] = useState("");
    const [password,setPassword] = useState("");
    const [pending,setPending] = useState(false);

    const handleSignIn = (provider) => {
        // console.log(`Signing in with ${provider}`); 
        setPending(true);
        // signIn(provider).finally(()=>{
        //     setPending(false);
        // })
      }
    
    return(
        <Card className="w-full h-full p-8">
            <CardHeader className="px-0 pt-0">
                <CardTitle className="text-2xl">Login to Continue</CardTitle>
                <CardDescription>
                Use you email or another service to continue
            </CardDescription> 
            </CardHeader>
            
            <CardContent className="space-y-5 px-0 pb-0">
            <form className="space-y-2.5">
                <Input
                disabled={pending}
                value={email}
                onChange={(e)=>{setEmail(e.target.value)}}
                placeholder="Email"
                type="email"
                required
                />
                <Input
                disabled={pending}
                value={password}
                onChange={(e)=>{setPassword(e.target.value)}}
                placeholder="Password"
                type="password"
                required
                />
                <Button type="submit" className="w-full" size="lg" disabled={pending}>
                    Continue
                </Button>
            </form> 
            <Separator/>
            <div className="flex flex-col gap-y-2.5">
                <Button
                onClick={()=>handleSignIn("google")}
                variant="outline"
                className="w-full relative"
                size="lg"
                >
                    <FcGoogle className="size-5 absolute top-2.5 left-2.5" /> 
                    Continue with Google 
                </Button>
                <Button
                onClick={()=>handleSignIn("github")}
                variant="outline"
                className="w-full relative"
                size="lg"
                >
                    <FaGithub className="size-5 absolute top-2.5 left-2.5" /> 
                    Continue with Github 
                </Button>
            </div>
            <p className="text-xs text-muted-foreground">
                Don't have an account? <span className="text-sky-700 hover:underline cursor-pointer" onClick={() => setState("SignUp")}>Sign Up</span>
            </p>
            </CardContent>
            
        </Card>
    )
}