import phonenumbers
from phonenumbers import geocoder, carrier

x = phonenumbers.parse("+14698319568", None)

caller_loc = geocoder.description_for_number(x, "us")
caller_carrier = carrier.name_for_number(x, "en")

print(caller_loc)
print(caller_carrier)
