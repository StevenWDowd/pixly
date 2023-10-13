import React from "react";
import { NavLink } from "react-router-dom";
import "./NavBar.css";

/** Renders a Nav bar.
 *  Props: none
 *  State: none
 *
 *  App -> NavBar
 */
function NavBar() {
  return (
    <nav className="NavBar">
      <NavLink className="NavBar-link" to="/add">Add a photo</NavLink>
      <NavLink className="NavBar-link" to="/photos">All photos</NavLink>
    </nav>
  );
}

export default NavBar;