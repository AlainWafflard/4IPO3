# Choisissez la bonne version de Python : 3.12, 3.13 ou 3.14
from Q61_calc import Calculator
# from Q61_calc_314 import Calculator
# from Q61_calc_313 import Calculator
# from Q61_calc_312 import Calculator

# indiquez le nom de votre groupe en argument, par ex. "Héritiers" ou "Pascal Case"
# cal = Calculator("<nom_groupe>")
cal = Calculator("")

p = cal.plus(4, 3)
print("4+3=", p) # 7

m = cal.moins(4, 3)
print("4-3=", m)

f = cal.fois(4, 3)
print("4*3=", f)

d = cal.divise(4, 3)
print("4//3=", d)

# Exemple d'Exception
try:
    # x = 5 / 0
    d = cal.divise(4, 0)
    print(d)
except:
    print("division par zéro impossible")

