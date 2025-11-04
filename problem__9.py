user_age = input("Enter Age: ")
age = int(user_age)
user_qualification = input("Enter your Qualification: ")

if age >= 18 and user_qualification.lower() == 'graduate':
    print("Eligible for Job")
else:
    print("Not Eligible")
