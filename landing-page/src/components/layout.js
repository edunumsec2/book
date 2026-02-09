import * as React from "react"
import Header from "./header"
import Footer from "./footer/footer"
import { Wrapper } from "../global-styles"

import { Container, ContainerLarge } from "../global-styles"

const Layout = ({ children }) => {
  return (
    <>
      <Wrapper>
        <ContainerLarge className="bg-purple-dark">
          <Container>
            <p className="w-full h-full text-center text-white py-1">
              {/* version actuelle des ressources : 2024-09-13 */}
            </p>
          </Container>
        </ContainerLarge>
        <Header />
        <main>{children}</main>
        <Footer />
      </Wrapper>
    </>
  )
}

export default Layout
