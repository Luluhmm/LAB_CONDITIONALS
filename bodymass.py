#Luluh Almogbil 
'''
## Bonus 1
### write a program that Calculates the BMI (body mass index) of the user:
- Ask the user to provide his wieght.
- Ask the user to provide hi height.
- print the BMI for the user.
- using conditionals tell the user that either :
- - You are overwieght you need to work out more and watch your diet.
- - You are fit & healthy.
- - You are underweight. Watch your health.

### Note
for formula , search the web.
'''

w = input("Please enter your weight in kg : ")
wieght = float(w)
h = input("Please enter your height in meters: ") # this will be string, pvm will intrepreter this as a string
height = float(h)

BMI = wieght / (height ** 2)
print("Your BMI is: ",round(BMI,3))

if BMI >= 25:
    print("You are overweighted, please watch your health and try to work out more")
elif BMI >= 18.5:
    print("Mashallah you are fit and healthy, keep going!")    
elif BMI < 18.5:
    print("You are underweight , please watch your health and eat more")      
