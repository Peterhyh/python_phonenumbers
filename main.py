import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from opencage.geocoder import

number = "213 244 1430"

parsed_number = phonenumbers.parse(number, "US")

if phonenumbers.is_possible_number(parsed_number):
    if phonenumbers.is_valid_number(parsed_number):
        caller_location = geocoder.description_for_number(parsed_number, "en")
        caller_carrier = carrier.name_for_number(parsed_number, "en")
        caller_timezone = timezone.time_zones_for_number(parsed_number)
        print(parsed_number)
        print(caller_location)
        print(caller_carrier)
        print(caller_timezone)
    else:
        print("NPA 200 not used")
else:
    print("invalid number")
