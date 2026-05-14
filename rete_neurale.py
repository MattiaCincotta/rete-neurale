import sys

# Costanti
FEATURES = 5

def prevedi(weights, bias, inputs):
    # Calcola la somma pesata.
    somma_pesata = sum(w * x for w, x in zip(weights, inputs)) + bias
    return 1 if somma_pesata >= 0 else 0

def main():
    # Inizializza i pesi
    weights = [0.7, 0.6, 0.5, 0.3, 0.4] 
    
    bias = 0.0

    print("--- Percettrone del Concerto ---")
    print("Inserisci i dati:")
    inputs = []
    
    try:
        inputs.append(int(input("Artista famoso? (1=Si, 0=No): ")))
        inputs.append(int(input("Bel meteo? (1=Si, 0=No): ")))
        inputs.append(int(input("Amici presenti? (1=Si, 0=No): ")))
        inputs.append(int(input("Cibo buono? (1=Si, 0=No): ")))
        inputs.append(int(input("Alcool disponibile? (1=Si, 0=No): ")))
    except ValueError:
        print("Errore: devi inserire solo numeri interi (1 o 0).")
        sys.exit(1)

    # Effettua previsione
    decisione = prevedi(weights, bias, inputs)

    # Stampa risultato
    if decisione == 1:
        print("\nVai al concerto!")
    else:
        print("\nResta a casa!")

if __name__ == "__main__":
    main()