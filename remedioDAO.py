import cadastro
import conexao

class RemedioDAO:

    def criar(self, nome, ean13, fabricante, preco):
        rem = cadastro.Remedio(nome, ean13, fabricante, preco)
        return rem

    
    def gravarNoBd(self):
        conexao.cursor()
        sql = "insert INTO Remedio VALUES(...)"