import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from tkinter import *


def find_user():
    error.config(text="")
    number = user_input.get()

    parsed_number = phonenumbers.parse(number, "US")

    if phonenumbers.is_possible_number(parsed_number):
        if phonenumbers.is_valid_number(parsed_number):
            caller_location = geocoder.description_for_number(
                parsed_number, "en")
            caller_carrier = carrier.name_for_number(parsed_number, "en")
            caller_timezone = timezone.time_zones_for_number(parsed_number)
            location.config(text=f"Location: {caller_location}")
            phone_timezone.config(text=f"Time Zone: {caller_timezone}")
            if caller_carrier == "":
                phone_carrier.config(text=f"Phone Carrier: N/A")
            else:
                phone_carrier.config(text=f"Phone Carrier: {caller_carrier}")
        else:
            error.config(text="NPA 200 not used")
            location.config(text="")
            phone_carrier.config(text="")
            phone_timezone.config(text="")
    else:
        error.config(text="Invalid Number")
        location.config(text="")
        phone_carrier.config(text="")
        phone_timezone.config(text="")


# UI ----------------------------
window = Tk()
window.title("Phone Number Locator")
window.minsize(width=500, height=500)
window.config(padx=50, pady=50)

title = Label(text="Enter Phone Number:")
title.grid(column=1, row=0)

user_input = Entry(width=20)
user_input.grid(column=2, row=0)

output = Label(text=f"")
output.grid(column=2, row=3)

location = Label(text="Location: --")
location.grid(column=2, row=5)

phone_carrier = Label(text="Phone Carrier: --")
phone_carrier.grid(column=2, row=6)

phone_timezone = Label(text="Time Zone: --")
phone_timezone.grid(column=2, row=7)

error = Label(text="")
error.grid(column=2, row=4)

button = Button(text="Search", command=find_user)
button.grid(column=2, row=2)

window.mainloop()
