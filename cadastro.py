class Remedio:
    def __init__(self, registroMS, nomeRemedio, ean13, ncm, precoVenda, fabricante, substancia):
        self.nomeRemedio = nomeRemedio
        self.ean13 = ean13
        self.ncm = ncm
        self.precoVenda = precoVenda
        self.fabricante = fabricante            
        self.registroMS = registroMS
        self.substancia = substancia

#EM MOVIMENTAÇÃO
    #def reduzEstoque(self, quantidadeReduzida):
    #    self.__quantidadeReduzida = quantidadeReduzida
    #    self.__quantidadeDoProduto = self.__quantidadeDoProduto - self.__quantidadeReduzida
    #    return self.__quantidadeDoProduto
    #
    #def aumentaEstoque(self, quantidadeAumentada): 
    #    self.__quantidadeAumentada = quantidadeAumentada
    #    self.__quantidadeDoProduto = self.__quantidadeDoProduto + self.__quantidadeAumentada

    #def geraNotaFiscal(self): #
    #    return self.__nomeRemedio, self.__lote, self.__preco, self.__quantidadeDoProduto, self.__nomeCategoria 
    #    
    #def registraEntrada(self, nomeFornecedor): #
    #    self.aumentaEstoque(self.__quantidadeAumentada)
    #    return self.__nomeRemedio, nomeFornecedor, self.__lote, self.__preco, self.__quantidadeDoProduto, self.__nomeCategoria
    #    