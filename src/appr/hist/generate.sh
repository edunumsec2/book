pandoc --wrap=preserve -s main.tex -o tmp.md
sed -i.bak -e 's/{\#une-brève-histoire-de-linformatique \.unnumbered}//' \
            -e 's/^r[0-9]*\.[0-9]*//g' \
            -e 's/.*!\[image\]/!\[image\]/g' \
            -e 's/.*!\[[^]]*\](\(.*\)){.*width=\"\(.*\)\"}/```{image} \1 \
:width: \2 \
:align: right \
```/g' \
            -e 's/\[\([XI]*\)\][{]\.smallcaps[}]/\1e/g' tmp.md

{ echo  '# Histoire de l'\''informatique 

```{admonition} Attention
:class: note
Ce document est en cours de rédaction.
```
'; cat tmp.md; } > main1.md

rm tmp.md tmp.md.bak
