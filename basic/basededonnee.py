import sqlite3 
#creation base de donnee 
#db=sqlite3.connect("first.db")
#print("ona cree la base ")
#creation dune table dans la base 
#db.execute("CREATE TABLE ETUDIANT
          # (matricule CHAR(20) PRIMARY KEY,
           #nom char(20),""
           #prenom char(20),
           #moyenne real );""")
#db.close()

#Representaion (Num_Rep , titre_Rep , lieu)
#rp=sqlite3.connect("first.db")
#rp.execute("""CREATE TABLE REPRESENTATION 
           # (num int  PRIMARY KEY,
    #        titre char(20),
           # lieu char(20));""")
#rp.close()


#ajouter des valeurs dans la base de donnee
"""db=sqlite3.connect("first.db")
db.execute("INSERT INTO ETUDIANT VALUES(?,?,?,?);",("203031050460","LILA"," liPada",17.89))
db.commit()
db.close ()"""


#rah njbdo linformation dylna 
"""db=sqlite3.connect ("first.db")
result= db.execute("SELECT * FROM ETUDIANT ;")
for r in result :
       print(r[0]," ",r[1]," ",r[2]," " ,r[3])
db.close ()"""
"""db=sqlite3.connect("first.db")
resault=db.execute("SELECT  nom ,prenom FROM ETUDIANT ;")
for r in resault :
       print(r[0]," ",r[1])
db.close ()"""


#rechercher un information dans la base 
"""db=sqlite3.connect("first.db")
resault=db.execute("SELECT * FROM ETUDIANT WHERE matricule=? ;",("202031050460",))
for r in resault:
       print(r[0]," ",r[1]," ",r[2]," " ,r[3])
db.close()"""
#insere des valeur en representaion affiche et recherche ...self.
rp=sqlite3.connect("first.db")
rp.execute("INSERT INTO REPRESENTAION VALUES (?,?,?);",(2200,"kike" ,"alg"))
rp.commit()
rp.close()
#affiche linfo
rp=sqlite3.connect("first.db")
info=rp.execute("SELECT num ,lieu FROM REPRESENTAION ;")
for i in info :
       print (i[0],"",i[1])
rp.close ()
#recherche info 
rp=sqlite3.connect("first.db")
reso=rp.execute("SELECT lieu FROM REPRESENTAION WHERE num=? ;",(2200,))
for j in reso :
       print (j[0])
       












