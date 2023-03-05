"""
1) Observe o trecho de código abaixo:

int INDICE = 13, SOMA = 0, K = 0;

enquanto K < INDICE faça

{

K = K + 1;

SOMA = SOMA + K;

}

imprimir(SOMA);
"""


index = 13
sum_var = 0
K = 0

while K < index:
    K += 1
    sum_var += K

print(sum_var)