#Esse é apenas uma estrutura, não é uma função
if __name__ == "__main__":
    try:
        print("teste")

    except Exception as e:
        print(str(e))    



#função com retorno
def soma(x, y):
    return x + y

if __name__ == "__main__":
    try:
        resultado = soma(5,8)
        print(resultado)
    except Exception as e:
        print(str(e))    


#from types import ClassMethodDescriptorType, coroutine

#para buscar pela função 
elif selecao == "2":
            query = "SELECT * FROM {};".format(input("informe a tabela a ser consultada"))
            dados = buscar(query)
            for linha in dados:
                print(linha)
                if linha in dados:
                    total = total + 1
                    print("quantidade de pacientes: ", len(nome))
            print("total de professores")        