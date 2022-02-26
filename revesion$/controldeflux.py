# # EXO01
# # Saisissez un flottant. S’il est positif ou nul, affichez sa racine, sinon affichez un message
# # d’erreur.

# import math as rac
# flottant=input("give me a number ")
# flottant=float(flottant)

# if flottant>=0 :
#     print(rac.sqrt(flottant))
# else :
#     print("errur")

# # exo02
# #  On désire sécuriser une enceinte pressurisée.
# # On se fixe une pression seuil et un volume seuil : pSeuil = 2.3, vSeuil = 7.41.
# # On demande de saisir la pression et le volume courant de l’enceinte et d’écrire un script
# # qui simule le comportement suivant :
# # – si le volume et la pression sont supérieurs aux seuils : arrêt immédiat ;
# # – si seule la pression est supérieure à la pression seuil : demander d’augmenter le volume de l’enceinte ;
# # – si seul le volume est supérieur au volume seuil : demander de diminuer le volume
# # de l’enceinte ;
# # – sinon déclarer que « tout va bien ».
# # Ce comportement sera implémenté par une alternative multiple

# ps=2.3
# vs=7.41
# p=input("puissance : ")
# p=float(p)
# v=input("volume : ")
# v=float(v)
# if v>vs and p>ps :
#     print("arret immédiat")
# elif p>ps and v<vs :
#     print("augmenter le volume encient !")
# elif v>vs and p<ps :
#     print("diminuer l'encient volume")
# else : print("tout va bien ")

# # Initialisez deux entiers : a = 0 et b = 10.
# # Écrire une boucle affichant et incrémentant la valeur de a tant qu’elle reste inférieure
# # à celle de b.
# # Écrire une autre boucle décrémentant la valeur de b et affichant sa valeur si elle est
# # impaire. Boucler tant que b n’est pas nul.

# a=0
# b=10
# for i in range(a,b):
#     print (i)
# for i in range(b,a,-1):
#     if i%2!=0 :
#         print (i)

# # Affichez chaque caractère d’une chaîne en utilisant une boucle for.
# # Affichez chaque élément d’une liste en utilisant une boucle 

# chaine="lolalilayiya"
# for i in chaine :
#     print (i)

# lista=[12,"youu",56]
# for i in lista :
#     print (i)

# #  Affichez les entiers de 0 à 15 non compris, de trois en trois, en utilisant une boucle for
# # et l’instruction range().

# a=0
# b=15
# for i in range(a,b,3):
#     print(i)

# #  Utilisez l’instruction break pour interrompre une boucle for d’affichage des entiers
# # de 1 à 10 compris, lorsque la variable de boucle vaut 5

# for i in range(a,b):
#     if i==5 :
#         break
#     print (i)

# # Utilisez l’instruction continue pour modifier une boucle for d’affichage de tous entiers de 1 à 10 compris,
# # sauf lorsque la variable de boucle vaut 5

# a=0
# b=15
# for i in range(a,b):
#     if i==5 :
#         continue
#     print (i)

# #  La clause else des boucles. Dans cet exercice, effectuez les saisies avec des integerbox
# # et les affichages avec des msgbox, tous deux appartenant au module easygui.
# # Initialisez une liste avec 5 entiers de votre choix puis saisissez un entier.
# # Dans une boucle for, parcourez la liste. Si l’entier saisie appartient à la liste, sauvez-le
# # et interrompez la boucle (puisque vous l’avez trouvé). Si la boucle s’est bien terminée,
# # utilisez une clause else pour afficher un message l’annonçant.
# # Entrez mai
from easygui import integerbox,msgbox

lista=[1,2,3,4,5]
val=integerbox(" mdli entier")
for i in range(0,5,1):
    if i==val:
        msgbox ("le nombre est existe")
        break
    elif i==4 :
        msgbox ("n'existe pas")








