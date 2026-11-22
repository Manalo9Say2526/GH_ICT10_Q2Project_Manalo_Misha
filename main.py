# input and display proccesing
from pyscript import display, document # type: ignore

def country_nickname(e): # initiating function 
    document.getElementById('output').innerHTML = " " # in order for the display not to overlap
    country = document.getElementById('Country').value # connects to ID input type and selected country

    countries = [ # list of countries
        'Philippines',
        'Vietnam',
        'Thailand',
        'Indonesia',
        'Malaysia',
        'Brunei',
        'Laos',
        'Timor-Leste',
        'Myanmar',
        'Singapore',
        'Cambodia'
    ]

    nicknames = ( # nickname tuples
        'Pearl of the Orient Seas',
        'Land of the Ascending Dragon',
        'Land of Smiles',
        'Emerald of the Equator',
        'Truly Asia',
        'Abode of Peace',
        'Land of a Million Elephants',
        'Land of the Rising Sun',
        'Golden Land',
        'Lion City',
        'Kingdom of Wonder'
    )
    
    

    display("Nickname: " + nicknames[countries.index(country)], target='output') # connecting tuple (nickname) and list (countries) to display, with indexing to determine or select the position of  the country and nickname

def element_finder(e):
    document.getElementById('output').InnerHTML = ' ' 
    element_symbol = document.getElementById('element').value.capitalize().strip()

    details = { # the details of the elements 
        "H": {
            "Element Symbol": "H",
            "Element Name": "Hydrogen",
            "Atomic Number": 1,
            "Atomic Mass": 1.008
        },
        "C": {
            "Element Symbol": "C",
            "Element Name": "Carbon",
            "Atomic Number": 6,
            "Atomic Mass": 12.011
        },
        "N": {
            "Element Symbol": "N",
            "Element Name": "Nitrogen",
            "Atomic Number": 7,
            "Atomic Mass": 14.007
        },
        "O": {
            "Element Symbol": "O",
            "Element Name": "Oxygen",
            "Atomic Number": 8,
            "Atomic Mass": 15.999
        },
        "P": {
            "Element Symbol": "P",
            "Element Name": "Phosphorus",
            "Atomic Number": 15,
            "Atomic Mass": 30.974
        },
        "S": {
            "Element Symbol": "S",
            "Element Name": "Sulfur",
            "Atomic Number": 16,
            "Atomic Mass": 32.06
        },
        "Se": {
            "Element Symbol": "Se",
            "Element Name": "Selenium",
            "Atomic Number": 34,
            "Atomic Mass": 78.971
        },
        "F": {
            "Element Symbol": "F",
            "Element Name": "Fluorine",
            "Atomic Number": 9,
            "Atomic Mass": 18.998
        },
        "Cl": {
            "Element Symbol": "Cl",
            "Element Name": "Chlorine",
            "Atomic Number": 17,
            "Atomic Mass": 35.45
        },
        "Br": {
            "Element Symbol": "Br",
            "Element Name": "Bromine",
            "Atomic Number": 35,
            "Atomic Mass": 79.904
        },
        "I": {
            "Element Symbol": "I",
            "Element Name": "Iodine",
            "Atomic Number": 53,
            "Atomic Mass": 126.90
        },
        "He": {
            "Element Symbol": "He",
            "Element Name": "Helium",
            "Atomic Number": 2,
            "Atomic Mass": 4.003
        },
        "Ne": {
            "Element Symbol": "Ne",
            "Element Name": "Neon",
            "Atomic Number": 10,
            "Atomic Mass": 20.180
        },
        "Ar": {
            "Element Symbol": "Ar",
            "Element Name": "Argon",
            "Atomic Number": 18,
            "Atomic Mass": 39.948
        },
        "Kr": {
            "Element Symbol": "Kr",
            "Element Name": "Krypton",
            "Atomic Number": 36,
            "Atomic Mass": 83.798
        },
        "Xe": {
            "Element Symbol": "Xe",
            "Element Name": "Xenon",
            "Atomic Number": 54,
            "Atomic Mass": 131.293
        },
        "Rn": {
            "Element Symbol": "Rn",
            "Element Name": "Radon",
            "Atomic Number": 86,
            "Atomic Mass": 222
        }
    }

    element_checker = element_symbol in details # to check if the selected element is in the dictionary
    display_message = (f'Sorry, {element_symbol} is not included in the list', f'{element_symbol} is included in the list {details.get(element_symbol)}') # to check if the element is in the list 
        
    display(display_message[element_checker], target='output') # display output

# participation activity
from pyscript import display, document  # type: ignore

def club_member(e):
    document.getElementById('output').innerHTML = ' ' 
    first_name = document.getElementById('firstname').value
    last_name = document.getElementById('lastname').value

    # creating a set to include the new member
    new_member = {f"{first_name} {last_name}"}

    # list of club members per grade level
    grade7 = {'Kylan Gentry', 'Amelie Griffith', 'Franklin Sierra', 'Saoirse Conrad'}
    grade8 = {'Marley Castro', 'Holly Glover', 'Avayah Austin', 'Salvatore Sal'}
    grade9 = {'Jasmeen Kaur', 'Sofia Navarro', 'Blake Pancho', 'Hailey Asis'}
    grade10 = {'Misha Manalo', 'Elise Lim', 'Adri Allas', 'Franchesca Dela Rosa'}

    # combination of all grade levels with the new member
    grade_levels = grade7 | grade8 | grade9 | grade10 | new_member

    # output of combination
    display(grade_levels, target='output')

    # counting of all members
    display(f'The total number of members: {len(grade_levels)}', target='output')

    



