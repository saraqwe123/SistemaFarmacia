import Entities.remedio as remedio


class RemedioDAO:

    def criar(self, registroMS, nomeRemedio, ean13, ncm, precoVenda, fabricante, substancia):
        self.rem = remedio.Remedio(self, registroMS, nomeRemedio, ean13, ncm, precoVenda, fabricante, substancia)
        return self.rem

    def gravarBD(self):
        nomeRemedio = input("Qual é o nome do remédio?: ")
        ean13 = int(input("Qual é o ean13 do remédio?: "))
        ncm = int(input("Qual é o ncm do remédio?: "))
        precoVenda = float(input("Qual é o preço do remédio?: "))
        fabricante = input("Qual é o fabricante do remédio?: ")
        substancia = input("Qual é a substância do remédio?: ")
        registroMS = input("Qual é o registro MS do remédio?: ")
        sql = "insert INTO Remedio (registroMS, nomeRemedio, ean13, ncm, precoVenda, fabricante, substancia) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", registroMS, nomeRemedio, ean13, ncm, precoVenda, fabricante, substancia
        return remedio.Remedio(registroMS, nomeRemedio, ean13, ncm, precoVenda, fabricante, substancia)
