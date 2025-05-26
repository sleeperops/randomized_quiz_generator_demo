# Rename class 'Question' into 'Item'

# Leads to the directory of the file
quiz_directory = r"quizes/questions.txt"
lines_list = []  # Stores each lines extracted from the quiz file

class Question:

    def __init__(self, question, option_a, option_b, option_c, option_d, correct_answer):
        self.question = question
        self.option_a = option_a
        self.option_b = option_b
        self.option_c = option_c
        self.option_d = option_d
        self.correct_answer = correct_answer

def read_quiz(file_directory):
    """
    Reads the quiz file and extracts each questions into a list
    Accepts the file directory of the quiz file and returns a list with all the questions
    """
    
    # Uses a context manager to open automatically close the file once the lines have been extracted
    with open(file_directory, "r") as quiz:
        temp_lines_list = quiz.readlines()  # Stores each lines of the quiz file to a temporary list before stripping      
        
        # Loops through the entire list and removes the /n in each line that is in that list
        for line in temp_lines_list: 
            line = str(line)  # Converts the lines into a string so that the strip method could be applied
            if line == "///":  
                continue
            else:
                lines_list.append(line.strip())  

    return lines_list  

def read_and_repack(lines_list):
    """
    Extracts each lines from the line_list and uses it to create an instance of the class named 'Question'.
    Accepts a list of lines that is read from the questions.txt file.
    Returns a list of instances of the class 'Questions'. 
    """
    quiz_items = []  # A list of objects (referred to as items) of the class 'Question'. The lines from line_list are passed as properties of these items
   
    for index, lines in lines_list:  # Loop through 'line_list' using the 'lines' variable to track the current line and 'index' to track its index
        if str(lines).startswith("Q:") == True:  # If the line starts with the 'Q:' prefix, construct an instance of the class 'Question' with the following properties:
            option_a = lines_list[index + 1]
            option_b = lines_list[index + 2]
            option_c = lines_list[index + 3]
            option_d = lines_list[index + 4]
            correct_answer = lines_list[index + 5]

            question_item = Question(lines, option_a, option_b, option_c, option_d, correct_answer)  # Construct an item
            quiz_items.append(question_item)  # Store the item into a list

    return quiz_items

print(read_and_repack(lines_list))






# print(read_quiz(quiz_directory))  # returns a list

