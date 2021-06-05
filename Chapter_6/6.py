def sync(phoneBook_List):
    pbSet = set()
    for phoneBook in phoneBook_List:
        pbSet = pbSet | phoneBook
    return pbSet
phonebook1 = {'123-45-67', '234-56-78', '345-67-89'}
phonebook2 = {'234-56-78'}
phonebook3 = {'345-67-89', '456-78-90'}
phonebook4 = {'234-56-78', '456-78-90'}
phonebooks = [phonebook1, phonebook2, phonebook3, phonebook4]

print(sync(phonebooks))