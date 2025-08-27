#Prado, Dandel Oliver S.
#G-6L
#mtpw = milk tea per week
#cimt = calories in milk tea
#cpy = calories per year
#ktcb = kilometers to burn calories
#mtbc = miles to burn calories
#user inputs the number or milk tea consumed per week and the approx calories in a cup
#outputs the number or km or mi needed to run in order to burn the total calories in a year

mtpw = float(input("How many times per week do you drink milk tea?: "))
cimt = float(input("How many calories does your usual milk tea contain?: "))
cpy = (mtpw * cimt) * 52

print("You consume approximately",cpy,"calories per year from milk tea.\n")

ktbc = cpy/60
mtbc = cpy/100
print("In order to burn this off, you need to:")
print("   - Run",round(ktbc)," kilometers to burn this off. (100 calories per mile)")
print("   - OR run",round(mtbc)," miles to burn this off. (60 calories per kilometer)")
