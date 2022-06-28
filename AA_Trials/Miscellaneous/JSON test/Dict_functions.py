# -Creare un dict

persona = {
    "nome": "Luca",                 # We have multiple couples of keys and values
    "cognome": "Rossi",
    "eta": 25                       # The key cannot be duplicated, it will take the last value
}

# print(len(persona))
# print(type(persona))

# -Accedere agli elementi con [], get(), keys(), values(), items(), check if the key exists

# print(persona["nome"])
# print(persona.get("cognome"))
#
x = list(persona.keys())[0]
print(type(x))
#
# y = persona.values()
# print(y)
#
# z = persona.items()         # z diventa una lista di touple (in questo caso tre perchè ci sono tre elementi nel dict)
# print(z)                    # ogni touple è composta dalla coppia key-value
#
# print("nome" in persona)


# -Modificare e aggiungere elementi con [] e update()

# persona["nome"] = "Marco"
# print(persona)
# persona.update({"nome": "Anna"})
# print(persona)
# persona["colore"] = "blu"
# # persona.update({"colore": "blu"})
# print(persona)


# -Rimuovere elementi con pop(key), popitem(), clear(), del

# persona.pop("nome")
# print(persona)
# persona.popitem()
# print(persona)
# persona.clear()
# print(persona)
# del persona["nome"]
# print(persona)
# del persona
# print(persona)

# -Ciclare elementi: key, values, values(), keys(), items()

# for x in persona:
#     print(x)                   # Stampa la key
#     print(persona[x])           # Stampa il value

# for x in persona.values():
#     print(x)                    # Stampa il value

# for x in persona.keys()
#     print(x)                    # Stampa la key

# for x, y in persona.items():
#     print(x, y)                 # Stampa la touple di key e value


# -Copiare dict con copy() e dict()

# x = persona.copy()      # Viene creata una copia di persona su cui possiamo andare a lavorare indipendentemente
# y = dict(persona)       # Viene creato un nuovo dict con gli stessi dati di persona
# print(x)
# print(y)


# -Dict annidati

persona2 = {
    "nome": "Luca",                 # We have multiple couples of keys and values
    "cognome": "Rossi",
    "eta": 25,
    "indirizzo": {
        "citta": "Novara",
        "CAP": "28100",
        "civico": 22
    }
}
print(persona2)
print(type(persona2["indirizzo"]["CAP"]))
