# Formatting again again
# Brayden Towner
# 11/02/2023

import os

exercise_int=1

# Just to keep it in one file, I'll use headers and cls to clarify exercises.
# This code repeats a lot
def next_exercise(exercise_name):
    # It tries to grab the local variable with this name which doesn't exist...
    # I knew of this keyword already
    global exercise_int
    # Only pause pre-exercise if this isn't the first
    if exercise_int > 1:
        os.system("pause")
    os.system("cls")
    print(f"Exercise {exercise_int}: {exercise_name}\n")
    exercise_int+=1

"""
    Intended to run after an exercise. It pauses the program, adds one to the exercise number, and displays the header

    Args:
        exercise_name (string): What the header should say
"""
next_exercise("Calm, cool, collected")

total_lie = "I LOVE PEOPLE"

print(total_lie.lower())

next_exercise("HAYDEN!!")

hayden_string = "Hayden"

# Concatenation using multiple methods
print("Concat:")
print(hayden_string + " " + " ".join([hayden_string, hayden_string])+" "+hayden_string)

print("Multiply:")
print((hayden_string + ' ')*4)

next_exercise("Huh? -------- Huh?")

questions = "Where now? Who now? When now?"
questions_array = questions.split("? ")

for i in range(len(questions_array)-1):
    questions_array[i]+="?"
for i in range(len(questions_array)):
    print(questions_array[i])
