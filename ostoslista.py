import json
import datetime
from collections import defaultdict

json_tiedosto_kt = "kt.json"
json_tiedosto_kulut = "kulut.json"



def lataa_kt():
    try:
        with open (json_tiedosto_kt) as tiedosto_kt:
            return json.load(tiedosto_kt)
    except FileNotFoundError:
        return[]
    

def tallenna_kt(tallenna_kt):
    with open(json_tiedosto_kt, "w") as tiedosto_kt:
        json.dump(tallenna_kt, tiedosto_kt)


def lataa_kulut():
    try:
        with open(json_tiedosto_kulut) as tiedosto_kulut:
            return json.load(tiedosto_kulut)
    except FileNotFoundError:
        return []
    

def tallenna_kulut(tallenna_kulut):
    with open(json_tiedosto_kulut, "w") as tiedosto_kulut:
        json.dump(tallenna_kulut, tiedosto_kulut)    


def kirjaudu_sisaan(kayttajat, tunnus, salasana):
    for kayttaja in kayttajat:
        if kayttaja["tunnus"] == tunnus and kayttaja["salasana"] == salasana:
            print("Kirjautuminen onnistui!")
            return kayttaja["tunnus"]
    print("Virheellinen valinta.")
    return None


def laske_kulut_yhteensa(kulut):
    kulut_yhteensa = defaultdict(int)
    for kulu in kulut:
        kayttaja = kulu["kayttaja"]
        hinta = int(kulu["hinta"])
        kulut_yhteensa[kayttaja] += hinta
    return kulut_yhteensa

kayttajat = lataa_kt()
kulut = lataa_kulut()


while True:
    print("1. Kirjaudu sisään")
    print("2. Luo käyttäjätunnus")
    valinta = input("Valitse toiminto: ")

    if valinta == "1":
        tunnus = input("Anna käyttäjätunnus:")
        salasana = input("Anna salasana: ")
        kirjautunut_kayttaja = kirjaudu_sisaan(kayttajat, tunnus, salasana)
        if kirjautunut_kayttaja:
            print("Tervetuloa takaisin " + tunnus + "!")
            while True:
                print("1. Syötä merkintä")
                print("2. Näytä lista")
                print("3. Kirjaudu ulos")
                print("4. Laske kulut yhteensä")
                valinta = input("Valitse toiminto: ")
                if valinta == "1":
                    kauppa = input("Kauppa: ")
                    hinta = input("Hinta: ")
                    pvm = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    kulut.append({"kauppa": kauppa, "hinta": hinta, "pvm": pvm, "kayttaja": kirjautunut_kayttaja})
                    tallenna_kulut(kulut)
                    
                elif valinta == "2":
                    for kulu in kulut:
                        if kulu["kayttaja"] == kirjautunut_kayttaja:
                            kauppa = kulu["kauppa"]
                            hinta = kulu["hinta"]
                            pvm = kulu["pvm"]
                            print(pvm + ": " + kauppa + ", " + hinta + "€")

                elif valinta == "3":
                    print("Kirjaudutaan ulos...")
                    break

                elif valinta == "4":
                    kulut_yhteensa = laske_kulut_yhteensa(kulut)
                    for kayttaja, summa in kulut_yhteensa.items():
                        print(f"{kayttaja}, {summa}€")

                else:
                    print("Valitse 1, 2 tai 3.")


                   
    elif valinta == "2":
        uusi_tunnus = input("Anna uusi käyttäjätunnus: ")
        uusi_salasana = input("Anna uusi salasana: ")
        uusi_kayttaja = {"tunnus": uusi_tunnus, "salasana": uusi_salasana}
        kayttajat.append(uusi_kayttaja)
        tallenna_kt(kayttajat)
        print("Käyttäjätunnus lisätty onnistuneesti")




