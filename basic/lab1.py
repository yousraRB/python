"""Exercice: étant donné deux nombre entier x et y, écrivez un programme permettant de calculer x
puissance y
x=int(input("mdli x :"))
y=int(input("medli y : "))
print(x**y)"""


""": Etant donnée un nombre réel positive, Effectuez les transformations suivantes : Un pied est
divisé en 12 pouces.Convertissez le pied donnée en entrée par l’utilisateur (le nombre réel positive) en
pouces. Un pied correspond à 1/3 de verge anglaise (yard), c'est-à-dire 0,3048 mètre. Transformez le
nombre qui à l’unité pied en mètre. Transformez le nombre obtenu dans la question précédente en
centimètre et en kilomètre.
p=float(input("med lkar3in : "))
print(p*12,"pouces")
print(p*0.3048,"metres")
print(p*0.3048*100,"cm")
print(p*0.3048/1000,"km")"""

""" étant donné un nombre entier, écrivez un programme permettant de vérifier si le nombre est
pair ou impair.
e=int(input("med le nombre : "))
if e%2==0 :
    print("pair")
else :
    print("impair")"""

""": Ecrivez un programme permettant d’afficher tout Les nombres d'Armstrong. Un nombre
d’Armstrong est un nombre égal à la somme des cubes de ses chiffres.
"""
"""n=int(input("chhal kyn mn nombre : "))

for i in range (0,n,1):
    s=0
    nbr=i
    while nbr!=0:
        s=s+(nbr%10)**3
        nbr=nbr//10
    if s==i :
        print (i,"est amstrong")
    else :
        print(i,"non amstrong")"""
        
"""Ecrire un programme permettant de vérifier si un nombre est parfait."""

"""n=int(input(" ara nombre :"))
s=0
for i in range (1,n//2+1,1):
    if n%i==0 :
        s=s+i

if n==s :
    print (n,"est parfait")
else :
    print(n,"nest pas parfait ")"""
    
"""Ecrire un programme permettant de calculer et d’afficher le nombre d’occurence d’un chiffre
C (0<= C <10) dans un entier naturel A."""

"""a=int(input("medli l A"))
c=int(input("medli chifr c "))
nbr=a
cpt=0
while nbr!=0 :
    x=nbr%10
    if c==x :
        cpt=cpt+1
    nbr=nbr//10

print("kyn ",cpt ,"fois",c,"dans",a)"""
"""Ecrire un programme qui permet de déterminer si un nombre est uniforme. Un nombre est
uniforme si tout ses chiffres sont identitiques."""
"""u=int(input("medli nombre ta3k"))
un=u
x=False
c=u%10
while u!=0 and x==False :
    n=u%10
    if n!=c :
        x=True
    u=u//10
if u==0 :
    print (un,"est uniforme")
else :
    print(un,"nest pas uniforme")"""

    

    


