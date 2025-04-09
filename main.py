# Runs a loop and accepts input until the user decides to exit
while True: 

    # Accepts the input for the question
    input_question = input("Enter a question or '//' to exist: ")

    # Accepts the input for the options   
    input_options = {"a":"", "b":"", "c":"", "d":""}
    for char in 'abcd':
        input_options[char] == input(f"Enter option {char}: ")
    
    # Accepts the input for the correct answer
    input_answer = input("Enter the letter of the correct answer: ")

    # Gives user the ability to exit or continue the loop
    user_option = input("Do you wish to continue? (any key to continue and // to exit): ")
    if user_option == "//":
        break

print(input_question)
print(input_options)
print(input_answer)