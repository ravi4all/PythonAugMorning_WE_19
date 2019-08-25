#Logical Operator - and, or, not

while True:
    msg = input("Enter your message : ")
    msg = msg.lower()
    if msg == "hello" or msg == "hi" or msg == "hey":
        print("Hi There...")
    elif msg == "bye":
        print("Bye...")
        break
    else:
        print("I don't understand")
