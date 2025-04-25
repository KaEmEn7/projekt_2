"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Kamil Mach
email: kamilmachuj@gmail.com
"""

import random
import time

end_time = None
#counter = 0

number_to_guess = 0
# definice vet
sentences_1 = ["Hi there, I've generated a random 4 digit number for you.",
             "Let's play a bulls and cows game.",
             "Timer will starts count after you enter your first guess. GOOD LUCK!"
            ]

# vypocet max delky jedne vety pro zarovnani "-"
def max_length(sentences):
    return max(len(sentence) for sentence in sentences)

# formatovany vypis kazde vety, podle max. delky
def format_senteces(sentences, max_length):
    for sentence in sentences:
        print(sentence)
        print("-" * max_length)

format_senteces(sentences=sentences_1, max_length=max_length(sentences_1))

# fce pro zapis historickych dat ze hry
def save_record(player_name, duration_time, counter):
    """Ulozi statistiky: Jmeno, Cas, Pocet pokusu do txt souboru.
    """
    with open("results.txt", "a") as file:
        file.write(f"Player: {player_name}, \t\tTime: {duration_time}, \t\tGuesses: {counter}\n")


def generate_random_4_digit_number():
    """
    Generuje nahodne ctyr mistne cislo jako retezec.

    """
    rng_number = random.randint(1000, 9999)
  #    rng_number = str(rng_number)
  #  print("generate_random_4_digit_number:", rng_number)
    return rng_number

# fce pro kontrolu, zda jsou vsechny znaky(cisla) unikatni
def is_unique_number(number):
    number= str(number)
    if len(set(number)) == len(number):
    #    print("is_unique_number:", number)
        return True
    else:
    #    print("is_unique_number:", number)
        return False

# fce pro generovani 4 mistneho cisla s unikatnimi cislicemi
def generate_unique_4_digit_number():
    """
    Pravidla pro hru:
    - nesmi zacinat 0
    - 4 mistne
    """
  # print("Kod se pustil")
    while True:
        number = generate_random_4_digit_number() # vygeneruje nahodne cislo
        if is_unique_number(number):  # kontrola zda cislo obssahuje uniqe cislice
        # print(number, ">> TOTO JE TO CISLO")
            return number # pokud ano, vrati

NUMBER_LENGTH = 4

def is_valid_guess(guess):
    """
    Kontrola že vstup splňuje:
    - Je to číslo
    - Má správnou délku
    - Nezačíná nulou
    """
    if not guess.isdigit():
        print("Invalid input: The guess must be a number.")
        return False
    if len(guess) != NUMBER_LENGTH:
        print(f"Invalid input: The guess must be {NUMBER_LENGTH} digits long.")
        return False
    if guess[0] == "0":
        print("Invalid input: The guess cannot start with 0.")
        return False
    return True

# funkce pro zjisteni poctu spravnych cislic (cows) a spravnych mist (bulls)
def bulls_and_cows(n_guess, p_guess):
    """
    Parametry:
    - n_guess: integer/cislo,  ktere ma hrac uhodnout (tajne/magicke cislo)
    - p_guess: integer/cislo, ktere hrac zadal (jeho hadaci pokus)

    Vystupove hodnoty:
    - bulls: pocet spravnych cislic na spravnych pozicich
    - cows: pocet spravnych cislic na spatnych pozicich
    """
    bulls = 0 # pocet spravnych cislic na spravnych mistech
    cows = 0 # pocet spravnyhc cislic na spatnych msitech

    # Prevod obou cisel na retezce pro snazsi porovnavani pozic
    n_guess = str(n_guess)
    p_guess = str(p_guess)

    #iterace pres vsechny pozice, pro zjisteni poctu bulls/cows
    for i in range(4):
        if p_guess[i] == n_guess[i]: # pokud splneno, pridame k bulls, spravna cislice na spravnem miste
            bulls += 1
        elif p_guess[i] in n_guess: # pokud splneno, pridame ke cows, spravna cislice na spatnem miste
            cows += 1

    # vypis vylsledku - zohlednuje jednotne a mnozne cislo
    if cows == 1:
        print("Bulls:", bulls, "\tCow:", cows, "\t\tGuesses:", counter)
    elif bulls == 1:
        print("Bull:", bulls, "\tCows:", cows, "\tGuesses:", counter)
    elif bulls == 1 and cows == 1:
        print("Bull:", bulls, "\tCow:", cows, "\tGuesses:", counter)
    else:
        print("Bulls:", bulls, "\tCows:", cows, "\tGuesses:", counter)

    return bulls, cows  # Vraci pocet bulls a cows


def main():
    """
    Hlavni funkce programu obsahujici logiku hry.
    """
    # incicializace promennych
    global counter
    counter = 0
    number_to_guess = generate_unique_4_digit_number()
    player_guess = str(input("Enter a number: "))
    start_time = 0  # Inicializace proměnné start_time

    while player_guess != number_to_guess:
        print("debug - hadane cislo je:", number_to_guess) #- debug pro kontrolu tajneho cisla
        if is_valid_guess(player_guess):
            counter += 1

            # Začátek časovače
            if start_time is None or start_time == 0:
                start_time = time.time()

            if str(player_guess) == str(number_to_guess):
                print("\n >>> Winner winner chicken dinner, you guessed the number! <<<")
                # Konec časovače
                end_time = time.time()
                duration_time = round(end_time - start_time, 3)
                start_time = None # resetovani casovace - jinak to pocita dal pri "y" na dalsi hru

                print("Results!\nTime:", duration_time, "seconds, \tAttempts:", counter, "\n")
                player_name = str(input("Enter your name: "))

                save_record(player_name, duration_time, counter)

                play_again = input("Do you want to play again? [y/n]:")

                if play_again == "y":
                    counter = 0
                    bulls = 0
                    cows = 0
                    number_to_guess = generate_unique_4_digit_number()
                    player_guess = str(input("\nEnter a number: "))
                else:
                    print("Goodbye!")
                    break

            elif str(player_guess) != str(number_to_guess):
                bulls, cows = bulls_and_cows(n_guess=number_to_guess, p_guess=player_guess)
                player_guess = str(input("\nEnter a next guess: "))

        else:
        # print("Did you type 4 digits number with unique digits? - Try again!", "debug - hadane cislo je:", number_to_guess)
            player_guess = str(input("Enter a number: "))


if __name__ == "__main__":
    main()

"""
1. počítání času, za jak dlouho uživatel uhádne tajné číslo
2. uchovávat statistiky počtu odhadů jednotlivých her
"""