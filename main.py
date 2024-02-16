import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from tkinter import *


def find_user():
    number = user_input.get()

    parsed_number = phonenumbers.parse(number, "US")

    if phonenumbers.is_possible_number(parsed_number):
        if phonenumbers.is_valid_number(parsed_number):
            caller_location = geocoder.description_for_number(
                parsed_number, "en")
            caller_carrier = carrier.name_for_number(parsed_number, "en")
            caller_timezone = timezone.time_zones_for_number(parsed_number)
        else:
            print("NPA 200 not used")
    else:
        print("invalid number")

    output.config(
        text=f"Location: {caller_location}\nPhone Carrier: {caller_carrier}\nTime Zone: {caller_timezone}")


# UI ----------------------------

window = Tk()
window.title("Phone Number Locator")
window.minsize(width=500, height=500)
window.config(padx=50, pady=50)

title = Label(text="Enter Phone Number:")
title.grid(column=1, row=0)

user_input = Entry(width=20)
user_input.grid(column=2, row=0)

button = Button(text="Search", command=find_user)
button.grid(column=2, row=2)

output = Label(text=f"")
output.grid(column=2, row=3)


window.mainloop()
