helloIntent = ["hi","hello","hey","hi there","hello there","hey there"]

# Membership Operator - in, not in
# Identity Operator - is, not is

chat = True
while chat:
    msg = input("Enter your message : ")
    msg = msg.lower()
    if msg in helloIntent:
        print("Hi There...")
    elif msg == "bye":
        print("Bye...")
        chat = False
    else:
        print("I don't understand")
