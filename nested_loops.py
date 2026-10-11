# 1
n = int(input())

if n > 0:
    print("Positive Number")

#2
age = int(input())

if age >= 18:
    print("Eligible to Vote")

#3
temp = int(input())

if temp > 40:
    print("High Temperature")

#4
n = int(input())

if n % 5 == 0:
    print("Divisible by 5")

#5
 amount = int(input())

if amount >= 1000:
    print("Free Delivery")

#6
ch = input()

if ch == "A":
    print("You entered A")

#7
  password = input()

if len(password) >= 8:
    print("Strong Length")


#8
  n = int(input())

if n >= 100 and n <= 999:
    print("Three Digit Number")

#if-else
# 9
n = int(input())

if n % 2 == 0:
    print("Even")
else:
    print("Odd")

#10
marks = int(input())

if marks >= 40:
    print("Pass")
else:
    print("Fail")

#11
age = int(input())

if age >= 18:
    print("Adult")
else:
    print("Minor")

#12
n = int(input())

if n > 0:
    print("Positive")
else:
    print("Non-Positive")

#13
n = int(input())

if n % 3 == 0:
    print("Divisible by 3")
else:
    print("Not Divisible by 3")

#14
correct_password = "python123"
password = input()

if password == correct_password:
    print("Login Successful")
else:
    print("Invalid Password")

#15
username = input()

if username == "admin":
    print("Welcome Admin")
else:
    print("Invalid Username")

#16
a = int(input())
b = int(input())

if a > b:
    print(a)
elif b > a:
    print(b)
else:
    print("Both are Equal")


#17
temp = int(input())

if temp > 30:
    print("Hot")
else:
    print("Comfortable")

#18
amount = int(input())

if amount >= 5000:
    print("Discount Available")
else:
    print("No Discount")

#19
marks = int(input())

if marks >= 90 and marks <= 100:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
elif marks >= 60:
    print("D")
else:
    print("F")


#
# 20
temp = int(input())

if temp >= 40:
    print("Very Hot")
elif temp >= 30:
    print("Hot")
elif temp >= 20:
    print("Warm")
else:
    print("Cold")   


#21
color = input()

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Wait")
elif color == "green":
    print("Go")
else:
    print("Invalid Signal")

#22
units = int(input())

if units <= 100:
    print("Low Usage")
elif units <= 300:
    print("Medium Usage")
elif units <= 500:
    print("High Usage")
else:
    print("Very High Usage")


#23
age = int(input())

if age < 5:
    print("Free Ticket")
elif age <= 12:
    print("Child Ticket")
elif age <= 59:
    print("Regular Ticket")
else:
    print("Senior Ticket")

#24
bmi = float(input())

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")

#25
month = int(input())

if month in [1, 3, 5, 7, 8, 10, 12]:
    print("31 Days")
elif month in [4, 6, 9, 11]:
    print("30 Days")
elif month == 2:
    print("28 or 29 Days")
else:
    print("Invalid Month")

#26
a = float(input())
b = float(input())
op = input()

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b != 0:
        print(a / b)
    else:
        print("Cannot Divide by Zero")
else:
    print("Invalid Operator")


#27
day = int(input())

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid Day")

#28
score = int(input())

if score >= 90:
    print("Excellent")
elif score >= 75:
    print("Very Good")
elif score >= 60:
    print("Good")
elif score >= 40:
    print("Average")
else:
    print("Needs Improvement")

#29
marks = int(input())
attendance = int(input())

if marks >= 60 and attendance >= 75:
    print("Eligible")
else:
    print("Not Eligible")  

#30
marks = int(input())
income = int(input())

if marks >= 85 or income < 300000:
    print("Scholarship Available")
else:
    print("No Scholarship")


#31
day = input()

if day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("Weekday")

#32
username = input()
password = input()

if username == "student" and password == "python123":
    print("Access Granted")
else:
    print("Access Denied")

#33
city = input()

if city == "Ahmedabad" or city == "Gandhinagar":
    print("Delivery Available")
else:
    print("Delivery Unavailable")

#34
n = int(input())

if n >= 10 and n <= 50:
    print("Inside Range")
else:
    print("Outside Range")

#35
amount = int(input())
otp = input()

if amount <= 50000 and otp == "1234":
    print("Transaction Approved")
else:
    print("Transaction Declined")

#36
username = input()
password = input()

if username == "admin":
    if password == "admin123":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")

#37
age = int(input())
status = input()

if age >= 18:
    if status == "pass":
        print("License Approved")
    else:
        print("Test Not Passed")
else:
    print("Age Not Eligible")

#38
balance = int(input())
amount = int(input())

if amount <= balance:
    if amount % 100 == 0:
        print("Withdrawal Successful")
    else:
        print("Enter Amount in Multiples of 100")
else:
    print("Insufficient Balance")


#39
attendance = int(input())
marks = int(input())

if attendance >= 75:
    if marks >= 40:
        print("Pass")
    else:
        print("Fail")
else:
    print("Not Eligible Due to Attendance")

#40
account_type = input()
balance = int(input())

if account_type == "savings":
    if balance >= 1000:
        print("Minimum Balance Maintained")
    else:
        print("Minimum Balance Not Maintained")
else:
    print("Unsupported Account")

#41
amount = int(input())
payment = input()

if amount >= 500:
    if payment == "card":
        print("Card Payment Accepted")
    elif payment == "upi":
        print("UPI Payment Accepted")
    else:
        print("Unsupported Payment Method")
else:
    print("Minimum Order Amount Not Reached")


#42
year = int(input())
attendance = int(input())

if year == 2 or year == 3 or year == 4:
    if attendance >= 75:
        print("Room Eligible")
    else:
        print("Attendance Too Low")
else:
    print("Not Eligible by Year")

#43
plan = input()
usage = int(input())

if plan == "basic":
    if usage > 100:
        print("Recommend Upgrade")
    else:
        print("Basic Plan Is Sufficient")
else:
    print("Already on Higher Plan")

#44
a = int(input())
b = int(input())
c = int(input())

if a == b and b == c:
    print("All are Equal")
elif a >= b and a >= c:
    if a == b:
        print("A and B are Equal and Greatest")
    elif a == c:
        print("A and C are Equal and Greatest")
    else:
        print("A is Greatest")
elif b >= a and b >= c:
    if b == c:
        print("B and C are Equal and Greatest")
    else:
        print("B is Greatest")
else:
    print("C is Greatest")

#45
marks = int(input())
attendance = int(input())

if attendance >= 75:
    if marks >= 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 60:
        print("Grade C")
    elif marks >= 40:
        print("Grade D")
    else:
        print("Grade F")
else:
    print("Not Eligible")


#46
salary = int(input())
rating = int(input())

if salary >= 30000:
    if rating == 5:
        print("Bonus: 20%")
    elif rating == 4:
        print("Bonus: 15%")
    elif rating == 3:
        print("Bonus: 10%")
    else:
        print("Bonus: 5%")
else:
    print("Not Eligible for Bonus")

#47
age = int(input())
distance = int(input())

if age < 5:
    print("Free")
elif age >= 60:
    print("Senior")
else:
    if distance <= 10:
        print("Regular - Short Distance")
    else:
        print("Regular - Long Distance")



#48
stock = int(input())
status = input()

if stock > 0:
    if status == "paid":
        print("Order Confirmed")
    elif status == "pending":
        print("Payment Pending")
    else:
        print("Invalid Payment Status")
else:
    print("Out of Stock")


#49
age = int(input())
ticket = input()

if age < 5:
    print("Free Travel")
elif age >= 60:
    print("Senior Passenger")
else:
    if ticket == "AC":
        print("AC Ticket")
    elif ticket == "Sleeper":
        print("Sleeper Ticket")
    else:
        print("Invalid Ticket Type")

#50
choice = int(input())

match choice:
    case 1:
        print("Add")
    case 2:
        print("View")
    case 3:
        print("Update")
    case 4:
        print("Delete")
    case _:
        print("Invalid Choice")


#51
a = float(input())
b = float(input())
op = input()

match op:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        if b != 0:
            print(a / b)
        else:
            print("Cannot Divide by Zero")
    case _:
        print("Invalid Operator")

#52
a = float(input())
b = float(input())
op = input()

match op:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        if b != 0:
            print(a / b)
        else:
            print("Cannot Divide by Zero")
    case _:
        print("Invalid Operator")


#53
color = input()

match color:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case "green":
        print("Go")
    case _:
        print("Invalid Signal")

#54
grade = input()

match grade:
    case "A":
        print("Excellent Performance")
    case "B":
        print("Very Good Performance")
    case "C":
        print("Good Performance")
    case "D":
        print("Needs Improvement")
    case "F":
        print("Failed")
    case _:
        print("Invalid Grade")

#55
code = int(input())

match code:
    case 1:
        print("Check Balance")
    case 2:
        print("Recharge")
    case 3:
        print("Data Usage")
    case 4:
        print("Customer Support")
    case _:
        print("Invalid Service")


#56
month = int(input())

match month:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")
    case _:
        print("Invalid Month")


#57
ext = input()

match ext:
    case "py":
        print("Python File")
    case "txt":
        print("Text File")
    case "pdf":
        print("PDF File")
    case "jpg":
        print("Image File")
    case _:
        print("Unknown File Type")

#58
student_id = input()

parts = student_id.split("-")

degree = parts[0]
batch = parts[1]
branch = parts[2]
roll_number = parts[3]

if branch == "CSE":
    print("CSE Student")
else:
    print("Non-CSE Student")


#59
email = input()

parts = email.split("@")
domain = parts[1]

if domain == "gmail.com":
    print("Gmail User")
else:
    print("Other Email Provider")

#60
name = input()

parts = name.split()

username = parts[0] + "." + parts[2]

if "." in username:
    print("Valid Username Format")
else:
    print("Invalid Username Format")


#61
n = int(input())

if n < 10:
    print("One Digit")
elif n < 100:
    print("Two Digits")
elif n < 1000:
    print("Three Digits")
else:
    print("Four or More Digits")

#62
price = int(input())
quantity = int(input())

subtotal = price * quantity

if subtotal >= 5000:
    discount_percent = 20
elif subtotal >= 2000:
    discount_percent = 10
else:
    discount_percent = 0

discount = subtotal * discount_percent / 100
final_amount = subtotal - discount

print("Subtotal:", subtotal)
print("Discount:", str(discount_percent) + "%")
print("Final: {:.2f}".format(final_amount))

#63
units = int(input())

if units <= 100:
    rate = 5
elif units <= 300:
    rate = 7
else:
    rate = 10

bill = units * rate

print("Units:", units)
print("Rate: ₹" + str(rate))
print("Bill: ₹" + str(bill))


#64
balance = 10000

print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")

choice = int(input())

match choice:
    case 1:
        print("Balance:", balance)

    case 2:
        amount = int(input())
        balance = balance + amount
        print("Deposit Successful")
        print("Balance:", balance)

    case 3:
        amount = int(input())

        if amount <= balance:
            balance = balance - amount
            print("Withdrawal Successful")
            print("Balance:", balance)
        else:
            print("Insufficient Balance")

    case 4:
        print("Exit")

    case _:
        print("Invalid Choice")


#65
choice = int(input())
quantity = int(input())

match choice:
    case 1:
        price = 250
    case 2:
        price = 150
    case 3:
        price = 200
    case 4:
        price = 120
    case _:
        price = 0
        print("Invalid Choice")

if price > 0:
    total = price * quantity

    if total >= 500:
        discount = total * 10 / 100
    else:
        discount = 0

    final_amount = total - discount

    print("Total:", total)
    print("Discount: {:.2f}".format(discount))
    print("Final: {:.2f}".format(final_amount))


#66
m1 = int(input())
m2 = int(input())
m3 = int(input())
attendance = int(input())

total = m1 + m2 + m3
average = total / 3

print("Total:", total)
print("Average: {:.2f}".format(average))

if attendance >= 75:
    if average >= 90:
        print("Outstanding")
    elif average >= 75:
        print("Very Good")
    elif average >= 60:
        print("Good")
    elif average >= 40:
        print("Pass")
    else:
        print("Fail")
else:
    print("Not Eligible")


#67
distance = int(input())
ride_type = input()

match ride_type:
    case "normal":
        rate = 15
    case "premium":
        rate = 25
    case _:
        rate = 0
        print("Invalid Ride Type")

if rate > 0:
    fare = distance * rate

    if distance > 20:
        fare = fare + fare * 10 / 100

    print("Fare: {:.2f}".format(fare))

#68
score = int(input())
percentage = int(input())
category = input()

match category:
    case "general":
        if score >= 80:
            if percentage >= 75:
                print("Admission Eligible")
            else:
                print("Admission Not Eligible")
        else:
            print("Admission Not Eligible")

    case "obc":
        if score >= 70:
            if percentage >= 70:
                print("Admission Eligible")
            else:
                print("Admission Not Eligible")
        else:
            print("Admission Not Eligible")

    case "sc":
        if score >= 60:
            if percentage >= 60:
                print("Admission Eligible")
            else:
                print("Admission Not Eligible")
        else:
            print("Admission Not Eligible")

    case _:
        print("Invalid Category")

#69
age = int(input("Enter age: "))

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")


#70
marks = int(input("Enter marks: "))

if marks >= 40:
    if marks >= 90:
        print("A")
    elif marks >= 75:
        print("B")
    else:
        print("Pass")
else:
    print("Fail")


    #71

marks = 85

if marks >= 40:
    print("Pass")
elif marks >= 75:
    print("Very Good")
else:
    print("Fail")

#72
#Marks	Output
95	A
85	B
50	Pass
30	Fail

#73





#75
#Marks	Attendance	Output
82	80	Grade B
92	80	Grade A
55	80	Pass
92	60	Not Eligible
