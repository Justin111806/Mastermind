import time
import random #Willekeurige code generator
import os #Console schoonmaken
import colorama #Kleurige tekst voor duidelijkheid. Gedaan door Package GitHub
from colorama import Fore, Back, Style
colorama.init(autoreset=True) #Automatisch terug naar standaard kleur

#Ontwikkelaarsoptie
debugmodus = False

#Kleuren spectrum
basis_kleuren = ["R", "G", "B", "P", "W", "Z"]

#Kleuren spectrum met kleurige tekst voor duidelijkheid
kleuren = [Fore.RED + "R",
           Fore.GREEN + "G",
           Fore.BLUE + "B",
           Fore.MAGENTA + "P", #Geen paars in colorama :(, dus magenta
           "W", #Wit is standaard kleur, hoeft niet colorama gebruiken
           Fore.BLACK + "Z"]

#Commentaar voor fout
commentaar = [Fore.RED + "...Fout.",
              Fore.RED + "...Net niet",
              Fore.RED + "...Helaas",
              Fore.RED + "...Wat was je denkproces daar?",
              Fore.RED + "...Totaal verkeerd",
              Fore.RED + "...Dat was een slechte gok"]

#Items voor shop
items = { #ander symbool voor items, anders wordt : verward
    "1": ("Kleurloze Kristal", 5),
    "2": ("Gefluister van Echo's", 2),
    "3": ("Kleurrijke Schilderspalet", 4),
    "4": ("Potlood Gum", 10),
    "5": ("Levend Oog", 7),
}

#Items die speler heeft gekocht
gekochte_items = {
    "Kleurloze Kristal": 0,
    "Gefluister van Echo's": 0,
    "Kleurrijke Schilderspalet": 0,
    "Potlood Gum": 0,
    "Levend Oog": 0,
}

goud = 0
spaarvarken = 0

#Functies voor items
def gebruik_kleurloze_kristal(code):
    onthulde_kleur = random.choice(code)
    os.system('cls' if os.name == 'nt' else 'clear')
    print_textballon(Fore.YELLOW + f"✨ De Kleurloze Kristal onthult: een kleur in de code is '{onthulde_kleur}'")
    input("Druk op Enter om verder te gaan...")
def gebruik_gefluister_van_echos(code, code_lengte):
    domme_tips = [
        "De code bestaat uit kleuren.", 
        "Gebruik kleuren die je nog niet hebt geprobeerd.",
        "Soms is rood… gewoon rood."
    ]
    slimme_tips = [
        f"De kleur op positie {random.randint(1, code_lengte)} is '{code[random.randint(0, code_lengte-1)]}'",
        f"De kleur '{random.choice(code)}' zit op de juiste plek in je laatste gok."  #Optioneel controleren met echte gok
    ]
    tip = random.choice(domme_tips + slimme_tips)
    os.system('cls' if os.name == 'nt' else 'clear')
    print_textballon(Fore.MAGENTA + f"👁‍🗨 Gefluister van Echo's: {tip}")
    input("Druk op Enter om verder te gaan...")
def gebruik_kleurrijke_schilderspalet(code):
    index = random.randint(0, len(code)-1)
    oude_kleur = code[index]
    nieuwe_kleur = random.choice([kleur for kleur in basis_kleuren if kleur != oude_kleur])
    code[index] = nieuwe_kleur
    os.system('cls' if os.name == 'nt' else 'clear')
    print_textballon(Fore.LIGHTBLUE_EX + f"🎨 De kleur op positie {index+1} is nu veranderd…")
    input("Druk op Enter om verder te gaan...")
    return code

def gebruik_potlood_gum(code):
    kleur = random.choice(code)
    while kleur in code:
        code.remove(kleur)
    os.system('cls' if os.name == 'nt' else 'clear')
    print_textballon(Fore.LIGHTWHITE_EX + f"✏️ De kleur '{kleur}' is uit de code gewist. Code is nu {len(code)} kleuren lang.")
    input("Druk op Enter om verder te gaan...")
    return code
def gebruik_levend_oog(keuze_input, code):
    hints = []
    for i, (a, b) in enumerate(zip(keuze_input, code)):
        if a == b:
            hints.append(f"🔮 Positie {i+1}: zwart pin mogelijk")
    if hints:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_textballon(Fore.CYAN + "👁 Levend Oog staart: " + " | ".join(hints))
        input("Druk op Enter om verder te gaan...")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_textballon("👁 Levend Oog ziet… niets.")
        input("Druk op Enter om verder te gaan...")

#Gebruik item samengesteld
def gebruik_item(item_nummer, code, keuze_input, gekochte_items, code_lengte):
    if item_nummer == "1":  # Kleurloze Kristal
        gebruik_kleurloze_kristal(code)

    elif item_nummer == "2":  # Gefluister van Echo's
        gebruik_gefluister_van_echos(code, code_lengte)

    elif item_nummer == "3":  # Kleurrijke Schilderspalet
        code[:] = gebruik_kleurrijke_schilderspalet(code)  # wijzig code in-place

    elif item_nummer == "4":  # Potlood Gum
        code[:] = gebruik_potlood_gum(code)

    elif item_nummer == "5":  # Levend Oog
        if keuze_input:
            gebruik_levend_oog(keuze_input, code)
        else:
                print_textballon(Fore.LIGHTBLACK_EX + "Het oog kan niets zien zonder een gok…")
    else:
        print_textballon("❌ Onbekend item.")

    return spaarvarken

#Game regels
code_lengte = 4
max_poging = 10

uitleg = True
gekozen_versie = None

#Laadscherm
for x in range(4):
  print("Aan het laden")
  time.sleep(0.5)
  os.system("clear")
  print("Aan het laden.")
  time.sleep(0.5)
  os.system("clear")
  print("Aan het laden..")
  time.sleep(0.5)
  os.system("clear")
  print("Aan het laden...")
  time.sleep(0.5)
  os.system("clear")

#ASCII art voor Main Menu
def ascii_menu():
    ascii_art_mastermind = r"""
    .___  ___.      ___           _______.___________. _______ .______      .___  ___.  __  .__   __.  _______  
    |   \/   |     /   \         /       |           ||   ____||   _  \     |   \/   | |  | |  \ |  | |       \ 
    |  \  /  |    /  ^  \       |   (----`---|  |----`|  |__   |  |_)  |    |  \  /  | |  | |   \|  | |  .--.  |
    |  |\/|  |   /  /_\  \       \   \       |  |     |   __|  |      /     |  |\/|  | |  | |  . `  | |  |  |  |
    |  |  |  |  /  _____  \  .----)   |      |  |     |  |____ |  |\  \----.|  |  |  | |  | |  |\   | |  '--'  |
    |__|  |__| /__/     \__\ |_______/       |__|     |_______|| _| `._____||__|  |__| |__| |__| \__| |_______/ 
    """
    print() #Ruimte tussen ASCII art
    ascii_art_start = r"""  
     __              _______.___________.    ___      .______     .___________.
    /_ |            /       |           |   /   \     |   _  \    |           |
     | |           |   (----`---|  |----`  /  ^  \    |  |_)  |   `---|  |----`
     | |            \   \       |  |      /  /_\  \   |      /        |  |     
     | |  __    .----)   |      |  |     /  _____  \  |  |\  \----.   |  |     
     |_| (__)   |_______/       |__|    /__/     \__\ | _| `._____|   |__|     
    """
    print() #Ruimte tussen ASCII art
    ascii_art_credits = r"""
      ___           ______ .______       _______  _______   __  .___________.    _______.
     |__  \        /      ||   _  \     |   ____||       \ |  | |           |   /       |
        ) |       |  ,----'|  |_)  |    |  |__   |  .--.  ||  | `---|  |----`  |   (----`
       / /        |  |     |      /     |   __|  |  |  |  ||  |     |  |        \   \    
      / /_   __   |  `----.|  |\  \----.|  |____ |  '--'  ||  |     |  |    .----)   |   
     |____| (__)   \______|| _| `._____||_______||_______/ |__|     |__|    |_______/    
    """
    print() #Ruimte tussen ASCII art
    ascii_art_sluiten = r"""
     ____              _______. __       __    __   __  .___________. _______ .__   __. 
    |___ \            /       ||  |     |  |  |  | |  | |           ||   ____||  \ |  | 
     ___) |          |   (----`|  |     |  |  |  | |  | `---|  |----`|  |__   |   \|  | 
    |___<             \   \    |  |     |  |  |  | |  |     |  |     |   __|  |  . `  | 
     ___) |  __   .----)   |   |  `----.|  `--'  | |  |     |  |     |  |____ |  |\   | 
    |____/  (__)  |_______/    |_______| \______/  |__|     |__|     |_______||__| \__| 
    """
    print() #Ruimte tussen ASCII art
    import os
    breedte_console = os.get_terminal_size().columns

    volledige_art = ascii_art_mastermind + "\n\n" + ascii_art_start + "\n\n" + ascii_art_credits + "\n\n" + ascii_art_sluiten

    # Print gecentreerd in console
    for regel in volledige_art.splitlines():
        spaties = (breedte_console - len(regel)) // 2
        print(" " * spaties + regel)

#ASCII art voor Shop
def toon_shop():
    ascii_shop = r"""
     _______________________________
    |                               |
    |     De Winkel van Zielen      |
    |_______________________________|
    """

    catalogus = [
        ("1. Kleurloze Kristal", 
         "Verandert naar een willekeurige kleur die in de code zit.",
        "5 goudstukken"),
        ("2. Gefluister van Echo's", 
         "Geeft willekeurige tips",
        "2 goudstukken"),
        ("3. Kleurrijke Schilderspalet", 
         "Vervangt een willekeurige kleur in de code met een andere willekeurige kleur.",
        "4 goudstukken"),
        ("4. Potlood Gum", 
         "Verwijdert een kleur uit de code (1× per ronde).",
        "10 goudstukken"),
        ("5. Levend Oog", 
         "Geeft een diep inzicht. Werkt alleen nadat je al 1 keer gegokt hebt.",
        "7 goudstukken"),
        ("0. Verlaat de Shop", 
         "Terug naar het spel."),
    ]

    print(ascii_shop)
    for item in catalogus:
        if len(item) == 3:
            naam, beschrijving, prijs = item
            print(f"{naam}\n   → {beschrijving}\n   💰 {prijs}\n")
        elif len(item) == 2:
            naam, beschrijving = item
            print(f"{naam}\n   → {beschrijving}\n")

#ASCII art voor Actiekeuze menu
def toon_actiekeuze_menu():
    actiemenu = f"""{Fore.CYAN}
╔════════════════════════════════╗
║  Wat wil je doen, avonturier?  ║
╠════════════════════════════════╣
║  1. 🔍 Code raden              ║
║  2. 🎴 Item gebruiken          ║
╚════════════════════════════════╝"""
    print("\n" + actiemenu)

#ASCII art voor Items menu
def toon_items_menu(gekochte_items):
    print(Fore.MAGENTA + "\n" + """\
╔══════════════════════════════════════╗
║       🎴 Beschikbare Items           ║
╠══════════════════════════════════════╣""")

    for nummer, (naam, aantal) in enumerate(gekochte_items.items(), start=1):
        print(f"║ {nummer}. {naam.ljust(30)}({aantal}x)║")

    print("╚══════════════════════════════════════╝")
    print(Fore.YELLOW + "Kies het nummer van het item dat je wil gebruiken (of 0 om terug te keren):")

#Textballon voor leuke print
def print_textballon(tekst):
    breedte = 70
    lijnen = tekst.split("\n")

    print("\n" * 5)  # Simuleert ruimte boven de ballon

    print("╭" + "─" * (breedte + 2) + "╮")
    for lijn in lijnen:
        print("│ " + lijn.ljust(breedte) + " │")
    print("╰" + "─" * (breedte + 2) + "╯")

    return len(lijnen) + 3  # Hoogte van ballon

#Normale spel logica WERKT 100%
def spel_logica_normaal():
    global uitleg, code_lengte, max_poging, debugmodus
    os.system('cls' if os.name == 'nt' else 'clear') #Console schoonmaken

    waarschuwing = True
    if waarschuwing:
        print("Je staat op het punt om de Normale versie te spelen.")
        print("Ga je verder?")
        print("1. Ja")
        print("2. Nee")
        print("3. Ja, met debugmodus (ontwikkelaarsoptie)")
        keuze = input("Maak een keuze (1-3): ")
        if keuze == "1":
            waarschuwing = False
        elif keuze == "2":
            return
        elif keuze == "3":
            waarschuwing = False
            debugmodus = True

        else:
            print("Ongeldige invoer. Probeer opnieuw.")
            input("Druk op Enter om verder te gaan...")
            os.system('cls' if os.name == 'nt' else 'clear')

    os.system('cls' if os.name == 'nt' else 'clear') #Console schoonmaken
    #Uitleg
    if uitleg:
        print("Welkom, de kleuren zijn: "
              + Fore.RED + "Rood, "
              + Fore.GREEN + "Groen, "
              + Fore.BLUE + "Blauw, "
              + Fore.MAGENTA + "Paars, "
              + Fore.WHITE + "Wit, " #Wit is standaard, maar anders wordt magenta paars naar wit
              + Fore.BLACK + "Zwart")

        #Kleuren spectrum printen voor duidelijkheid
        for x in kleuren:
            print(x)

        print("Je hoeft alleen de EERSTE letter te typen, hoofdletters maakt niet uit. SPATIES WEL.")
        print("Zwarte Pin = juiste kleur en plek. Witte Pin = juiste kleur maar verkeerde plek.")
        print(f"Code lengte: {code_lengte}")
        print(f"Maximale pogingen: {max_poging}")
        uitleg = False #Eindigt uitleg

    #Code genereren
    code = random.choices(basis_kleuren, k=code_lengte)
    poging = 0
    print("Code is gegenereerd!")

    #Debugging
    if debugmodus:
        print(Fore.YELLOW + f"[DEBUG] Geheime code: {' '.join(code)}" + Style.RESET_ALL)
        input("Druk op Enter om verder te gaan...")

    #Game loop
    while poging < max_poging:
        print(f"Poging {poging + 1}/{max_poging}: Geef je gok (Voorbeeld: r g b p)")
        keuze_input = input(Fore.MAGENTA + "").strip().upper().split()

        #Ongeldige input
        if len(keuze_input) != code_lengte or not all(kleur in basis_kleuren for kleur in keuze_input):
            print(Fore.RED + "Dat kan niet, geef exact geldige kleuren (R G B P W Z)")
            continue

        #Calculatie van zwarte en witte pinnen
        correct_positie = sum(g == c for g, c in zip(keuze_input, code))
        correct_kleur = sum(min(keuze_input.count(c), code.count(c)) for c in set(basis_kleuren)) - correct_positie

        #Commentaar na fout
        if correct_positie != code_lengte:
            print(random.choice(commentaar))

        #Gewonnen
        if correct_positie == code_lengte:
            print(Style.BRIGHT + Fore.GREEN + "JE HEBT GEWONNEN!")
            break

        #Update pogingen
        poging += 1

        #Print zwarte en witte pinnen
        print(Fore.BLACK + f"Zwarte pinnen: {correct_positie}")
        print(Fore.CYAN + f"Witte pinnen: {correct_kleur}")

    #Verloren
    if poging == max_poging:
        print(Style.DIM + Fore.RED + "JE HEBT VERLOREN!")
        print(f"De juiste code was: {' '.join(code)}")

    #Opnieuw spelen
    opnieuw = input("Opnieuw spelen? (ja/nee): ").strip().lower()
    if opnieuw == "ja":
        spel_logica_normaal() #Spel herstart

#rusttijd tussen rondes
def rust_tussen_rondes(goud, gekochte_items, ronde_nummer=None, huidige_kleuren=None):

    while True:
        if goud == 1:
            print_textballon(f"Je hebt {goud} goudstuk \n"
            " Wat wil je doen?\n"
            "  1. Rusten\n"
            "  2. Kopen\n"
            "  3. Verder naar de volgende ronde",
            )
        else:
            print_textballon(
            f"Je hebt {goud} goudstukken \n"
            " Wat wil je doen?\n"
            "  1. Rusten\n"
            "  2. Kopen\n"
            "  3. Verder naar de volgende ronde",
            )

        keuze = input("Maak je keuze: ").strip()

        if keuze == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            print_textballon("Je rust je even uit...", )
            input("Druk op Enter om verder te gaan...")

            os.system('cls' if os.name == 'nt' else 'clear')
            print_textballon("Je bent nu uitgerust!", )
            input("Druk op Enter om verder te gaan...")

            os.system('cls' if os.name == 'nt' else 'clear') #Wist gehele console

        elif keuze == "2":
            os.system('cls' if os.name == 'nt' else 'clear') #Wist gehele console

            while True:
                toon_shop()
                keuze_kopen = input("Kies een itemnummer om te kopen: ")

                if keuze_kopen == "0":
                    os.system('cls' if os.name == 'nt' else 'clear') #Wist gehele console
                    break
                elif keuze_kopen in items:
                    naam, prijs = items[keuze_kopen]
                    if goud >= prijs:
                        goud -= prijs
                        gekochte_items[naam] += 1
                        os.system('cls' if os.name == 'nt' else 'clear') #Wist gehele console
                        print_textballon(Fore.YELLOW + f"Je hebt '{naam}' gekocht.")
                        input("Druk op Enter om verder te gaan...")
                        os.system('cls' if os.name == 'nt' else 'clear') #Wist gehele console
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear') #Wist gehele console
                        print_textballon(Fore.RED + "Niet genoeg goud...")
                        input("Druk op Enter om verder te gaan...")
                        os.system('cls' if os.name == 'nt' else 'clear')
                else:
                    os.system('cls' if os.name == 'nt' else 'clear') #Wist gehele console
                    print_textballon(Fore.RED + "Ongeldige keuze...")
                    input("Druk op Enter om verder te gaan...")
                    os.system('cls' if os.name == 'nt' else 'clear') #Wist gehele console

        elif keuze == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            print_textballon("Je gaat nu verder...")
            input("Druk op Enter om verder te gaan...")
            #Update rondes, maar het werkt niet, help.
            ronde_nummer =+ 1
            start_ronde_n(ronde_nummer + 1)
            return goud, gekochte_items, spaarvarken, ronde_nummer #Geeft de waarden terug aan rust_tussen_rondes


        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print_textballon(Fore.RED + "Ongeldige keuze, probeer opnieuw.")
            input("Druk op Enter om verder te gaan...")
            os.system('cls' if os.name == 'nt' else 'clear')

#Smaarten spel logica
def spel_logica_smaarten():
    global uitleg, code_lengte, max_poging, debugmodus
    os.system('cls' if os.name == 'nt' else 'clear')

    #Waarschuwing voor Smaarten versie
    waarschuwing = True
    while waarschuwing:
        print("Je staat op het punt om de Smaarten versie te spelen.")
        print("Het is aanbevolen om eerst de Normale versie te spelen.")
        print(Fore.RED + "De Smaarten versie is helaas NIET AF. Het was maar een passion project, waar ik aan werkte toen de Normale versie af was.")
        print("Ga je verder?")
        print("1. Ja")
        print("2. Nee")
        print("3. Ja, met debugmodus (AANBEVOLEN, want de code vanaf nu is niet geweldig.)")
        keuze = input("Maak een keuze (1-3): ")
        if keuze == "1":
            waarschuwing = False
        elif keuze == "2":
            return
        elif keuze == "3":
            waarschuwing = False
            debugmodus = True

        else:
            print("Ongeldige invoer. Probeer opnieuw.")
            input("Druk op Enter om verder te gaan...")
            os.system('cls' if os.name == 'nt' else 'clear')

        os.system('cls' if os.name == 'nt' else 'clear') #Console schoonmaken

    #Introductie tekst
    teksten = [
        "...",
        "Welkom, verloren ziel.",
        "Je bent gestorven, maar het lot is je nog niet helemaal vergeten...",
        "Ik ben ✼⨸ℤ⛇♞...",
        "Maar noem mij gerust maar Smaarten, de GameMaster.",
        "Er is een kans voor jou om terug te keren naar de overwereld.",
        "Een spel: Mastermind.",
        "Win 6 keer, en je ontwaakt opnieuw in het land der levenden.",
        "Maar als je maar voor 1 keer verliest...",
        "Zal je voorgoed wegzakken naar de hel.",
        "Voordat we beginnen, moet je dit contract ondertekenen.",
        "Vertel mij je voornaam..."
    ]

    #Dialoog
    for tekst in teksten[:-1]:
        print_textballon(tekst)
        input("Druk op Enter om verder te gaan...")
        os.system('cls' if os.name == 'nt' else 'clear')

    #Laatste vraag (naam)
    print_textballon(teksten[-1])
    naam = input(">>> ").strip()
    os.system('cls' if os.name == 'nt' else 'clear')

    #Reactie op naam
    if naam.lower() in ["smaarten", "gamemaster"]:
        reactie = "Haha... Jij noemt jezelf zoals ik? Hoe typisch. Geesten vergeten hun naam snel, dus ik vergeef het je."
    elif naam.lower() == "bart":
        reactie = "...Ik hoop dat u een goede tijd gaat hebben met het spel."
    elif naam.lower() == "justin":
        reactie = "...Hallo, mijn maker."
    else:
        reactie = f"{naam}... Ik hoop voor je dat dat je echte naam is..."

    #Print reactie
    print_textballon(reactie)
    input("Druk op Enter om verder te gaan...")
    os.system('cls' if os.name == 'nt' else 'clear')

    #Begin Spel
    print_textballon("Het contract is getekend. Laten we beginnen...")
    input("Druk op Enter om het spel te starten...")
    os.system('cls' if os.name == 'nt' else 'clear')

    # Uitleg vragen
    print_textballon("Wil je de regels van het spel horen? (1-2)")
    keuze = input("1. Ja.\n2. Nee. ").strip().lower()
    os.system('cls' if os.name == 'nt' else 'clear')

    if keuze == "1":
        uitleg = [
            "Het spel is simpel.",
            "Ik kies een geheime code uit kleuren.",
            "Voor nu is het maar 6 kleuren:",
            "Rood, Groen, Blauw, Paars, Wit, Zwart.",
            "Jij moet raden wat de code is.",
            "Na elke poging geef ik feedback:",
            "- Zwarte pin: Juiste kleur, op de juiste plek.",
            "- Witte pin: Juiste kleur, op de verkeerde plek.",
            "Je hebt een beperkt aantal pogingen...",
            "En slechts één leven.",
            "En herrinner... Type je antwoorden met spaties tussen de letters."
        ]

        #Uitleg printen
        for x in uitleg:
            print_textballon(x)
            input("Druk op Enter om verder te gaan...")
            os.system('cls' if os.name == 'nt' else 'clear')

    #Niet uitleg
    elif keuze == "2":
        print_textballon("...Goed, laten we beginnen.")
        input("Druk op Enter om verder te gaan...")
        os.system('cls' if os.name == 'nt' else 'clear')

    #Verkeerde invoer
    else:
        print_textballon("Antwoord met 1, of 2.")
        input("Druk op Enter om verder te gaan...")
        os.system('cls' if os.name == 'nt' else 'clear')

    #Code genereren
    code = random.choices(basis_kleuren, k=code_lengte)
    poging = 0

    print_textballon("Code gegenereerd...")
    input("Druk op Enter om verder te gaan...")

    #Game loop
    while poging < max_poging:
        os.system('cls' if os.name == 'nt' else 'clear') #Wist oude ballon bij begin poging

        #Debug
        if debugmodus:
            print(Fore.YELLOW + f"[DEBUG] Geheime code: {' '.join(code)}" + Style.RESET_ALL)
            input("Druk op Enter om verder te gaan...")

        print_textballon(f"Poging {poging + 1}/{max_poging} Voer je gok in (kleuren: R, G, B, P, W, Z")
        keuze_input = input(Fore.MAGENTA).strip().upper().split()

        #Ongeldige input
        if len(keuze_input) != code_lengte or not all(kleur in basis_kleuren for kleur in keuze_input):
            os.system('cls' if os.name == 'nt' else 'clear')
            print_textballon(Fore.RED + "...Dat kan niet, geef exact geldige kleuren (R G B P W Z)")
            input("Druk op Enter om verder te gaan...")
            continue

        correct_positie = sum(g == c for g, c in zip(keuze_input, code))
        correct_kleur = sum(min(keuze_input.count(c), code.count(c)) for c in set(basis_kleuren)) - correct_positie

        #Niet code gekraakt
        if correct_positie != code_lengte:
            os.system('cls' if os.name == 'nt' else 'clear')
            print_textballon(random.choice(commentaar))
            input("Druk op Enter om verder te gaan...")

            os.system('cls' if os.name == 'nt' else 'clear')
            print_textballon(Fore.BLACK + f"Zwarte pinnen: {correct_positie} " + Fore.CYAN + f"Witte pinnen: {correct_kleur} ")
            input("Druk op Enter om verder te gaan...")
            poging += 1
            continue

        #Gewonnen
        if correct_positie == code_lengte:
            os.system('cls' if os.name == 'nt' else 'clear')
            print_textballon(Style.BRIGHT + Fore.GREEN + "...Correct")
            input("Druk op Enter om verder te gaan...")
            os.system('cls' if os.name == 'nt' else 'clear')

            #Update goud
            goud = 30

            print_textballon("Je gaat door naar de tweede ronde...")
            input("Druk op Enter om verder te gaan...")
            os.system('cls' if os.name == 'nt' else 'clear')

            print_textballon("Maar geen zorgen, ik geef je tijd om te rusten.")
            input("Druk op Enter om verder te gaan...")
            os.system('cls' if os.name == 'nt' else 'clear')

            #Rusttijd
            ronde_nummer = +1
            rust_tussen_rondes(goud, gekochte_items, spaarvarken, ronde_nummer)
            return True, ronde_nummer

    #Verloren
    if poging == max_poging:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_textballon(Style.DIM + Fore.RED + "...Helaas. Je hebt verloren.")
        input("Druk op Enter om verder te gaan...")
        os.system('cls' if os.name == 'nt' else 'clear')
        print_textballon(f"De juiste code was: {' '.join(code)}")
        input("Druk op Enter om verder te gaan...")

        #Opnieuw spelen
        opnieuw = input("Je sterft. Opnieuw proberen? (ja/nee): ").strip().lower()
        if opnieuw == "ja":
            spel_logica_smaarten() #Spel herstart

def spel_logica_smaarten_advanced(ronde_nummer, goud, huidige_kleuren):
    global code_lengte, max_poging, debugmodus, gekochte_items

    huidige_code_lengte = code_lengte + (ronde_nummer - 1)
    huidige_max_poging = max_poging - ronde_nummer + 1

    #Genereer code
    code = random.choices(huidige_kleuren, k=huidige_code_lengte)
    poging = 0

    print_textballon("De code is gegenereerd. Veel succes...")
    input("Druk op Enter om verder te gaan...")
    os.system('cls' if os.name == 'nt' else 'clear')

    #Game loop
    while poging < huidige_max_poging:
        os.system('cls' if os.name == 'nt' else 'clear')

        #Debug
        if debugmodus:
            print(Fore.YELLOW + f"[DEBUG] Geheime code: {' '.join(code)}" + Style.RESET_ALL)
            input("Druk op Enter om verder te gaan...")

        print_textballon(f"Poging {poging + 1}/{huidige_max_poging} - Code lengte: {len(code)}")
        toon_actiekeuze_menu()
        actie = input(Fore.MAGENTA + "👉 ").strip()
        os.system('cls' if os.name == 'nt' else 'clear')

        #Gokken
        if actie == "1":
            keuze_input = input(Fore.MAGENTA + "Voer je gok in (bv. R G B P): ").strip().upper().split()

            if len(keuze_input) != len(code) or not all(kleur in huidige_kleuren for kleur in keuze_input):
                print_textballon(Fore.RED + f"Dat kan niet. Geef exact {len(code)} geldige kleuren.")
                input("Druk op Enter om verder te gaan...")
                os.system('cls' if os.name == 'nt' else 'clear')
                continue

            correct_positie = sum(g == c for g, c in zip(keuze_input, code))
            correct_kleur = sum(min(keuze_input.count(c), code.count(c)) for c in set(huidige_kleuren)) - correct_positie

            poging += 1

            #Commentaar na fout
            if correct_positie != huidige_code_lengte:
                print_textballon(random.choice(commentaar))
                input("Druk op Enter om verder te gaan...")
                os.system('cls' if os.name == 'nt' else 'clear')

                print_textballon(Fore.BLACK + f"Zwarte pinnen: {correct_positie} " + Fore.CYAN + f"Witte pinnen: {correct_kleur}")
                input("Druk op Enter om verder te gaan...")
                os.system('cls' if os.name == 'nt' else 'clear')
                continue

            #Gewonnen
            if correct_positie == huidige_code_lengte:
                goud += 30
                print_textballon(Style.BRIGHT + Fore.GREEN + "...Correct.")
                input("Druk op Enter om verder te gaan...")
                os.system('cls' if os.name == 'nt' else 'clear')

                print_textballon(f"Goed gespeeld, het is tijd voor ronde {ronde_nummer +1} ...")
                input("Druk op Enter om verder te gaan...")
                os.system('cls' if os.name == 'nt' else 'clear')

                print_textballon("Je mag nu even uitrusten.")
                input("Druk op Enter om verder te gaan...")
                os.system('cls' if os.name == 'nt' else 'clear')

                #Start volgende ronde
                ronde_nummer += 1
                rust_tussen_rondes(ronde_nummer + 1, goud, huidige_kleuren)
                return True, ronde_nummer, goud

        #Item menu
        elif actie == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            while True:
                toon_items_menu(gekochte_items)
                gekozen = input("Welk item wil je gebruiken? (0 om terug te gaan) ").strip()
                if gekozen == "0":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break

                if not gekozen.isdigit():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print_textballon("Ongeldige invoer. Probeer opnieuw.")
                    input("Druk op Enter om verder te gaan...")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue

                #Nummers met item namen voor duidelijkheid
                item_mapping = {
                    "1": "Kleurloze Kristal",
                    "2": "Gefluister van Echo's", 
                    "3": "Kleurrijke Schilderspalet",
                    "4": "Potlood Gum",
                    "5": "Levend Oog"
                }

                if gekozen in item_mapping:
                    item_naam = item_mapping[gekozen]
                    if gekochte_items[item_naam] > 0:
                        if gekozen == "1":
                            gebruik_kleurloze_kristal(code)
                        elif gekozen == "2":
                            gebruik_gefluister_van_echos(code, huidige_code_lengte)
                        elif gekozen == "3":
                            code = gebruik_kleurrijke_schilderspalet(code,)
                        elif gekozen == "4":
                            code = gebruik_potlood_gum(code)
                            huidige_code_lengte = len(code)  #Update lengte
                        elif gekozen == "5":
                            if 'keuze_input' in locals():
                                gebruik_levend_oog(keuze_input, code) #geen probleem als keuze_input niet bestaat
                            else:
                                os.system('cls' if os.name == 'nt' else 'clear')

                                print_textballon("Je hebt nog geen gok gedaan om Levend Oog te gebruiken.")
                                input("Druk op Enter om verder te gaan...")
                                os.system('cls' if os.name == 'nt' else 'clear')

                        gekochte_items[item_naam] -= 1
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print_textballon("Dat item heb je het niet.")
                        input("Druk op Enter om verder te gaan...")

                #Als de if elso loop niet werkt
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print_textballon("Dat item heb je niet.")
                    input("Druk op Enter om verder te gaan...")
                    os.system('cls' if os.name == 'nt' else 'clear')

        #Verkeerde input
        else:
            print_textballon("Kies 1 of 2.")
            input("Druk op Enter om verder te gaan...")
            os.system('cls' if os.name == 'nt' else 'clear')

    if poging == huidige_max_poging:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_textballon(Style.DIM + Fore.RED + "...Helaas. Je hebt verloren.")
        input("Druk op Enter om verder te gaan...")
        os.system('cls' if os.name == 'nt' else 'clear')
        print_textballon(f"De juiste code was: {' '.join(code)}")
        input("Druk op Enter om verder te gaan...")

        #Opnieuw spelen
        opnieuw = input("Je, sterft. Opnieuw proberen? (ja/nee): ").strip().lower()
        if opnieuw == "ja":
            spel_logica_smaarten() #Spel herstart

#Ronde logica DAT NIET WERKT IK HEB GEEN IDEE WAAROM
def start_ronde_n(ronde_nummer):
    global code_lengte, max_poging, debugmodus

    os.system('cls' if os.name == 'nt' else 'clear') #Wist scherm

    #Safety precausion als ronde_nummer 1 is
    if ronde_nummer == 1:
        ronde_nummer += 1
    if ronde_nummer <=6:
        print_textballon(f"Welkom terug... Klaar voor ronde {ronde_nummer}? Deze keer wordt het moeilijker...")
        input("Druk op Enter om verder te gaan...")
        os.system('cls' if os.name == 'nt' else 'clear')

        #Moeilijkheidsgraad per ronde
        huidige_kleuren = basis_kleuren.copy()
        if ronde_nummer >= 2:
           huidige_kleuren.append("O") #Oranje
           print_textballon("Ik heb een nieuwe kleur toegevoegd... O (Oranje)")
           input("Druk op Enter om verder te gaan...")
           os.system('cls' if os.name == 'nt' else 'clear')
           print_textballon("En uw aantal pogingen gaat omlaag (-1)")
           input("Druk op Enter om verder te gaan...")
           os.system('cls' if os.name == 'nt' else 'clear')
           spel_logica_smaarten_advanced(ronde_nummer, goud, huidige_kleuren)
        elif ronde_nummer >= 3:
            huidige_kleuren.append("T") #Turquoise
            print_textballon("Ik heb een nieuwe kleur toegevoegd... T (Turquoise)")
            input("Druk op Enter om verder te gaan...")
            os.system('cls' if os.name == 'nt' else 'clear')
            print_textballon("En uw aantal pogingen gaat omlaag (-2)")
            input("Druk op Enter om verder te gaan...")
            os.system('cls' if os.name == 'nt' else 'clear')
            spel_logica_smaarten_advanced(ronde_nummer, goud, huidige_kleuren)
        elif ronde_nummer >= 4:
            huidige_kleuren.append("A") #Amber
            print_textballon("Ik heb een nieuwe kleur toegevoegd... A (Amber)")
            input("Druk op Enter om verder te gaan...")
            os.system('cls' if os.name == 'nt' else 'clear')
            print_textballon("En uw aantal pogingen gaat omlaag (-3)")
            input("Druk op Enter om verder te gaan...")
            os.system('cls' if os.name == 'nt' else 'clear')
            spel_logica_smaarten_advanced(ronde_nummer, goud, huidige_kleuren)
        elif ronde_nummer >= 5:
            huidige_kleuren.append("L") #Lilac
            print_textballon("Ik heb een nieuwe kleur toegevoegd... L (Lilac)")
            input("Druk op Enter om verder te gaan...")
            os.system('cls' if os.name == 'nt' else 'clear')
            print_textballon("En uw aantal pogingen gaat omlaag (-4)")
            input("Druk op Enter om verder te gaan...")
            os.system('cls' if os.name == 'nt' else 'clear')
            spel_logica_smaarten_advanced(ronde_nummer, goud, huidige_kleuren)
        elif ronde_nummer >= 6:
            huidige_kleuren.append("C") #Cyan
            print_textballon("Ik heb een nieuwe kleur toegevoegd... C (Cyan)")
            input("Druk op Enter om verder te gaan...")
            os.system('cls' if os.name == 'nt' else 'clear')
            print_textballon("En uw aantal pogingen gaat omlaag (-5)")
            input("Druk op Enter om verder te gaan...")
            os.system('cls' if os.name == 'nt' else 'clear')
            spel_logica_smaarten_advanced(ronde_nummer, goud, huidige_kleuren)

    else:
        print_textballon("...Je hebt het gedaan.")
        input("Druk op Enter om verder te gaan...")
        os.system('cls' if os.name == 'nt' else 'clear')
        print_textballon("Alle 6 rondes... gewonnen.")
        input("Druk op Enter om verder te gaan...")
        os.system('cls' if os.name == 'nt' else 'clear')
        print_textballon("Het contract is vervuld.")
        input("Druk op Enter om verder te gaan...")
        os.system('cls' if os.name == 'nt' else 'clear')
        print_textballon("Verspil niet jouw tweede kans, oke?")
        input("Druk op Enter om terug naar aarde te gaan")
        os.system('cls' if os.name == 'nt' else 'clear')
        credits()

#Credits
def credits():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Gemaakt door: Justin Fung)")
    print("Speciale dank aan: ")
    print("Maarten Mert Wildenberg voor de laadscherm.")
    print("Lukas Li voor de goud/goudstukken code")
    print("ChatGpt voor de ASCII art")
    print("Tech With Tim voor de colorama package. #Youtuber")
    print("De Python Reddit Community voor de willekeurige wijsheid dat ze aan mij gaven.")
    input("Druk op een toets om terug te gaan.")

# Startkeuze voor gameversie
def kies_versie():
    global gekozen_versie
    while gekozen_versie not in ["1", "2"]:
        print("Kies spelversie:")
        print("1. Normale versie (Voor checken PO Informatica)")
        print("2. Smaarten versie")
        gekozen_versie = input("Maak een keuze (1-2): ").strip()

# Hoofdmenu
while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    #ASCII art
    ascii_menu()
    print("") #Ruimte tussen ASCII art en menu
    keuze = input("Maak een keuze (1-3): ").strip()

    if keuze == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        gekozen_versie = None  # Reset keuze telkens als speler opnieuw kiest
        kies_versie()  # Laat speler kiezen
        if gekozen_versie == "1":
            spel_logica_normaal()
        elif gekozen_versie == "2":
            spel_logica_smaarten()
        else:
            print("Ongeldige keuze. Probeer opnieuw.")
    elif keuze == "2":
        credits()
    elif keuze == "3":
        print("Tot de volgende keer!")
        break