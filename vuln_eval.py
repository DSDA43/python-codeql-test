# Vulnerable code using eval() with simulated user input
def insecure_eval():
    user_input = input("Enter something: ")
    eval(user_input)

insecure_eval()
