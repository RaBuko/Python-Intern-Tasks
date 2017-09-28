# Python-Intern-Tasks

Zad1. 
Parser z pliku launchlog.txt i segregujący loty kosmiczne według zleconych danych.
Struktura do zwrócenia wyniku to słownik (dictionary)

def group_by(stream, field, success=None)
stream - strumień pliku do sparsowania
field - ciąg znaków "year" lub "month" wpływające na segregowanie zwróconych danych
success - czy lot kosmiczny się udał (True), czy nie (False) lub nie jest to istotne (None)

Zad2.
Symulator rzucenia czaru i wyliczenia jego obrażeń gdzie czarem jest ciąg znaków.
Zasady:
1.  Czar musi zaczynać się od pierwszego wystąpienia "fe" a kończyć się z ostatnim użyciem "ai". 
2.  W przypadku braku tych ciągów znaków czar nie zadaje obrażeń.
3.  Czar zadaje ilość obrażeń (dmg) na podstawie zawartych w środku "podczarów":
3a. "fe" 2dmg
3b. "dai" 5dmg
3c. "ain" 3dmg
3d. "jee" 3dmg
3e. "ai" 2dmg
3f. "je" 2dmg
3g. "ne" 2dmg
4.  W przypadku gdy podczary się nakładają pierwszeństwo ma ten o wyższej ilości obrażeń
5.  Każda dodatkowa litera użyta w ciągu znaków czaru odejmuje 1dmg
