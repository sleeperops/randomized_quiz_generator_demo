# Check for spelling errors

# Read quiz has to run first and set a value for line list before you can use extract and repack

# Leads to the directory of the file
import random

quiz_directory = r"quizzes/questions.txt"

class Item:

    def __init__(self, question, option_a, option_b, option_c, option_d, correct_answer):
        self.question = question
        self.option_a = option_a
        self.option_b = option_b
        self.option_c = option_c
        self.option_d = option_d
        self.correct_answer = correct_answer

def read_quiz(file_directory):
    """
    Reads the quiz.txt file and extracts each questions into a list
    Accepts the file directory of the quiz.txt and returns a list with all the questions
    """
    
    # Stores each lines extracted from the quiz.txt
    lines_list = []  

    # Use a context manager to open and automatically close the file once the lines have been extracted
    with open(file_directory, "r") as quiz:
        temp_lines_list = quiz.readlines()  # Stores each lines of the quiz.txt file to a temporary list before stripping      
        
        # Loops through the entire list and removes the /n in each line that is in that list
        for line in temp_lines_list: 
            line = str(line)  # Converts the lines into a string so that the strip method could be applied
            if line == "///":  
                continue
            else:
                lines_list.append(line.strip())  

    return lines_list  

def extract_and_repack(lines_list):
    """
    Extracts each lines from the line_list and uses it to create an instance of the class named 'Item'.
    Accepts a list of lines that is read from the questions.txt file.
    Returns a list of instances of the class 'Item'. 
    """

    # A list of objects (referred to as items) of the class 'Item'. The lines from line_list are passed as properties of these items
    quiz_dict = {}

    # Assign each item a number as a form of identifier.
    counter = 1

    # Loop through 'line_list' using the 'lines' variable to track the current line and 'index' to track its index
    for index, lines in enumerate(lines_list):  
        if str(lines).startswith("Q:") == True:  # If the line starts with the 'Q:' prefix, construct an instance of the class 'Item' with the following properties:
            question = lines
            option_a = lines_list[index + 1]
            option_b = lines_list[index + 2]
            option_c = lines_list[index + 3]
            option_d = lines_list[index + 4]
            correct_answer = lines_list[index + 5]

            # Construct an instance of the class 'Item' using the above lines as properties
            question_item = Item(question, option_a, option_b, option_c, option_d, correct_answer) 

            # Store each item in a dictionary using the property 'question' as the key and the item itself as the value
            quiz_dict[counter] = question_item 

            # Increments by 1 for every loop
            counter += 1

    return quiz_dict

def shuffle(min,max):
    """
    Creates a list of numbers in a random order. 
    Accepts a minimum and maximum number and returns a randomly ordered list of numbers in that range.
    """
    # A list of randomly ordered numbers
    shuffled_sequence = []

    while len(shuffled_sequence) != max:  # Loop until the amount of numbers in the list matches the length of the range
        random_num = random.randint(min, max)  # Generate a random number in the specified range
        if random_num not in shuffled_sequence:  # If the random number is not yet in the list
            shuffled_sequence.append(random_num)  # Add it to the list

    return shuffled_sequence
    
# UI ----------------------
def display_question(question_dict, question_index):
    """
    Displays the item in a questionnaire format.
    Accepts the dictionary from where the item belongs(question_dict) and the key that corresponds to that item
    Returns the item in a question-options format
    """
    return f"""
{question_dict[question_index].question}
{question_dict[question_index].option_a}
{question_dict[question_index].option_b}
{question_dict[question_index].option_c}
{question_dict[question_index].option_d}
"""

def score_count(result_summary):
    """
    Evaluates the amount of correct answer from a result summary
    Accepts the result summary dictionary of a quiz
    Returns the number of correct answers in a result summary
    """
    true_count = 0
    for key in result_summary:  # Loop through results of the summary
        if result_summary[key] == True:  # If an item has a value of True
            true_count += 1  # Increment the counter by one
    return true_count 

# UI ----------------------
# Initialization
quiz_lines_list = read_quiz(quiz_directory)
quiz_items_dict = extract_and_repack(quiz_lines_list)  # List of questions/items


# Header ------------------
print("Welcome to the Quiz app")
print("")

# Program Loop ------------
while True:

    # Initialize randomize_index. Stores a random sequence of numbers based on the range of the given dictionary.
    randomized_index = shuffle(1, len(quiz_items_dict))

    # Initialize quiz_result_summary dictionary. Records the finished items along with the results.
    quiz_result_summary = {}

    # Asks the user for permission to start the test
    input_start_option = input("Start the test? (any key to start, x to exit): ")

    if input_start_option.lower() == "x": 
        break

    else:

        # Pick a random question from the question dictionary (quiz_item_dict)
        for index in randomized_index:

            # Print the question in a question-options format
            print(display_question(quiz_items_dict,index)) 

            # Request for an answer 
            input_answer = input("Answer: ")  

            # Tells whether the input answer is correct (True) or incorrect (False)
            answer_state = None 

            # If the input answer is the same as the correct answer
            if f"A: {input_answer.lower()}" == quiz_items_dict[index].correct_answer:  
                answer_state = True  # Mark the answer as True, indicating that the answer is correct

            # If it is not
            else:
                answer_state = False  # Mark as false, indicating that it is incorrect

            # Record the answer in a dictionary. Use the question's index as the key and it's state as the value
            quiz_result_summary[index] = answer_state

    print(quiz_result_summary)

    # Prints the score over the total number of items
    print(f" Total Score: {score_count(quiz_result_summary)}/{len(quiz_items_dict)}")