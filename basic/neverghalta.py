"""Homework: Créer des requêtes en SQL
ETUDIANT (Numetu, Nometu, Dtnaiss, Cdsexe)
SEXE (Cdsexe, bsexeL)
ENSEIGNANT (Numens, Nomens,grade, Ancien)
MATIERE (Numat, Nomat, Coeff, Numens)
NOTES (Numetu, Numat, Note)
À partir de la Base de données ETUDIANTS ci dessus, écrire les requêtes SQL permettant de répondre
aux questions suivantes.
1. Afficher quel était l'âge moyen des garçons et des filles au premier janvier 2000.
2. Afficher le nom et le grade des enseignants d'histoire.
3. Afficher les noms et numéro des étudiants qui n'ont pas de notes en Sociologie.
4. Afficher le nom et le coefficient des matières qui sont enseignées par des maîtres de conférences
ou des assistants.
5. Afficher pour chaque étudiant (nom et numéro), et par ordre alphabétique, la moyenne qu'il a
obtenue dans chaque matière.
6. Afficher le nom, l'âge et le sexe des étudiants qui ont eu une note d'informatique supérieure à la
moyenne générale de la classe.
7. Afficher, pour chaque étudiant (nom et numéro) qui a une note dans chacune des matières, la
moyenne obtenue au diplôme.
8. Afficher le nom le grade et l'ancienneté des enseignants qui enseignent dans plus d'une matière.
9. Afficher le nombre de garçons et le nombre de filles qui ont réussi au diplôme : moyenne >= 10"""
import sqlite3
db=sqlite3.connect("maneghltch.db")
db.execute("CREATE TABLE  ETUDIANT (numetu char (20) PRIMARY KEY,nometu char(20),dtnaiss char(20),cdsex char(20),FOREIGN KEY (cdsex) REFERENCES SEXE (cdsex));")
db.execute("CREATE TABLE SEXE (cdsexe char(20) PRIMARY KEY, bsexel char(20) ;")
db.execute("CREATE TABLE ENSEIGNANT (numens char(20) PRIMARY KEY,nomens char(20),grad char(20),ancien INTEGER ;")
db.execute("CREATE TABLE MATIERE (numat char(20) PRIMARY KEY ,nomat char(20),coef INTEGER,numens char(20,FOREIGN KEY (numens) REFERENCES ENSEIGNANT (numens);")
db.execute("CREATE TABLE NOM (numetu char(20) ,numat char(20) ,note real,FOREIGN KEY(numat)REFERENCES (numat),PRIMARY KEY(numat,numet);")
db.execute("INSERT INTO ETUDIANT (?,?,?,?) ;",("12345","aoka","10/11/1999)","h"))
db.execute("INSERT INTO ETUDIANT (?,?,?,?) ;",("12346","yoma","10/11/1990)","f"))
db.execute("INSERT INTO ETUDIANT (?,?,?,?) ;",("12347","zola","10/11/1989)","h"))
db.execute("INSERT INTO ETUDIANT (?,?,?,?) ;",("12348","xona","10/11/1979)","f"))
db.execute("INSERT INTO SEXE (?,?) ;",("h","homme"))
db.execute("INSERT INTO SEXE (?,?) ;",("f","femme"))
db.execute("INSERT INTO ENSEIGNANT (?,?,?,?) ;",("1","hommer","assistant",5))
db.execute("INSERT INTO ENSEIGNANT (?,?,?,?) ;",("2","zommer","conferences",5))
db.execute("INSERT INTO ENSEIGNANT (?,?,?,?) ;",("3","yommer","professeur",30))
db.execute("INSERT INTO ENSEIGNANT (?,?,?,?) ;",("4","lommer","professeur",30))
db.execute("INSERT INTO MATIER (?,?,?,?) ;",("1","informatique",3,3))
db.execute("INSERT INTO MATIER (?,?,?,?) ;",("2","histoire",1,1))
db.execute("INSERT INTO MATIER (?,?,?,?) ;",("4","histoire",1,4))
db.execute("INSERT INTO MATIER (?,?,?,?) ;",("3","Sociologie",2,2))
db.execute("INSERT INTO NOTE (?,?,?) ;",("12345","1",15.5))
db.execute("INSERT INTO NOTE (?,?,?) ;",("12345","3",None))
db.execute("INSERT INTO NOTE (?,?,?) ;",("12346","3",None))
db.commite()
"""print("Afficher quel était l'âge moyen des garçons et des filles au premier janvier 2000.")
db.execute("SELECT dtnaiss FROM ETUDIANT AS DATE ;")"""
print ("Afficher le nom et le grade des enseignants d'histoire.")
prof=db.execute("SELECT E.nomens,E.grad FROM ENSEIGNANT E ,MATIER M WHERE E.numens=M.numens and M.nomat=?;",("histoire"))
for p in prof :
    print ("nom:"+p[0]+"grade:"+ p[1])
print ("Afficher les noms et numéro des étudiants qui n'ont pas de notes en Sociologie.")
nom=db.execute("SELECT DISTINCT E.nometu,E.numetu FROM ETUDIANT E, NOTE N, MATIER M WHERE E.numetu=N.numetu and M.numat=N.numat and M.nom='Sociologie' and N.note is null)); ")
for n in nom :
    print (n[0],n[1])
#Afficher le nom et le coefficient des matières qui sont enseignées par des maîtres de conférences


