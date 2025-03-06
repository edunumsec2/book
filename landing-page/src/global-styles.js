import tw, { styled } from "twin.macro"

export const Wrapper = styled.div`
  ${tw`
        w-full
        overflow-x-hidden
        box-border
    `}
`

export const Container = tw.div`
    flex
    flex-wrap
    max-w-screen-lg
    w-full
    mx-auto
    flex-col
    sm:flex-row
    overflow-x-hidden
    px-4
    lg:px-0
`

export const ContainerVertical = tw.div`
    flex
    flex-wrap
    max-w-screen-lg
    w-full
    mx-auto
    flex-col
    overflow-x-hidden
    px-4
    lg:px-0
`

export const ContainerLarge = tw.div`
    flex
    w-full
    my-0
    mx-auto
`
export const H1 = styled.h1`
  ${tw`
        text-3xl
        pb-5 md:pb-6
        text-purple-dark
        leading-normal
    `}
`

export const H2 = tw.h2`
    text-2xl
    py-4
    text-purple-dark
    leading-normal
`

export const H3 = tw.h3`
    text-xl

    pb-4
`

export const Text = tw.p`
    pb-5
`

export const Button = tw.a`
    py-2
    px-6
    rounded-3xl
    bg-transparent
    text-lg
    text-blue-dark
    border-blue-dark
    border-solid
    border-2
    hover:bg-blue-dark
    hover:text-white
    no-underline
`

export const ButtonBlue = styled.a`
  ${tw`
        bg-purple-dark
        text-white
        rounded-3xl
        py-2
        px-4
        text-center
        mx-auto
        no-underline
    `}
`

export const ButtonRed = styled.a`
  ${tw`
        bg-turquoise-dark
        text-white
        rounded-3xl
        py-2
        px-4
        text-center
        mx-auto
        no-underline
    `}
`
