from module import validate

"""while True :
    user_input = input("Hey! enter number of days to convert into weeks!\n")
    list_of_days = user_input.split(",")
    print (list_of_days)
    print (set(list_of_days))
    print (type(list_of_days))
    print (type(set(list_of_days)))
    for num_of_days_element in set(list_of_days) :
        validate()
    if user_input == "exit":
        break"""

while True :
    user_input = input("Hey! enter number of days and unit to convert!\n")
    days_and_unit = user_input.split(":")
    print (days_and_unit)
    days_and_unit_dictionary = {"days":days_and_unit[0],"unit":days_and_unit[1]}
    print(days_and_unit_dictionary)
    print(type(days_and_unit_dictionary))
    validate()
    



