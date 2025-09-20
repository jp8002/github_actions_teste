
import pytest
from src.calculadora import somar, dividir

def test_somar():
    assert somar(2, 3) == 5
    assert somar(-1, 1) == 0

def test_dividir():
    assert dividir(10, 2) == 5
    with pytest.raises(ValueError):
        dividir(10, 0)

def test_subtrair():
    assert subtrair(3,2) == 1
    assert subtrair(2,3) == -1
    assert subtrair(0,0) == 0

def test_multiplicar():
    assert multiplicar(2,2) == 4
    assert multiplicar(2,.5) == 1
    assert multiplicar(2,10) == 20
    