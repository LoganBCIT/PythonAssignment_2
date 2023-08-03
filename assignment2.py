# author: Logan Dutton-Anderson

from data import countries_and_capitals, countries, capitals, countries_capitals_dictionary
import re


def write_countries_capitals_to_file(filename):
    """
    This function takes one parameter: a filename. The filename is first validated by using a regular expression.

    Valid filenames must follow these rules:

    Must contain only letters or digits.
    Must be of length 1-8 characters, plus a “.txt” file extension.

    For example, these are all valid filenames:
    a.txt
    5x.txt
    AbcE123z.txt

    If the filename is not valid, prompts the user for another filename inside the function. This process continues
    over and over until the user enters a valid filename.
    Uses a regular expression to validate the filename.
    Once the user has entered a valid filename, opens the file for writing only, and processes the
    countries_capitals_dictionary variable.
    Uses a for/in loop to process the dictionary (for country, capital in countries_capitals_dictionary.items():)
    We will use it to write that data in the following format, to the file named by the user, then close the file.

    :param filename: File name being checked.
    """
    while True:
        if re.search("^[a-zA-Z0-9]{1,8}[.]txt$", filename):
            f = open(filename, 'w')
            for country, capital in countries_capitals_dictionary.items():
                f.writelines(f'The capital of {country} is {capital}.\n')
            f.close()
            break
        else:
            print('Invalid file name, please ensure there are only letters and digits in your file name.')
            filename = (input('Please enter your new file name:'))
            continue


def save_capitals():
    """
    This function opens files for writing only. Uses regular expressions to find all the capital cities that meet the
    patterns commented beside the file opening statement, and writes them to the files with the given names.
    Closes each file when it’s finished.
    """
    f = open("vowel_vowel_vowel.txt", 'w')  # Contain three consecutive vowels
    for capital in capitals:
        if re.search("^.*[aeiou][aeiou][aeiou].*$", capital, re.IGNORECASE):
            f.writelines(f'{capital}\n')
    f.close()

    f = open("cons_cons_cons.txt", 'w')  # Contain three consecutive consonants
    for capital in capitals:
        if re.search("^.*[bcdfghjklmnpqrstvwxyz][bcdfghjklmnpqrstvwxyz][bcdfghjklmnpqrstvwxyz].*$", capital,
                     re.IGNORECASE):
            f.writelines(f'{capital}\n')
    f.close()

    f = open("i_before_e.txt", 'w')  # Contain i somewhere before e. For example: Ireland
    for capital in capitals:
        if re.search("^.*i.*e.*$", capital, re.IGNORECASE):
            f.writelines(f'{capital}\n')
    f.close()

    f = open("a_a.txt", 'w')  # Start with a, and end with a
    for capital in capitals:
        if re.search("^a.*a$", capital, re.IGNORECASE):
            f.writelines(f'{capital}\n')
    f.close()

    f = open("end_with_vowel.txt", 'w')  # End with a vowel
    for capital in capitals:
        if re.search("^.*[aeiou]$", capital, re.IGNORECASE):
            f.writelines(f'{capital}\n')
    f.close()

    f = open("weird.txt", 'w')  # Contains apostrophe, space, or x
    for capital in capitals:
        if re.search("^.*\'| |x.*$", capital, re.IGNORECASE):
            f.writelines(f'{capital}\n')
    f.close()

    f = open("not_start.txt", 'w')  # Does not start with a-e, l-p, or s
    for capital in capitals:
        if re.search("^[^a-el-ps].*$", capital, re.IGNORECASE):
            f.writelines(f'{capital}\n')
    f.close()
