import * as React from "react"

import Layout from "../components/layout"
import { Seo } from "../components/seo"
import { Container } from "../global-styles"

const NotFoundPage = () => (
  <Layout>
    <Container className="flex-col">
      <h1 className="py-20 text-3xl sm:text-4xl leading-10 font-light max-w-2xl">
        Oups ! Erreur 404.
      </h1>
      <p className="pb-4">
        La page que vous recherchez n'existe pas ; le serveur a renvoyé une
        erreur 404.
      </p>
      <p className="pb-20">
        Vous voulez en savoir plus sur l'erreur 404 ? Consultez{" "}
        <a
          href="https://fr.wikipedia.org/wiki/Erreur_HTTP_404"
          target="_blank"
          rel="noreferrer"
        >
          {" "}
          l'article sur Wikipédia.
        </a>
      </p>
    </Container>
  </Layout>
)

export default NotFoundPage

export const Head = () => <Seo title="404: Not found" />
