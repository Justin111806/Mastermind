import sys
import time
import random #Willekeurige code generator
import os #Console schoonmaken
import colorama #Kleurige tekst voor duidelijkheid. Gedaan door Package GitHub
from colorama import Fore, Back, Style
colorama.init(autoreset=True) #Automatisch terug naar standaard kleur

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
commentaar = [Fore.RED + "Nee, dat is fout, L.",
              Fore.RED + "Nope, dat is hem niet.",
              Fore.RED + "Helaas, je hebt hem niet juist",
              Fore.RED + "Wow, waarom dacht je dat? Dat is super fout.",
              Fore.RED + "LOL JE BENT ZO DOM BRO",
              Fore.RED + "Nou ja, ik snap niet wart je denkproces daar was."]

#Game regels
code_lengte = 4
max_poging = 10

uitleg = True
gekozen_versie = None

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

#De Game Master
def smaarten_zegt(tekst):
    import textwrap
    import os

    #ASCII art Game Master
    master_ascii = r"""
    _____
    /     \
    | () () |
    \  ^  /
    |||||
    |||||
     __|||||__
    /  |||||  \
    /   |||||   \
    /    |||||    \
    /     |||||     \
    /      |||||      \
    /       |||||       \
    /        |||||        \
    /_________/   \_________\
    |   SMAARTEN DE WIJZE   |
    |                       |
    |                       |
     \_______________________/
    """
    breedte_console = os.get_terminal_size().columns
    smaarten_art = master_ascii
    
    # Print gecentreerd in console
    for regel in smaarten_art.splitlines():
        spaties = (breedte_console - len(regel)) // 2
        print(" " * spaties + regel)
    print()

    #Text wrappen
    max_breedte = 42
    regels = textwrap.wrap(tekst, width=max_breedte)

    # Bepaal breedte van de ballon
    breedte = max(len(r) for r in regels)
    rand_boven = " " + "_" * (breedte + 2)
    rand_onder = " " + "-" * (breedte + 2)

    # Bereken centrering voor de ballon
    spaties = (breedte_console - (breedte + 4)) // 2

    # Print de ballon gecentreerd
    print(" " * spaties + rand_boven)
    for regel in regels:
        print(" " * spaties + f"| {regel.ljust(breedte)} |")
    print(" " * spaties + rand_onder)

#De Demoon
def shop_demoon(tekst):
    import textwrap
    import os

    #ASCII art Demoon
    demoon_ascii = r"""
           (    )
          ((((()))
          |o\ /o)|
          ( (  _')
           (._.  /\__
          ,\___,/ '  ')
    '.,_)     (  .- .   .    )
       \ .   ' . /-''-----'
        )      \/ 
       /        |
      (   .     |
       \   |  . |
        \      /
       ,' - . ' 
    """
    breedte_console = os.get_terminal_size().columns
    demoon_art = demoon_ascii

    # Print gecentreerd in console
    for regel in demoon_art.splitlines():
        spaties = (breedte_console - len(regel)) // 2
        print(" " * spaties + regel)
    print()

    max_breedte = 42
    regels = textwrap.wrap(tekst, width=max_breedte)

    # Bepaal breedte van de ballon
    breedte = max(len(r) for r in regels)
    rand_boven = " " + "_" * (breedte + 2)
    rand_onder = " " + "-" * (breedte + 2)

    # Bereken centrering voor de ballon
    spaties = (breedte_console - (breedte + 4)) // 2

    # Print de ballon gecentreerd
    print(" " * spaties + rand_boven)
    for regel in regels:
        print(" " * spaties + f"| {regel.ljust(breedte)} |")
    print(" " * spaties + rand_onder)

#Normale versie
def spel_logica_normaal():
    global uitleg, code_lengte, max_poging
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
    print(code)

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

#Smaarten versie
def spel_logica_smaarten():
    global uitleg, code_lengte, max_poging
    os.system('cls' if os.name == 'nt' else 'clear')

    # Warning
    waarschuwing = True
    while waarschuwing:
        print("Je staat op het punt om de Smaarten versie te spelen.")
        print("Het is aanbevolen om eerste de normale versie te spelen.")
        print("De Smaarten versie vraagt voor een langere speeltijd en is bedoeld om te worden gespeeld in rust.")
        print("Ga je verder?")
        print("1. Ja")
        print("2. Nee")
        keuze = input("Maak een keuze (1-2): ")
        if keuze == "1":
            waarschuwing = False
        elif keuze == "2":
            return
        else:
            print("Ongeldige invoer. Probeer opnieuw.")
            time.sleep(1.5)
            os.system('cls' if os.name == 'nt' else 'clear')

    #Spel logica
    global uitleg, code_lengte, max_poging
    os.system('cls' if os.name == 'nt' else 'clear') #Console schoonmaken

    #Uitleg
    if uitleg:
        smaarten_zegt("Welkom, de kleuren zijn: "
              + Fore.RED + "Rood, "
              + Fore.GREEN + "Groen, "
              + Fore.BLUE + "Blauw, "
              + Fore.MAGENTA + "Paars, "
              + Fore.WHITE + "Wit, " #Wit is standaard, maar anders wordt magenta paars naar wit
              + Fore.BLACK + "Zwart")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear') #Console schoonmaken

        #Kleuren spectrum printen voor duidelijkheid
        for x in kleuren:
            print(x)

        smaarten_zegt("Je hoeft alleen de EERSTE letter te typen, hoofdletters maakt niet uit. SPATIES WEL.")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear') #Console schoonmaken
        smaarten_zegt("Zwarte Pin = juiste kleur en plek. Witte Pin = juiste kleur maar verkeerde plek.")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear') #Console schoonmaken
        smaarten_zegt(f"Code lengte: {code_lengte}")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear') #Console schoonmaken
        smaarten_zegt(f"Maximale pogingen: {max_poging}")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear') #Console schoonmaken
        uitleg = False #Eindigt uitleg

    #Code genereren
    code = random.choices(basis_kleuren, k=code_lengte)
    poging = 0
    smaarten_zegt("Code is gegenereerd!")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear') #Console schoonmaken

    #Debugging
    print(code)

    #Game loop
    while poging < max_poging:
        smaarten_zegt(f"Poging {poging + 1}/{max_poging}: Geef je gok (Voorbeeld: r g b p)")
        keuze_input = input(Fore.MAGENTA + "").strip().upper().split()

        #Ongeldige input
        if len(keuze_input) != code_lengte or not all(kleur in basis_kleuren for kleur in keuze_input):
            smaarten_zegt(Fore.RED + "Dat kan niet, geef exact geldige kleuren (R G B P W Z)")
            continue

        #Calculatie van zwarte en witte pinnen
        correct_positie = sum(g == c for g, c in zip(keuze_input, code))
        correct_kleur = sum(min(keuze_input.count(c), code.count(c)) for c in set(basis_kleuren)) - correct_positie

        #Commentaar na fout
        if correct_positie != code_lengte:
            smaarten_zegt(random.choice(commentaar))

        #Gewonnen
        if correct_positie == code_lengte:
            smaarten_zegt(Style.BRIGHT + Fore.GREEN + "JE HEBT GEWONNEN!")
            break

        #Update pogingen
        poging += 1

        #Print zwarte en witte pinnen
        smaarten_zegt(Fore.BLACK + f"Zwarte pinnen: {correct_positie}")
        smaarten_zegt(Fore.CYAN + f"Witte pinnen: {correct_kleur}")

    #Verloren
    if poging == max_poging:
        smaarten_zegt(Style.DIM + Fore.RED + "JE HEBT VERLOREN!")
        smaarten_zegt(f"De juiste code was: {' '.join(code)}")

    # Felicitatie
    smaarten_zegt("Goed gedaan! Het is tijd voor de tweede ronde...")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    smaarten_zegt("...maar geen zorgen!")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    smaarten_zegt("Je kan je even uitrusten bij mijn beste vriend.")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

    # Shop met Demoon
    shop_demoon("Hallo, sterveling...")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    shop_demoon("Smaarten stuurde je?")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    shop_demoon("Je mag hier even op adem komen... en misschien iets kopen. Hehehe...")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

    #Shop logica
    items = {
        "1": ("Zwarte Kristal (Hint)", 3),
        "2": ("Glinsterende Kaart (Extra poging)", 5),
        "3": ("Vreemde Oogbal (Verwijdert een foute kleur)", 4)
    }

    goud = 10
    #Shop loop
    while True:
        shop_demoon("Wat ga je doen?")
        shop_demoon("1. Rusten (Save) 2. Kopen 3. Verder gaan naar de tweede ronde")
        keuze = input()
        if keuze == "1":
            shop_demoon("Je rust je even uit...")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            shop_demoon("Je bent nu uitgerust!")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
        elif keuze == "2":
            shop_demoon(f"\nJe hebt {goud} goudstukken.")
            shop_demoon("Wat wil je kopen?")
            for key, (naam, prijs) in items.items():
                shop_demoon(f"{key}. {naam} - {prijs} goud")

            keuze = input("Maak je keuze: ").strip()
            if keuze in items:
                naam, prijs = items[keuze]
                if goud >= prijs:
                    goud -= prijs
                    shop_demoon(Fore.YELLOW + f"Je hebt '{naam}' gekocht.")
                else:
                    shop_demoon(Fore.RED + "Niet genoeg goud, sterveling...")
            elif keuze == "4":
                shop_demoon("Tot ziens, sterveling... Veel succes in de tweede ronde...")
                break
            else:
                print("Ongeldige keuze.")
        elif keuze == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            shop_demoon("Tot ziens, sterveling... Veel succes in de tweede ronde...")
            time.sleep(2)
            spel_logica_smaarten() #Spel herstart
        else:
            shop_demoon("Ongeldige keuze, probeer opnieuw.")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')

#Credits
def credits():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Gemaakt door: Justin Fung)")
    print("Speciale dank aan: CREDITS YOUTUBERS HIER JUSTIN")
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