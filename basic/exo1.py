""" Soit la base de données d’un festival de musique : Dans une représentation peut participer 
un ou plusieurs musiciens. Un musicien ne peut participer qu’à une seule représentation.
• Representation (Num_Rep , titre_Rep , lieu)
• Musicien (Num_mus , nom , #Num_Rep)
• Programmer (idProgrammer , #Num_Rep , tarif)
1. La liste des titres des représentations.
2. La liste des titres des représentations ayant lieu au «  alg».
3. La listeti des noms des musiciens et les titres des représentaons auxquelles ils participent.
4. Le nombre des musiciens qui participent à la représentations n°2."""

import sqlite3
"""nc=sqlite3.connect("exo.db")
nc.execute(" CREATE TABLE REPRESENTATI(num INTEGER  PRIMARY KEY ,titre char(20) ,lieu varchar(20) );")
nc.execute("CREATE TABLE MUSICIEN (num INTEGER PRIMARY KEY,nom char(20),numrep INTEGER ,FOREIGN KEY(numrep) REFERENCES REPRESENTATION(num));")
nc.execute("CREATE TABLE PROGRAMMER  (id INTEGER ,numrep INTEGER , tarif REAL,FOREIGN KEY(numrep) REFERENCES REPRESENTATION(num),PRIMARY KEY(id,numrep));")

nc.execute("INSERT INTO REPRESENTATION VALUES (?,?,?) ;",(111,"3onwan","alg"))

nc.execute("INSERT INTO REPRESENTATION VALUES (?,?,?) ;",(222,"3onwan2","alg2"))

nc.execute("INSERT INTO MUSICIEN VALUES (?,?,?) ;",(1111,"KIKA",111))

nc.execute("INSERT INTO MUSICIEN VALUES (?,?,?) ;",(2222,"lil",111))

nc.execute("INSERT INTO  PROGRAMMER  VALUES (?,?,?) ;",(11111,111,15.44))

nc.execute("INSERT INTO  PROGRAMMER  VALUES (?,?,?) ;",(22222,221,10.44))
nc.commit()"""
"""nc=sqlite3.connect("exo.db")
titre=nc.execute("SELECT titre FROM REPRESENTATION ;")
for t in titre :
    print (t[0])
nc.close()
"""
"""nc=sqlite3.connect("exo.db")
titre = nc.execute("SELECT titre FROM REPRESENTATION WHERE lieu= ? ;",("alg",))
for t in titre :
    print (t[0])
nc.close()
"""
"""nc=sqlite3.connect("exo.db")
nc.execute("INSERT INTO MUSICIEN VALUES (?,?,?) ;", (1001,"KIKA",222))
nom=nc.execute("SELECT M.nom ,R.titre FROM MUSICIEN M ,  REPRESENTATION R WHERE M.numrep=R.num and M.nom=? ;",("KIKA",) )
for n in nom :
    print (" nom :",n[0],"titre :", n[1])
nc.close()"""
"""nc=sqlite3.connect("exo.db")
nombre=nc.execute("SELECT COUNT(*) AS NOMBRE FROM  REPRESENTATION WHERE num=? ;",(111,))
for n in nombre :
    print (n[0])
nc.close ()"""






