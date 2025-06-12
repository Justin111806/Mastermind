import random

kleuren = ["Rood", "Groen", "Blauw", "Paars", "Wit", "Zwart"]
code_lengte = 4
max_poging = 10

code = random.choices(kleuren, k=code_lengte)
poging = 0

print(code) #Debug

print("Mastermind")
print(f"Kleuren: {','.join(kleuren)}")
print(f"Lengte code: {code_lengte}, Maximale pogingen: {max_poging}")

while poging < max_poging:
  keuze = input(f"Poging {poging + 1}/{max_poging}, Wat is je keuze: ").strip().split()
  if len(keuze) != code_lengte or not all(kleuren in kleuren for kleuren in keuze):
    print("Dat kan niet, 4 kleuren aub")
    continue
  
  correct_positie = sum(g == c for g, c in zip(keuze, code))
  correct_kleur = sum(min(keuze.count(c), code.count(c)) for c in set(code))
  correct_kleur -= correct_positie
  print(f"{correct_positie} kleuren goed geplaatst.")
  print(f"{correct_kleur} correcte kleuren in verkeerde positie.")
  
  if correct_positie == code_lengte:
    print("JE HEBT GEWONNEN!")
    exit()
  
  poging += 1
  
print("JE HEBT VERLOREN L")