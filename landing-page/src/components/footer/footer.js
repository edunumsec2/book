import React from "react"
import { Container, ContainerLarge } from "../../global-styles"
import { Link } from "gatsby"

import logo_vd from "./logo-vd.svg"
import logo_github from "./logo-github.svg"
import logo_discord from "./logo-discord.svg"

import external from "../../images/external-link-white.png"

const Footer = () => (
  <ContainerLarge className="bg-purple-dark">
    <Container className="hidden sm:flex">
      <div className="py-16 grid grid-cols-3 col-auto w-full text-white">
        <div>
          <img src={logo_vd} alt="Logo du Canton de Vaud" />
        </div>
        <div>
          <ul>
            <li className="pb-6">
              <a
                href="https://enseigner.modulo-info.ch/"
                target="_blank"
                rel="noreferrer"
                className="no-underline"
              >
                <div className="flex flex-row items-center">
                  Enseigner
                  <img
                    className="ml-2"
                    src={external}
                    width="20"
                    alt="Icône lien externe"
                  />
                </div>
              </a>
            </li>
            <li className="pb-6">
              <a
                href="https://apprendre.modulo-info.ch/"
                target="_blank"
                rel="noreferrer"
                className="no-underline"
              >
                <div className="flex flex-row items-center">
                  Apprendre
                  <img
                    className="ml-2"
                    src={external}
                    width="20"
                    alt="Icône lien externe"
                  />
                </div>
              </a>
            </li>
            <li className="pb-6">
              <Link to="/a-propos" className="no-underline">
                A propos
              </Link>
            </li>
            <li>
              <Link to="/faq" className="no-underline">
                FAQ
              </Link>
            </li>
          </ul>
        </div>
        <div>
          <ul>
            <li className="pb-6">
              <a
                className="no-underline"
                target="_blank"
                rel="noreferrer"
                href="https://github.com/edunumsec2/book#documents-importants"
              >
                <div className="flex flex-row w-full items-center">
                  Ressources pilotes
                  <img
                    className="ml-2"
                    src={external}
                    width="20"
                    alt="Icône lien externe"
                  />
                </div>
              </a>
            </li>
            <li>
              <a href="mailto:contact@modulo-info.ch" className="pt-auto">
                contact@modulo-info.ch
              </a>
            </li>
          </ul>
          <div className="flex flex-row w-full items-center mt-5">
            <a
              className="mr-5"
              href="https://discord.gg/b8qu79t6HQ"
              target="_blank"
              rel="noreferrer"
            >
              <img
                src={logo_discord}
                alt="Accéder au serveur Discord"
                width="40px"
              />
            </a>
            <a
              href="https://github.com/edunumsec2/book"
              target="_blank"
              rel="noreferrer"
            >
              <img
                src={logo_github}
                alt="Accéder au dépôt GitHub"
                width="40px"
              />
            </a>
          </div>
        </div>
      </div>
    </Container>
    <Container className="flex sm:hidden text-white text-center items-center pt-16">
      <ul>
        <li className="pb-6 text-lg">
          <a
            href="https://enseigner.modulo-info.ch/"
            target="_blank"
            rel="noreferrer"
            className="no-underline"
          >
            Enseigner
          </a>
        </li>
        <li className="pb-6 text-lg">
          <a
            href="https://apprendre.modulo-info.ch/"
            target="_blank"
            rel="noreferrer"
            className="no-underline"
          >
            Apprendre
          </a>
        </li>
        <li className="pb-6 text-lg">
          <Link to="/a-propos" className="no-underline">
            A propos
          </Link>
        </li>
        <li className="pb-10 text-lg">
          <Link to="/faq" className="no-underline">
            FAQ
          </Link>
        </li>
        <li className="text-lg">
          <a
            className="no-underline"
            target="_blank"
            rel="noreferrer"
            href="https://github.com/edunumsec2/book#documents-importants"
          >
            <div className="flex flex-row w-full items-center">
              Ressources pilotes
            </div>
          </a>
        </li>
      </ul>
      <p className="pb-20 text-lg">info@modulo.ch</p>
      <img className="pb-6" src={logo_vd} alt="Logo du Canton de Vaud" />
    </Container>
  </ContainerLarge>
)

export default Footer
