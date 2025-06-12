import random
import time
import sys

def typewriter_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Voor een newline aan het eind
    input("Druk op Enter om door te gaan...")

kleuren = ["R", "G", "B", "P", "W", "Z"]
code_lengte = 4
max_poging = 10

code = random.choices(kleuren, k=code_lengte)
poging = 0

print(code) #Debug

typewriter_print("Mastermind") #Print naam
typewriter_print("Welkom, de kleuren zijn: Rood, Groen, Blauw, Paars, Wit, Zwart")
typewriter_print("Geen zorgen, je hoeft alleen de eerste letter te typen")
typewriter_print(f"Lengte code: {code_lengte}, Maximale pogingen: {max_poging}") # Uitleg

while poging < max_poging:
  keuze = input(f"Poging {poging + 1}/{max_poging}, Wat is je keuze: ").strip().split()
  if len(keuze) != code_lengte or not all(kleur in kleuren for kleur in keuze):
    typewriter_print("Dat kan niet, 4 kleuren aub")
    continue
  
  correct_positie = sum(g == c for g, c in zip(keuze, code))
  correct_kleur = sum(min(keuze.count(c), code.count(c)) for c in set(code))
  correct_kleur -= correct_positie
  typewriter_print(f"{correct_positie} kleuren goed geplaatst.")
  typewriter_print(f"{correct_kleur} correcte kleuren in verkeerde positie.")
  
  if correct_positie == code_lengte:
    typewriter_print("JE HEBT GEWONNEN!")
    exit()
  
  poging += 1
  
typewriter_print("JE HEBT VERLOREN L")