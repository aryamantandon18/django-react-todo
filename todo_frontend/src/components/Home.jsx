import React, { useEffect, useState } from 'react'
import { useAuth } from '../context/context'
import axios from 'axios'
import { server } from '../main';
import { LoginInCard } from './user/Login';
import { SignUpCard } from './user/Signup';

const Home = () => {
  const {isAuthenticated,user} = useAuth();
  const [state,setState] = useState("Login");

  useEffect(()=>{
    console.log("Line 8")
    const {data} = axios.get(`${server}/getUser`)
    console.log("Line 9",data);
  },[])
  
  return (
    <div>
      {isAuthenticated ? (
        <div>
          {/* Render something when the user is authenticated */}
          <p>Welcome back!</p>
        </div>
      ) : (
          <div className="h-[760px] flex items-center justify-center bg-[#5C3B58]">
          <div className="md:h-auto md:w-[420px]">
          {state === "Login" ? <LoginInCard setState={setState}/> : <SignUpCard setState={setState}/>}
          </div>
        </div>
      )}
    </div>
  );

}

export default Home