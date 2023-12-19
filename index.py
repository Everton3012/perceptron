import numpy as np
#import keras
#import tensorflow

"""
entradas = np.array([1 , 9, 5])
pesos = np.array([0.8 , 0.1, 0 ])

def soma(e , p):
    return e.dot(p)
    

s = soma(entradas, pesos)

def stepFunction(soma):
    if(s >= 1):
        return 1
    return 0

saida = stepFunction(s)

print(s)
print(saida)
"""
entradas = np.array([[0, 0],
                    [0 ,1],
                    [1 ,0],
                    [1 ,1]])
                    
saidas = np.array([[1 ,0],
                  [0 ,1]])
                    
pesos = np.array([[0 ,0],
                 [0 ,0]])

taxa_aprendizado = 0.5

def Soma(e, p):
    return e.dot(p)

s = Soma(entradas, pesos)

def funcao_degrau(soma):
    if(soma >= 1):
        return 1
    return 0

def calculo_saida(reg):
    s = reg.dot(pesos)
    return funcao_degrau(s)

def calcula_e_atualiza():
    erro_total = 1
    while(erro_total != 0):
        erro_total = 0

        for i in range (len(saidas)):
            calc_saida = calculo_saida(np.array(entradas[i]))
            erro = abs(saidas[i] - calc_saida)
            erro_total += erro

            for j in range(len(pesos)):
                pesos[i] = pesos[j] + (taxa_aprendizado * entradas[i][j] * erro)
                print("Pesos Atualizados > " + str(pesos[j]))

        print("Total de Erros: " + str(erro_total))

calcula_e_atualiza()