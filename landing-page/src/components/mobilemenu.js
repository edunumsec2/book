import React, { useState } from "react"
import { styled } from "twin.macro"
import { ButtonRed, ButtonBlue } from "../global-styles"

const MenuIcon = styled.button`
  display: flex;
  flex-direction: column;
  margin-top: auto;
  margin-bottom: auto;
  justify-content: space-around;
  width: 1.5rem;
  height: 1.5rem;
  background: transparent;
  border: none;
  cursor: pointer;
  z-index: 5;

  div {
    width: 1.5rem;
    height: 0.2rem;
    background: black;
    border-radius: 5px;
    transform-origin: 0.8px;
    position: relative;
    transition:
      opacity 300ms,
      transform 300ms;

    :first-child {
      transform: ${({ nav }) => (nav ? "rotate(45deg)" : "rotate(0)")};
    }

    :nth-child(2) {
      opacity: ${({ nav }) => (nav ? "0" : "1")};
    }

    :nth-child(3) {
      transform: ${({ nav }) => (nav ? "rotate(-45deg)" : "rotate(0)")};
    }
  }

  @media (min-width: 640px) {
    display: none;
  }
`

const MenuLinks = styled.nav`
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  background-color: white;
  z-index: 3;
  height: 100vh;
  width: 100%;
  position: absolute;
  top: 0;
  right: 0;
  transition: all 300ms;
  transform: ${({ nav }) => (nav ? "translateX(0)" : "translateX(100%)")};

  ul {
    list-style-type: none;
  }

  li {
    margin-top: 1rem;
  }

  a {
    text-decoration: none;
    font-size: 1.5rem;

    :hover {
      color: #6ab4ff;
      transition: color 300ms;
    }
  }
`

const MobileMenu = () => {
  const [nav, showNav] = useState(false)

  return (
    <>
      <MenuIcon nav={nav} onClick={() => showNav(!nav)}>
        <div />
        <div />
        <div />
      </MenuIcon>
      <MenuLinks nav={nav}>
        <ul>
          <li>
            <a href="/">Accueil</a>
          </li>
          <li>
            <a href="/a-propos">A propos</a>
          </li>
          <li>
            <a href="/faq">FAQ</a>
          </li>
          <li className="mt-10">
            <ButtonBlue
              href="https://enseigner.modulo-info.ch"
              target="_blank"
              rel="noreferrer"
            >
              Enseigner
            </ButtonBlue>
          </li>
          <li className="mt-10">
            <ButtonRed
              href="https://apprendre.modulo-info.ch"
              target="_blank"
              rel="noreferrer"
            >
              Apprendre
            </ButtonRed>
          </li>
        </ul>
      </MenuLinks>
    </>
  )
}

export default MobileMenu
