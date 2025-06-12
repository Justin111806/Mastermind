import random

kleuren = ["R", "G", "B", "P", "W", "Z"]
code_lengte = 4
max_poging = 10

doorgaan = ["Ja", "Nee"]

code = random.choices(kleuren, k=code_lengte)
poging = 0

print(code) #Debug

print("Mastermind") #Print naam
while doorgaan == "Ja":
  
print("Welkom, de kleuren zijn: Rood, Groen, Blauw, Paars, Wit, Zwart")
print("Geen zorgen, je hoeft alleen de eerste letter te typen")
print(f"Lengte code: {code_lengte}, Maximale pogingen: {max_poging}") # Uitleg

while poging < max_poging:
  keuze = input(f"Poging {poging + 1}/{max_poging}, Wat is je keuze: ").strip().split()
  if len(keuze) != code_lengte or not all(kleur in kleuren for kleur in keuze):
    print("Dat kan niet, 4 kleuren aub")
    continue
  
  correct_positie = sum(g == c for g, c in zip(keuze, code))
  correct_kleur = sum(min(keuze.count(c), code.count(c)) for c in set(code))
  correct_kleur -= correct_positie
  print(f"{correct_positie} kleuren goed geplaatst.")
  print(f"{correct_kleur} correcte kleuren in verkeerde positie.")
  
  if correct_positie == code_lengte:
    print("JE HEBT GEWONNEN!")
    print(input("Wil je nog een keer spelen? (ja/nee)"))
    if doorgaan == "nee":
      print("Bedankt voor het spelen!")
      exit()
    elif doorgaan == "Ja":
      
  
  poging += 1
  
print("JE HEBT VERLOREN L")