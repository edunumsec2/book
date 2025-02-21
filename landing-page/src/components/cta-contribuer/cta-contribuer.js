import React from "react"

import logo_github from "./logo-github.svg"
import logo_discord from "./logo-discord.svg"
import { Container, H2 } from "../../global-styles"
import { Link } from "gatsby"

class Contribuer extends React.Component {
  render() {
    return (
      <Container className="text-center bg-purple-light my-16">
        <H2 className="w-full text-white pt-12">Contribuer au projet</H2>
        <p className="text-white w-3/4 text-lg mx-auto">
          Vous pouvez contribuer au projet en consultant notre{" "}
          <Link to="/marcheasuivre"> marche à suivre</Link>, en nous retrouvant
          sur notre channel Discord, ou en proposant vos contenus sur GitHub, si
          vous possédez déjà un compte utilisateur.{" "}
        </p>
        <div className="flex w-full">
          <div className="ml-auto px-5 my-10">
            <a
              href="https://github.com/edunumsec2/book"
              target="_blank"
              rel="noreferrer"
              className="no-underline"
            >
              <img className="h-16" src={logo_github} alt="Logo GitHub" />
              <p className="text-white mt-2">GitHub</p>
            </a>
          </div>
          <div className="mr-auto px-5 my-10">
            <a
              href="https://discord.gg/b8qu79t6HQ"
              target="_blank"
              rel="noreferrer"
              className="no-underline"
            >
              <img className="h-16" src={logo_discord} alt="Logo Discord" />
              <p className="text-white mt-2">Discord</p>
            </a>
          </div>
        </div>
      </Container>
    )
  }
}

export default Contribuer
