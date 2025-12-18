
def finite_sequence_with_return():
    """ sample of a finite sequence
        and return
    """
    return range(0, 50, 2)


def infinite_sequence_with_yield():
    """ sample of a infinite sequence
        and yield
    """
    num = 0
    while True:
        yield num
        num += 2


# MAIN
if __name__ == "__main__":
    print("sequence, return, for loop")
    for i in finite_sequence_with_return():
        print(i, end=" ")
    print()

    print("sequence, yield, for loop")
    for j in infinite_sequence_with_yield():
        if j >= 50 : break
        print(j, end=" ")
    print()

    print("sequence, generator")
    gen = infinite_sequence_with_yield()
    print(gen)
    while True :
        k = next(gen)
        if k >= 10 : break
        print(k, end=" ")

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))