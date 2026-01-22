# Test per la funzione moltiplicazione

from operazioni import moltiplicazione

def test_moltiplicazione_numeri_interi():
    assert moltiplicazione(2, 3) == 6
    assert moltiplicazione(5, 0) == 0
    assert moltiplicazione(-2, 3) == -6
    assert moltiplicazione(-2, -3) == 6

def test_moltiplicazione_numeri_decimali():
    assert moltiplicazione(2.5, 4.0) == 10.0
    assert moltiplicazione(1.5, 2.0) == 3.0
    assert moltiplicazione(-1.5, 2.0) == -3.0

def test_moltiplicazione_con_stringhe():
    assert moltiplicazione("hello", 5) is None
    assert moltiplicazione(10, "world") is None
    assert moltiplicazione("a", "b") is None

def test_moltiplicazione_con_uno():
    assert moltiplicazione(5, 1) == 5
    assert moltiplicazione(1, 5) == 5
    assert moltiplicazione(1, 1) == 1

def test_moltiplicazione_con_zero():
    assert moltiplicazione(0, 100) == 0
    assert moltiplicazione(100, 0) == 0
