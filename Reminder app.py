import time
import win32com.client as w
def Duration():
    while True:
        try:
            Minutes=int(input("After how many minutes you want to get reminded? : "))
            Minutes*=60
            print(f"Reminder set for {Minutes//60} minutes. Waiting...")
            time.sleep(Minutes)
            break
        except ValueError:
            print("Please enter a valid value!")
def reminder():
    Sound=w.Dispatch("SAPI.SpVoice")
    Reminding=input("For what you want to be reminded for? :")
    try:
        Repeat=int(input("How many times you want it to repeat? : "))
    except ValueError:
        print("Wrong input! Repeat is set to 1")
        Repeat=1
    try:
        Snooze=int(input("Snooze for how many seconds? : "))
    except ValueError:
        print("Wrong Input! The snooze is set to 1")
        Snooze=1
    if Repeat <= 0:
        Repeat = 1
    if Snooze <= 0:
        Snooze = 1
    Duration()
    for i in range(Repeat):
        Sound.Speak(Reminding)
        time.sleep(Snooze)
def Use():
    while True:
        User=input("Do you want to use reminder app ? YES/NO : ")
        if User.strip().lower()=="yes":
            reminder()
        else:
            print("Thanks for using Reminder app")
            break
Use()