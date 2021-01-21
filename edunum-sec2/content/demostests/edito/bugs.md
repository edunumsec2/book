# Bugs constatés


* Titres

Si le document markdown ne contient pas au moins un titre de niveau 1 `# titre`, le document ne s'affiche pas dans l'output HTML. 

* Contenus spéciaux en fin de document

Si le document se termine par une image, une directive Sphinx, un gif, etc. (toutes les possibilités n'ont pas été testées), un bug apparaît, consistant en la création d'une nouvelle page présente sur l'output HTML, mais non référencée dans le TOC. 