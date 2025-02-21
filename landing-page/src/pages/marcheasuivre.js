import * as React from "react"

import Layout from "../components/layout"
import { Seo } from "../components/seo"
import { H1, H2, Text, Container } from "../global-styles"

const Contrib = () => (
  <Layout>
    <Container className="flex flex-col">
      <H1>Contribuer à modulo</H1>
      <Text>Il existe trois variantes de contribution au projet modulo.</Text>
      <H2>Contribution non formatée</H2>
      <Text>
        Cette variante implique de proposer vos contenus, non formatés,
        directement sur un dépôt FTP. Les contenus sont également disponibles
        pour les autres enseignant-e-s en consultation. Pour cela, il faut
        contacter l'équipe modulo à l'adresse modulo-team@epfl.ch, qui vous
        transmettra les accès.
      </Text>
      <H2>Contribution formatée</H2>
      <Text>
        Cette variante consiste à pré-formater les contenus que vous souhaitez
        déposer grâce aux templates prévus à cet effet, disponibles{" "}
        <a
          href="https://github.com/edunumsec2/book/blob/master/templates/template-activite.md"
          target="_blank"
          rel="noopener noreferrer"
        >
          ici
        </a>
        . Le dépôt du fichier après formatage se fait de la même façon qu'au
        point précédent. L'avantage de cette solution est qu'elle permet à
        l'équipe modulo, après processus de validation, d'intégrer
        potentiellement vos contenus dans le site.
      </Text>
      <H2>Contribution avancée</H2>
      <Text>
        Cette modalité de contribution implique de se créer un compte GitHub et
        de proposer du contenu directement dpeuis cette plateforme, en suivant
        la marche à suivre détaillée{" "}
        <a
          href="https://github.com/edunumsec2/book/blob/master/CONTRIBUTING.md"
          target="_blank"
          rel="noopener noreferrer"
        >
          ici
        </a>
        .
      </Text>
    </Container>
  </Layout>
)

export default Contrib

export const Head = () => <Seo title="Marche à suivre" />
