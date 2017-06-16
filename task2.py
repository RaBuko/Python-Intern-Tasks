"""
Rafał Bukowski
task2
"""


def damage(spell: str) -> int:
    # wydzielenie właściwej części czaru
    spell_start_index = spell.find("fe")
    searching_index = len(spell)
    spell_end_index = -1

    while searching_index > 0:
        spell_end_index = spell.find("ai", searching_index)
        searching_index -= 1
        if spell_end_index != -1:
            break

    # sprawdzenie czy 'fe' w ogóle istnieje i czy jest przed 'ai'
    if spell_start_index == -1 or spell_start_index > spell_end_index:
        return 0
    spell = spell[spell_start_index: spell_end_index + 2]

    # sprawdzenie czy występuje tylko jedno 'fe'
    total_dmg = 0
    spell = spell[2:]
    total_dmg += 1
    if spell.find("fe") != -1:
        return 0

    # dodawanie punktów za subspells
    def checksubspells(spell: str, total_dmg: int, subspell: str, actual_dmg: int):
        while spell.find(subspell) != -1:
            spell = spell.replace(subspell, "", 1)
            total_dmg += actual_dmg
        return spell, total_dmg

    spell, total_dmg = checksubspells(spell, total_dmg, "dai", 5)
    spell, total_dmg = checksubspells(spell, total_dmg, "ain", 3)
    spell, total_dmg = checksubspells(spell, total_dmg, "jee", 3)
    spell, total_dmg = checksubspells(spell, total_dmg, "ai", 2)
    spell, total_dmg = checksubspells(spell, total_dmg, "je", 2)
    spell, total_dmg = checksubspells(spell, total_dmg, "ne", 2)

    # odejmowanie punktów za dodatkowe litery
    while len(spell) != 0:
        spell = spell[:-1]
        total_dmg -= 1
    if total_dmg < 0:
        return 0
    return total_dmg
    pass

# Testowanie
p = lambda spl: print("Czar: " + spl + " | Ilość obrażeń: " + str(damage(spl)))
p('xxxxxfejejeeaindaiyaiaixxxxxx')
p('jejefeai')
p("jejeai")
p('dadsafeokokok')
p('aioooofe')
p('feeai')
p('feaineain')
p('jee')
p('fefefefefeaiaiaiaiai')
p('fdafafeajain')
p('fexxxxxxxxxxai')
p('fedaineai')
