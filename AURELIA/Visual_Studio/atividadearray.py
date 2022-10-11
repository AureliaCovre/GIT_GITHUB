import numpy as np

if __name__ == "__main__":
    
    #Array com os dados fornecidos  
    arr = np.array([[1, 1, 150], [1, 2, 200], [1, 3, 78], [1, 2,50], [2, 1, 150], [2, 2, 200], [2, 3, 78], [2, 2,50]])
               
        
    try: 
        
        #qual o id do vendedor que fez o maior valor total em vendas
        
        #criando o atributo
        total_vendedores = [0,0]
        
        """[Criando a condição de cada vendedor]
    
        Args:
        id_vendedor_1 = código do vendedor 1 que efetuou a venda
        id_vendedor_2 = código do vendedor 2 que efetuou a venda
        
        """
        for i in range(len(arr)):
            if 1 == arr[i][0]:
               total_vendedores[0] += arr[i][2] 
               id_vendedor_1 = arr[0][0]
            elif 2 == arr[i][0]:
               total_vendedores[1] += arr[i][2]
               id_vendedor_2 = arr[4][0]

        #criando os prints de acordo com os resultados
        if total_vendedores[0] > total_vendedores[1]:
            print("Id do vendedor que fez a maior venda é:", + id_vendedor_1, "\n")
        elif total_vendedores[0] == total_vendedores[1]:
            print("O valor total de vendas dos vendedores são iguais, portanto: ")
            print("Segue id dos vendedores: ", id_vendedor_1, id_vendedor_2, "\n")
        elif total_vendedores[0] < total_vendedores[1]:
           print("Id do vendedor que fez a maior venda é:", + id_vendedor_2, "\n")

    except Exception as e:
        print(str(e))
    
    try:    
        #qual o cliente que fez o maior numero de compras 
        
        #criando o atributo
        total_clientes = [0,0,0]
        
        """[Criando a condição de cada cliente]
    
        Args:
        id_cliente_1 = código do cliente 1 que efetuou a compra
        id_cliente_2 = código do cliente 2 que efetuou a compra
        id_cliente_3 = código do cliente 3 que efetuou a compra
        
        """
        for i in range(len(arr)):
           if 1 == arr[i][1]:
               total_clientes[0] += arr[i][2] 
               id_cliente_1 = arr[i][1]              
           elif 2 == arr[i][1]:
               total_clientes[1] += arr[i][2]
               id_cliente_2 = arr[i][1]  
           elif 3 == arr[i][1]:
              total_clientes[2] == arr[i][2]
              id_cliente_3 = arr[i][1] 
        
        #calculando a quantidade máxima das compras efetuadas do cliente 
        cliente_maior_compra = max(total_clientes[0], total_clientes[1], total_clientes[2])
        
        #criando os prints de acordo com os resultados                     
        if cliente_maior_compra == total_clientes[0]:
            print("O cliente que efetuou a maior compra foi: ", id_cliente_1)
        elif cliente_maior_compra == total_clientes[1]:
            print("O cliente que efetuou a maior compra foi: ", id_cliente_2)
        elif cliente_maior_compra == total_clientes[2]:
            print("O cliente que efetuou a maior compra foi: ",id_cliente_3)
                
    except Exception as e:
        print(str(e)) 