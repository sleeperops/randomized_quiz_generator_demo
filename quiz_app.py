# Leads to the directory of the file
quiz_directory = r"quizes/questions.txt"

question_list = []

def read_quiz(file_directory):
    with open(file_directory, "r") as quiz:
        temp_questions_lines = quiz.readlines()  # Stores each line of the quiz file to a temp list
        questions_lines = []  # Stores the cleaned lines into the true list

        for line in temp_questions_lines: 
            line = str(line)  
            if line == "///":  
                continue
            else:
                questions_lines.append(line.strip())  

    return questions_lines  

read_quiz(quiz_directory) # returns a list

