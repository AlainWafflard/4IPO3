# reference
# https://docs.python.org/3/tutorial/errors.html

class TooBigNumberException(Exception):
    """
    Programs may name their own exceptions by creating a new exception class.
    Exceptions should typically be derived from the Exception class, either directly or indirectly.
    Exception classes can be defined which do anything any other class can do, but are usually kept simple,
    often only offering a number of attributes
    that allow information about the error to be extracted by handlers for the exception.
    """
    def __init__(self, val ):
        print("TooBigNumberException : Jedi says 'too high value, {} is'".format(x))
        # in this example, the exception is only printed
        # but the exception can also be appended in  a log-table, sent by mail to someone, etc.


# MAIN
# the purpose of this code is to get a number lower than 5 from a stupid user
if __name__ == '__main__':
    try:
        x = int(input("Please enter a number above 5 and below 10 : "))
        # make an error :
        # type a text instead of a number
        # => a "ValueError" exception will be launched

        if x < 5 :
            # make an error :
            # type a number below 5
            # => a user-defined "TooBigNumberError" exception will be launched
            raise Exception("Standard Exception: Jedi says 'too low value, {} is'".format(x))

        if x > 10 :
            # make an error :
            # type a number above 10
            # => a user-defined "TooBigNumberError" exception will be launched
            raise TooBigNumberException(x)

    except ValueError:
        print("Jedi says : no valid number, it is.  Try again...")

    else:
        # input is OK
        print("Everything OK : Jedi says 'Welcome Jedi number {}'".format(x))

    finally:
        print("end of MAIN")


