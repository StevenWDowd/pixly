import React from "react";
import { NavLink, Link } from "react-router-dom";
import "./NavBar.css"

function NavBar() {
  return (
    <nav className="NavBar">
      <NavLink className="NavBar-link" to="/add">Add a photo</NavLink>
      <NavLink className="NavBar-link" to="/photos">All photos</NavLink>
    </nav>
  );
}

export default NavBar;