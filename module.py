num_of_days_in_week = 7
num_of_days_in_month = 30

def week_calculation(num_of_days,conversion_unit):
    if conversion_unit == "weeks":
        return (f"{num_of_days} days are {num_of_days // num_of_days_in_week} weeks and {num_of_days % num_of_days_in_week} days!\n")
    elif conversion_unit == "months":
        num_of_months = num_of_days // num_of_days_in_month
        remaining_days = num_of_days % num_of_days_in_month
        num_of_weeks = remaining_days // num_of_days_in_week
        number_of_days = remaining_days % num_of_days_in_week
        return (f"{num_of_days} days are {num_of_months} months, {num_of_weeks} weeks and {number_of_days} days ")
    else :
        print ("invalid unit !!")
    
def validate(days_and_unit_dictionary):
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number >= 7 :
            value = week_calculation(user_input_number,days_and_unit_dictionary["unit"])
            print (f"{value}")
        elif user_input_number < 7 :
            print (f"7 is a minimum number of days in a week!")
        else :
            print (f"no conversion!")
    except ValueError:
        print (f"enter a valid number!")
