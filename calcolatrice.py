from operazioni import somma, sottrazione

# crea una semplice calcolatrice che può sommare e sottrarre due numeri
def calcolatrice(operazione: str, a: float, b: float):
    if operazione == "somma":
        return somma(a, b)
    elif operazione == "sottrazione":
        return sottrazione(a, b)
    else:
        return None 
    
# Esempi di utilizzo con output esplicito degli input e output
if __name__ == "__main__":  
    print("Somma di 3 e 5:", calcolatrice("somma", 3, 5))          # Output: 8
    print("Sottrazione di 10 e 4:", calcolatrice("sottrazione", 10, 4))  # Output: 6
    print("Moltiplicazione 3 per 2:", calcolatrice("moltiplicazione", 3, 2)) # Output: 6
    print("Operazione non valida:", calcolatrice("divisione", 2, 3)) # Output: None
    x = input("Inserisci il primo numero: ")
    y = input("Inserisci il secondo numero: ")
    print("Somma di", x, "e", y, ":", calcolatrice("somma", float(x), float(y)))
    print("Sottrazione di", x, "e", y, ":", calcolatrice("sottrazione", float(x), float(y)))