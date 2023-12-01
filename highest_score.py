# Input a list of student scores
student_scores = input().split()  # Take input from the user and split it into a list based on spaces

# Convert each element of the list from string to integer
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])  # Convert each score from string to integer

# Write your code below this row 👇
highest_score = student_scores[0]  # Initialize the highest_score with the first element of student_scores

# Iterate over each score in the student_scores list
for score in student_scores:
    if score > highest_score:  # Check if the current score is greater than the current highest_score
        highest_score = score  # Update highest_score with the current score if it's higher

# Print the highest score found in the list
print(f"The highest score in the class is: {highest_score}")  # Use f-string to format and print the highest score
