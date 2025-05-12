# Initialize class item_question
# Intitialize 'question', 'options', and 'correct' as properties of that class
# Initialize 'question_list'
# Read each line from 'quiz.txt' and group each question, options and correct answers
#     into variables, then store them into 'question_list'.
# Use random package to select a random question from the list.
# Ask the user a question until they exit.
# Count the number of times they generated a question 
# Count the number of times they met the correct answer
# Calculate the difference and display the result

# Leads to the directory of the file
quiz_directory = r"quizes/questions.txt"

# Defines the the properties of each question
class itemQuestion:
    
    def __init__(self, question, option, correct):
        self.question = question
        self.option = option
        self.correct = correct

question_list = []

# Reads each the quiz.txt and stores each lines into a list called "questions_lines"
def read_quiz(file_directory):
    with open(file_directory, "r") as quiz:
        questions_lines = quiz.readlines()  # Stores each line of the quiz into a list

    return questions_lines  #!! see this question
print(read_quiz(quiz_directory))

# write each lines to a list
# if the variable starts with a q, write it as a question
# if it starts with an A, write it as the answer, 
# if it starts with a ///, skip
# otherwise write it as an option
# wrap up the variable and put it on the questions list