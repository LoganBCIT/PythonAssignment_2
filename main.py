# author: Logan Dutton-Anderson

from data import countries_and_capitals, countries, capitals, countries_capitals_dictionary
import assignment2
import re


def main():
    assignment2.write_countries_capitals_to_file('0123456789.txt')
    assignment2.save_capitals()


if __name__ == '__main__':
    main()
