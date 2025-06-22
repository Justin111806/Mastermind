import sys
import time
import random #Willekeurige code generator
import textwrap #Text wrappen
import shutil
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
commentaar = [Fore.RED + "Nee, dat is fout, L.",
              Fore.RED + "Nope, dat is hem niet.",
              Fore.RED + "Helaas, je hebt hem niet juist",
              Fore.RED + "Wow, waarom dacht je dat? Dat is super fout.",
              Fore.RED + "LOL JE BENT ZO DOM BRO",
              Fore.RED + "Nou ja, ik snap niet wart je denkproces daar was."]

#Items voor shop
items = { #ander symbool voor items, anders wordt : verward
    "1": ("Kleurloze Kristal", 3),
    "2": ("Gefluister van Echo's", 5),
    "3": ("Kleurrijke Schilderspalet", 4),
    "4": ("Gouden Spaarvarken", 6),
    "5": ("Potlood Gum", 2),
    "6": ("Levend Oog", 10),
    "7": ("Ziel fragment", 15)
}

#Items die speler heeft gekocht
gekochte_items = {
    "Kleurloze Kristal": 0,
    "Gefluister van Echo's": 0,
    "Kleurrijke Schilderspalet": 0,
    "Gouden Spaarvarken": 0,
    "Potlood Gum": 0,
    "Levend Oog": 0,
    "Ziel fragment": 0
}

goud = 0
spaarvarken = 0

#Functies voor items
def gebruik_kleurloze_kristal(code):
    onthulde_kleur = random.choice(code)
    print_textballon(Fore.YELLOW + f"✨ De Kleurloze Kristal onthult: een kleur in de code is '{onthulde_kleur}'")
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
    game_master(Fore.MAGENTA + f"👁‍🗨 Gefluister van Echo's: {tip}")
def gebruik_kleurrijke_schilderspalet(code):
    index = random.randint(0, len(code)-1)
    oude_kleur = code[index]
    nieuwe_kleur = random.choice([kleur for kleur in basis_kleuren if kleur != oude_kleur])
    code[index] = nieuwe_kleur
    print_textballon(Fore.LIGHTBLUE_EX + f"🎨 De kleur op positie {index+1} is nu veranderd…")
    return code
    
def gebruik_gouden_spaarvarken(spaarvarken):
    rente = int(spaarvarken * 0.2)
    spaarvarken += rente
    print_textballon(Fore.YELLOW + f"💰 Je spaarvarken groeide met {rente} goudstukken! Totaal: {spaarvarken}")
    return spaarvarken

def gebruik_potlood_gum(code):
    kleur = random.choice(code)
    while kleur in code:
        code.remove(kleur)
    print_textballon(Fore.LIGHTWHITE_EX + f"✏️ De kleur '{kleur}' is uit de code gewist.")
    return code
def gebruik_levend_oog(keuze_input, code):
    hints = []
    for i, (a, b) in enumerate(zip(keuze_input, code)):
        if a == b:
            hints.append(f"🔮 Positie {i+1}: zwart pin mogelijk")
    if hints:
        print_textballon(Fore.CYAN + f"👁 Levend Oog staart: " + " | ".join(hints))
    else:
        print_textballon("👁 Levend Oog ziet… niets.")
        
#Flashbacks LORE
ziel_flashbacks = [
    "🕯 Een kind fluistert: 'Ze hadden beloofd me niet te vergeten...'",
    "🕯 Je ziet een bloedrode maan boven een verlaten plein.",
    "🕯 Een stem: 'Jij… bent net als hij...'",
]
def gebruik_ziel_fragment():
    print_textballon(random.choice(ziel_flashbacks))

#Gebruik item samengesteld
def gebruik_item(item_nummer, code, keuze_input, gekochte_items, spaarvarken, code_lengte):
    if item_nummer == "1":  # Kleurloze Kristal
        gebruik_kleurloze_kristal(code)

    elif item_nummer == "2":  # Gefluister van Echo's
        gebruik_gefluister_van_echos(code, code_lengte)

    elif item_nummer == "3":  # Kleurrijke Schilderspalet
        code[:] = gebruik_kleurrijke_schilderspalet(code)  # wijzig code in-place

    elif item_nummer == "4":  # Gouden Spaarvarken
        nieuw = gebruik_gouden_spaarvarken(spaarvarken)
        return nieuw  # Return nieuw spaarvarken bedrag

    elif item_nummer == "5":  # Potlood Gum
        code[:] = gebruik_potlood_gum(code)

    elif item_nummer == "6":  # Levend Oog
        if keuze_input:
            gebruik_levend_oog(keuze_input, code)
        else:
            game_master(Fore.LIGHTBLACK_EX + "Het oog kan niets zien zonder een gok…")

    elif item_nummer == "7":  # Ziel fragment
        game_master(Fore.LIGHTMAGENTA_EX + "🕯️ Je hoort gefluister uit het verleden…")
        game_master(Fore.LIGHTMAGENTA_EX + random.choice([
            "‘Je moet het vuur in jezelf vinden…’",
            "‘Hij loog tegen ons allemaal…’",
            "‘Het was nooit slechts een spel…’"
        ]))

    else:
        game_master("❌ Onbekend item.")

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

#Wist actie menu
def clear_actie_menu():
    print("\033[F" * 6 + "\033[K" * 6)

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

#Wist items menu
def clear_items_menu():
    print("\033[F" * 8 + "\033[K" * 8)

#De Game Master
def game_master():
    import os

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
    regels = master_ascii.strip("\n").splitlines()
    for regel in regels:
        spaties = (breedte_console - len(regel)) // 2
        print(" " * spaties + regel)
    print()
    return len(regels) + 2  # +2 voor lege lijn + ruimte tussen tekstballon
    
#De Demoon
def shop_demoon():
    import os

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
    regels = demoon_ascii.strip("\n").splitlines()
    for regel in regels:
        spaties = (breedte_console - len(regel)) // 2
        print(" " * spaties + regel)
    print()
    return len(regels) + 2

#Textballon voor Game Master en Shop Demoon
def print_textballon(tekst, ascii_hoogte):
    breedte = 60
    lijnen = []

    # Tekst opdelen in regels
    woorden = tekst.split(" ")
    regel = ""
    for woord in woorden:
        if len(regel) + len(woord) + 1 <= breedte:
            regel += woord + " "
        else:
            lijnen.append(regel.strip())
            regel = woord + " "
    lijnen.append(regel.strip())

    y_offset = ascii_hoogte + 1
    sys.stdout.write(f"\033[{y_offset};1H")
    sys.stdout.flush()

    print("┌" + "─" * (breedte + 2) + "┐")
    for lijn in lijnen:
        print("│ " + lijn.ljust(breedte) + " │")
    print("└" + "─" * (breedte + 2) + "┘")

    return len(lijnen) + 3  # Hoogte van tekstballon teruggeven

#Clear textballon
def clear_textballon_vast(ascii_hoogte, ballon_hoogte):
    y_offset = ascii_hoogte + 1
    sys.stdout.write(f"\033[{y_offset};1H")
    for _ in range(ballon_hoogte):
        print(" " * 80)
    sys.stdout.write(f"\033[{y_offset};1H")
    sys.stdout.flush()

#rusttijd tussen rondes
def rust_tussen_rondes(goud, gekochte_items, spaarvarken):
    if spaarvarken > 0:
        spaarvarken = gebruik_gouden_spaarvarken(spaarvarken)

    while True:
        hoogte_ascii = shop_demoon()
        ballon_tekst = (
            f"Je hebt {goud} goudstukken en {spaarvarken} in je spaarvarken.\n"
            "Wat wil je doen?\n"
            "1. Rusten (Save)\n"
            "2. Kopen\n"
            "3. Verder naar de volgende ronde"
        )
        hoogte_ballon = print_textballon(ballon_tekst, hoogte_ascii)

        keuze = input("Maak je keuze: ").strip()

        if keuze == "1":
            clear_textballon_vast(hoogte_ascii, hoogte_ballon)
            print_textballon("Je rust je even uit...", hoogte_ascii)
            input("Druk op Enter om verder te gaan...")
            
            clear_textballon_vast(hoogte_ascii, hoogte_ballon)
            print_textballon("Je bent nu uitgerust!", hoogte_ascii)
            input("Druk op Enter om verder te gaan...")
            
            clear_textballon_vast(hoogte_ascii, hoogte_ballon)

        elif keuze == "2":
            clear_textballon_vast(hoogte_ascii, hoogte_ballon)
            
            while True:
                print_textballon("Wat wil je kopen? (0 om te stoppen)", hoogte_ascii)
                for key, (naam, prijs) in items.items():
                    print(f"{key}. {naam} - {prijs} goud")
                keuze_kopen = input("Maak je keuze: ").strip()

                if keuze_kopen == "0":
                    clear_textballon_vast(hoogte_ascii, hoogte_ballon)
                    break
                elif keuze_kopen in items:
                    naam, prijs = items[keuze_kopen]
                    if goud >= prijs:
                        goud -= prijs
                        gekochte_items[naam] += 1
                        clear_textballon_vast(hoogte_ascii, hoogte_ballon)
                        print_textballon(Fore.YELLOW + f"Je hebt '{naam}' gekocht.", hoogte_ascii)
                        input("Druk op Enter om verder te gaan...")
                        clear_textballon_vast(hoogte_ascii, hoogte_ballon)
                    else:
                        clear_textballon_vast(hoogte_ascii, hoogte_ballon)
                        print_textballon(Fore.RED + "Niet genoeg goud, sterveling...", hoogte_ascii)
                        input("Druk op Enter om verder te gaan...")
                        clear_textballon_vast(hoogte_ascii, hoogte_ballon)
                else:
                    clear_textballon_vast(hoogte_ascii, hoogte_ballon)
                    print_textballon(Fore.RED + "Ongeldige keuze...", hoogte_ascii)
                    input("Druk op Enter om verder te gaan...")
                    clear_textballon_vast(hoogte_ascii, hoogte_ballon)

        elif keuze == "3":
            clear_textballon_vast(hoogte_ascii, hoogte_ballon)
            print_textballon("Veel succes...", hoogte_ascii)
            input("Druk op Enter om verder te gaan...")
            start_ronde_n(2, goud)
            return goud, gekochte_items, spaarvarken

        else:
            clear_textballon_vast(hoogte_ascii, hoogte_ballon)
            print_textballon(Fore.RED + "Ongeldige keuze, probeer opnieuw.", hoogte_ascii)
            time.sleep(2)
            clear_textballon_vast(hoogte_ascii, hoogte_ballon)

#Normale spel logica
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

#Smaarten spel logica
def spel_logica_smaarten():
    global uitleg, code_lengte, max_poging, debugmodus
    os.system('cls' if os.name == 'nt' else 'clear')

    #Waarschuwing voor Smaarten versie
    waarschuwing = True
    while waarschuwing:
        print("Je staat op het punt om de Smaarten versie te spelen.")
        print("Het is aanbevolen om eerste de normale versie te spelen.")
        print("De Smaarten versie vraagt voor een langere speeltijd en is bedoeld om te worden gespeeld in rust.")
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
            time.sleep(1.5)
            os.system('cls' if os.name == 'nt' else 'clear')

        os.system('cls' if os.name == 'nt' else 'clear') #Console schoonmaken

    ascii_hoogte = game_master()

    if uitleg:
        ballon_hoogte = print_textballon("Welkom, de kleuren zijn: "
                + Fore.RED + "Rood, "
                + Fore.GREEN + "Groen, "
                + Fore.BLUE + "Blauw, "
                + Fore.MAGENTA + "Paars, "
                + Fore.WHITE + "Wit, "
                + Fore.BLACK + "Zwart", ascii_hoogte)
        input("Druk op Enter om verder te gaan...")
        clear_textballon_vast(ascii_hoogte, ballon_hoogte)

        for x in kleuren:
            print(x)

        ballon_hoogte = print_textballon("Je hoeft alleen de EERSTE letter te typen, hoofdletters maakt niet uit. SPATIES WEL.", ascii_hoogte)
        input("Druk op Enter om verder te gaan...")
        clear_textballon_vast(ascii_hoogte, ballon_hoogte)

        ballon_hoogte = print_textballon("Zwarte Pin = juiste kleur en plek. Witte Pin = juiste kleur maar verkeerde plek.", ascii_hoogte)
        input("Druk op Enter om verder te gaan...")
        clear_textballon_vast(ascii_hoogte, ballon_hoogte)

        ballon_hoogte = print_textballon(f"Code lengte: {code_lengte}", ascii_hoogte)
        input("Druk op Enter om verder te gaan...")
        clear_textballon_vast(ascii_hoogte, ballon_hoogte)

        ballon_hoogte = print_textballon(f"Maximale pogingen: {max_poging}", ascii_hoogte)
        input("Druk op Enter om verder te gaan...")
        clear_textballon_vast(ascii_hoogte, ballon_hoogte)

        uitleg = False

    code = random.choices(basis_kleuren, k=code_lengte)
    poging = 0

    #Debug
    if debugmodus:
        print(Fore.YELLOW + f"[DEBUG] Geheime code: {' '.join(code)}" + Style.RESET_ALL)
        input("Druk op Enter om verder te gaan...")

    ballon_hoogte = print_textballon("Code is gegenereerd!", ascii_hoogte)
    input("Druk op Enter om verder te gaan...")

    while poging < max_poging:
        clear_textballon_vast(ascii_hoogte, ballon_hoogte)  #Wist oude ballon bij begin poging
        
        ballon_hoogte = print_textballon(f"Poging {poging + 1}/{max_poging} Voer je gok in (kleuren: R, G, B, P, W, Z", ascii_hoogte)
        keuze_input = input(Fore.MAGENTA).strip().upper().split()

        #Ongeldige input
        if len(keuze_input) != code_lengte or not all(kleur in basis_kleuren for kleur in keuze_input):
            clear_textballon_vast(ascii_hoogte, ballon_hoogte)
            ballon_hoogte = print_textballon(Fore.RED + "Dat kan niet, geef exact geldige kleuren (R G B P W Z)", ascii_hoogte)
            continue

        correct_positie = sum(g == c for g, c in zip(keuze_input, code))
        correct_kleur = sum(min(keuze_input.count(c), code.count(c)) for c in set(basis_kleuren)) - correct_positie

        #Niet code gekraakt
        if correct_positie != code_lengte:
            clear_textballon_vast(ascii_hoogte, ballon_hoogte)
            ballon_hoogte = print_textballon(random.choice(commentaar), ascii_hoogte)
            input("Druk op Enter om verder te gaan...")
            
            clear_textballon_vast(ascii_hoogte, ballon_hoogte)
            ballon_hoogte = print_textballon(Fore.BLACK + f"Zwarte pinnen: {correct_positie} " + Fore.CYAN + f"Witte pinnen: {correct_kleur} ", ascii_hoogte)
            input("Druk op Enter om verder te gaan...")
            poging += 1
            continue

        #Gewonnen
        if correct_positie == code_lengte:
            clear_textballon_vast(ascii_hoogte, ballon_hoogte)
            ballon_hoogte = print_textballon(Style.BRIGHT + Fore.GREEN + "🎉 JE HEBT GEWONNEN!", ascii_hoogte)
            goud = 50
            spaarvarken = 0
            ballon_hoogte = print_textballon("Goed gedaan! Het is tijd voor de tweede ronde...", ascii_hoogte)
            input("Druk op Enter om verder te gaan...")
            clear_textballon_vast(ascii_hoogte, ballon_hoogte)
            ballon_hoogte = print_textballon("Je kan je even uitrusten bij mijn beste vriend.", ascii_hoogte)
            input("Druk op Enter om verder te gaan...")
            os.system('cls' if os.name == 'nt' else 'clear')
            rust_tussen_rondes(goud, gekochte_items, spaarvarken)
            break

#Ronde logica
def start_ronde_n(ronde_nummer, goud):
    global uitleg, code_lengte, max_poging, debugmodus, gekochte_items, spaarvarken

    os.system('cls' if os.name == 'nt' else 'clear')
    ascii_hoogte = game_master()

    ballon_hoogte = print_textballon(f"Welkom terug! Klaar voor ronde {ronde_nummer}? Deze keer wordt het moeilijker!", ascii_hoogte)
    input("Druk op Enter om verder te gaan...")
    clear_textballon_vast(ascii_hoogte, ballon_hoogte)

    # Moeilijkheidsgraad per ronde
    huidige_kleuren = basis_kleuren.copy()
    if ronde_nummer >= 2:
        huidige_kleuren.append("O") #Oranje
    if ronde_nummer >= 3:
        huidige_kleuren.append("T") #
    if ronde_nummer >= 4:
        huidige_kleuren.append("A") #Amber

    huidige_code_lengte = code_lengte + (ronde_nummer - 1)
    huidige_max_poging = max_poging - ronde_nummer + 1

    code = random.choices(huidige_kleuren, k=huidige_code_lengte)
    poging = 0

    if debugmodus:
        print(Fore.YELLOW + f"[DEBUG] Geheime code: {' '.join(code)}" + Style.RESET_ALL)
        input("Druk op Enter om verder te gaan...")

    ballon_hoogte = print_textballon("De code is gegenereerd. Veel succes...", ascii_hoogte)
    input("Druk op Enter om verder te gaan...")
    clear_textballon_vast(ascii_hoogte, ballon_hoogte)

    #Game loop
    while poging < huidige_max_poging:
        clear_textballon_vast(ascii_hoogte, ballon_hoogte)
        ballon_hoogte = print_textballon(f"Poging {poging + 1}/{huidige_max_poging}", ascii_hoogte)
        input("Druk op Enter om verder te gaan...")
        clear_textballon_vast(ascii_hoogte, ballon_hoogte)

        ballon_hoogte = print_textballon("Wat wil je doen?", ascii_hoogte)
        toon_actiekeuze_menu()
        actie = input(Fore.MAGENTA + "👉 ").strip()
        clear_textballon_vast(ascii_hoogte, ballon_hoogte)

        #Gokken
        if actie == "1":
            keuze_input = input(Fore.MAGENTA + "Voer je gok in (bv. R G B P): ").strip().upper().split()

            if len(keuze_input) != huidige_code_lengte or not all(kleur in huidige_kleuren for kleur in keuze_input):
                ballon_hoogte = print_textballon(Fore.RED + "Dat kan niet. Geef exact geldige kleuren.", ascii_hoogte)
                input("Druk op Enter om verder te gaan...")
                clear_textballon_vast(ascii_hoogte, ballon_hoogte)
                continue

            correct_positie = sum(g == c for g, c in zip(keuze_input, code))
            correct_kleur = sum(min(keuze_input.count(c), code.count(c)) for c in set(huidige_kleuren)) - correct_positie
            
            poging += 1

            if correct_positie != huidige_code_lengte:
                ballon_hoogte = print_textballon(random.choice(commentaar), ascii_hoogte)
                input("Druk op Enter om verder te gaan...")
                clear_textballon_vast(ascii_hoogte, ballon_hoogte)
                
                ballon_hoogte = print_textballon(Fore.BLACK + f"Zwarte pinnen: {correct_positie} " + Fore.CYAN + f"Witte pinnen: {correct_kleur}", ascii_hoogte)
                input("Druk op Enter om verder te gaan...")
                clear_textballon_vast(ascii_hoogte, ballon_hoogte)
                continue

            if correct_positie == huidige_code_lengte:
                goud += 50
                spaarvarken = 0
                ballon_hoogte = print_textballon(Style.BRIGHT + Fore.GREEN + "🎉 JE HEBT GEWONNEN!", ascii_hoogte)
                input("Druk op Enter om verder te gaan...")
                clear_textballon_vast(ascii_hoogte, ballon_hoogte)

                ballon_hoogte = print_textballon(f"Goed gedaan! Het is tijd voor de {ronde_nummer}e ronde...", ascii_hoogte)
                input("Druk op Enter om verder te gaan...")
                clear_textballon_vast(ascii_hoogte, ballon_hoogte)

                ballon_hoogte = print_textballon("Je kan je even uitrusten bij mijn beste vriend.", ascii_hoogte)
                input("Druk op Enter om verder te gaan...")
                os.system('cls' if os.name == 'nt' else 'clear')

                rust_tussen_rondes(goud, gekochte_items, spaarvarken)
                break

        elif actie == "2":
            clear_textballon_vast(ascii_hoogte, ballon_hoogte)
            while True:
                toon_items_menu(gekochte_items)
                gekozen = input("Welk item wil je gebruiken? (0 om terug te gaan) ").strip()
                if gekozen == "0":
                    clear_items_menu()
                    break
                    
                if not gekozen.isdigit():
                    clear_items_menu()
                    ballon_hoogte = print_textballon("Ongeldige invoer. Probeer opnieuw.", ascii_hoogte)
                    input("Druk op Enter om verder te gaan...")
                    clear_textballon_vast(ascii_hoogte, ballon_hoogte)
                    continue
                    
                # Map numbers to item names
                item_mapping = {
                    "1": "Kleurloze Kristal",
                    "2": "Gefluister van Echo's", 
                    "3": "Kleurrijke Schilderspalet",
                    "4": "Gouden Spaarvarken",
                    "5": "Potlood Gum",
                    "6": "Levend Oog",
                    "7": "Ziel fragment"
                }
                
                if gekozen in item_mapping:
                    item_naam = item_mapping[gekozen]
                    if gekochte_items[item_naam] > 0 and gekozen != "4":
                        if gekozen == "1":
                            gebruik_kleurloze_kristal(code)
                        elif gekozen == "2":
                            gebruik_gefluister_van_echos(code, huidige_code_lengte)
                        elif gekozen == "3":
                            code = gebruik_kleurrijke_schilderspalet(code)
                        elif gekozen == "5":
                            code = gebruik_potlood_gum(code)
                        elif gekozen == "6":
                            if 'keuze_input' in locals():
                                gebruik_levend_oog(keuze_input, code)
                            else:
                                ballon_hoogte = print_textballon("Je hebt nog geen gok gedaan om Levend Oog te gebruiken.", ascii_hoogte)
                                input("Druk op Enter om verder te gaan...")
                                clear_textballon_vast(ascii_hoogte, ballon_hoogte)
                                clear_items_menu()
                                continue
                                
                        gekochte_items[item_naam] -= 1
                        clear_items_menu()
                        break
                    else:
                        clear_items_menu()
                        ballon_hoogte = print_textballon("Dat item kan je nu niet gebruiken of je hebt het niet.", ascii_hoogte)
                        input("Druk op Enter om verder te gaan...")
                        clear_textballon_vast(ascii_hoogte, ballon_hoogte)
                else:
                    clear_items_menu()
                    ballon_hoogte = print_textballon("Dat item kan je nu niet gebruiken of je hebt het niet.", ascii_hoogte)
                    input("Druk op Enter om verder te gaan...")
                    clear_textballon_vast(ascii_hoogte, ballon_hoogte)


        else:
            ballon_hoogte = print_textballon("Kies 1 of 2.", ascii_hoogte)
            input("Druk op Enter om verder te gaan...")
            clear_textballon_vast(ascii_hoogte, ballon_hoogte)

#Credits
def credits():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Gemaakt door: Justin Fung)")
    print("Speciale dank aan: ")
    print("ChatGpt voor de ASCII art")
    
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