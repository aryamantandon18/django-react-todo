import React from 'react'

const MenuLink = ({label,onClick}) => {
    return (
        <div className="px-5 py-4 cursor-pointer hover:bg-gray-100 transition" onClick={onClick}>
            {label}
        </div>
    )
}

export default MenuLink