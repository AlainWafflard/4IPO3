# factorielle

# vu que
# factorielle de 4 = 4 * 3 * 2
# et que 
# factorielle de 5 = 5 * 4 * 3 * 2
# on peut écrire que
# factorielle de 5 = 5 * factorielle de 4

def factorielle(n):
    if n <= 1 :
        return 1
    else:
        return n * factorielle(n-1)

x = int(input("factorielle de ? "))
print(factorielle(x))
