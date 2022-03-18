pandoc -s main.tex -o tmp.md
{ echo  '# Histoire de l'\''informatique 

```{admonition} Attention
:class: note
Ce document est en cours de rédaction.
```
'; cat tmp.md; } > main1.md

rm tmp.md
