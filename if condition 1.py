height= float(input("enter your height :"))
weight=float(input("enter your weight :"))
BMI= weight/height**2
print(BMI)
if 30<=BMI:
     print("obesity")

  # If BMI is between 25 and 29, print "Overweight"

if BMI>=25 and BMI<=29:
     print("overweight")

#If BMI is between 18.5 and 25, print "Normal"

if  BMI>=18.5 and BMI<=25:
     print("normal")

#If BMI is less than 18.5, print "Underweight"

if BMI<18.5:
     print("underweight")


