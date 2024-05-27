# Fiind dat un dictionar {"a":1,"b":2,"c":3} scrieti o functie care primeste ca parametru cheia si returneaza valoarea
dict={"a":1,
      "b":2,
      "c":3
      }

def LucrarecuDict (x):
    try:
        cheie=x
        print(dict[cheie])
    except ValueError:
        print("Cheia interogata nu este in dictionar")

LucrarecuDict("a")