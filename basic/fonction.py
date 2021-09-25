"""def somme ( a,b):
    s=a+b
    return s

a=int(input("atiini a : "))
b=int(input("atini b :"))

print (somme(a,b))"""

"""n=int (input ("atini n :"))
def fact(n):
    f=1
    for i in range (1,n+1,1):
        f=f*i
    return f
print(fact(n))"""

"""n=int (input ("atini n :"))
def premier (n):
    i=2
    trv=False
    while i<=n/2 and trv==False :
        if n%i==0 :
            trv=True
        i=i+1
    
   
    if trv==True or n==1 or n==0 :
        print(" non premier")
    else:
        print("premier")

premier (n)"""

"""def lista (list,val):
    if val in list:
        print ("kyna")
    else :
        print("mkch")

l=[1,3,5,5,10,20]
val=int (input ("atini val:"))
lista (l,val)"""

"""d1 = {‘nom’: [‘ikram’, ‘nesrine’, ‘manel’, ‘yasmine’], ‘age’: [18, 15, 20]}
1. Ecrivez une fonction lambda permettant de capitaliser une chaine.
2. En utilisant le question 1, mettez la première lettre des noms en majuscule.
3. L’utilisateur a oublié de mentionner l’age de yasmine, donnez lui la chance de corriger son
erreur."""

"""d1 = {'nom': ['ikram', 'nesrine', 'manel','yasmine'], 'age': [18, 15, 20]}
l=[]

for kelma in d1['nom']:
    l.append(kelma.capitalize())

print(l)
d1['age'].append(35)
print(d1)
m=[]
capital=lambda mot : mot.capitalize()

for i in d1['nom']:
    m.append(capital(i))
    
print(m)"""




    
        



