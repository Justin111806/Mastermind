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
              + "Wit, " #Wit is standaard, hoeft niet colorama gebruiken
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
