"""
4 - Dois veículos (um carro e um caminhão) saem respectivamente de cidades opostas pela mesma rodovia. O carro de Ribeirão Preto em direção a Franca, a uma velocidade constante de 110 km/h e o caminhão de Franca em direção a Ribeirão Preto a uma velocidade constante de 80 km/h. Quando eles se cruzarem na rodovia, qual estará mais próximo a cidade de Ribeirão Preto?

IMPORTANTE:

a) Considerar a distância de 100km entre a cidade de Ribeirão Preto <-> Franca.

b) Considerar 2 pedágios como obstáculo e que o caminhão leva 5 minutos a mais para passar em cada um deles e o carro possui tag de pedágio (Sem Parar)

c) Explique como chegou no resultado.
    
"""


"""
Resposta:

Quando os dois se encontrarem, a distância até Ribeirão será a mesma para os dois veículos.
Para calcular a distância em que eles se encontram da cidade, é necesessário saber a posição dos pedágios e avaliar por quantos pedágios o caminhão passou no ato do encontro.

Mas considerando que o caminhão tenha passado pelos dois pedágios, e que o carro e o caminhão iniciaram a viagem ao mesmo tempo temos:
"""

# ----------------------------------------------------------------------
#1) Calcular a velocidade média do caminhão devido aos pedágios
# Tempo gasto pelo caminhão nos pedágios
toll_time = 2 * 5 / 60  # 2 pedágios, cada um com 5 minutos de atraso (em h)

# Velocidade do caminhão em km/h
truck_speed = 80

# Tempo que o caminhão leva para percorrer a distância
distance = 100  # Distância entre as cidades em km
truck_time = (distance / truck_speed) + toll_time  # 1.41666 h

# velocidade média do caminhão

truck_avarage_speed = distance / truck_time  # 70.58 km/h



# ----------------------------------------------------------------------
#2) Calcular o tempo de percurso do carro:
# Velocidade do carro em km/h
car_speed = 110

# Tempo que o carro leva para percorrer a distância
car_time = (distance / car_speed)  #0.91 h




# ----------------------------------------------------------------------
#23) Calcular o encontro:

# Encontro:
# Tempo que se encontram --> distancia perocorrida pelo carro / velocidade do carro
# tempo que se encontram --> distância percorrida pelo caminhão / velocidade media do caminhão
# Ou seja, tempo que se encontram --> distancia perocorrida pelo carro / velocidade do carro = distância percorrida pelo caminhão / velocidade media do caminhão
# também temos que distância percorrida pelo carro + distância percorrida pelo caminhão = 100km, então a distância percorrida pelo carro = 100 - dist. percorrida pelo caminhão
# substituindo:
# (distance - truck_distance)/car_speed = truck_distance/ truck_avarage_speed
# (distance * truck_avarage_speed) = (truck_distance * car_speed) + (truck_distance * truck_avarage_speed)
# (distance * truck_avarage_speed) = (truck_distance) * ( car_speed + truck_avarage_speed)
# Então:

truck_distance = (distance * truck_avarage_speed) / ( car_speed + truck_avarage_speed)
car_distance = distance - truck_distance


print(f'Eles se encontram a {car_distance:.2f} km de distância de Ribeirão Preto,  {truck_distance/truck_avarage_speed*60:.0f} minutos após iniciarem a viagem')
