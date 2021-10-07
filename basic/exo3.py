import sqlite3
"""Exercice 03: Soit la base de données relationnelle des vols quotidiens d’une compagnie aérienne qui 
contient les tables Avion, Pilote et Vol. 
Table Avion (
NA : numéro avion de type entier (clé primaire), 
Nom : nom avion de type texte (12), 
Capacite : capacité avion de type entier, 
Localite : ville de localité de l’avion de type texte (10) 
) 
Table Pilote (
NP : numéro pilote de type entier, 
Nom : nom du pilote de type texte (25), 
Adresse : adresse du pilote de type texte (40) 
) 
Table Vol (
NV : numéro de vol de type texte (6), 
NP : numéro de pilote de type entier, 
NA : numéro avion de type entier, 
VD : ville de départ de type texte (10), 
VA : ville d’arrivée de type texte (10), 
HD : heure de départ de type entier, 
HA : heure d’arrivée de type entier 
) 
1) Insérer les avions suivants dans la table Avion : 
• (100, AIRBUS, 300, RABAT)
• (101,B737,250,CASA)
• (101, B737,220,RABAT) 
2) Afficher tous les avions
3) Afficher tous les avions par ordre croissant sur le nom
4) Afficher les noms et les capacités des avions
5) Afficher les localités des avions sans redondance
6) Afficher les avions dans la localité et Rabat ou Casa
7) Modifier la capacité de l’avion numéro 101, la nouvelle capacité et 220
8) Supprimer les avions dans la capacité et inférieure à 200
9) Afficher la capacité maximale, minimale, moyenne des avions
10) Afficher les données des avions dont la capacité et la plus basse
11) Afficher les données des avions dont la capacité et supérieure à la capacité moyenne
12) Afficher le nom et l’adresse des pilotes assurant les vols IT100 et IT104
13) Afficher les numéros des pilotes qui sont en service
14) Afficher les numéros des pilotes qui ne sont pas en service
15) Afficher les noms des pilotes qui conduisent un AIRBUS"""
db=sqlite3.connect("exo3.db")
"""db.execute("CREATE TABLE AVION (NA INTEGER  PRIMARY KEY,nom char(12),capacite INTEGER,localite char(10));")
db.execute("CREATE TABLE PILOTE (n INTEGER PRIMARY KEY,nom char(25),adres char(40));")
db.execute("CREATE TABLE VOL (nv char (6) PRIMARY KEY,np INTEGER,na INTEGER,vd char(20),va char(20),hd INTEGER,ha INTEGER,FOREIGN KEY (na)REFERENCES AVION (NA),FOREIGN KEY (np) REFERENCES PILOTE (n));") 
db.execute("INSERT INTO AVION VALUES (?,?,?,?) ;",(100, "AIRBUS", 300, "RABAT"))
db.execute("INSERT INTO AVION VALUES (?,?,?,?) ;",(101,"B737",250,"CASA"))
db.execute("INSERT INTO AVION VALUES (?,?,?,?) ;",(102," B737",220,"RABAT"))
db.commit()"""
#DESC :ordre decroissent / ASC :croissent 
print ("affichage tous les avions")
avions=db.execute("SELECT * FROM AVION ;")
for a in avions :
    print (a[0],a[1],a[2],a[3])
print("Afficher tous les avions par ordre croissant sur le nom")
avions=db.execute("SELECT * FROM AVION ORDER  BY nom  DESC ;")
for a in avions :
    print (a[0],a[1],a[2] ,a[3])
print ("Afficher les noms et les capacités des avions")
avions=db.execute("SELECT nom,capacite FROM AVION ;")
for a in avions :
    print (a[0],a[1])
print("Afficher les localités des avions sans redondance ")

#DISTINCT : tanhi les redondance 
avions=db.execute("SELECT DISTINCT localite  FROM AVION ;")
for b in avions  :
    print(b[0])

print("Afficher les nom avions dans la localité et Rabat ou Casa")
avions=db.execute("SELECT nom FROM AVION WHERE localite =? or localite =? ;",("RABAT","CASA"))
for a in avions :
    print (a[0])
print("Afficher la capacité maximale, minimale, moyenne des avions")
max=db.execute("SELECT MAX(capacite) AS max,MIN(capacite) AS min,AVG(capacite) AS moy FROM AVION ;")
for a in max :
    print ("max :",a[0],"min :",a[1],"moyenne",a[2])
min=a[1]
print("Afficher les données des avions dont la capacité et la plus basse")
cap=db.execute("SELECT * FROM AVION WHERE capacite=(SELECT MIN(capacite)  FROM AVION) ;")
for c in cap :
    print(c[0],c[1],c[2],c[3])
print("Afficher les données des avions dont la capacité et supérieure à la capacité moyenne")
cap=db.execute("SELECT * FROM AVION WHERE capacite>=(SELECT AVG(capacite) FROM AVION);")
for c in cap :
    print (c[0],c[1],c[2],c[3])
print ("Afficher le nom et l’adresse des pilotes assurant les vols IT100 et IT104")
vol=db.execute("SELECT p.nom,p.adres FROM PILOTE p,VOL v WHERE v.NV=? and  v.NV=? and p.n=v.np  ;",("IT100","IT104"))
for v in vol :
    print (v[0],v[1])
print ("Afficher les numéros des pilotes qui sont en service")
np=db.execute("SELECT NP FROM VOL ; ")
for n in np :
    print(n[0])
print ("Afficher les numéros des pilotes qui ne sont pas en service")
np=db.execute("SELECT n FROM PILOTE WHERE n NOT IN  (SELECT np FROM VOL); ")
for n in np :
    print(n[0])
print ("Afficher les noms des pilotes qui conduisent un AIRBUS")
np=db.execute("SELECT p.nom FROM PILOTE P,VOL v,AVION a WHERE p.n=v.np and a.NA=v.na and a.nom=? ;",("AIRBUS",))
for n in np :
    print(n[0])
#7) Modifier la capacité de l’avion numéro 101,
print ("la nouvelle capacité et 220")
#update: pour modifier 
db.execute("UPDATE  AVION  SET capacite=999 WHERE NA=101 ;")
db.commit()
np=db.execute("SELECT capacite FROM AVION WHERE NA=101 ;")
for n in np :
    print (n[0])
#8)Supprimer les avions dans la capacité et inférieure à 300
print("apres la suppression ")
db.execute("DELETE  FROM AVION WHERE capacite<=300 ;")
db.commit()
np=db.execute("SELECT * FROM AVION  ;")
for n in np :
    print (n[0],n[1],n[2],n[3])
