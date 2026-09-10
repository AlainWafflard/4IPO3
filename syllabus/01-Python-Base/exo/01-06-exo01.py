
m = 0
n = 1

print("**{0:>2}***{1:>4}**".format("**", "****"))

for i in range(12):
    p = m + n
    print("* {0:>2} : {1:>4} *".format(i+1, p))
    m = n
    n = p

print("**{0:>2}***{1:>4}**".format("**", "****"))
