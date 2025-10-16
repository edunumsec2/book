import * as React from "react"

import Layout from "../components/layout"
import { Seo } from "../components/seo"
import { H1, H2, Text, Container } from "../global-styles"

const Contrib = () => (
  <Layout>
    <Container className="flex flex-col">
      <H1>Contribuer à modulo</H1>
      <Text>Il existe trois niveaux de contribution au projet modulo.</Text>
      <H2>Contributions non modérées </H2>
      <Text>
          Cette variante implique de proposer vos contenus, sans contrainte de format,
          sur la <a href="https://www.bdrp.ch" target="_blank">Banque de Ressources Pédagogiques (BDRP)</a>,
	  soit sous forme de fichiers, soit sous forme de lien. Veillez à renseigner les mots-clés (en particulier
	  le chapitre concerné) en y incluant également le mot-clé "Modulo". Ceci permettra à l'équipe de modération de
	  recenser les contributions et d'en inclure une sélection dans modulo, selon l'un des deux niveau de contribution
	  ci-dessous.

      </Text>
      <H2>Contributions externes</H2>
      <Text>
	  L'équipe de modération mettra en évidence certaines contributions déposées dans la BDRP en
	  incluant un lien dans la page <a href="https://enseigner.modulo-info.ch/contrib/index.html"> contributions externes </a>
	  de modulo. Si vous désirez inclure un lien sans passer par la BDRP, vous pouvez nous envoyer un message à contact@modulo-info.ch.
      </Text>
      <H2>Contributions intégrées</H2>
      <Text>
	  L'équipe de modération pourra également intégrer directement certaines contributions déposées dans la BDRP
	  à modulo. Il faudra pour ceci formatter les contenus en Sphinx et utiliser les conventions de de modulo, par
	  exemple pour les <a href="https://github.com/edunumsec2/book/blob/master/doc/activite.md" target="_blank">activités</a>.
	  Une discussion entre l'équipe de modération et l'auteur-ice de la ressource aura lieu concernant d'éventuelles adaptations
	  et déterminer qui se charge du reformattage. L'intégration se fait sous forme de pull request directement dans
	  <a href="https://github.com/edunumsec2/book/blob/master/README.md" target="_blank"> github</a>.

	  Des contributions techniques, telles que des fonctionnalités supplémentaires au site, sont également bienvenues,
	  veuillez en discuter avec l'équipe de modération (contact@modulo-info.ch). 
        .
      </Text>
    </Container>
  </Layout>
)

export default Contrib

export const Head = () => <Seo title="Marche à suivre" />
