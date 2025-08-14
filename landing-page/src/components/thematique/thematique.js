import React from "react"

import tw, { styled } from "twin.macro"
import { H3 } from "../../global-styles"

import representation_info from "./picto_representation_info.svg"
import algorithmique from "./picto_algorithmique.svg"
import programmation from "./picto_programmation.svg"
import ao from "./picto_architecture_ordinateurs.svg"
import reseaux from "./picto_reseaux.svg"
import enjeux from "./picto_enjeux_sociaux.svg"

const Thematique = styled.div`
  ${tw`
    w-full sm:w-1/2 md:w-1/3
    pb-10
    sm:pr-12 md:pr-16
  `}

  div {
    min-height: 87px;
    ${tw`
      flex 
      flex-col
    `}

    img {
      margin-top: auto;
      margin-bottom: auto;
      width: 60px;
    }
  }

  H3 {
    ${tw`
      pt-6
    `}
  }
`

const Thematiques = () => (
  <>
    <Thematique>
      <div>
        <img
          src={representation_info}
          alt="Pictogramme représentation de l'information"
        />
      </div>
      <H3>Représentation de l'information</H3>
      <p>
        Découvrez comment le réel est transformé pour être représenté sous forme
        numérique et quels sont les bénéfices ou les inconvénients qui en
        découlent.
      </p>
      <p></p>
    </Thematique>
    <Thematique>
      <div>
        <img src={algorithmique} alt="Pictogramme algorithmique" />
      </div>
      <H3>Algorithmique</H3>
      <p>
        Découvrez comment un ordinateur apprend à résoudre un problème, et
        comment le rendre plus efficace.
      </p>
    </Thematique>
    <Thematique>
      <div>
        <img src={programmation} alt="Pictogramme programmation" />
      </div>
      <H3>Programmation</H3>
      <p>
        Découvrez l’univers étendu des langages informatiques et apprenez à
        donner des instructions à un ordinateur.
      </p>
    </Thematique>
    <Thematique>
      <div>
        <img src={ao} alt="Pictogramme architecture des ordinateurs" />
      </div>
      <H3>Architecture des ordinateurs</H3>
      <p>
        Découvrez comment sont construits les ordinateurs et les composants qui
        sont à l’origine de l’informatique.
      </p>
    </Thematique>
    <Thematique>
      <div>
        <img src={reseaux} alt="Pictogramme réseaux" />
      </div>
      <H3>Réseaux</H3>
      <p>
        Découvrez les protocoles qui permettent à Internet d’exister, et au
        monde entier d’être connecté en permanence.
      </p>
    </Thematique>
    <Thematique>
      <div>
        <img
          style={{ marginTop: "auto", marginBottom: "auto" }}
          src={enjeux}
          alt="Pictogramme enjeux sociaux"
        />
      </div>
      <H3>Enjeux sociaux</H3>
      <p>
        Découvrez les transformations que les technologies de l’informatique
        opèrent sur les sociétés, et réflechissez à leur impact sur nos
        existences.
      </p>
    </Thematique>
  </>
)

export default Thematiques
