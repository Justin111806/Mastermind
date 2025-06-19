import random

kleuren = ["R", "G", "B", "P", "W", "Z"]
commentaar = ["Nee, dat is fout, L.", "Nope, dat is hem niet.", "Helaas, je hebt hem niet juist", "Wow, waarom dacht je dat? Dat is super fout."]
code_lengte = 4
max_poging = 10

print("Mastermind")  # Print naam
print("Welkom, de kleuren zijn: Rood, Groen, Blauw, Paars, Wit, Zwart")
for x in kleuren:
    print(x)
print("Geen zorgen, je hoeft alleen de eerste letter te typen en hoofdletters hoeft niet. Spaties wel.")
print(f"Lengte code: {code_lengte}, Maximale pogingen: {max_poging}")

while True:  # Eindeloze loop tot speler nee zegt
    code = random.choices(kleuren, k=code_lengte)
    poging = 0

    print(code)  # Debug voor testen kleurcode

    while poging < max_poging:
        keuze = input(f"Poging {poging + 1}/{max_poging}, Wat is je keuze (bv. R G B P): ").strip().upper().split()

        if len(keuze) != code_lengte or not all(kleur in kleuren for kleur in keuze): # Controleert of invoer geldig is
            print("Dat kan niet, geef exact 4 geldige kleuren (R G B P W Z)")
            continue

        correct_positie = sum(g == c for g, c in zip(keuze, code))
        correct_kleur = sum(min(keuze.count(c), code.count(c)) for c in set(kleuren)) - correct_positie
        
        if correct_positie != code_lengte:
            for _ in range(1):
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