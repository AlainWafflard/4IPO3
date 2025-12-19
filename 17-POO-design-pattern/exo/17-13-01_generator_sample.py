
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


def finite_sequence_with_yield(target):
    """ sample of a infinite sequence
        and yield
    """
    num = 0
    while num < target:
        yield num
        num += 2


# MAIN
if __name__ == "__main__":
    print("finite sequence, return, for-loop")
    for i in finite_sequence_with_return():
        print(i, end=" ")
    print()

    print("infinite sequence, yield, for-loop")
    for j in infinite_sequence_with_yield():
        if j >= 50 :
            print()
            break
        print(j, end=" ")

    print("infinite sequence, generator")
    gen1 = infinite_sequence_with_yield()
    # print(" generator ? oui, à cause du yield : ", gen)
    while True :
        k = next(gen1)
        if k >= 50 :
            print()
            break
        print(k, end=" ")
    print("+", next(gen1), end=" ")
    print("+", next(gen1), end=" ")
    print()

    print("finite sequence, generator")
    gen2 = finite_sequence_with_yield(50)
    while True :
        k = next(gen2, None)
        if k is None :
            print()
            break
        print(k, end=" ")

