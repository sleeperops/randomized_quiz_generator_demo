# Directory of the file that stores all formatted question
question_directory = r"C:\Users\Pau\Desktop\Computer Engineering notes and more\OOP_Materials\randomized_quiz_generator_demo\questions\questions"

# Runs a loop and accepts input until the user decides to exit
while True: 

    # Accepts the input for the question
    input_question = input("Enter a question: ")
    with open(question_directory, "a") as question_file:  # Writes the question into the file
        question_file.write(f'''{input_question}
''')
    print(input_question)

    # Accepts the input for the options   
    input_options = {"a":"", "b":"", "c":"", "d":""}
    for char in input_options:  # Loops through the options and sets a value for each
        input_options[char] = input(f"Enter option {char}: ")

    with open(question_directory, "a") as question_file:  # Writes the option into the file
        question_file.write(f'''{input_options}
''')
    print(input_options)


    # Accepts the input for the correct answer
    input_answer = input("Enter the letter of the correct answer: ")
    with open(question_directory, "a") as question_file:  # Writes the correct answer into the file
        question_file.write(f'''{input_answer}
''')

    # Gives user the ability to exit or continue the loop
    user_option = input("Do you wish to continue? (any key to continue and // to exit): ")
    if user_option == "//":
        break

print(input_question)
print(input_options)
print(input_answer)