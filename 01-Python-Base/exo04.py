
corbeille = {
    "pomme"     : 1,
    "poire"     : 3,
    "raisin"    : 5,
    "mangue"    : 3,
}


corbeille["raisin"] += 5
# corbeille.append({"tomate":6})/
corbeille["tomate"] = 6

print(corbeille)
# print(corbeille["pomme"])
# print(corbeille["noix"])
print(corbeille.get("noix",0))

for key, val in corbeille.items():
    if val == 3 :
        print(key)

