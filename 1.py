arquivo = open("arquivo.txt", "w")

arquivo.write("Essa é a primeira linha escrita por nós. \n")
arquivo.write("Essa é a nossa segunda linha.")
arquivo.write("Essa deveria ser a terceira linha porém ainda é a segunda. \n")
arquivo.write("Essa sim é a terceira.")

arquivo.close()

with open("arquivo.txt","a+") as arquivo:
    arquivo.write("Eimagem 1\n")
    arquivo.read()

with open("arquivo.txt","a+") as arquivo:
    arquivo.write("Eimagem 2")
    arquivo.read()

with open("arquivo.txt","a+") as arquivo:
    arquivo.write("Eimagem 3\n")
    arquivo.read()
