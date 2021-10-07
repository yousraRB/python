import sqlite3

"""• Départements :( DNO int, DNOM, DIR, VILLE)
• Employés : ( ENO, ENOM, PRof, DATEEMB, SALaire , COMM, #dno)
1. Donnez la liste des employés ayant une commission
2. Donnez les noms, emplois et salaires des employés par emploi croissant, et pour chaque emploi,
par salaire décroissantOF entier
3. Donnez le salaire moyen des employés
4. Donnes les numéros de département et leur salaire maximum"""
"""dp=sqlite3.connect("exo2.db")
dp.execute("CREATE TABLE DEPARTEMENT  (DNO INTEGER PRIMARY KEY,nom char(20),dir char(10),ville char(10));")
dp.execute("CREATE TABLE EMPLOYES (eno int,enom char (20),prof int,sal real,com char (20),DNO INTEGER ,FOREIGN KEY (DNO) REFERENCES DEPARTEMENT(DNO) ,PRIMARY KEY (eno) );")
dp.execute("INSERT INTO DEPARTEMENT VALUES (?,?,?,?) ;",(1212,"informatique","acad","reghaia") )
dp.execute("INSERT INTO DEPARTEMENT VALUES (?,?,?,?) ;",(1313,"informatique","isil","bbzouar") )
dp.execute("INSERT INTO EMPLOYES VALUES (?,?,?,?,?,?) ;",(2020,"NESSRINE",555,20000,"consiel",1212))
dp.execute("INSERT INTO EMPLOYES VALUES (?,?,?,?,?,?) ;",(1413,"yousra",666,20000,None,1313))
dp.commit()
emp=dp.execute("SELECT * FROM EMPLOYES WHERE com NOT NULL  ;")
for r in emp :
    print( r[0] ," " ,r[1]," " ,r[2], " ",r[3]," ",r[4]," " ,r[5])
dp.close()"""
""""nc=sqlite3.connect("exo2.db")
for n in nom :
    print (n[0],n[1],n[2])
nc.close ()"""
"""dp=sqlite3.connect("exo2.db")
moy=dp.execute("SELECT AVG(sal) AS moy FROM EMPLOYES ;")
for m in moy :
    print (m[0])
dp.close()"""
dp=sqlite3.connect("exo2.db")
dp.execute("INSERT INTO EMPLOYES VALUES (?,?,?,?,?,?) ;",(3030,"NESSRINE",555,50000,"consiel",1212))
dp.commit()
max=dp.execute("SELECT DNO,MAX(sal) AS max FROM EMPLOYES GROUP BY DNO  ;")
for m in max :
    print (m[0],m[1])
dp.close ()








