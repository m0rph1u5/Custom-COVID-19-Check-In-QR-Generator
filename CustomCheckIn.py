# Custom COVID-19 Check-In : QR Generator

import replit
import time
import qrcode
from PIL import Image

def welcome():
    choice = 0
    while choice <= 3:
        print("\nCustom COVID-19 Check-In & QR Generator")

        try:
            print("\n1. Generate Check-In Link \n2. Generate Check-In QR \n3. Exit ")
            choice = int(input("\nSelect Generator: "))

            if choice == 1:
                location = str(input("Enter a Location"))
                locat = location.replace(" ", "+")
                checkin = ("https://checkin.covid-19.sa.gov.au/?businessName=" + (
                    locat) + "&planId=000000000000000000000000")

                # Combination

                print(
                    "https://checkin.covid-19.sa.gov.au/?businessName=" + (locat) + "&planId=000000000000000000000000")

            elif choice == 2:
                location = str(input("Enter a Location"))
                locat = location.replace(" ", "+")
                checkin = ("https://checkin.covid-19.sa.gov.au/?businessName=" + (
                locat) + "&planId=000000000000000000000000")

                # Combination

                print("https://checkin.covid-19.sa.gov.au/?businessName=" + (locat) + "&planId=000000000000000000000000")
                img = qrcode.make(checkin)
                img.save((location) + ".png")

            elif choice == 3:
                replit.clear()
                print("\n\nProgram terminated")
                return
            else:
                print("\nWrong selection, please choose options 1-3")
                time.sleep(2)
                replit.clear()
                welcome()

            end = input("\nWould you like to continue Y/N ")
            if end == "y":
                replit.clear()
            if end == "n":
                replit.clear()
                print("\n\nProgram terminated")
                return
            elif end == "3":
                replit.clear()
                print("\n\nProgram terminated")
                return

        except ValueError:
            print("\nPlease enter a number!")
            time.sleep(1)
            replit.clear()


welcome()
