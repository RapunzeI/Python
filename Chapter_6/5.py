def lookup(phonebook):
    while True:
        first_name = input('Enter the first name: ')
        last_name = input('Enter the last name: ')

        if (first_name, last_name) in phonebook:
            print(phonebook[first_name, last_name])

phoneBook = {('Anna', 'Karenina'):'(123)456-78-90', ('Yu', 'Tsun'):'(901)234-56-78', ('Hans', 'Castorp'):'(321)908-76-54'}
lookup(phoneBook)