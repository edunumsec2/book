import * as React from "react"

import Layout from "../components/layout"
import { Seo } from "../components/seo"
import { H1, H2, H3, Text, Container } from "../global-styles"

const Apropos = () => (
  <Layout>
    <Container className="flex flex-col">
      <H1>A propos de Modulo</H1>
      <Text>
        Modulo s’inscrit dans le projet d’éducation numérique mis en place par
        le canton de Vaud. Parallèlement, il répond à l’ordonnance fédérale
        visant à introduire l’informatique comme discipline obligatoire au
          gymnase, voie maturité. Une description plus détaillée de cette
	  démarche a été publiée dans un numéro spéacial de la  <a href="https://irem.univ-grenoble-alpes.fr/revues/petit-x/consultation/numero-119-special-informatique-petit-x/1-modulo-des-moyens-d-enseignement-de-l-informatique-a-visee-participative-1351544.kjsp?RH=1702464606726" target="_blank"> revue Petit x </a>. 
	  
      </Text>
      <H2>Objectifs</H2>
      <Text>
        Pour accompagner les enseignant·e·s et les élèves dans cette étape
        décisive de l’éducation vaudoise, Modulo propose des moyens
        d’enseignement aux enseignant·e·s, parmi lesquels des éléments de
        théorie, des exercices et des travaux pratiques. De la même manière,
        Modulo propose des ressources aux élèves qui intègrent de la théorie,
        des exercices et des activités, afin de faciliter l’apprentissage et le
        suivi des enseignements.
      </Text>
      <Text>
        Le projet accorde une importance particulière à la liberté
        d'enseignement au gymnase. Ainsi, les ressources proposées ne sont pas
        obligatoires ; elles sont offertes aux enseignant·e·s et peuvent être
        récupérées, réutilisées, partagées et exploitées selon les besoins et
        les choix pédagogiques de chacun·e.
      </Text>
      <H2>Rédaction</H2>
      <Text>
        Le contenu de Modulo est rédigé par des enseignant·e·s d'informatique au
        gymnase, une équipe pluridisciplinaire du centre LEARN à l'EPFL, appuyés
        par un pannel d'expert·e·s issus de l'UNIL, la HEP Vaud et l'EPFL. Une
        nouvelle version de Modulo est mise ligne tous les 6 mois, selon
        l'avancement de la rédaction.
      </Text>
      <H2>Contenu</H2>
      <Text>
        Le plan d'études vaudois comprend les cinq thèmes suivants :
        représentation de l'information, algorithmique, programmation,
        architecture des ordinateurs et réseaux. Un sixième thème, les enjeux
        sociaux du numérique, permet aux étudiant·e·s d'aborder le rôle du
        numérique, sa signification et son impact sur la société.
      </Text>
      <Text>
        Le contenu permet d'aborder le numérique sous un angle critique, et de
        comprendre les opportunités et les limites de la science informatique et
        du numérique en général. Des retours sont demandés aux enseignant·e·s et
        aux étudiant·e·s via des formulaires anonymes afin d'adapter le contenu,
        le rendre varié et intéressant.
      </Text>
      <H3>Plus d'informations</H3>
      <ul className="pb-10">
        <li>
          <a
            href="https://www.admin.ch/gov/fr/accueil/documentation/communiques.msg-id-71332.html"
            target="_blank"
            rel="noreferrer"
          >
            Ordonnance fédérale sur l'enseignement de l'informatique
          </a>
        </li>
        <li>
          <a
            href="https://www.ciip.ch/files/2/Decision_Plan-action-numerique_2018-11-22.pdf"
            target="_blank"
            rel="noreferrer"
          >
            Décision CIIP du 29 novembre 2018 (PDF)
          </a>
        </li>
      </ul>
    </Container>
  </Layout>
)

export default Apropos

export const Head = () => <Seo title="A propos" />
