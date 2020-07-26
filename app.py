import csv
import useful_tools
from Employee import Employee
from Question import Question
from Chef import Chef
from FrenchChef import FrenchChef

## Practicing the basics
## Thanks to freecodecamp.com
## https://youtu.be/rfscVS0vtbw

## Dictionaries (Key-Value Pairs)
# monthConversions = {
#     "Jan": "January",
#     "Feb": "Februrary",
#     "Mar": "March",
#     "Apr": "April",
#     "May": "May",
#     "Jun": "June",
#     "Jul": "July",
#     "Aug": "August",
#     "Sep": "September",
#     "Oct": "October",
#     "Nov": "November",
#     "Dec": "December"
# }

# print(monthConversions["Nov"])
# print(monthConversions.get("Sep", "Not Found"))
# print(monthConversions.get("Sept", "ERROR: Key Not Found"))


## While Loops Guessing Game
# secret_word = "giraffe"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False

# while guess != secret_word and not(out_of_guesses):
#     if guess_count < guess_limit:
#         guess = input("Enter your guess: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True
    
# if out_of_guesses:
#     print("You're out of guesses!")
# else:
#     print("You win!")


## For Loops
# planets = [
#     "Mars",
#     "Jupiter",
#     "Pluto",
# ]

# for planet in planets:
#     print(planet)

# for index in range(5):
#     if index == 0:
#         print("First")
#     else:
#         print("The rest")

## Exponent function
# def raise_to_power(base_number, power_number):
#     result = 1
#     for i in range(power_number):
#         result = result * base_number
#     return result

# print(raise_to_power(2, 3))


## 2D Lists & Nested Loops
# number_grid = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
# ]

# for row in number_grid:
#     for column in row:
#         print(column)


## Build a translator: the Giraffe Language translator
# For example: all vowels -> g
# def translate(phrase):
#     translation = ""
#     for letter in phrase:
#         if letter.lower() in "aeiou":
#             if letter.isupper():
#                 translation = translation + "G"
#             else:
#                 translation = translation + "g"
#         else:
#             translation = translation + letter
#     return translation

# print(translate(input("Enter a phrase: ")))


## Try / Except
# try:
#     number = int(input("Enter a number: "))
#     print(number)
# except ValueError as err:
#     print(err)
# except:
#     print("Error occurred")


## Reading files
# r - read
# w - write
# a - append
# rw - read/write

# Read and print each row in a TXT file
# movies = open('movies.txt', 'r')
# print(movies.readable())
# print(movies.readlines())

# for movie in movies.readlines():
#     print(movie)

# movies.close()

# Append to TXT files
# movies_file = open('movies.txt', 'a')
# movies_file.write("\nHarry Potter")
# movies_file.close()

# Create new TXT file
# books_file = open('books.txt', 'w')
# books_file.write("The First 90 days\nRadical Candor")
# books_file.close()

# Read and print each row in a CSV file
# with open('tv-shows.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter = ',')
#     row_count = 0
#     for row in csv_reader:
#         if row_count == 0:
#             print(f'---> Column names are {", ".join(row)}')
#             row_count += 1
#         else:
#             print(f'Watch "{row[0]}" on {row[1]}"')
#             row_count += 1
#     print(f'There were {row_count} shows')

# Another way to read and print each row in a CSV file
# with open('tv-shows.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     for row in csv_reader:
#         show, network = row
#         if show.find('_') >= 0:
#             print(f'---> What to watch and where:')
#         else:
#             print(f'Watch "{show}" on {network}')

# Read CSV files into a dictionary using DictReader
# with open('tv-shows.csv', mode = 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     print('---> What to watch and where:')
#     for row in csv_reader:
#         print(f'Watch "{row["show_name"]}" on {row["where_to_watch"]}')


## Modules and Pip
# print(useful_tools.roll_dice(10))


## Classes & Objects
# employee1 = Employee(
#     "Raymond",
#     "Holt",
#     "2020/01/01",
#     "99th Precinct",
#     "Captain",
#     True
# )
# employee2 = Employee(
#     "Jake",
#     "Peralta",
#     "2019/01/01",
#     "99th Precinct",
#     "Detective",
#     True
# )

# # print(employee1.first_name + " " + employee1.last_name)
# print("Is " + employee1.first_name + " a captain?")
# print(employee1.is_captain())


## Multiple Choice Quiz
# question_prompts = [
#     "What colour are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
#     "What colour are strawberries?\n(a) Blue\n(b) Green\n(c) Red\n\n",
#     "What colour are pineapples?\n(a) Pink\n(b) Yellow/Green\n(c) White\n\n",
# ]

# questions = [
#     Question(question_prompts[0], "a"),
#     Question(question_prompts[1], "c"),
#     Question(question_prompts[2], "b"),
# ]


# def run_test(questions):
#     score = 0
#     for question in questions:
#         response = input(question.prompt)
#         if response == question.answer.lower():
#             score += 1
#     print("You got " + str(score) + "/" + str(len(questions)) + " correct")

# run_test(questions)


## Inheritance
myChef = Chef()
myChef.make_dessert()

myFrenchChef = FrenchChef()
myFrenchChef.make_dessert()
myFrenchChef.make_chicken()
myFrenchChef.make_bread()