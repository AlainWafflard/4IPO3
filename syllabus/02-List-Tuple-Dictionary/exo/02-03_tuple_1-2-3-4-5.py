#Votre entreprise comprend trois membres du personnel.  Modélisez chaque
#personne sous forme d’un tuple, placez tous ces tuples dans une liste
#et imprimez-la.
#- Alain Térieur, 1170 Bruxelles, 55 ans
#- Alex Térieur, 1140 Bruxelles, 50 ans
#- Jean Neymar, 1030 Bruxelles, 45 ans 

# tuple personne : Prénom, Nom, code postal, âge

# 1ère manière
personne1 = ( "Alain", "Térieur", 1170, 55 )
personne2 = ( "Alex", "Térieur", 1140, 50 )
personne3 = ( "Jean", "Neymar", 1030, 45 )
l = [ personne1, personne2, personne3 ]
print( "SQ1, 1e manière : toute la liste : ", l )

# 2e manière
employee_l = [
    ( "Alain", "Térieur", 1170, 55 ),
    ( "Alex", "Térieur", 1140, 50 ),
    ( "Jean", "Neymar", 1030, 45 ),
]
print( "SQ1, 2e manière : toute la liste : ", employee_l )

# sous question 2
# Imprimer une fraction de la liste de tuples 
print( "SQ2 : juste le nom de la 3e personne :", employee_l[2][1])

# sous question 3
# chercher et imprimer le prénom de Neymar
on_cherche = "Neymar"
for e in employee_l :
    if e[1] == on_cherche :
        print( "SQ3 : prénom de" , on_cherche, " : ", e[0] )

# sous question 4
# construire liste avec prénoms des « Térieur ».
# 1ère manière
on_cherche = "Térieur"
lst1 = []
for e in employee_l :
    if e[1]==on_cherche :
        lst1.append(e[0])
print( "SQ4, 1e manière :", lst1)

# 2ère manière, en compréhension
lst2 = [ e[0] for e in employee_l if e[1]==on_cherche ]
print( "SQ4, 2e manière :", lst2)
sep = " et "
str2 = sep.join(lst2)
print( "SQ4, le string : ", str2)

# sous question 5
# imprimer tous les prénoms
print( "SQ5, 1e manière : ", [ l[i][0] for i in range(len(l))] )
print( "SQ5, 2e manière : ", " et ".join([ emp[0] for emp in employee_l ]))


