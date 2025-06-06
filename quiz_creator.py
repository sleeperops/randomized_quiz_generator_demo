# Directory of the quiz file that stores all formatted questions
quiz_directory = r"quizzes/questions.txt"

#question_id_tracker = 0

# def generate_id(file_directory):
#     """
#     Accepts no arguments and generates a designated number for each question
#     """
#     global question_id_tracker

#     question_id_tracker += 1  # Increments one value to the question_id_tracker every time the function is called
#     with open(file_directory, "a") as fd:
#         fd.write(f'''
# {question_id_tracker}
# ''')  # Remove

def write_question(input_question, file_directory):
    """
    Accepts a question and writes it into a specified file
    """
    with open(file_directory, "a") as fd:  # Writes the question into the specified file
        fd.write(f'''Q: {input_question}
''')

def write_option(file_directory):
    """
    Asks for the options and writes it into a specified file
    """
    with open(file_directory, "a") as fd:
        for char in "abcd":  # Creates a block of string with that contains the options
            option = input(f"Option {char}: ")
            fd.write(f'''{option}
''')


def write_correct(input_answer, file_directory):
    """
    Accepts and writes the correct answer into the specified file
    """
    with open(file_directory, "a") as question_file:  # Writes the correct answer into the file
        question_file.write(f'''A: {input_answer}
''')
    
# Runs a loop; accepts and writes the inputs until the user decides to exit
while True: 
    # Accepts the input for the question
    input_question = input("Enter a question: ")

    # # Generate the question_id
    # generate_id(quiz_directory)

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

#print(question_id_tracker)
