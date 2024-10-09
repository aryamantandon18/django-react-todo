import React, { useCallback, useState } from 'react'
import { MdAccountCircle } from "react-icons/md"
import MenuLink from './MenuLink';

const UserOptions = ({userId}) => {
    const [isOpen, setIsOpen] = useState(false);

    const toggleOpen = useCallback(()=>{
        setIsOpen((value)=> !value)
    },[]);
    const submitLogout = async()=>{
        // router.push('/');
    }

  return (
    <div className="py-1 relative inline-block rounded-full border border-gray-200 px-4 hover:shadow-slate-700 shadow">
    <button className="flex items-center gap-2" onClick={toggleOpen}>
    <svg fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className=" w-6 h-6 lg:w-7 lg:h-7">
            <path strokeLinecap="round" strokeLinejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
        </svg>

        <MdAccountCircle className="text-5xl hidden lg:block"/>
    </button>    
    {isOpen && (
        <div className="w-[180px] md:w-[220px] absolute top-[63px] right-0 bg-white border rounded-xl shadow-md flex flex-col cursor-pointer">
            {userId ? (
                <>
                    <MenuLink
                        label='Inbox'
                        onClick={() => {
                            setIsOpen(false);
                            // router.push('/inbox');
                        }}
                    />

                    <MenuLink
                        label='My properties'
                        onClick={() => {
                            setIsOpen(false);
                            // router.push('/myproperties');
                        }}
                    />

                    <MenuLink
                        label='My favorites'
                        onClick={() => {
                            setIsOpen(false);
                            // router.push('/myfavorites');
                        }}
                    />

                    <MenuLink
                        label='My reservations'
                        onClick={() => {
                            setIsOpen(false);
                            // router.push('/myreservations');
                        }}
                    />
                    <MenuLink
                    label="Airbnb your property"
                    onClick={()=>{
                        setIsOpen(false);
                    }}
                    />

                    <MenuLink 
                    label="Log out"
                    onClick={submitLogout}
                    />
                </>
            ) : (
                <>
                    <MenuLink 
                        label='Log in'
                        onClick={() => {
                            toggleOpen
                            // loginModal.open();
                        }}
                    />

                    <MenuLink 
                        label='Sign up'
                        onClick={() => {
                            toggleOpen
                            // signupModal.open();
                        }}
                    />
                </>
            )}
        </div>
    )}
   
</div>
  )
}

export default UserOptions