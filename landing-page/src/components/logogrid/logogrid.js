import React from "react"
import tw, { styled } from "twin.macro"

import logo_learn from "./logo-learn-epfl.svg"
import logo_unil from "./logo-unil.svg"
import logo_hep from "./logo-hep.jpg"

const LogosContainer = styled.div`
  ${tw`
    flex
    flex-col
    sm:flex-row
    place-items-center
    w-5/6
    mx-auto
  `}
`

const LogoContainer = styled.div`
  ${tw`
    w-2/3
    md:w-full
    mb-10
    sm:px-12
    sm:pt-6
  `}

  img {
    ${tw`
      
  `}
  }
`

class LogoGrid extends React.Component {
  render() {
    return (
      <LogosContainer>
        <LogoContainer>
          <a href="https://learn.epfl.ch/" target="_blank" rel="noreferrer">
            <img src={logo_learn} alt="Logo centre LEARN - EPFL" />
          </a>
        </LogoContainer>
        <LogoContainer>
          <img src={logo_unil} alt="Logo Université de Lausanne" />
        </LogoContainer>
        <LogoContainer>
          <img src={logo_hep} alt="Logo Haute Ecole Pédagogique" />
        </LogoContainer>
      </LogosContainer>
    )
  }
}

export default LogoGrid
