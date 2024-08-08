import conexao

class Remedio:
    
    def _init_(self):
        self.__nomeRemedio = ""
        self.__ean13 = ""
        self.__data = ""
        self.__hora = ""
        self.__lote = 0
        self.__preco = 0
        self.__quantidadeDoProduto = 0
    
    def getCategoria(self, nomeCategoria):
        self.__nomeCategoria = nomeCategoria
        return self.__nomeCategoria

    def getRemedio(self, nomeRemedio):
        self.__nomeRemedio = nomeRemedio
        return self.__nomeRemedio
    
    def reduzEstoque(self, quantidadeDoProduto):
        
        self.__quantidadeDoProduto = quantidadeDoProduto
        self.__quantidadeDoProduto -= 1
    
    
    def geraNotaFiscal(self):
        self.reduzEstoque()
        return self.__nomeRemedio, self.__data, self.__hora, self.__lote, self.__preco, self.__quantidadeDoProduto  
    
    def aumentaEstoque(self):
        self.__quantidadeDoProduto += 1
        
    def registraEntrada(self, nomeFornecedor):
        self.aumentaEstoque()
        return self.__nomeRemedio, nomeFornecedor, self.__data, self.__lote, self.__preco, self.__quantidadeDoProduto  
        
            

        
        
            
    
class Vendas:
    
    def _init_(self, nomeFornecedor):
        self.__nomeFornecedor = nomeFornecedor
        
    def getFornecedor(self):
        return self.__nomeFornecedor

class RemedioDAO:

    def criar(self, ean13, data, hora, lote, preco):
        remedio = Remedio(ean13, data, hora, lote, preco)
        return remedio
        
def main():
    remedio = RemedioDAO()

    venda = Vendas("EU")

main()