import csv

compromised_users = []

with open("passwords.csv") as password_file:
    password_csv = csv.DictReader(password_file)
    password_row = []
    for password_row in password_csv:
        print(password_row["Username"])