
"""l=["yoya","youyi","lila","louli","mima","moumi"]
f=open ("fichier1.txt","w")
for mot in l :
    
    f.write(mot + "\n") 
f.close()
f=open("fichier1.txt","r")
for ling in f :
    print (ling)
f.close ()
f=open("fichier1.txt","r")
while True :
    ling =f.readline ()
    if not ling :
        break;
    print(ling)
f.close()"""
"""Exercice: Ecrire un programme permettant de regrouper dans une liste les mots commun de F1 et F2
que vous allez créer vous même."""

"""f=open("fichier.txt","w")
n=int (input ("taille  de f:"))
for i in range (n):
    val=input("kelma ")
    f.write (val + "\n")
f.close();
g=open("gichier.txt","w")
m=int (input ("taille  de g:"))
for i in range (m):
    val=input("kelma ")
    g.write (val + "\n")
g.close();
f=open("fichie.txt","r")
l=[]
for kelma in f :
    g=open("gichier.txt","r")
    for kelma2 in g:
        if kelma==kelma2:
            l.append(kelma.strip())
    g.close()
f.close()
print (l)"""


""" Écrire un programme qui attend deux fichier Val et Coeff puis qui calcule la moyenne des 
valeurs pondérée par les coefficients"""
"""f=open("fichier.txt","w")
s=0
n=int (input("nombre des valur "))
for i in range (n) :
    val=int (input("valeur :"))
    s=s+val
    f.write(str(val) +"\n")
f.close ()
g=open("gichier.txt","w")
cpt=0
for i in range (n) :
    cof =int (input("coefficient  :"))
    cpt=cpt+cof
    g.write(str(cof) +"\n")
g.close ()
print("la moyene est :",s/cpt)"""

"""Soit un fichier typé intitulé concours.txt qui comporte les enregistrements relatifs aux 
candidats d’un concours. Chaque enregistrement est composé de : NCIN, NOM, PRENOM, AGE, 
DECISION : (type contenant les identificateurs suivants : admis, refusé, ajourné), et séparé par point 
virgule (;).
1. Définir la fonction saisir() qui permet de remplir les données relatives aux candidats dans le 
fichier concours.txt
2. Définir la fonction admis() qui permet créer le fichier admis.txt comportant les données 
relatives aux candidat admis
3. Afin de sélectionner en priorité les candidats admis et âgés moins de 30 ans, créer la fonction 
attente() qui produira à partir du fichier admis.txt, un nouveau fichier intitulé attente.txt 
comportant les données relatives aux candidats admis et âgés plus que 30 ans. Une ligne du 
fichier attente.txt comprend le NCIN, le NOM et PRENOM d’un candidat séparés par point 
virgule (;).
4. Définir la fonction statistiques(dec) qui permet de retourner le pourcentage des candidats pour 
la décision dec (admis, refusé et ajourné). Exemple :Le pourcentage des candidats admis = 
(Nombre des candidats admis / Nombre des candidats) *100
5. Définir la fonction supprimer() qui supprimera du fichier admis.txt les candidat âgés plus que 
30"""

"""def saisir (n):
    f=open("concour.txt","w")
    for i in range (n):
        nom=input("nom:")
        prenom=input("prenom")
        age=int (input("age:"))
        decision=input(" decision : refuse/admis/ajourne")
        f.write(nom  +";" + prenom  +";"  + str(age)+";" + decision +"\n" )
    f.close ()
"""
#la fonction str me entier to string 
#split : string to liste          strip: supprime 
"""
def admis ():
    f=open("concour.txt","r")
    g=open("admis.txt","w")
    for kelma in f :
        lista=kelma.split(";")
        if lista [3].strip()=="admis":
            g.write(kelma)
    g.close()
    f.close()
    
    
def attent ():
    g=open("admis.txt","r")
    h=open("attent.txt","w")
    for kelma in g:
        list=kelma.split(";")
        if int(list[2])>=30:
            h.write(kelma)
    g.close ()
    h.close()
    
def stat (kelma):
    f=open("concour.txt","r")
    nbk=0 
    total=0
    for mot in f:
        lista=mot.split(";")
        if lista[3].strip()==kelma:
            nbk=nbk+1
        total=total+1
    f.close()
    return (nbk/total)*100
def supprime ():
    g=open("admis.txt","r")
    l=[]
    for kelma in g:
        list=kelma.split(";")
        if int(list[2])<30:
            l.append(kelma)
    g.close ()
    g=open("admis.txt","w")
    g.writelines(l)
    g.close()

            
    
n=int (input("chhal kyn mn condidat :"))
f=saisir(n)
f=open("concour.txt","r")
for kelma in f :
    print(kelma)
f.close()

admis()
print("les admis :")
g=open("admis.txt","r")
for kelma in g :
    print (kelma)
g.close()


    
attent ()
h=open("attent.txt","r")
print ("les admis moin de 30ans")
for kelma in h :
    print(kelma)
h.close()
kelma=input(" wshmn pourcentage hab thsb :")
p=stat(kelma)
print("le pourcentage des condidats ",kelma ,"est: " ,p)


supprime()
g=open("admis.txt","r")
for i in g :
    print(i)
g.close()"""
    


    
    
    
    



    






                


            





    
