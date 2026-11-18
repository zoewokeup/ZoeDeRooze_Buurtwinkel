"""Startbestand: Bestellingen voor een buurtwinkel.

Vervang elke `pass` door je eigen code. `pass` is een tijdelijke lege instructie:
de functie doet voorlopig niets en geeft None terug.
Behoud de functienamen en parameters. De volledige afspraken en voorbeelden
staan in opdracht.md. Extra hulpfuncties zijn toegestaan.
"""

from gegevens import PRODUCTEN


# 1. Maak een klantnaam bruikbaar
def maak_klantnaam(naam):
    """Geef de opgeschoonde klantnaam terug, of 'Onbekende klant'."""
    # TODO: Schrijf hier je code.
    if naam.isdigit():
        return "Niet toegestaan"

    if not naam.strip():
        return "Onbekende klant"
    return naam.strip().title()


# 2. Bereken een regelbedrag
def bereken_regelbedrag(prijs, aantal):
    """Geef het regelbedrag terug, afgerond op twee decimalen."""
    # TODO: Schrijf hier je code.
    return round(prijs * aantal, 2)


# 3. Bereken het te betalen bedrag
def bereken_totaal(subtotaal, bezorgen):
    """Geef het eindbedrag terug, inclusief eventuele korting en bezorgkosten."""
    # TODO: Schrijf hier je code.
    korting = 0
    bezorgkosten = 0
    if subtotaal >= 25:
        korting = subtotaal * 0.05

    if bezorgen:
        bezorgkosten = 5

    if bezorgen and subtotaal >= 40:
        bezorgkosten = 3
    return round(subtotaal - korting + bezorgkosten, 2)


# 4. Verwerk een lijst productcodes
def maak_productlijst(tekst):
    """Geef opgeschoonde codes terug, zonder lege delen of dubbels, in volgorde."""
    # TODO: Schrijf hier je code.
    codes = tekst.split()
    resultaat = []

    for code in codes:
        code = code.strip()
        if code and code not in resultaat:
            resultaat.append(code)
    return resultaat


# 5. Maak een productkaart
def maak_productkaart(code, catalogus):
    """Geef de productkaart terug als string, of 'Product niet gevonden.'."""
    # TODO: Schrijf hier je code.
    if code not in catalogus:
        return "Product niet gevonden."

    product = catalogus[code]
    return (
        f"Code: {code}\n"
        f"Naam: {product['naam']}\n"
        f"Prijs: €{product['prijs']:.2f}\n"
        f"Voorraad: {product['voorraad']}\n"
        f"Categorie: {product['categorie']}")


# 6. Bereken het subtotaal
def bereken_subtotaal(bestelling, catalogus):
    """Geef de som van de regelbedragen terug, afgerond op twee decimalen."""
    # TODO: Schrijf hier je code. Gebruik bereken_regelbedrag.
    subtotaal = 0

    for code, aantal in bestelling.items():
        if code in catalogus:
            subtotaal += bereken_regelbedrag(catalogus[code]["prijs"], aantal)
    return round(subtotaal, 2)


# 7. Tel bestelde eenheden per categorie
def tel_per_categorie(bestelling, catalogus):
    """Geef een dictionary terug met de bestelde aantallen per categorie."""
    # TODO: Schrijf hier je code.
    resultaat = {}

    for code, aantal in bestelling.items():
        if code in catalogus:
            categorie = catalogus[code]["categorie"]
            if categorie in resultaat:
                resultaat[categorie] += aantal
            else:
                resultaat[categorie] = aantal
    return resultaat


# 8. Zoek beschikbare producten per categorie
def filter_producten(catalogus, categorie):
    """Geef codes van beschikbare producten in de categorie terug, in volgorde."""
    # TODO: Schrijf hier je code.
    resultaat = []
    for code, product in catalogus.items():
        if (product["categorie"].lower() == categorie.lower()
            and product["voorraad"] > 0): resultaat.append(code)

    return resultaat


# 9. Verwerk een bestelling in de voorraad
def verwerk_bestelling(bestelling, catalogus):
    """Werk de voorraad bij en geef True terug; bij ongeldige bestelling False.
    Bij een ongeldige of lege bestelling mag geen enkele voorraad veranderen.
    """
    # TODO: Schrijf hier je code.

    if not bestelling:
        return False

    for code, aantal in bestelling.items():
        if (code not in catalogus
            or aantal <= 0
            or catalogus[code]["voorraad"] < aantal):
            return False
    
    for code, aantal in bestelling.items():
        catalogus[code]["voorraad"] -= aantal
    return True


# Hoofdprogramma: gebruik hier de functies die je hierboven hebt geschreven.
if __name__ == "__main__":

    # TODO 1: Vraag de klantnaam en toon de opgeschoonde naam.
    naam = input("Klantnaam: ")
    klant = maak_klantnaam(naam)
    if klant == "Niet toegestaan":
        print("Bestelling geannuleerd.")
        exit()
    else:
        print("Klantnaam:", klant)

    # TODO 2: Vraag een categorie en toon de beschikbare productkaarten.
    categorie = input("\nCategorie: ")
    producten = filter_producten(PRODUCTEN, categorie)
    print("\nBeschikbare producten:")
    if not producten:
        print("Geen beschikbare producten gevonden.")
        exit()
    else:
        for code in producten:
            print()
            print(maak_productkaart(code, PRODUCTEN))

        # TODO 3: Verzamel productcodes en geldige aantallen in een bestelling.
    # Meld onbekende en uitverkochte producten en sla ze over.
    # Je mag geldige getalinvoer aannemen; omzetten kan met int(input(...)).

    bestelling = {}
    tekst = input("\nWelke producten? ")
    codes = maak_productlijst(tekst.replace(",", " "))
    for code in codes:
        if code not in PRODUCTEN:
            print(code,"is onbekend.")
            exit()
        
        elif PRODUCTEN[code]["voorraad"] == 0:
            print(code, "is uitverkocht.")
            exit()
        aantal = int(input("Aantal van " + code + ": "))
        voorraad = PRODUCTEN[code]["voorraad"]
        
        if aantal > voorraad:
            print(code, "heeft slechts", voorraad, "stuks in voorraad.")
            exit()
        bestelling[code] = aantal

    # TODO 4: Meld een lege bestelling en stop in dat geval zonder verwerking.
    # Geen nieuwe invoer: controleer de bestelling uit stap 3.
    # Bij {}: toon "Geen bestelbare producten. Er is geen bestelling geplaatst."
    # Ga dan niet verder met stap 5 en wijzig geen voorraad.

    if not bestelling:

        print("\nGeen bestelbare producten. "
            "Er is geen bestelling geplaatst.")

    else:

        # TODO 5: Vraag of de klant afhaalt (0) of laat bezorgen (1).
        bezorgen = (int(input("\nAfhalen (0) of bezorgen (1): "))== 1)

        # TODO 6: Toon het volledige besteloverzicht en de berekende bedragen.
        subtotaal = bereken_subtotaal(bestelling, PRODUCTEN)
        korting = 0
        if subtotaal >= 25:
            korting = round(subtotaal * 0.05, 2)
        bezorgkosten = 0

        if bezorgen:
            bezorgkosten = 5

            if subtotaal >= 40:
                bezorgkosten = 3
        totaal = bereken_totaal(subtotaal, bezorgen)

        print("\n===== BESTELOVERZICHT =====")
        print(f"Klant: {klant}")
        print("\nArtikelen:")

        for code, aantal in bestelling.items():
            product = PRODUCTEN[code]
            regelbedrag = bereken_regelbedrag(product["prijs"], aantal)

            print(f"- {product['naam']}: "
                f"{aantal} x €{product['prijs']:.2f} "
                f"= €{regelbedrag:.2f}")

        print(f"\nSubtotaal: €{subtotaal:.2f}")
        print(f"Korting: -€{korting:.2f}")
        print(f"Bezorgkosten: €{bezorgkosten:.2f}")
        print(f"Eindbedrag: €{totaal:.2f}")
        print("\nAantallen per categorie:")

        categorieen = tel_per_categorie(bestelling, PRODUCTEN)

        for categorie, aantal in categorieen.items():
            print(f"- {categorie}: {aantal}")

        # TODO 7: Vraag bevestiging (1) of annulering (0).
        # Verwerk alleen bij bevestiging en toon het resultaat en de resterende voorraad.

        bevestiging = int(input("\nBevestigen (1) / Annuleren (0): "))
        if bevestiging == 1:
            if verwerk_bestelling(bestelling, PRODUCTEN):
                print("\nBestelling verwerkt.")
                print("\nResterende voorraad:")

                for code in bestelling:
                    print(f"{PRODUCTEN[code]['naam']}: "
                        f"{PRODUCTEN[code]['voorraad']} stuks")
            else:
                print("Bestelling kon niet verwerkt worden.")
        else:
            print("Bestelling geannuleerd.")