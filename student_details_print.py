name = input("enter your name:")
age = int(input("enter your age:"))
student_class = input("enter your class:")
marks = float(input("enter your marks:"))

total_marks = 500

percentage = (marks / total_marks)* 100

print("hello", name)
print("you are", age, "years old")
print("you are in", student_class)
print("you got", marks)
print("total percentage", percentage)

