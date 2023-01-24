# -*- coding: utf-8 -*-

import pandas as pd
import random
import string

def main():
    formato_reg = [[],[]]
    qtd_reg = inteiro_positivo("Informe a quantidade de registros: ")
    qtd_campos = inteiro_positivo(
        "\nInforme a quantidade de campos de cada registro: ")
    
    for i in range(qtd_campos):
        while True:
            tipo_campo = input(f'\nO tipo do {i+1}º campo será (X/9): ')
            if tipo_campo not in ['X', 'x', '9']:
                print("O campo deve ser ou numérico (9) ou alfanumérico (X)")
            else: break
        formato_reg[0].append(tipo_campo)
        tamanho_campo = inteiro_positivo("Qual o tamanho do campo? ")
        formato_reg[1].append(tamanho_campo)
     

    arq = construir_arq(formato_reg[0], formato_reg[1], qtd_reg)
    
    print("\nRegistros gerados com sucesso!\n")
    nome_arq = input("Agora digite o nome do arquivo .DAT: ")
    
    arq_salvar = pd.DataFrame(arq)
    arq_salvar.to_csv(f'{nome_arq}.dat', index = False, header = False)
    
    print("Arquivo salvo!")

    return None

#------------------------------------------------------------------------------

def inteiro_positivo_zero(msg = "Digite um número inteiro: "):
    while True:
        try:
            num = int(input(msg))
            if num < 0:
                print("O número deve ser maior ou igual a 0")
            else: return num
        except (TypeError, ValueError):
            print("Erro! A entrada de ser um número inteiro.\n")
            
#------------------------------------------------------------------------------
            
def inteiro_positivo(msg = "Digite um número inteiro positivo: "):
    while True:
        try:
            num = int(input(msg))
            if num <= 0:
                print("O número deve ser maior que 0.\n")
            else: return num
        except (TypeError, ValueError):
            print("Erro! Digite um número inteiro maior que 0.\n")

#------------------------------------------------------------------------------

def construir_arq(tipos_campo, tamanhos, qtd_reg):
    arq = []
    campos = []
    reg = ''
    
    for i in range(len(tipos_campo)):
        
        if tipos_campo[i] == '9':
            
            while True:    
                tipo_valores = input(
                f'\n{i+1}º Campo 9({tamanhos[i]}) aleatório (A), intervalo (I) ou conjunto de valores (C)? ')
                if tipo_valores in 'AaIiCc': break
                print("(A/I/C)")
                
            if tipo_valores in 'Aa':
                for j in range(qtd_reg):
                    valor = str(random.randint(0, (10**tamanhos[i])-1))
                    campos.append('0' * (tamanhos[i]-len(valor)) + valor)
                    
            elif tipo_valores in 'Ii':
                while True:
                    lim_inferior = inteiro_positivo_zero("Limite inferior: ")
                    lim_superior = inteiro_positivo("Limite superior: ")
                    if lim_superior > lim_inferior: break
                    print("O limite superior deve ser maior do que o limite inferior!\n")
                for j in range(qtd_reg):
                    valor = str(random.randint(lim_inferior, lim_superior))
                    campos.append('0' * (tamanhos[i]-len(valor)) + valor)
                    
            else:
                conjunto_9 = obter_conjunto()
                for j in range(len(conjunto_9)):
                    conjunto_9[j] = str(conjunto_9[j])
                for j in range(qtd_reg):
                    valor = random.choice(conjunto_9)
                    campos.append('0' * (tamanhos[i]-len(valor)) + valor)
                
        if tipos_campo[i] in 'Xx':
            while True:
                tipo_valores = input(
                f'\n{i+1}º Campo (X({tamanhos[i]}) aleatório (A) ou conjunto de valores (C)? ')
                if tipo_valores in 'AaCc': break
                print("(A/C)")
                
            if tipo_valores in 'Aa':
                letras = string.ascii_uppercase
                for j in range(qtd_reg):
                    valor = ''.join(random.choice(letras) for i in range (tamanhos[i]))
                    campos.append(valor)
                    
            else:
                conjunto_X = obter_conjunto()
                for j in range(qtd_reg):
                    valor = random.choice(conjunto_X)
                    if len(valor) < tamanhos[i]:
                        campos.append(valor + (' ' * (tamanhos[i] - len(valor))))
                    elif len(valor) > tamanhos[i]:
                        campos.append(valor[:tamanhos[i]])
                    else:
                        campos.append(valor)
        
    for i in range(qtd_reg):
        reg = ''
        for j in range(0, qtd_reg * len(tipos_campo), qtd_reg):
            reg += campos[j+i]
        arq.append(reg)
    
    return arq

#------------------------------------------------------------------------------

def obter_conjunto():
    conjunto = []

    no_itens = inteiro_positivo("Número de itens: ")
    for i in range(no_itens):
        entrada = input(f'{i+1}º item: ')
        conjunto.append(entrada)
    return conjunto

#------------------------------------------------------------------------------

main()