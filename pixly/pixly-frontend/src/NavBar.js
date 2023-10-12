import React from "react";
import { NavLink, Link } from "react-router-dom";

function NavBar(){
  return(
    <nav>
      <NavLink to="/">Add a photo</NavLink>
      <NavLink>All photos</NavLink>
    </nav>
  )
}

export default NavBar