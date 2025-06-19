import random # Voor genereren Mastermind code
import os # Voor scherm schoonmaken
import colorama
from colorama import Fore, Back, Style
colorama.init()

kleuren = ["R", "G", "B", "P", "W", "Z"]

commentaar = ["Nee, dat is fout, L.", "Nope, dat is hem niet.", "Helaas, je hebt hem niet juist", "Wow, waarom dacht je dat? Dat is super fout.", "LOL JE BENT ZO DOM BRO", "Nou ja, ik snap niet wat je denkproces daar was."]

code_lengte = 4

max_poging = 10

#functie menu
def toon_menu():
    #ASCII Art
    print(".___ ___.       ___           _______.___________. _______ .______      .___  ___.  __  .__   __. ._______")
    print("|   \/   |     /   \         /       |           ||   ____||   _  \     |   \/   | |  | |  \ |  | |       \ ") 
    print("|  \  /  |    /  ^  \       |   (----`---|  |----`|  |__   |  |_)  |    |  \  /  | |  | |   \|  | |  .--.  |")
    print("|  |\/|  |   /  /_\  \       \   \       |  |     |   __|  |      /     |  |\/|  | |  | |  . `  | |  |  |  |")
    print("|  |  |  |  /  _____  \  .----)   |      |  |     |  |____ |  |\  \----.|  |  |  | |  | |  |\   | |  '--'  |")
    print("|__|  |__| /__/     \__\ |_______/       |__|     |_______|| _| `._____||__|  |__| |__| |__| \__| |_______/ ")
    print("") #Leeg voor spatie tussen ASCII en menu
    print("1. Start spel")
    print("2. Instellingen (BETA WERKT NIET ECHT, JUSTIN GAAT DIT FIXEN TRUST")
    print("3. Credits")
    print("4. Stop")

#functie instellingen
def instellingen():
    os.system('cls' if os.name == 'nt' else 'clear') # Scherm schoonmaken
    global code_lengte, max_poging
    try: # Zorgt ervoor als niks invoer, normale instellingen
        code_lengte = int(input("Nieuwe code lengte (standaard 4): ") or code_lengte) # Keuze veranderen lengte code
        print("Geslaagd!")
        max_poging = int(input("Nieuwe maximale pogingen (standaard 10): ") or max_poging) # Keuze verandereren maximale pogingen
        print("Geslaagd!")
    except ValueError:
        print("Ongeldige invoer, NIET VERANDERDE instellingen blijven ongewijzigd.") # geen geldig invoer, normale instellingen

#functie credits
def credits():
    os.system('cls' if os.name == 'nt' else 'clear') #Scherm schoonmaken
    print("Gemaakt door: Justin Fung)")
    print("Speciale dank aan: CREDITS YOUTUBERS HIER JUSTIN")

#uitleg voor nieuwe spelers
uitleg = True

#Gehele gedeelte moet True zijn om te kunnen herkennen als speler wilt spelen of niet
while True:
    os.system('cls' if os.name == 'nt' else 'clear') # Scherm schoonmaken

    #Begin code
    toon_menu()
    keuze = input("Maak een keuze (1-4): ").strip() #kan nu menu gebruiken
#Spelgedeelte
    if keuze == "1":  # Start spel
        os.system('cls' if os.name == 'nt' else 'clear')
        if uitleg:
            print("Welkom, de kleuren zijn: Rood, Groen, Blauw, Paars, Wit, Zwart")
            for x in kleuren:
                print(x)
            print("Geen zorgen, je hoeft alleen de eerste letter te typen en hoofdletters hoeft niet. SPATIES WEL (GAAT VERANDEREN MAAR JUSTIN IS DOM).")
            print("Wanneer je een Zwarte Pin krijgt, betekent dat je een JUISTE KLEUR op de JUISTE PLEK hebt.")
            print("Wanneer je een Witte Pin krijgt, betekent dat je een JUISTE KLEUR op de VERKEERDE PLEK hebt.")
            print(f"Je code lengte is: {code_lengte}")
            print(f"De maximale pogingen zijn: {max_poging}")
            uitleg = False

        code = random.choices(kleuren, k=code_lengte)
        poging = 0

        #print(code) #Debugging
        print("Code is gegenereerd!")
        #Laat spel beginnen
        while poging < max_poging:
            keuze_input = input(f"Poging {poging + 1}/{max_poging}, Wat is je keuze (bv. R G B P): ").strip().upper().split()

            #Code voor invoer fout
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
            print(f"U heeft {correct_positie} Zwarte Pinnen.") #laat zien hoeveel goede posities
            print(f"U heeft {correct_kleur} Witte Pinnen.") #laat zien hoeveel foute posities maar juiste kleur
        #Code voor verloren
        if poging == max_poging:
            print("JE HEBT VERLOREN!")
            print(f"De juiste code was: {' '.join(code)}")

        opnieuw = input("Wil je nog een keer spelen? (ja/nee): ").strip().lower()
        if opnieuw != "ja":
            print("Naar het menu.")
            os.system('cls' if os.name == 'nt' else 'clear') # Scherm schoonmaken
            (toon_menu())
#Instellingen
    elif keuze == "2":
        instellingen()
        input("Veranderingen opgeslaan! Druk op een willekeurig karakter om terug te gaan naar het menu.") #Invoer om terug naar menu te gaan
#Credits
    elif keuze == "3":
        credits()
        input("Druk op een willekeurig karakter om terug te gaan naar het menu.") #Invoer om terug naar menu te gaan
#Eindigd spel
    elif keuze == "4":
        print("Tot de volgende keer!") #Invoer om terug naar menu te gaan
        break