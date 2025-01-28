


from tkinter import *
from tkinter import ttk
from römischezahlen_louis import konverter  # Importiere die Konvertierungsfunktion

# Funktion für die Button-Aktion
def convert():
    try:
        input_value = feet.get()
        if input_value.isupper() and isinstance(input_value, str) == True and len(input_value) > 0:
            result = konverter(input_value)
            dezimal.set(result)
        else:
            dezimal.set(
                '''
                Invalid input, 
                pleas input a capitalized Letter 
                Like: I, V, X, L, C, D, M.
                ''') 
    except Exception as e:
        dezimal.set(f"Fehler: {e}")

# Hauptfenster
window = Tk()
window.title("Römische Zahlen Umrechner")
window.geometry("400x400")  # Statische Größe des Fensters

# Haupt-Frame
mainframe = ttk.Frame(window, width=400, height=400, padding="20 20 20 20")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.grid_propagate(False)  # Behalte die feste Frame-Größe bei

# Eingabefeld
feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=30, textvariable=feet)
feet_entry.grid(column=2, row=1, columnspan=2, pady=10)

# Ausgabe-Label
dezimal = StringVar()
ttk.Label(mainframe, textvariable=dezimal).grid(column=1, row=2, columnspan=2, pady=10)

# Button zum Umrechnen
ttk.Button(mainframe, text="Umrechnen", command=convert).grid(column=1, row=3, columnspan=2, pady=10)

# Beschriftungen
ttk.Label(mainframe, text="Eingabe:").grid(column=0, row=1, sticky=E, padx=10)
ttk.Label(mainframe, text="Ausgabe:").grid(column=0, row=2, sticky=E, padx=10)

# Padding für alle Widgets im Frame
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Fokus auf das Eingabefeld setzen
feet_entry.focus()

# Starte die Tkinter-Event-Schleife
window.mainloop()
