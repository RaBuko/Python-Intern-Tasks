"""
Rafał Bukowski
Task1
"""


def group_by(stream, field, success=None):

    # odczytanie i usunięcie niepotrzebnych linii
    dictionary = {}
    lines = stream.readlines()
    lines.pop(0)
    lines.pop(0)
    new_lines = []

    # wyselekcjonowanie linii zgodnych z podanym parametrem success
    for line in lines:
        if success is None:
            if line.find("   S   ") != -1 or line.find("   F   ") != -1:
                new_lines.append(line)
        elif success:
            if line.find("   S   ") != -1:
                new_lines.append(line)
        else:
            if line.find("   F   ") != -1:
                new_lines.append(line)
    del lines

    # włożenie do słownika danych zgodnych z paramtrem field
    for line in new_lines:
        if field == "month":
            month = line[18:21]
            if month not in dictionary:
                dictionary[month] = 0
            dictionary[month] += 1
        elif field == "year":
            year = line[13:17]
            if year not in dictionary:
                dictionary[year] = 0
            dictionary[year] += 1
        else:
            print("Źle podane argumenty funkcji")
            return

    return dictionary

#Testowanie
dict = group_by(open("launchlog.txt"), "year", None)
for item in dict.items():
    print(item)