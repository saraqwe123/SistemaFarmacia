import cadastro
class Movimentacao:
    def reduzEstoque(self, quantidadeReduzida):
        self.quantidadeReduzida = quantidadeReduzida
        self.quantidadeDoProduto = self.quantidadeDoProduto - self.quantidadeReduzida
        return self.quantidadeDoProduto
    
    def aumentaEstoque(self, quantidadeAumentada): 
        self.quantidadeAumentada = quantidadeAumentada
        self.quantidadeDoProduto = self.quantidadeDoProduto + self.quantidadeAumentada
        return self.quantidadeDoProduto

    def geraNotaFiscal(self, nomeRemedio, precoVenda, data, hora): 
        cadastrar = cadastro.Remedio(nomeRemedio, precoVenda)
        return cadastrar.nomeRemedio, cadastrar.precoVenda, data, hora, self.quantidadeDoProduto
        
    #def registraEntrada(self, nomeFornecedor): #
    #    self.aumentaEstoque(self.quantidadeAumentada)
    #    return self.nomeRemedio, nomeFornecedor, self.lote, self.preco, self.quantidadeDoProduto, self.nomeCategoria