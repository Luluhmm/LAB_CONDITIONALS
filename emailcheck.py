#Luluh Almogbil
'''
## Bonus 2
### write a program that asks the user to provide his name and his email using input , then do the following:
- Check that the name length is more than 2 characters.
- Check that the email is valid (using string operations and coditionals)
- You only accept @gmail emails . 
- if the email is valid, display a welcome message to the user . for example :
```
welcome Ahmed, you registered with the email ahmed@gmail.com !

```
- if the email or name is not valid, display the message : 
```
 the email is not valid , please provide a valid email .
```

or 

```
the name length must be more than 2 characters, please provide a valid name.
```

### Note: don't use regular expressions or a library yet.
'''
name = input("Please enter your name: ")
email = input("Please enter your email: ")
print (len(name))

if len(name) > 2 :
   print("the name is valid, now lets check the email")
   if "@gmail.com" in email and email.index("@gmail.com") > 0 and "@" in email == 1 :
       print("valid gmail")
       print("Welcome",name,"you registered with the",email,"!")
   else:
       print(" the email is not valid , please provide a valid email ")
       
else:
    print("the name is not valid, please re-write your full name to be more than just 2 characters")