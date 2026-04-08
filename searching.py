from pathlib import Path
import json


def read_data(file_name, field):
    """
    Reads a JSON file and returns data for a given field.

    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    Returns:
        list | str | None:
            - list: If data retrieved by the selected field contains numeric data.
            - str: If field is 'dna_sequence'.
            - None: If the field is not supported.
    """
    # get current working directory path
    cwd_path = Path.cwd()
    
    file_path = cwd_path / file_name

def read_data(hodnoty,klic):
    if klic in hodnoty==False:
        return None

    with open(hodnoty,"r") as file:
            data= json.load(file)
    return data[klic]

def linear_search(sekvence,number):
    position=[]
    for index, x in enumerate(sekvence):
        if x == number:
            position.append(index)
    y = sekvence.count(number)

    sl = {"positions": position,
            "count": y}
    return sl

def binary_search(seznam,cislo):
    mislo=[]
    lev = 0
    prva

import time
start = time.perf_counter()
def main():
    sequential_data = read_data("sequential.json","unordered_numbers")
    print(sequential_data)
    pocet_cyklu = linear_search(sequential_data, 20)
    print (pocet_cyklu)

    end = time.perf_counter()
    duration = end - start
    print(f"Měření trvalo {duration:.8f} s")

if __name__ == "__main__":
    main()

