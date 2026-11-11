import random 

def simular_canica(niveles=12):
    """     
    Simula el camino aleatorio de una canica a traves de niveles de obstaculos.
    
    Parametros:
    niveles (int): El numero de niveles por los que pasala canica (por efecto 12).
    
    Retorna:
    None (o imprime el camino recorrido).
    """
    for i in range(niveles):
        camino = random.choice(["Izquierda", "Derecha"])
        print(camino)
simular_canica()
