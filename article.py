class Articulo:
    def __init__(self, cod, des, pri, sto):
        self.code = cod
        self.description = des
        self.price = pri
        self.stock = sto

class Cliente:
    def __init__(self, id_card, nom, dire, pho):
        self.id_card = id_card
        self.nombre = nom
        self.direccion = dire
        self.phone = pho
    
class Venta:
    def __init__(self, fac, dat, cli, tot, detal_vent):
        self.factura = fac
        self.dato = dat
        self.cliente = cli
        self.total = tot
        self.detale_venta = detal_vent

class SaleDet:
    def __init__(self, arti, pre, mon):
        self.articulo = arti
        self.precio = pre
        self.monto = mon