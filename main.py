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
    game_master(Fore.YELLOW + f"✨ De Kleurloze Kristal onthult: een kleur in de code is '{onthulde_kleur}'")
def gebruik_gefluister_van_echos(code, code_lengte):
    domme_tips = [
        "De code bestaat uit kleuren.", 
        "Gebruik kleuren die je nog niet hebt geprobeerd.",
        "Soms is rood… gewoon rood."
    ]
    slimme_tips = [
        f"De kleur op positie {random.randint(1, code_lengte)} is '{code[random.randint(0, code_lengte-1)]}'",
        f"De kleur '{random.choice(code)}' zit op de juiste plek in je laatste gok."  # Optioneel controleren met echte gok
    ]
    tip = random.choice(domme_tips + slimme_tips)
    game_master(Fore.MAGENTA + f"👁‍🗨 Gefluister van Echo's: {tip}")
def gebruik_kleurrijke_schilderspalet(code):
    index = random.randint(0, len(code)-1)
    oude_kleur = code[index]
    nieuwe_kleur = random.choice([kleur for kleur in basis_kleuren if kleur != oude_kleur])
    code[index] = nieuwe_kleur
    game_master(Fore.LIGHTBLUE_EX + f"🎨 De kleur op positie {index+1} is nu veranderd…")
    return code
def gebruik_gouden_spaarvarken(spaarvarken):
    rente = int(spaarvarken * 0.2)
    spaarvarken += rente
    shop_demoon(Fore.YELLOW + f"💰 Je spaarvarken groeide met {rente} goudstukken! Totaal: {spaarvarken}")
    return spaarvarken
def gebruik_potlood_gum(code):
    kleur = random.choice(code)
    while kleur in code:
        code.remove(kleur)
    game_master(Fore.LIGHTWHITE_EX + f"✏️ De kleur '{kleur}' is uit de code gewist.")
    return code
def gebruik_levend_oog(keuze_input, code):
    hints = []
    for i, (a, b) in enumerate(zip(keuze_input, code)):
        if a == b:
            hints.append(f"🔮 Positie {i+1}: zwart pin mogelijk")
    if hints:
        game_master(Fore.CYAN + f"👁 Levend Oog staart: " + " | ".join(hints))
    else:
        game_master("👁 Levend Oog ziet… niets.")
#Flashbacks LORE
ziel_flashbacks = [
    "🕯 Een kind fluistert: 'Ze hadden beloofd me niet te vergeten...'",
    "🕯 Je ziet een bloedrode maan boven een verlaten plein.",
    "🕯 Een stem: 'Jij… bent net als hij...'",
]
def gebruik_ziel_fragment():
    game_master(random.choice(ziel_flashbacks))

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
    print(Fore.CYAN + "\n╔════════════════════════════════╗")
    print("║  Wat wil je doen, avonturier? ║")
    print("╠════════════════════════════════╣")
    print("║  1. 🔍 Code raden              ║")
    print("║  2. 🎴 Item gebruiken          ║")
    print("╚════════════════════════════════╝")

#ASCII art voor Items menu
def toon_items_menu(gekochte_items):
    print(Fore.MAGENTA + "\n╔══════════════════════════════════════╗")
    print("║       🎴 Beschikbare Items           ║")
    print("╠══════════════════════════════════════╣")
    iets_te_gebruiken = False
    for nummer, (naam, aantal) in enumerate(gekochte_items.items(), start=1):
        if aantal > 0:
            print(f"║ {nummer}. {naam.ljust(30)} ({aantal}x) ║")
            iets_te_gebruiken = True
    print("╚══════════════════════════════════════╝")
    if not iets_te_gebruiken:
        print(Fore.LIGHTBLACK_EX + "Je hebt geen items om te gebruiken...")
    else:
        print(Fore.YELLOW + "Kies het nummer van het item dat je wil gebruiken:")

#De Game Master
def game_master(tekst):
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

#Shop tussen rondes
def rust_tussen_rondes(goud, gekochte_items, spaarvarken):
    #Conditie om loop ooit te stoppen
    if goud<= 0 or not gekochte_items:  
        temp_result = rust_tussen_rondes(goud, gekochte_items, spaarvarken)
        if len(temp_result) == 3:
            goud, gekochte_items, spaarvarken = temp_result
        else:
            goud, gekochte_items = temp_result
        if spaarvarken > 0:
            spaarvarken = gebruik_gouden_spaarvarken(spaarvarken)
    while True:
        shop_demoon(f"Je hebt {goud} goudstukken en {spaarvarken} in je spaarvarken. Wat wil je doen?")

        shop_demoon("1. Rusten (Save) 2. Kopen 3. Verder naar de volgende ronde")
        keuze = input().strip()

        if keuze == "1":
            shop_demoon("Je rust je even uit...")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            shop_demoon("Je bent nu uitgerust!")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')

        #Kopen
        elif keuze == "2":
            shop_demoon("Wat wil je kopen?")
            for key, (naam, prijs) in items.items():
                shop_demoon(f"{key}. {naam} - {prijs} goud")

            keuze_kopen = input("Maak je keuze: ").strip()
            if keuze_kopen in items:
                naam, prijs = items[keuze_kopen]
                if goud >= prijs:
                    goud -= prijs
                    shop_demoon(Fore.YELLOW + f"Je hebt '{naam}' gekocht.")
                    gekochte_items[naam] += 1
                    return goud, gekochte_items
                else:
                    shop_demoon(Fore.RED + "Niet genoeg goud, sterveling...")
            elif keuze_kopen == "4":
                shop_demoon("Tot ziens, sterveling...")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                shop_demoon("Ongeldige keuze.")

        elif keuze == "3":
            shop_demoon("Goed, op naar de volgende ronde!")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            start_ronde_n(2, goud)
            return goud, gekochte_items, spaarvarken

        else:
            shop_demoon("Ongeldige keuze, probeer opnieuw.")

    # Fallback return
    return goud, gekochte_items, spaarvarken

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
        game_master("Welkom, de kleuren zijn: "
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

        game_master("Je hoeft alleen de EERSTE letter te typen, hoofdletters maakt niet uit. SPATIES WEL.")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear') #Console schoonmaken
        game_master("Zwarte Pin = juiste kleur en plek. Witte Pin = juiste kleur maar verkeerde plek.")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear') #Console schoonmaken
        game_master(f"Code lengte: {code_lengte}")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear') #Console schoonmaken
        game_master(f"Maximale pogingen: {max_poging}")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear') #Console schoonmaken
        uitleg = False #Eindigt uitleg

    #Code genereren
    code = random.choices(basis_kleuren, k=code_lengte)
    poging = 0
    game_master("Code is gegenereerd!")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear') #Console schoonmaken

    #Debugging
    print(code)

    #Game loop
    while poging < max_poging:
        game_master(f"Poging {poging + 1}/{max_poging}" "Voer je gok in (bv. R G B P): ")
        keuze_input = input(Fore.MAGENTA).strip().upper().split()

        # Ongeldige invoer
        if len(keuze_input) != code_lengte or not all(kleur in basis_kleuren for kleur in keuze_input):
            game_master(Fore.RED + "Dat kan niet, geef exact geldige kleuren (R G B P W Z)")
            continue

        # Calculatie van zwarte en witte pinnen
        correct_positie = sum(g == c for g, c in zip(keuze_input, code))
        correct_kleur = sum(min(keuze_input.count(c), code.count(c)) for c in set(basis_kleuren)) - correct_positie

        # Feedback bij fout
        if correct_positie != code_lengte:
            game_master(random.choice(commentaar))

        # Gewonnen
        if correct_positie == code_lengte:
            game_master(Style.BRIGHT + Fore.GREEN + "🎉 JE HEBT GEWONNEN!")
            break

        # Update pogingen en print pin-info
        poging += 1
        game_master(Fore.BLACK + f"Zwarte pinnen: {correct_positie}")
        game_master(Fore.CYAN + f"Witte pinnen: {correct_kleur}")
        
    # Felicitatie
    goud = 0 #Start goud
    goud += 50  #Beloning
    spaarvarken = 0 #Start spaarvarken
    game_master("Goed gedaan! Het is tijd voor de tweede ronde...")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    game_master("...maar geen zorgen!")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    game_master("Je kan je even uitrusten bij mijn beste vriend.")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    rust_tussen_rondes(goud, gekochte_items, spaarvarken)

#Ronde logica
def start_ronde_n(ronde_nummer, goud):
    game_master(f"Welkom terug! Klaar voor ronde {ronde_nummer}? Deze keer wordt het moeilijker!")

    #Moeilijkheid aanpassen per ronde
    huidige_kleuren = basis_kleuren.copy()
    if ronde_nummer >= 2:
        huidige_kleuren.append("O")  #Voeg oranje toe
    if ronde_nummer >= 3:
        huidige_kleuren.append("T")  #Voeg turquoise toe
    if ronde_nummer >= 4:
        huidige_kleuren.append("A")  #Voeg amber toe

    huidige_code_lengte = code_lengte + (ronde_nummer - 1)  #Wordt elke ronde langer
    huidige_max_poging = max_poging - ronde_nummer + 1       #Minder pogingen

    code = random.choices(huidige_kleuren, k=huidige_code_lengte)
    poging = 0
    game_master("Code is gegenereerd!")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

    print(code)  #Debug

    while poging < max_poging:
        game_master(f"Poging {poging + 1}/{max_poging}")
        game_master(Style.BRIGHT + Fore.YELLOW + "\nWat wil je doen?")

        #ActiesMenu ACII
        toon_actiekeuze_menu()
        actie = input(Fore.MAGENTA + "👉 ").strip()

        if actie == "1":
            keuze_input = input(Fore.MAGENTA + "Voer je gok in (bv. R G B P): ").strip().upper().split()

            # Ongeldige invoer
            if len(keuze_input) != code_lengte or not all(kleur in basis_kleuren for kleur in keuze_input):
                game_master(Fore.RED + "Dat kan niet, geef exact geldige kleuren (R G B P W Z)")
                continue

            # Calculatie van zwarte en witte pinnen
            correct_positie = sum(g == c for g, c in zip(keuze_input, code))
            correct_kleur = sum(min(keuze_input.count(c), code.count(c)) for c in set(basis_kleuren)) - correct_positie

            # Feedback bij fout
            if correct_positie != code_lengte:
                game_master(random.choice(commentaar))

            # Gewonnen
            if correct_positie == code_lengte:
                game_master(Style.BRIGHT + Fore.GREEN + "🎉 JE HEBT GEWONNEN!")
                break

            # Update pogingen en print pin-info
            poging += 1
            game_master(Fore.BLACK + f"Zwarte pinnen: {correct_positie}")
            game_master(Fore.CYAN + f"Witte pinnen: {correct_kleur}")

        elif actie == "2":
            toon_items_menu(gekochte_items)
            gekozen = input("Welk item wil je gebruiken? ").strip()
            if gekozen in gekochte_items and gekozen != "4" and gekochte_items[gekozen] > 0:
                # Item gebruik functie oproepen
                if gekozen == "1":
                    gebruik_kleurloze_kristal(code)
                elif gekozen == "2":
                    gebruik_gefluister_van_echos(code, code_lengte)
                elif gekozen == "3":
                    code = gebruik_kleurrijke_schilderspalet(code)
                elif gekozen == "5":
                        code = gebruik_potlood_gum(code)
                elif gekozen == "6":
                    if 'keuze_input' in locals():
                        gebruik_levend_oog(keuze_input, code)
                    else:
                        game_master("Je hebt nog geen gok gedaan om Levend Oog te gebruiken.")
                gekochte_items[gekozen] -= 1
            else:
                game_master("Dat item kan je nu niet gebruiken of je hebt het niet.")

        else:
            game_master("Kies 1 of 2.")
            
        # Felicitatie
        goud = 0 #Start goud
        goud += 50  #Beloning
        spaarvarken = 0 #Start spaarvarken
        game_master(f"Goed gedaan! Het is tijd voor de {ronde_nummer} ronde...")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        game_master("...maar geen zorgen!")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        game_master("Je kan je even uitrusten bij mijn beste vriend.")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        rust_tussen_rondes(goud, gekochte_items, spaarvarken)

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