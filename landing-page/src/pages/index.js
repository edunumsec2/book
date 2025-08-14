import * as React from "react"

import Layout from "../components/layout"
import { Seo } from "../components/seo"
import LogoGrid from "../components/logogrid/logogrid"
import Thematiques from "../components/thematique/thematique"
import Contribuer from "../components/cta-contribuer/cta-contribuer"
import { Button, Container, ContainerLarge, H2 } from "../global-styles"
import tw, { styled } from "twin.macro"

import mosaique from "../images/home-mosaic.svg"

const BigText = styled.h1`
  line-height: 1.5 !important;

  ${tw`
    py-20
    text-3xl sm:text-4xl
    leading-10
    font-light
    max-w-2xl
  `}
`

const IndexPage = () => (
  <Layout>
    <Container>
      <BigText>
        Modulo est un catalogue de ressources destiné à{" "}
        <span className="text-purple-light">l'enseignement</span> et à{" "}
        <span className="text-turquoise-dark">l'apprentissage</span> de{" "}
        <span className="text-blue-darkest">l'informatique</span> au gymnase.
      </BigText>
    </Container>
    <ContainerLarge className="bg-gray-light">
      <Container>
        <Container className="w-full md:w-1/2 flex-col pr-5 pl-0 pt-12">
          <H2 className="text-purple-dark">
            Un projet open-source et collaboratif
          </H2>
          <p className="text-lg">
            A la rentrée 2022, l'informatique a été introduite comme discipline
            obligatoire au gymnase. Afin d'accompagner ce changement, le canton
            de Vaud finance le projet Modulo et propose du contenu pour
            apprendre et enseigner. Rédigé par les grandes institutions
            pédagogiques du canton et par un groupe
            d'enseignant&middot;e&middot;s, Modulo est un projet collaboratif
            auquel chacun&middot;e peut contribuer.
          </p>
          <Button
            href="/a-propos"
            className="self-start mb-10 mt-6 smmd:my-auto"
          >
            En savoir plus
          </Button>
        </Container>
        <div className="md:w-1/2 px-0 hidden md:block sm:my-auto">
          <img src={mosaique} alt="Mosaïque décorative" />
        </div>
      </Container>
    </ContainerLarge>
    <ContainerLarge className="block md:hidden">
      <img src={mosaique} alt="Mosaïque décorative" />
    </ContainerLarge>
    <Container className="block">
      <H2 className="mt-10">Thématiques</H2>
    </Container>
    <Container className="justify-center mt-5">
      <Thematiques />
    </Container>
    <Contribuer />
    <Container className="flex-col">
      <p className="sm:text-lg text-center w-full leading-10 mb-10 sm:mb-6 ">
        Un projet mené par
      </p>
    </Container>
    <Container className="block pb-10">
      <LogoGrid />
    </Container>
  </Layout>
)

export default IndexPage

export const Head = () => <Seo />
