# /bin/bash

echo Welcome Prométhée 
hat=$(pwd)
#export PATH=$PATH:$hat
sleep 1

#fichier de lecture de trame 
echo Entrez le nom du fichier contenant les trames :
read nom
while [ ! -f $nom ]
do
echo Fichier non trouvé         vérifiez votre saisie
echo 
echo Vérifiez que ce script se trouve dans le bon repertoire 
echo 
echo voici le chemin du script:
pwd
read nom
done
echo "Félicitations ! "
file=$nom
destination="resultat.txt"
nblignes=0

#on affiche les numéros des lignes contenant les offsets "0000"
lignes=$(awk '/0000/{print FNR " " }' $file)
for x in $lignes
do 
nblignes=$((nblignes+1))
done
echo $nblignes trames détectées
sleep 1
#intialisation des variables
b=0
cpt=0

[ $nblignes -eq 1 ]  && $file > destination

#Une liste des lignes de début de trame se trouve dans $ligne  
echo début du traitement
sleep 1 
for i in $lignes 
do
cpt=$((cpt+1))
[ $i -eq 1 ] && continue
head -n $((i-1)) "$file"|tail -n +$b > $destination && b=$i
[ $cpt -eq  $nblignes  ] && tail -n +$i "$file" > $destination
done
 

echo fin du traitement

