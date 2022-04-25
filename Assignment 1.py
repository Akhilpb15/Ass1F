# QUESTION 1
print("This program can calculate avg of three numbers")

n1=float(input("Enter the 1st number:- "))
n2=float(input("Enter the 2nd number:- "))
n3=float(input("Enter the 3rd number:- "))
AVERAGE=(n1 + n2 + n3) / 3
#as avg of a number of 

print("The Average of three given numbers is: " , AVERAGE)

print("*-:::::::::::::::::::::::-")

#QUESTION 2
print("PYTHON PROGRAM TO CALCULATE THE INCOME TAX OF PERSON AFTER SEVERAL DEDUCTION OF MONEY (GROSS INCOME>$25000)")
gross_income=int(input("Please Enter the Gross Income:$ "))
numberofdependents=int(input("Please Enter the number of dependents: "))
#deduction1=Standard Deduction
deduction1=10000
#deduction2=Dependent Deduction
deduction2=int(3000*numberofdependents)
Taxable_income=int(gross_income)-int(deduction1)-int(deduction2)
Tax=.20*Taxable_income
 
print("The total income tax of a person in $: " , Tax)


print("*")


print("-:::::::::::::::::::::::-")


#QUESTION 3

Student = []
print("Enter the SID: ")
SID = int(input())
print("Enter the name of the student: ")
Name = input()
print("Enter the gender of the student:")
Gender = input()
print("Enter your Course Name:")
Course = input()
print("Enter the CGPA of the student:")
CGPA = float(input())
Student.append(SID)
Student.append(Name)
Student.append(Gender)
Student.append(Course)
Student.append(CGPA)
print(Student)



print("-:::::::::::::::::::::::-")


#QUESTION 4
print("This python program can be use to enter marks of 5 students")
list=[]
#first we take input and then use append to display the marks
s_marks_1=int(input("Enter the Marks of First Student:"))
s_marks_2=int(input("Enter the Marks of Second Student: "))
s_marks_3=int(input("Enter the Marks of Third Student: "))
s_marks_4=int(input("Enter the Marks of Fourth Student: "))
s_marks_5=int(input("Enter the Marks of Fifth Student: "))
list=[s_marks_1,s_marks_2,s_marks_3,s_marks_4,s_marks_5]
print("The List of marks of five student is as follows: " ,list)
list.sort()
print("The List of marks of five students in a sorted manner: ",list)

print("*-::::::::::::::-*")


#QUESTION 5
# replacing 'Black' and 'Pink' with 'Purple'
color2 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color2[3:5] = ['Purple']
print("The modified list is color 2 =", color2)
