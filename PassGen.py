import random
length = input("Enter the Length of the Password: ")
if length.isnumeric():
    Name = input("Enter Your Name: ").lower()
    Father_Name = input("Enter Your Father Name: ").lower()
    Birth_year = input("Enter your BirthYear (eg.2003,1998): ")
    Hero = input("Enter the name of your favourite Hero/Fictional Character: ")

    password = ""

    length = int(length) / 4
    length = round(length, 2)
    for i in range(0, int(length)):
        Random_Name = random.choice(Name)
        Random_FatherName = random.choice(Father_Name)
        Random_BirthYear = random.choice(Birth_year)
        Random_Hero = random.choice(Hero)

        password += Random_Name + Random_FatherName + Random_BirthYear + Random_Hero

    print("Your Randomly Generated Password is: " + password)

else:
    print("--> Error!! Invalid Character\n"
          "--> Enter A Number from 0-9")
