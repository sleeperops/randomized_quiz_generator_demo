# Check for spelling errors

# Read quiz has to run first and set a value for line list before you can use extract and repack

# Leads to the directory of the file
quiz_directory = r"quizes/questions.txt"

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

# Testing Section-------------------------------------------------
quiz_lines_list = read_quiz(quiz_directory)
quiz_items_list = extract_and_repack(quiz_lines_list)

print(f"""LINES LIST: 
      {quiz_lines_list}
""")
print(f"""REPACKED LINES LIST:
       {quiz_items_list}
""")
print((quiz_items_list[1].option_a))
