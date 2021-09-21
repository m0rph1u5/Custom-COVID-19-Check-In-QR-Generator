# Custom COVID-19 Check-In : QR Generator
import qrcode
from PIL import Image
print("Custom COVID-19 Check-In : QR Generator \n***USE AT OWN RISK***")

# Input
location = str(input("Enter a Location"))
locat = location.replace(" ", "+")
checkin = ("https://checkin.covid-19.sa.gov.au/?businessName="+ (locat) +"&planId=000000000000000000000000")

# Combination

print("https://checkin.covid-19.sa.gov.au/?businessName="+ (locat) +"&planId=000000000000000000000000")

end = input("\nWould you like to Generate a QR Code? Y/N ")
if end == "y":
    img = qrcode.make(checkin)
    img.save((location) + ".png")
if end == "n":
    print("\n\nProgram terminated")


