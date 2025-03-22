"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Kamil Mach
email: kamilmachuj@gmail.com
"""

import random
import time

start_time = None
end_time = None
#counter = 0

number_to_guess = 0
# definice vet
sentences_1 = ["Hi there, I've generated a random 4 digit number for you.",
             "Let's play a bulls and cows game.",
             "Timer will starts count after you enter your first guess. GOOD LUCK!"
            ]

# vypocet max delky jedne vety pro zarovnani "-"
def max_lenght(sentences):
    return max(len(sentence) for sentence in sentences)


# formatovany vypis kazde vety, podle max. delky
def format_senteces(sentences, max_lenght):
    for sentence in sentences:
        print(sentence)
        print("-" * max_lenght)

format_senteces(sentences=sentences_1, max_lenght=max_lenght(sentences_1))

# fce pro zapis historickych dat ze hry
def save_record(player_name, duration_time, counter):
    with open("results.txt", "a") as file:
        file.write(f"Player: {player_name}, \t\tTime: {duration_time}, \t\tGuesses: {counter}\n")

"""
-   program dále vytvoří tajné 4místné číslo (číslice musí být unikátní a nesmí začínat 0) hráč hádá číslo.
    Program jej upozorní, pokud zadá číslo kratší nebo delší než 4 čísla, pokud bude obsahovat duplicity,
    začínat nulou, příp. obsahovat nečíselné znaky,"""


def generate_random_4_digit_number():
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

# ofce pro generovani 4 mistneho cisla s unikatnimi cislicemi
def generate_unique_4_digit_number():
  #    print("Kod se pustil")

    while True:
        number = generate_random_4_digit_number() # vygeneruje nahodne cislo
        if is_unique_number(number):  # kontrola zda cislo obssahuje uniqe cislice
        #    print(number, ">> TOTO JE TO CISLO")
            return number # pokud ano, vrati

number_to_guess = generate_unique_4_digit_number()

"""hráč hádá číslo. Program jej upozorní, pokud zadá číslo kratší nebo delší než 4 čísla,
 pokud bude obsahovat duplicity, začínat nulou, příp. obsahovat nečíselné znaky,"""

"""program dále vypíše počet bull/ bulls (pokud uživatel uhodne jak číslo, tak jeho umístění),
 příp. cows/ cows (pokud uživatel uhodne pouze číslo, ale ne jeho umístění).
 Vrácené ohodnocení musí brát ohled na jednotné a množné číslo ve výstupu.
 Tedy 1 bull a 2 bulls (stejně pro cow/cows).
 
 bull = spravne cislo na spravnem miste
 cow = spravne cislo na spatnem miste
 """

# funkce pro zjisteni poctu spravnych cislic (cows) a spravnych mist (bulls)
def bulls_and_cows(n_guess, p_guess):
    bulls = 0
    cows = 0
    n_guess = str(n_guess) # oboji na string skrz porovani pozic
    p_guess = str(p_guess)

    for i in range(4):
        if p_guess[i] == n_guess[i]:
            bulls += 1
        elif p_guess[i] in n_guess:
            cows += 1

    if cows == 1:
        print("Bulls:", bulls, "\tCow:", cows, "\t\tGuesses:", counter)
    elif bulls == 1:
        print("Bull:", bulls, "\tCows:", cows, "\tGuesses:", counter)
    elif bulls == 1 and cows == 1:
        print("Bull:", bulls, "\tCow:", cows, "\tGuesses:", counter)
    else:
        print("Bulls:", bulls, "\tCows:", cows, "\tGuesses:", counter)

    return bulls, cows  

player_guess = str(input("Enter a number: "))
counter = 0


while player_guess != number_to_guess:
    # print("debug - hadane cislo je:", number_to_guess) - debug pro kontrolu tajneho cisla

    if player_guess.isdigit() and len(player_guess) == 4 and is_unique_number(player_guess) == True and player_guess[0] != "0":
        # print(player_guess[0])
        # print("OK - Your guess is in valid format")
        counter += 1
        # Začátek časovače
        if start_time is None:
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
        print("Did you type 4 digits number with unique digits? - Try again!", "debug - hadane cislo je:", number_to_guess)
        player_guess = str(input("Enter a number: "))


"""
1. počítání času, za jak dlouho uživatel uhádne tajné číslo
2. uchovávat statistiky počtu odhadů jednotlivých her"""