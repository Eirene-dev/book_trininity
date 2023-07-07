import * as React from "react";
import { Menu, MenuButton, MenuList, MenuItem, Button } from "@chakra-ui/react";
import { useNavigate } from "react-router-dom";

function MenuBar() {
  const navigate = useNavigate();

  const handleMenuClick = (path) => {
    navigate(path); 
  };

  return (
    <Menu>
      <MenuButton as={Button}>Menu</MenuButton>
      <MenuList>
        <MenuItem onClick={() => handleMenuClick("/")}>Home</MenuItem>
        <MenuItem onClick={() => handleMenuClick("/chat")}>Chat</MenuItem>
        <MenuItem onClick={() => handleMenuClick("/finetuning")}>Fine-tuning</MenuItem>
        <MenuItem onClick={() => handleMenuClick("/settings")}>Settings</MenuItem>
      </MenuList>
    </Menu>
  );
}

export default MenuBar;
