import * as React from "react"
import { useSiteMetadata } from "../hooks/useSiteMetadata"

export const Seo = ({ title, description, lang, meta }) => {
  const {
    title: defaultTitle,
    description: defaultDescription,
    author,
  } = useSiteMetadata()

  const seo = {
    title: title || defaultTitle,
    description: description || defaultDescription,
    author: author,
  }

  return (
    <>
      <title>{seo.title}</title>
      <meta name="description" content={seo.description}></meta>
      <meta name="og:title" content={seo.title}></meta>
      <meta name="og:description" content={seo.description}></meta>
      <meta name="og:type" content="website"></meta>
    </>
  )
}
