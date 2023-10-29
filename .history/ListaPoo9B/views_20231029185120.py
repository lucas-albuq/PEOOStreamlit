from ListaPoo9b.cliente import Cliente, NCliente

class View:
    @classmethod
    def cliente_inserir(cls, nome, email, fone):
        c = Cliente(0, nome, email, fone)
        NCliente.inserir