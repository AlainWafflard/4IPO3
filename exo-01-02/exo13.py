def get_tuple():
    return ( 1, 2, 4 )

if __name__ == "__main__":
    mon_tuple = get_tuple()
    print(mon_tuple)

    x, y, z = get_tuple()
    print(x, y, z, sep="-")
