
# convert height to inches
def convert_to_inches(usr_height):
    
    # split the input string into a list
    height_list = usr_height.split(" ")

    # convert the list elements to integers
    num_ft = int(height_list[0])
    num_inches = int(height_list[1])

    # calculate the total inches
    total_inches = (num_ft * 12) + num_inches

    return total_inches

# convert weight to kg
def metric_conversion_weight(usr_weight):
    num_kg = int(usr_weight) * 0.45

    return num_kg

# convert height to meters
def metric_conversion_height(usr_height):
    num_meters = int(usr_height) * 0.025

    return num_meters

# square the height for BMI formula
def meters_squared(usr_height):
    return usr_height ** 2

# calculate BMI
def bmi_conversion(usr_height, usr_weight):

    # call function to convert weight to kg
    usr_weight_kg = metric_conversion_weight(usr_weight)

    # call function to convert height to meters
    usr_height_meters = metric_conversion_height(usr_height)

    # call function to square the height
    usr_height_meters = meters_squared(usr_height_meters)
    
    # calculate BMI
    bmi = usr_weight_kg / usr_height_meters

    return bmi

# categorize BMI
def bmi_category(bmi):
    # basic if-else statements to categorize BMI
    if (bmi < 18.5):
        print ("\nYour BMI is %.3f. Category: Underweight" % bmi)
        return "Underweight"

    elif (bmi >= 18.5 and bmi < 25):
        print ("\nYour BMI is %.3f. Category: Normal weight" % bmi)
        return "Normal weight"

    elif (bmi >= 25 and bmi < 30):
        print ("\nYour BMI is %.3f. Category: Overweight" % bmi)
        return "Overweight"

    elif (bmi >= 30):
        print ("\nYour BMI is %.3f. Category: Obese" % bmi)
        return "Obese"


def main():
    # Introductory messages
    print ("Welcome to BMI Calculator")
    # Instructions
    print ("Height should be entered in the form of 'ft in'. Ex: 5 11")
    print ("Weight should be entered in lbs\n")

    # User input
    usr_height = input("Enter your height: ")
    # Convert height to inches
    usr_height = convert_to_inches(usr_height)

    # User input
    usr_weight = input("Enter your weight: ")

    # Call BMI function based on gathered user input
    bmi = bmi_conversion(usr_height, usr_weight)

    # Call BMI category function based on calculated BMI
    bmi_category(bmi)

# Run the main function
if __name__=="__main__":
    main()