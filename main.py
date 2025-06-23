import time #Voor laadscherm
import random #Willekeurige code generator
import os #Console schoonmaken
import colorama #Kleurige tekst voor duidelijkheid. Gedaan door Package GitHub
from colorama import Fore, Style
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

#Normale spel logica
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

#Credits
def credits():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Gemaakt door: Justin Fung)")
    print("Speciale dank aan: ")
    print("Maarten Mert Wildenberg voor de hulp met de laadscherm code.")
    
    input("Druk op een toets om terug te gaan.")

# Hoofdmenu
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    
    #ASCII art
    ascii_menu()
    print("") #Ruimte tussen ASCII art en menu
    keuze = input("Maak een keuze (1-3): ").strip()

    if keuze == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        spel_logica_normaal()
    elif keuze == "2":
        credits()
    elif keuze == "3":
        print("Tot de volgende keer!")
        break
