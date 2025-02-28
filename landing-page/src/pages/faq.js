import * as React from "react"

import Layout from "../components/layout"
import { Seo } from "../components/seo"
import Contribuer from "../components/cta-contribuer/cta-contribuer"
import { ContainerVertical, H1, H2 } from "../global-styles"

const Faq = () => (
  <Layout>
    <ContainerVertical className="block mb-10">
      <H1>FAQ</H1>
      <p>
        Modulo est un projet financé par le canton de Vaud avec une forte
        composante participative. Vous trouverez ici une liste de questions
        fréquemment posées à propos du projet. En cas de questions
        supplémentaires, ou si vous souhaitez participer au projet, n'hésitez
        pas à nous contacter via contact@modulo-info.ch !
      </p>
    </ContainerVertical>
    <ContainerVertical>
      <H2>A qui s'adressent ces ressources ?</H2>
      <p>
        Le catalogue de ressources Modulo est destiné à enseigner et à apprendre
        l'informatique au gymnase. Il a été ainsi séparé en deux parties
        distinctes. La première, destinée aux enseignant&middot;e&middot;s,
        propose du contenu, des exercices interactifs et des cas pratiques afin
        de transmettre un savoir en classe. La seconde partie, destinée aux
        élèves, fait office de support de cours et vient compléter les
        informations transmises par l'enseignant&middot;e durant les cours et
        travaux pratiques.
      </p>
    </ContainerVertical>
    <ContainerVertical>
      <H2>Qui rédige le contenu ?</H2>
      <p>
        Le contenu de Modulo est rédigé par des enseignant&middot;e&middot;s
        d'informatique au gymnase, une équipe pluridisciplinaire du centre LEARN
        à l'EPFL, appuyés par un pannel d'expert&middot;e&middot;s issus de
        l'UNIL, la HEP Vaud et l'EPFL. Une nouvelle version de Modulo est mise
        ligne tous les 6 mois, selon l'avancement de la rédaction.
      </p>
    </ContainerVertical>
    <ContainerVertical>
      <H2>Comment utiliser ces contenus ?</H2>
      <p>
        Le catalogue est sous license Creative Commons{" "}
        <a
          target="blank"
          rel="noreferrer"
          href="https://creativecommons.org/licenses/?lang=fr"
        >
          BY-NC-SA
        </a>
        , signifiant qu'elles peuvent être copiées, transformées, adaptées, et
        diffusées, hormis à des fins commerciales, tant qu'elles créditent le
        groupe de travail présenté ci-dessus, et qu'elles utilisent la même
        licence pour d'éventuels partages futurs. Il vous est ainsi possible de
        consulter le catalogue simplement, d'en récupérer le code source pour
        faire votre propre cours, ou encore de proposer des modifications sur la
        branche master du Github en suivant la documentation présente sur le
        dépôt du projet.
      </p>
    </ContainerVertical>
    <ContainerVertical>
      <H2>Pourquoi avoir choisi ces six thématiques ?</H2>
      <p>Elles correspondent au contenu du nouveau plan d'études vaudois.</p>
    </ContainerVertical>
    <ContainerVertical>
      <H2>Quelle est la démarche pédagogique suivie ?</H2>
      <p>
        La démarche pédagogique est décrite dans cet{" "}
        <a href="https://irem.univ-grenoble-alpes.fr/revues/petit-x/consultation/numero-119-thematique-sur-l-informatique-petit-x/1-modulo-des-moyens-d-enseignement-de-l-informatique-a-visee-participative-1351544.kjsp?RH=1702464606726">
          article
        </a>
        .
      </p>
    </ContainerVertical>
    <ContainerVertical>
      <H2>Comment contribuer ?</H2>
      <p>
        Vous pouvez contribuer au contenu de base via notre Github. Les
        instructions d'installation de l'environnement se trouvent{" "}
        <a
          target="blank"
          rel="noreferrer"
          href="https://github.com/edunumsec2/book/blob/master/README.md"
        >
          {" "}
          ici
        </a>
        .
      </p>
    </ContainerVertical>
    <Contribuer className="mb-10" />
  </Layout>
)

export default Faq

export const Head = () => <Seo title="FAQ" />
