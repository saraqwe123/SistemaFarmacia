import DAOs.remedioDAO as remedio

def main():
    dao = remedio.RemedioDAO()
    print(dao.gravarBD())

main()