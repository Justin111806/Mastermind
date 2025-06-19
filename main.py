import random
import os

kleuren = ["R", "G", "B", "P", "W", "Z"]
commentaar = ["Nee, dat is fout, L.", "Nope, dat is hem niet.", "Helaas, je hebt hem niet juist", "Wow, waarom dacht je dat? Dat is super fout."]
code_lengte = 4
max_poging = 10
def toon_menu():
    print("=== Mastermind Menu ===")
    print("1. Start spel")
    print("2. Instellingen")
    print("3. Credits")
    print("4. Stop")

def instellingen():
    global code_lengte, max_poging
    try:
        code_lengte = int(input("Nieuwe code-lengte (standaard 4): ") or code_lengte)
        max_poging = int(input("Maximale pogingen (standaard 10): ") or max_poging)
    except ValueError:
        print("Ongeldige invoer, instellingen blijven ongewijzigd.")

def credits():
    print("Gemaakt door jou :)")

uitleg = True  # Uitleg voor eerste ronde

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    toon_menu()
    keuze = input("Maak een keuze (1-4): ").strip()

    if keuze == "1":  # Start spel
        os.system('cls' if os.name == 'nt' else 'clear')
        if uitleg:
            print("Welkom, de kleuren zijn: Rood, Groen, Blauw, Paars, Wit, Zwart")
            for x in kleuren:
                print(x)
            print("Geen zorgen, je hoeft alleen de eerste letter te typen en hoofdletters hoeft niet. Spaties wel.")
            print(f"Lengte code: {code_lengte}, Maximale pogingen: {max_poging}")
            uitleg = False

        code = random.choices(kleuren, k=code_lengte)
        poging = 0

        while poging < max_poging:
            keuze_input = input(f"Poging {poging + 1}/{max_poging}, Wat is je keuze (bv. R G B P): ").strip().upper().split()

            if len(keuze_input) != code_lengte or not all(kleur in kleuren for kleur in keuze_input):
                print("Dat kan niet, geef exact 4 geldige kleuren (R G B P W Z)")
                continue

            correct_positie = sum(g == c for g, c in zip(keuze_input, code))
            correct_kleur = sum(min(keuze_input.count(c), code.count(c)) for c in set(kleuren)) - correct_positie

            if correct_positie != code_lengte:
                reactie = random.choice(commentaar)
                print(reactie)

            if correct_positie == code_lengte:
                print("JE HEBT GEWONNEN!")
                break

            poging += 1
            print(f"{correct_positie} kleuren goed geplaatst.")
            print(f"{correct_kleur} correcte kleuren in verkeerde positie.")

        if poging == max_poging:
            print("JE HEBT VERLOREN!")
            print(f"De juiste code was: {' '.join(code)}")

        opnieuw = input("Wil je nog een keer spelen? (ja/nee): ").strip().lower()
        if opnieuw != "ja":
            print("Bedankt voor het spelen!")
            break

    elif keuze == "2":
        instellingen()

    elif keuze == "3":
        credits()
        input("Druk op Enter om terug te gaan naar het menu.")

    elif keuze == "4":
        print("Tot de volgende keer!")
        break

    else:
        print("Ongeldige keuze. Probeer opnieuw.")
