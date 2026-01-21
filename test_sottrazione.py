# Salva questo codice in un file separato, ad esempio 'test_sottrazione.py',
# e poi esegui 'pytest' nella stessa directory da un terminale.

# Per la dimostrazione, possiamo anche definire la funzione qui, 
# ma in un progetto reale la importeresti da un altro modulo.

from operazioni import sottrazione

def test_sottrazione_numeri_interi():
    assert sottrazione(5, 2) == 3
    assert sottrazione(10, -3) == 13
    assert sottrazione(0, 0) == 0
    assert sottrazione(-5, -2) == -3

def test_sottrazione_numeri_decimali():
    assert sottrazione(5.5, 2.0) == 3.5
    assert sottrazione(10.0, 3.5) == 6.5
    assert sottrazione(-1.0, 0.5) == -1.5

def test_sottrazione_con_stringhe():
    assert sottrazione("hello", 5) is None
    assert sottrazione(10, "world") is None
    assert sottrazione("a", "b") is None

def test_sottrazione_con_zero():
    assert sottrazione(5, 0) == 5
    assert sottrazione(0, 5) == -5