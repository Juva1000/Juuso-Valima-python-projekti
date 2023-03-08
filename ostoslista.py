import json
import datetime


data = {}
with open("ostokset.json", "w") as f:
    json.dump(data, f)


def main():
    while True:
        print("Tervetuloa sovellukseeni")
        print("Valitse seuraavista:")
        print("1. Lisää ostos")
        print("2. Muokkaa ostoksia")
        print("3. Lopeta")
        valinta = input("Valintasi: ")

        if valinta == "1":
            lisaa_ostos()
        elif valinta == "2":
            muokkaa_ostoksia()
        elif valinta == "3":
            print("Kiitos ohjelman käytöstä!")
            break
        else:
            print("Virheellinen valinta, yritä uudelleen.")


def lisaa_ostos():
    print("Lisää ostos alkaa")
    kayttajatunnus = input("Anna käyttäjätunnus: ")
    kauppa = input("Kauppa: ")
    hinta = input("Hinta: ")
    time = datetime.datetime.now().strftime("%H:%M")
    date = datetime.datetime.now().strftime("%d.%m.%Y")

    item_dict = {"kauppa": kauppa, "hinta": hinta, "aika": time, "paiva": date}
    with open("ostokset.json", "r+") as f:
        data = json.load(f)
        if kayttajatunnus not in data:
            data[kayttajatunnus] = []
        data[kayttajatunnus].append(item_dict)
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
    print("Ostos tallennettu")


def muokkaa_ostoksia():
    print("Muokkaa ostoksia alkaa")
    kayttajatunnus = input("Anna käyttäjätunnus: ")
    with open("ostokset.json", "r") as f:
        data = json.load(f)
    ostokset = data.get(kayttajatunnus, [])

    for i, ostos in enumerate(ostokset):
        print(f"{i+1}. Kauppa: {ostos['kauppa']}, Hinta: {ostos['hinta']}, Aika: {ostos['aika']}, Päivä: {ostos['paiva']}")
    
    if not ostokset:
        print("Ei ostoksia tälle käyttäjälle")
        return
    
    while True:
        valinta = input("Valitse muokattava ostos tai paina 'q' poistuaksesi: ")
        if valinta == 'q':
            break
        elif not valinta.isnumeric():
            print("Virheellinen syöte, yritä uudelleen.")
            continue
        valinta = int(valinta)
        if valinta < 1 or valinta > len(ostokset):
            print("Virheellinen syöte, yritä uudelleen.")
            continue
        
        
        ostos = ostokset[valinta-1]
        print(f"Muokataan ostosta: {ostos['kauppa']}, {ostos['hinta']}, {ostos['aika']}, {ostos['paiva']}")
        uusi_kauppa = input("Anna uusi kauppa tai jätä tyhjäksi jos ei muutosta: ")
        if uusi_kauppa:
            ostos['kauppa'] = uusi_kauppa
        uusi_hinta = input("Anna uusi hinta tai jätä tyhjäksi jos ei muutosta: ")
        if uusi_hinta:
            ostos['hinta'] = uusi_hinta
        
        
        with open("ostokset.json", "w") as f:
            json.dump(data, f, indent=4)
        
        print("Ostos muokattu")


if __name__ == "__main__":
    main()
