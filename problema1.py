# Scrieti o functie care citeste un string de la tastatura si afiseaza lungimea lui. Tratati cazul in care textul nu este string
def String():
    try:
        cuvantul=int(input("scrie ceva: "))
        print (len(cuvantul))
    except Exception:
        print("Cuvantul introdus trebuie sa fie string")

String()