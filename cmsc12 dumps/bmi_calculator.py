# Given the weight (in kg) and height (in meters), calculate the person’s BMI and determine its classification.

# crude code
#-------------------------------------------
# w = float(input("Weight in kg: "))
# h = float(input("height in m: "))

# bmi = w/(h**2)

# if bmi < 18.5:
#     print(bmi)
#     print("underweight")
#-------------------------------------------

def bmi_calc (weight, height):
    return weight / (height ** 2)

def bmi_categ(bmi): 
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    elif 30 <= bmi:
        return "Obese"  

def main(): 
    print("BMI CALCULATOR")
    print("~" * 30)
    try: 
        weight = float(input("Weight (kg): "))
        height = float(input("Height (m): "))

        if weight <= 0 or height <= 0:
            print("Error")
            return
        
        #calculate and classify bmi
        bmi = bmi_calc(weight, height)
        category = bmi_categ(bmi)

        print(f"\nResults:")
        print(f"Weight:", weight, "kg")
        print(f"Height:", height, "m")
        print(f"BMI:", "%.2f" %bmi)
        print(f"You are", category)
    
    except ValueError:
        print("Error. Please try again.")

main()
