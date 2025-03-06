<p align="center">
    <img alt="Logo Modulo" src="https://user-images.githubusercontent.com/12733352/187911585-9ba02dd4-3eda-4102-bbaa-45e15bdb0473.png" width="300" />
</p>
<h1 align="center">
  Site web
</h1>

Ce répertoire contient le code source pour le site informationnel Modulo, actuellement accessible sur [https://modulo-info.ch](https://modulo-info.ch/) et hébergé chez Infomaniak. Ce projet, complémentaire aux [ressources Modulo](https://github.com/edunumsec2/book), permet de communiquer plus largement les informations importantes liées à Modulo.

## Technologies

Le site est développé avec le framework JavaScript [Gatsby](https://www.gatsbyjs.com/) (v.4.0), les styles sont gérés par le framework CSS [Tailwind](https://tailwindcss.com/), tous les deux open source. De manière similaire à [Sphinx](https://www.sphinx-doc.org/en/master/) qui génère une documentation statique pour le projet principal, Gatsby génère des fichiers HTML/CSS/JS statiques permettant une très grande portabilité - aucune technologie spécifique n'est requise du côté du serveur.

## 🚀 Installation

1. **Pré-requis**

   [**Visual Studio Code**](https://code.visualstudio.com/) ou n'importe quel éditeur de code de votre choix.

   [**Node.js**](https://nodejs.org/en/download/) _(v.16.x.x LTS)_ nécessaire pour l'installation de Gatsby, permet à celui-ci de générer les fichiers statiques. Node permet également d'accéder au Node Package Manager (NPM) - outil similaire à pip pour Python.

   ```shell
   # pour vérifier si Node est installé
   node --version # expected : v.16.x.x
   ```

   _Si la commande ne fonctionne pas, vous devez peut-être relancer un nouveau Terminal ou redémarrer la machine._

   [**GitHub Desktop**](https://desktop.github.com/) **(recommandé)** pour cloner ce répertoire. GitHub Desktop fournit une interface graphique agréable d'utilisation pour Git, en gardant les choses simples puisqu'il enlève certaines complexités de Git (utilisation d'un agent ssh par exemple). Pour Ubuntu, voir [github_ubuntu_desktop.sh](https://gist.github.com/berkorbay/6feda478a00b0432d13f1fc0a50467f1).

   _A la place de GitHub Desktop, vous pouvez aussi utiliser [Git](https://git-scm.com/downloads) via votre terminal, mais il faudra [se familiariser avec les commandes](https://rogerdudler.github.io/git-guide/), [générer une clé SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) et la [connecter à votre compte GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) pour pouvoir récupérer le projet._

2. **Gatsby CLI**

   Installer Gatsby Command Line Interface (CLI) via NPM. Gatsby CLI permettra d'exécuter les commandes de développement ou de build (voir [utilisation](#utilisation)).

   ```shell
   # install gatsby cli
   npm install -g gatsby-cli
   ```

   ```shell
   # check installation
   gatsby --version # expected : Gatsby CLI version: 4.16.0
   ```

_Si vous êtes bloqués dans l'installation de Node, Git ou Gatsby CLI, vous pouvez trouver de l'aide supplémentaire [ici](https://www.gatsbyjs.com/docs/tutorial/part-0/)_.

3. **Cloner le projet**

   Via GitHub Desktop.

   Ou alors via votre terminal :

   ```shell

   # aller dans votre répertoire de développement
   cd my-dev-repository

   # cloner le projet
   git clone git@github.com:edunumsec2/modulo-website.git

   ```

4. **Installation des dépendances**

   A la racine du projet, installer les [dépendances](https://github.com/edunumsec2/modulo-website/blob/master/package.json) :

   ```shell

   # aller dans le répertoire du projet
   cd modulo-website

   # installer les dépendances
   npm install --force

   ```

## Utilisation

todo (gatsby build, clean, develop)

## Structure du projet

todo

## Ressources utiles

todo
