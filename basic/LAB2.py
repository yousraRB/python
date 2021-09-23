"""Soit la chaine suivante s='python'.
utiliser l'indexation pour afficher ce qui suit:
1. y
2. o
3. py
4. th
5. thon """
"""s='python'
print(s[1])
print (s[4])
print(s[:2])
print(s[2:4])
print(s[2:])"""


"""Soit la liste suivante: l = [3, 7, [1, 4, 'bonjour']]
modifier le mot 'bonjour' par le mot 'salam'"""
"""l=[3,7,[1,4,'bonjour']]
print(l[2][2])
l[2][2]='salam'
print(l)"""

"""Soit la liste suivante: [1,1,1,1,1,2,2,2,3,3,3,3,3,3]
créer une nouvelle contenant les éléments de la première liste sans répétition, et afficher le résultat"""
"""l=[1,1,1,1,1,2,2,2,3,3,3,3,3,3]
m=set(l)
print(m)"""

"""Soit la liste suivante: liste = [1, 2, ['x', 'y', 'z']]
• afficher le chiffre 2
• afficher la lettre y
• afficher x et y"""
"""l=[1, 2, ['x', 'y', 'z']]
print(l[1])
print(l[2][1])
print(l[2][:2])"""
"""n=int(input("taille"))
l=[]
for i in range (n):
    val=int(input ("ara valeur"))
    l.append(val)
print(l)
for var in l :
    print (var)"""


"""Afficher le mot 'bonjour' dans les cas suivants:
d1 = {'cle': 'bonjour'}
• d2 = {'cle': {'cle2': 'bonjour'}}
• d3 = {'cle': [ { 'cle2' : [ 'cle3', [ 'bonjour' ] ] } ] } """

"""d1 = {'cle': 'bonjour'}
print(d1['cle'])
d2 = {'cle': {'cle2': 'bonjour'}}
print (d2['cle' ]['cle2'])
d3 = {'cle': [ { 'cle2' : [ 'cle3', [ 'bonjour' ] ] } ] } 
print(d3['cle'][0]['cle2'][1])"""


    
    




