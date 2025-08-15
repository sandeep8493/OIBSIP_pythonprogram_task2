height=float(input("Height in Meters"))
weight=int(input("Weight in Kilograms"))
bmi=(weight/(height**2))
print("BMI IS =",bmi)
if bmi<18.5 :
    print("UNDERWEIGHT")
elif (18.5< bmi) and (bmi<=24.9) :
    print("NORMAL")
else :
    print("OVERWEIGHT")