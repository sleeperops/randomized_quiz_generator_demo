# Directory of the quiz file that stores all formatted questions
quiz_directory = r"C:\Users\Pau\Desktop\Computer Engineering notes and more\OOP_Materials\randomized_quiz_generator_demo\questions\questions"

def write_question(input_question, file_directory):
    """
    Accepts a question and writes it into a specified file
    """
    with open(file_directory, "a") as fd:  # Writes the question into the specified file
        fd.write(f'''{input_question}
''')

def write_option(file_directory):
    """
    Asks for and writes the options into a specified file
    """
    option_block = ""
    for char in "abcd":  # Creates a block of string with that contains the options
        option = input(f"Option {char}: ")
        option_block += f'''{char}). {option}
'''
    with open(file_directory) as fd:  # Writes that block of string into the file
        fd.write(option_block)

def write_correct(input_answer, file_directory):
    """
    Accepts and writes the correct answer into the specified file
    """
    with open(file_directory, "a") as question_file:  # Writes the correct answer into the file
        question_file.write(f'''{input_answer}
''')
    
# Runs a loop; accepts and writes the inputs until the user decides to exit
while True: 
    # Accepts the input for the question
    input_question = input("Enter a question: ")

    # Writes the input into a specified quiz file
    write_question(input_question,quiz_directory)

    # Accepts the input for the options and writes it into the specified quiz file at the same time
    write_option(quiz_directory)
        
    # Accepts the input for the correct answer
    input_answer = input("Enter the letter of the correct answer: ")
    
    # Writes the input for the correct answer
    write_correct(input_answer, quiz_directory)

    # Gives user the ability to exit or continue the loop
    user_option = input("Do you wish to continue? (any key to continue and // to exit): ")
    if user_option == "//":
        break

