from datetime import datetime
import webbrowser

helloIntent = ["hi","hello","hey","hi there","hello there","hey there"]
timeIntent = ["tell me time","time please","time","what's the time"]
dateIntent = ["tell me date","date please","date","what's the date today"]

chat = True
while chat:
    msg = input("Enter your message : ")
    msg = msg.lower()
    if msg in helloIntent:
        print("Hi There...")
    elif msg in dateIntent:
        date = datetime.now().date()
        print(date.strftime("%d/%m/%y,%a"))
    elif msg in timeIntent:
        time = datetime.now().time()
        print(time.strftime("%H/%M/%S,%p"))
    elif msg.startswith("open"):
        web = msg.split()[1]
        webbrowser.open(web+'.com')
    elif msg == "bye":
        print("Bye...")
        chat = False
    else:
        print("I don't understand")
