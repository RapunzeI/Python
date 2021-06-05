def reverse(dict):
    new_dict = {}
    for element in dict:
        new_dict[dict[element]] = element
    return new_dict

phonebook = {'Smith, Jane':'123-45-67', 'Doe, John':'9876543', 'Baker,David':'5678901'}
print(reverse(phonebook))