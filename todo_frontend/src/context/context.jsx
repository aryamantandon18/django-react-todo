import { createContext,useContext,useState } from "react";

export const MyContext = createContext();

export const MyProvider = ({children})=>{
  const [isAuthenticated,setIsAuthenticated] = useState();
  const [user,setUser] = useState();

  return(
    <MyContext.Provider value={{isAuthenticated,setIsAuthenticated,user,setUser}}>
      {children}
    </MyContext.Provider>
  )
};

// Custom hook to access the context easily
export const useAuth = () => {
    return useContext(MyContext);
  };