# Importa la funzione che vuoi testare (supponendo che sia in un file chiamato 'my_module.py'
# o che tu la incolli direttamente qui per semplicità)

from operazioni import somma

def test_somma_numeri_interi():
    assert somma(1, 2) == 3
    assert somma(-1, 5) == 4
    assert somma(0, 0) == 0

def test_somma_numeri_decimali():
    assert somma(1.5, 2.5) == 4.0
    assert somma(-1.0, 0.5) == -0.5

def test_somma_con_stringhe():
    assert somma("hello", 5) is None
    assert somma(10, "world") is None
    assert somma("a", "b") is None

def test_somma_con_zero():
    assert somma(0, 5) == 5