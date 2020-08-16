import csv
from sys import argv, exit
import re


# Eina per is csv failo padarytus listus ir kiekviename is ju tikrina, kad kiekvenas segmento pasikartojimu skaicius atitinka txt faile rasta segmentu pasikartojimu skaiciu.


def main():
    validate_files(argv)
    str_list = read_csv()
    repeats_list = find_max_str()

    for i in range(1, len(str_list)):
        for n in range(len(repeats_list)):
            if str(repeats_list[n]) != str_list[i][n+1]:
                break
            else:
                if n == (len(repeats_list) - 1):
                    print(f'{str_list[i][0]}')
                    exit(0)
                else:
                    continue
    print('No match')
    exit(1)


# Patikrina, ar useris suvede reikiama kieki argumentu.


def validate_files(argv):
    if len(argv) != 3:
        print("Erorr: CSV file and text file are required.")
        exit(1)


# Atidaro csv faila, ji perskaito ir sudeda i list'a.


def read_csv():
    with open(argv[1], 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data


# Atidaro txt faila, ji perskaito ir sudeda i lista. Naudojamas "next", kad nebutu listas liste kaip butu su "list(reader)", nes txt faile yra tik 1 eilute.


def read_txt():
    with open(argv[2], 'r') as file2:
        reader = csv.reader(file2)
        data2 = next(reader)
    return data2


# Su "re.findall" suranda grupes, kuriose be pertrauku kartojamas segmentas is csv failo. Tada isrenka didziausia grupe pagal "len".
# Didziausios grupes "len" padalina is csv segmento "len", jog suzinotu, kiek kartu buvo pakartotas csv segmentas.
# Pakartojimu skaiciu sudeda i nauja list'a.


def find_max_str():
    sequence = read_txt()
    str_list = read_csv()
    repeats_list = []
    for i in range(1, len(str_list[0])):
        groups = re.findall(fr'(?:{str_list[0][i]})+', sequence[0])
        largest = max(groups, default="", key=len)
        repeats = len(largest) // len(str_list[0][i])
        repeats_list.append(repeats)
    return repeats_list


main()