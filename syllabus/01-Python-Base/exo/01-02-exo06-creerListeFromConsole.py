# créez liste à partir de la console
# Remarquez le "while true"

q = []
while True:
    x = input("entrez un nombre : ")
    if( x == "q" ):
        break
    q.append(int(x))

print("q=", q )
