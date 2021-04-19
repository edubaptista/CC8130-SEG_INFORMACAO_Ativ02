# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 20:13:37 2021

@author: Eduardo Baptista
"""

from collections import Counter

#Funcao do the monobit test para chaves aleatorias
def the_monobit_test(c_binaria):
    qtd_de_1 = 0
    for bit in c_binaria:
        if bit == '1':
            qtd_de_1 += 1
    if (qtd_de_1 > 9654) and (qtd_de_1 < 10346):
        return "Aprovado"
    else:
        return "Reprovado"

#Funcao do the poker test para chaves aleatorias
def the_poker_test(c_binaria):
    cont_seg = [c_binaria[i:i+4] for i in range(0, len(c_binaria), 4)]
    contador = Counter(cont_seg)

    fi = 0
    for string, qtd in contador.items():
        fi += qtd*qtd
    x = ((16/5000) * fi) - 5000

    if (x > 1.03) and (x < 57.4):
        return "Aprovado"
    else:
        return "Reprovado"

#Funcao do the runs test para chaves aleatorias
def the_runs_test(c_binaria):
    contador = 1
    repeticoes = []
    contador_0 = [0, 0, 0, 0, 0, 0]
    contador_1 = [0, 0, 0, 0, 0, 0]
    if len(c_binaria) > 1:
        for i in range(1, len(c_binaria)):
            if c_binaria[i - 1] == c_binaria[i]:
                contador += 1
            else:
                repeticoes.append([c_binaria[i - 1], contador])
                contador = 1
        repeticoes.append([c_binaria[i], contador])

    for rep in repeticoes:
        if rep[0] == '0':
            if rep[1] >= 6:
                contador_0[5] += 1
            else:
                contador_0[rep[1]-1] += 1
        if rep[0] == '1':
            if rep[1] >= 6:
                contador_1[5] += 1
            else:
                contador_1[rep[1]-1] += 1

    zk = False
    uk = False
    if (contador_0[0] > 2267) and (contador_0[0] < 2733) and (contador_0[1] > 1079) and (contador_0[1] < 1421) and \
        (contador_0[2] > 502) and (contador_0[2] < 748) and (contador_0[3] > 223) and (contador_0[3] < 402) and \
        (contador_0[4] > 90) and (contador_0[4] < 223) and (contador_0[5] > 90) and (contador_0[5] < 223):
        zk = True

    if (contador_1[0] > 2267) and (contador_1[0] < 2733) and (contador_1[1] > 1079) and (contador_1[1] < 1421) and \
        (contador_1[2] > 502) and (contador_1[2] < 748) and (contador_1[3] > 223) and (contador_1[3] < 402) and \
        (contador_1[4] > 90) and (contador_1[4] < 223) and (contador_1[5] > 90) and (contador_1[5] < 223):
        uk = True

    if zk and uk:
        return "Aprovado"
    else:
        return "Reprovado"

#Funcao do the long test para chaves aleatorias
def the_long_run_test(c_binaria):
    contador = 1
    if len(c_binaria) > 1:
        for i in range(1, len(c_binaria)):
            if c_binaria[i - 1] == c_binaria[i]:
                contador += 1
            else:
                if contador >= 34:
                    return "Reprovado"
                contador = 1
    return "Aprovado"

#Funcao de conversao das chaves aleatorias de hexadecimal para binario 
def converte_hexa_para_binario(chave_hexa):
    chave_binaria = ''
    for caractere in chave_hexa:
        chave_binaria += "{0:04b}".format(int(caractere, 16))
    return chave_binaria


txt_chaves = open('Chaves_de_Criptografia_2021.S1.txt', 'r')
chaves_separadas = []
chaves_binarias = []

for chave in txt_chaves:
    chave_temp = chave[1:]
    chave_temp = chave_temp[:-2]
    chaves_separadas.append(chave_temp)
    chaves_binarias.append(converte_hexa_para_binario(chave_temp))

num_chave = 1
for chave_binaria in chaves_binarias:
    monobit_resultado = the_monobit_test(chave_binaria)
    poker_resultado = the_poker_test(chave_binaria)
    runs_resultado = the_runs_test(chave_binaria)
    long_resultado = the_long_run_test(chave_binaria)

    if (monobit_resultado=="Aprovado") and (poker_resultado=="Aprovado") and \
            (runs_resultado=="Aprovado") and (long_resultado=="Aprovado"):
        print(str(num_chave) + "ª chave binária aprovada no teste.")
    else:
        print(str(num_chave) + "ª chave binária não aprovada no teste. " +
            "\nResultados: \nThe Monobit Test: " + monobit_resultado + ". \nThe Poker Test: " +
            poker_resultado + ". \nThe Runs Test: " + runs_resultado + ". \nThe Long Run Test: " +
            long_resultado)
    num_chave += 1