import json

# Leggere JSON in Python

# x = '{"nome": "Luca", "cognome": "Rossi", "eta": 25}'     # Questa è una stringa
#
# y = json.loads(x)
#
# print(y)
# print(type(y))      # y is a dictionary, siamo passati da una stringa a JSON
# print(y["nome"])


# Da Python in JSON

# x = {
#     "nome": "Luca",
#     "cognome": "Rossi",
#     "eta": 25
# }
#
# y = json.dumps(x)
# z = json.dumps(["roma", "napoli"])      # abbiamo creato direttamente una string da una list
#
# print(y)
# print(type(y))      # in questo caso abbiamo una stringa, siamo quindi passati da JSON a stringa
# print(z)
# print(type(z))

# I dati convertibili in JSON sono:
# -dict
# -list
# -tuple
# -string
# -int
# -float
# -True
# -False
# -None


# Formattare e ordinare il JSON

x = {
    "nome": "Luca",
    "cognome": "Rossi",
    "isOnline": False,
    "interessi": ["calcio", "basket"],
    "moneteInTasca": 4.56,
    "fidanzata": None,
    "eta": 25
}

y = json.dumps(x, indent=4, separators=(". ", "= "), sort_keys=True)

print(y)
