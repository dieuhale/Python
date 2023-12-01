# Prompt the user to input a list of student heights
student_heights = input("Enter student heights separated by space: ").split()
# Split the input string into a list of strings, where each string is a height

# Initialize total_height to accumulate the sum of all heights
total_height = 0
# Initialize number_of_students to count the number of students
number_of_students = 0

# Iterate over each height in the student_heights list
for height in student_heights:
    total_height += int(height)  # Add the current height (converted to integer) to total_height
    number_of_students += 1  # Increment the count of students by 1

# Calculate the average height by dividing total height by number of students
# round() is used to round the result to the nearest whole number
average_height = round(total_height / number_of_students)

# Print the total height, number of students, and average height
print(f"total height = {total_height}")
print(f"number of students = {number_of_students}")
print(f"average height = {average_height}")








