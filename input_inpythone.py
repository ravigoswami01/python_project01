# user_name = input()

# print("Hello, " + user_name + "!")



# intput string conveted  in to number 

# num = int(input("Enter a number: "))

# print("You entered:", num)
student_name = input("Enter student name: ")

math_marks = int(input("Enter Math marks: "))
hindi_marks = int(input("Enter Hindi marks: "))
english_marks = int(input("Enter English marks: "))

total = math_marks + hindi_marks + english_marks
percentage = total / 3

print("\nStudent Name:", student_name)
print("Math Marks:", math_marks)
print("Hindi Marks:", hindi_marks)
print("English Marks:", english_marks)
print("Total Marks:", total)
print("Percentage:", percentage)