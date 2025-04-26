import pytest
from src.calculo_envio import calcular_costo_envio

def test_envio_estandar():
    assert calcular_costo_envio(5, 100, False) == 60.0

def test_limite_peso_superior():
    assert calcular_costo_envio(30, 100, False) == 351.0

def test_peso_invalido():
    assert calcular_costo_envio(0.09, 100, False) == -1

def test_envio_urgente():
    assert calcular_costo_envio(10, 200, True) == 122.4

# Nuevos tests agregados

def test_peso_maximo_valido():
    assert calcular_costo_envio(50, 200, False) == 520.0

def test_peso_maximo_invalido():
    assert calcular_costo_envio(50.1, 200, False) == -1

def test_distancia_minima_valida():
    assert calcular_costo_envio(5, 1, False) == 50.01

def test_distancia_maxima_valida():
    assert calcular_costo_envio(5, 3000, False) == 80.0

def test_distancia_superior_invalida():
    assert calcular_costo_envio(5, 3000.1, False) == -1

def test_envio_urgente_con_manejo_pesado():
    assert calcular_costo_envio(35, 500, True) == 547.2
