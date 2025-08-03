# Vulnerable code using eval()
def insecure_eval(user_input):
    eval(user_input)

insecure_eval("print('hello from eval')")
