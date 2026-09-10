import sys

noteEtudiant = [
    [ 10,13,15,19,16,18,13,13,12,13 ],
    [ 12, 3, 5, 9,10,12, 3,10,12,10 ],
    [ 12,15,14,19,16,20,15,16,13,13 ],
    [ 10,16,12,14,15,17,13,14,15, 7 ],
    [ 16,12,16,12,10,11, 9,14,13, 9 ],
]
nomCours = [ "Math", "Droit", "Marketing", "Communication", "Statistiques", "Ressources Humaines", "Programmation", "Français", "English", "Base de données" ]
nomEtudiant = [ "Julie", "Sophie", "Maxime", "Arthur", "John" ]

# Afficher le nombre de notes dans l’ensemble du tableau qui sont
# au moins égales à 18
n18 = 0 
for l in noteEtudiant:
    for c in l:
        if( c >= 18 ):
            n18 += 1
print( "nb cotes >= 18 :", n18 )

# Déterminer le nombre d’étudiant qui ont au moins un échec
nb_et_echec = 0
for ce in noteEtudiant:
    for c in ce:
        if c < 10 :
            nb_et_echec += 1
            break;
print("nombre étudiants avec échecs :", nb_et_echec)

# n = index étudiant donné
name = str(input("nom de l'étudiant : "))
if( not (name in nomEtudiant )):
    # étudiant non trouvé
    print("cet étudiant n'existe pas")
    sys.exit()
for n in range(len(nomEtudiant)):
    if nomEtudiant[n]==name:
        break;

# Afficher la moyenne de l’étudiant donné
m = 0 
for i in range(len(nomCours)):
    m += noteEtudiant[n][i]
m /= len(nomCours)
print( "Etudiant", nomEtudiant[n], " : moyenne", m )

# Afficher si l’étudiant qui porte le nom donné a eu un échec (note < 10).
l_echec = []
for j in range(len(noteEtudiant[n])):
    if noteEtudiant[n][j] < 10 :
        l_echec.append(nomCours[j])
if(len(l_echec) > 0 ):
    print( "L'étudiant", name, "a un échec en", ",".join(l_echec) )
else:
    print( "L'étudiant", name, "n'a pas d'échec." )

