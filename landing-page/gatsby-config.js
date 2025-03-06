module.exports = {
  siteMetadata: {
    title: `Modulo - Catalogue de ressources informatiques`,
    description: `Apprendre et enseigner l'informatique au gymnase grâce à un contenu didactique.`,
    author: `Centre LEARN - EPFL`,
    siteUrl: `https://www.epfl.ch/education/educational-initiatives/center-learn/`,
  },
  plugins: [
    `gatsby-plugin-no-sourcemaps`,
    `gatsby-plugin-postcss`, // used by Tailwindcss
    `gatsby-plugin-emotion`, // for Taliwindcss styling with styled-components
    {
      resolve: `gatsby-plugin-google-fonts`,
      options: {
        fonts: [`poppins\:200,300,400`],
        display: "swap",
      },
    },
    {
      resolve: "gatsby-plugin-htaccess",
      options: {
        https: true,
        SymLinksIfOwnerMatch: true,
        host: "modulo-info.ch",
        redirect: [
          "RewriteRule ^not-existing-url/?$ /existing-url [R=301,L,NE]",
          {
            from: "edunumsec2.ch",
            to: "modulo-info.ch",
          },
        ],
      },
    },
  ],
}
