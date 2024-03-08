

def convert_to_inches(usr_height):
    
    height_list = usr_height.split(" ")

    num_ft = int(height_list[0])
    num_inches = int(height_list[1])

    total_inches = (num_ft * 12) + num_inches

    return total_inches


def metric_conversion_weight(usr_weight):
    num_kg = int(usr_weight) * 0.45

    return num_kg


def metric_conversion_height(usr_height):
    num_meters = int(usr_height) * 0.025

    return num_meters

def meters_squared(usr_height):
    return usr_height ** 2


def bmi_conversion(usr_height, usr_weight):

    usr_weight_kg = metric_conversion_weight(usr_weight)

    usr_height_meters = metric_conversion_height(usr_height)

    usr_height_meters = meters_squared(usr_height_meters)
    
    bmi = usr_weight_kg / usr_height_meters

    return bmi

def bmi_category(bmi):

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

    print ("Welcome to BMI Calculator")
    print ("Height should be entered in the form of 'ft in'. Ex: 5 11")
    print ("Weight should be entered in lbs\n")

    usr_height = input("Enter your height: ")
    usr_height = convert_to_inches(usr_height)

    usr_weight = input("Enter your weight: ")

    bmi = bmi_conversion(usr_height, usr_weight)

    bmi_category(bmi)


if __name__=="__main__":
    main()