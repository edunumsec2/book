# Utilisation de GitHub Desktop

GitHub Desktop est téléchargeable sur le [site officiel](https://desktop.github.com/) (Windows et MacOS). Pour Ubuntu, vous pouvez suivre [ces instructions](https://gist.github.com/berkorbay/6feda478a00b0432d13f1fc0a50467f1).

Si vous n'êtes pas familiers avec Git, nous vous invitons à lire cette [documentation](https://docs.github.com/en/get-started/quickstart).

## 1. Récupération du projet
Après vous êtres connecté à votre compte GitHub (File \ Options \ Accounts \ Sign in), vous pouvez récupérer le projet avec le bouton 'Clone Repository' et en indiquant l'URL `git@github.com:edunumsec2/book.git`.

![recuperation-projet](https://user-images.githubusercontent.com/12733352/196887243-3af3e1fe-2e9a-4e05-95bc-16c18bd179af.gif)

Si vous rencontrez une erreur similaire à celle ci-dessous, il vous faut peut-être insérer la commande ci-dessous via le Terminal : git remote set-url origin git@github.com:edunumsec2/book.git`. Cette commande permet de récupérer le projet via SSH au lieu de HTTPS.

![image](https://user-images.githubusercontent.com/12733352/196886617-91ad5964-6d45-4c8b-94f4-768af2242f00.png)

## 2. Création d'une nouvelle branche

Lorsque vous travailler sur du nouveau contenu, nous vous proposons de travailler avec une nouvelle branche.

![ezgif com-gif-maker(1)](https://user-images.githubusercontent.com/12733352/196887901-e5e2662b-295c-414a-9a12-f1561dac4331.gif)

## 3. "Enregistrement" des modifications (commit)

Pour sauvegarder votre travail, vous pouvez l'enregistrer (commit) en indiquant un commentaire (visible par tout le monde).

![ezgif com-gif-maker(2)](https://user-images.githubusercontent.com/12733352/196888726-e7dc90ff-5de8-4e73-9e2a-0d8d5d7e01ec.gif)

## 4. Publication de la branche

Si la branche n'est pas encore publiée, vous pouvez la publier.

![ezgif com-gif-maker(3)](https://user-images.githubusercontent.com/12733352/196889281-b99a1a82-f9c8-49dc-85ae-af63a194eb73.gif)

## 5. Demande de fusion des modifications (pull request)

Puis, vous pouvez faire un pull request (une demande de fusion avec le projet principal). Cette étape se déroule directement sur le site GitHub et non pas dans l'application (un clic dans l'application ouvre votre navigateur internet).

![ezgif com-gif-maker(4)](https://user-images.githubusercontent.com/12733352/196892862-6f1a9d15-d7a0-439b-a493-e4cebe743a58.gif)

A partir de là, les modifications seront revues par les modérateurs de la communauté et un retour vous sera donné ! Plus d'informations sur la [gouvernance](https://github.com/edunumsec2/book/blob/documentation/GOVERNANCE.md) du projet.
