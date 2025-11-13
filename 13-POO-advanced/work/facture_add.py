
class InvoiceDetail:
    def __init__(self, name, price, qnt):
        self.name = name
        self.price = price
        self.qnt  = qnt

    def __add__(self, other):
        return ( self.price * self.qnt ) + ( other.price * other.qnt)

    def __sub__(self, other):
        return ( self.price * self.qnt ) - ( other.price * other.qnt)


if __name__ == "__main__":
    id1 = InvoiceDetail( "sac de pommes", 2.0, 4)
    id2 = InvoiceDetail( "sac de poires", 2.5, 3)
    print( "montant à payer :", id1 + id2 )
    print( "montant soustrait :", id1 - id2 )
