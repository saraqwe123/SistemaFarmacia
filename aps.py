class Remedio:
    
    def __init__(self, ean13, data, hora, lote, preco):
        self.__nomeRemedio = ""
        self.__ean13 = ean13
        self.__data = data
        self.__hora = hora
        self.__lote = lote
        self.__preco = preco
        self.__quantidadeDoProduto = 0
        self.__quantidadeAumentada = 0
        self.__quantidadeReduzida = 0

    def getCategoria(self, nomeCategoria):
        self.__nomeCategoria = nomeCategoria
        return self.__nomeCategoria

    def getRemedio(self, nomeRemedio):
        self.__nomeRemedio = nomeRemedio
        return self.__nomeRemedio
    
    def getEstoque(self, quantidadeDoProduto):
        self.__quantidadeDoProduto = quantidadeDoProduto
        return self.__quantidadeDoProduto
    
    def reduzEstoque(self, quantidadeReduzida):
        self.__quantidadeReduzida = quantidadeReduzida
        self.__quantidadeDoProduto = self.__quantidadeDoProduto - self.__quantidadeReduzida
        return self.__quantidadeDoProduto
    
    def aumentaEstoque(self, quantidadeAumentada):
        self.__quantidadeAumentada = quantidadeAumentada
        self.__quantidadeDoProduto = self.__quantidadeDoProduto + self.__quantidadeAumentada

    def geraNotaFiscal(self):
        return self.__nomeRemedio, self.__data, self.__hora, self.__lote, self.__preco, self.__quantidadeDoProduto, self.__nomeCategoria 
        
    def registraEntrada(self, nomeFornecedor):
        self.aumentaEstoque(self.__quantidadeAumentada)
        return self.__nomeRemedio, nomeFornecedor, self.__data, self.__lote, self.__preco, self.__quantidadeDoProduto, self.__nomeCategoria
        
class Vendas:
    
    def __init__(self, nomeFornecedor):
        self.__nomeFornecedor = nomeFornecedor
        
    def getFornecedor(self):
        return self.__nomeFornecedor

class RemedioDAO:

    def criar(self, ean13, data, hora, lote, preco):
        remedio = Remedio(ean13, data, hora, lote, preco)
        return remedio
        
def main():
    remedio = RemedioDAO()
    remedioNovo = remedio.criar(23123123123, "19/04/2023", "15:08:09", 3, 3.99)
    remedioNovo1 = remedio.criar(23123123123, "29/02/2012", "17:38:29", 6, 7.99)

    venda = Vendas("EU")

    print(remedioNovo.getRemedio("dipirona"))
    print(remedioNovo.getCategoria("antibiotico"))
    print(remedioNovo.getEstoque(500))
    print(remedioNovo.reduzEstoque(8))
    print(remedioNovo.geraNotaFiscal()) 
    print(remedioNovo1.getRemedio("anador"))
    print(remedioNovo1.getCategoria("analgesico"))
    print(remedioNovo1.registraEntrada(venda.getFornecedor()))

main()