print("WELCOME TO BMI Generator!")
h=float(input("ENTER YOUR HEIGHT (in m):\n"))
w=float(input("ENTER YOUR WEIGHT (in kg):\n"))
bmi=round(w/h**2)
if bmi <18.5:
    print("underweight")
elif bmi<25:
    print("normal")
elif bmi<30:
    print("overweight")
elif bmi<35:
    print("obese")
else :print("clinically obese")