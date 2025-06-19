import random #Willekeurige code generator
import os #Console schoonmaken
import colorama #Kleurige tekst
from colorama import Fore, Back, Style
colorama.init()
#Kleuren spectrum
kleuren = ["R", "G", "B", "P", "W", "Z"]
#Commentaar voor fout
commentaar = ["Nee, dat is fout, L.", "Nope, dat is hem niet.", "Helaas, je hebt hem niet juist",
              "Wow, waarom dacht je dat? Dat is super fout.", "LOL JE BENT ZO DOM BRO",
              "Nou ja, ik snap niet wat je denkproces daar was."]
#Game regels
code_lengte = 4
max_poging = 10

uitleg = True
gekozen_versie = None

#Normale versie
def spel_logica_normaal():
    global uitleg, code_lengte, max_poging
    os.system('cls' if os.name == 'nt' else 'clear')
    #Uitleg
    if uitleg:
        print("Welkom, de kleuren zijn: Rood, Groen, Blauw, Paars, Wit, Zwart")
        for x in kleuren:
            print(x)
        print("Je hoeft alleen de eerste letter te typen, hoofdletters maakt niet uit. SPATIES WEL.")
        print("Zwarte Pin = juiste kleur en plek. Witte Pin = juiste kleur maar verkeerde plek.")
        print(f"Code lengte: {code_lengte}")
        print(f"Max pogingen: {max_poging}")
        uitleg = False
    #Code genereren
    code = random.choices(kleuren, k=code_lengte)
    poging = 0
    print("Code is gegenereerd!")
    #Game loop
    while poging < max_poging:
        keuze_input = input(f"Poging {poging + 1}/{max_poging}, geef je gok (bv. R G B P): ").strip().upper().split()

        if len(keuze_input) != code_lengte or not all(kleur in kleuren for kleur in keuze_input):
            print("Dat kan niet, geef exact geldige kleuren (R G B P W Z)")
            continue

        correct_positie = sum(g == c for g, c in zip(keuze_input, code))
        correct_kleur = sum(min(keuze_input.count(c), code.count(c)) for c in set(kleuren)) - correct_positie

        if correct_positie != code_lengte:
            print(random.choice(commentaar))

        if correct_positie == code_lengte:
            print("JE HEBT GEWONNEN!")
            break

        poging += 1
        print(f"Zwarte pinnen: {correct_positie}")
        print(f"Witte pinnen: {correct_kleur}")
    #Verloren
    if poging == max_poging:
        print("JE HEBT VERLOREN!")
        print(f"De juiste code was: {' '.join(code)}")
    #Opnieuw spelen
    opnieuw = input("Opnieuw spelen? (ja/nee): ").strip().lower()
    if opnieuw == "ja":
        spel_logica_normaal()
#Smaarten versie
def spel_logica_smaarten():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Smaarten versie is nog in ontwikkeling.")
    input("Druk op Enter om terug te keren.")
#Credits
def credits():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Gemaakt door: Justin Fung)")
    print("Speciale dank aan: CREDITS YOUTUBERS HIER JUSTIN")
    input("Druk op een toets om terug te gaan.")

# Startkeuze voor gameversie
while gekozen_versie not in ["1", "2"]:
    print("Kies spelversie:")
    print("1. Normale versie")
    print("2. Smaarten versie")
    gekozen_versie = input("Maak een keuze (1-2): ").strip()

# Hoofdmenu
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    #ASCII art
    print(".___  ___.      ___           _______.___________. _______ .______      .___  ___.  __  .__   __.  _______  ")
    print("|   \/   |     /   \         /       |           ||   ____||   _  \     |   \/   | |  | |  \ |  | |       \ ")
    print("|  \  /  |    /  ^  \       |   (----`---|  |----`|  |__   |  |_)  |    |  \  /  | |  | |   \|  | |  .--.  |")
    print("|  |\/|  |   /  /_\  \       \   \       |  |     |   __|  |      /     |  |\/|  | |  | |  . `  | |  |  |  |")
    print("|  |  |  |  /  _____  \  .----)   |      |  |     |  |____ |  |\  \----.|  |  |  | |  | |  |\   | |  '--'  |")
    print("|__|  |__| /__/     \__\ |_______/       |__|     |_______|| _| `._____||__|  |__| |__| |__| \__| |_______/ ")
    print("") #Ruimte tussen ASCII art en menu
    print("1. Start")
    print("2. Credits")
    print("3. Sluiten")

    keuze = input("Maak een keuze (1-3): ").strip()

    if keuze == "1":
        if gekozen_versie == "1":
            spel_logica_normaal()
        elif gekozen_versie == "2":
            spel_logica_smaarten()
    elif keuze == "2":
        credits()
    elif keuze == "3":
        print("Tot de volgende keer!")
        break
    else:
        print("Ongeldige keuze. Probeer opnieuw.")
