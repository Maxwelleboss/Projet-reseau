# /bin/bash

echo test

file="Trame.txt"
nblignes=0

#on affiche les numéros des lignes contenant les offsets "0000"
lignes=$(awk '/0000/{print FNR " " }' $file)
for x in $lignes
do 
echo $x 
nblignes=$((nblignes+1))
done
echo $nblignes 

#intialisation des variables
b=0
cpt=0


#Une liste des lignes de début de trame se trouve dans $ligne  


for i in $lignes 
do
cpt=$((cpt+1))
[ $i -eq 1 ] && continue
head -n $((i-1)) "$file"|tail -n +$b > Spathis$cpt.txt 
b=$i
[ $cpt -eq  $nblignes  ] && tail -n +$i "$file" > Spathis$io.txt
#execute py3.py sur le fichier et le stocke dans un fichier txt
python3 py3.py Spathis$cpt.txt > Resultat$cpt.txt
done





