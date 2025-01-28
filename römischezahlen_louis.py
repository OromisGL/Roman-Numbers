# Römische Zahlen

# Schreibe ein Python-Programm,
# das eine beliebige römische Zahl in eine „gewöhnliche” Dezimalzahl umrechnet.

Römische_Zahlen = {
    'I': 1,  
    'V': 5,  
    'X': 10, 
    'L': 50, 
    'C': 100, 
    'D': 500, 
    'M': 1000
    }

def konverter(roman):
    dezimal = 0
    next_val = 0
    for i in roman:
        current_val = Römische_Zahlen[i]
        if current_val > next_val:
            dezimal += current_val - 2 * next_val
        else:
            dezimal += current_val
        next_val = current_val

                
    return dezimal


""" 
Rzahl = input("Eine Römische Zahl eingeben: ")

if Rzahl.isupper() and isinstance(Rzahl, str) == True and len(Rzahl) > 0:
    print(konverter(Rzahl))
else:
    print("Invalid input, pleas input a capitalized Letter Like: I, X, C, L.") """

