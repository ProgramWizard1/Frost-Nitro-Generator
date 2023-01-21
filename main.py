import requests
import random
import string
import time

print(""" Frost - Nitro Generator / 
 """)

time.sleep(2)
print("Made by CasuallyD1scord")
time.sleep(0.3)
print("Thanks for using this generator!")
time.sleep(0.3)
print("Join our server: https://discord.gg/5hhqdyvqqm")
time.sleep(0.3)
print(" ")
time.sleep(0.2)

num = int(input('Input how many codes to generate: '))

with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
    print("Your nitro codes are being generated, be patient if you entered the high number!")

    start = time.time()

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.gift/{code}\n")

    print(f"Generated {num} codes | Time taken: {time.time() - start}\n")

with open("Nitro Codes.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f" Valid | {nitro} ")
            break
        else:
            print(f" Invalid | {nitro} ")



print("\n Finished generating. Please see Valid Codes.txt to see if there are any valid codes. If there are none, try again.")
