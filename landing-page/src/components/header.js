import React from "react"
import Logo from "../images/modulo-logo-animated.svg"
import MobileMenu from "./mobilemenu.js"
import tw, { styled } from "twin.macro"
import { Container, ButtonBlue, ButtonRed } from "../global-styles"
import { Link } from "gatsby"

const HeaderContainer = styled.header`
  ${tw`
    flex 
    justify-end 
    box-border 
    py-10
    content-start
    w-full
    items-center
  `}
`

const LogoLink = tw.a`
  mr-auto
`

const DesktopMenu = styled.div`
  ${tw`
    hidden sm:block
  `}

  ul {
    ${tw`
      flex flex-row items-center list-none p-0
    `}
  }
`

const Header = () => (
  <header>
    <Container>
      <HeaderContainer>
        <LogoLink href="/">
          <img id="logo" src={Logo} alt="Logo Modulo" />
        </LogoLink>
        <MobileMenu />
        <DesktopMenu>
          <ul>
            <li className="pb-0">
              <Link to="/a-propos" className="no-underline">
                A propos
              </Link>
            </li>
            <li className="pb-0">
              <Link to="/faq" className="ml-5 no-underline">
                FAQ
              </Link>
            </li>
            <li className="pb-0">
              <ButtonBlue
                className="ml-5"
                href="https://enseigner.modulo-info.ch"
                target="_blank"
                rel="noreferrer"
              >
                Enseigner
              </ButtonBlue>
            </li>
            <li className="pb-0">
              <ButtonRed
                className="ml-3"
                href="https://apprendre.modulo-info.ch"
                target="_blank"
                rel="noreferrer"
              >
                Apprendre
              </ButtonRed>
            </li>
          </ul>
        </DesktopMenu>
      </HeaderContainer>
    </Container>
  </header>
)

export default Header
