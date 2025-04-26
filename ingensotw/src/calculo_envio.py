# src/calculo_envio.py

def calcular_costo_envio(peso_kg, distancia_km, es_urgente):
    """
    Calcula el costo de envío basado en:
    - peso_kg: debe estar entre 0.1 y 50 kg.
    - distancia_km: debe estar entre 1 y 3000 km.
    - es_urgente: booleano (True/False) para envío express.

    Reglas:
    - Costo base: $10 por kg + $0.01 por km.
    - Envío urgente: +20% al total.
    - Si peso >= 30 kg: +$50 por 'manejo pesado'.
    """
    if peso_kg < 0.1 or peso_kg > 50 or distancia_km < 1 or distancia_km > 3000:
        return -1  # Error: valores inválidos

    costo = (peso_kg * 10) + (distancia_km * 0.01)

    if es_urgente:
        costo *= 1.2

    if peso_kg >= 30:
        costo += 50

    return round(costo, 2)
