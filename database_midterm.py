# Create an idea for a database to use
# Create a module that showcases database based off user input

import sys
sys.path.append(r"C:\Users\HP\PycharmProjects\Midterm-Project")

import csv
smash = r"C:\Users\HP\PycharmProjects\Midterm-Project\Midterm Database.csv"

def show_all(csv_path):
    with open(csv_path, newline='', encoding='cp1252') as database:
        reader = csv.DictReader(database)
        for row in reader:
            print(row)

show_all(smash)

def search(csv_path):
    method = input("Enter search method (number, name, series, tier):").strip().lower()
    if method == 'name':
        def search_by_name(csv_path):
            name = input("Enter character name:").strip().lower()
            with open(csv_path, newline='', encoding='cp1252') as database:
                reader = csv.DictReader(database)
                found = False
                for row in reader:
                    if row['Name'].strip().lower() == name:
                        print(row)
                        found = True
                if not found:
                    print("None found.")
                    search(smash)
        search_by_name(smash)
    elif method == 'number':
        def search_by_number(csv_path):
            number = input("Enter character number:").strip().lower()
            with open(csv_path, newline='', encoding='cp1252') as database:
                reader = csv.DictReader(database)
                found = False
                for row in reader:
                    if row['Number'].strip().lower() == number:
                        print(row)
                        found = True
                if not found:
                    print("None found.")
                    search(smash)
        search_by_number(smash)
    elif method == 'series':
        def search_by_series(csv_path):
            series = input("Enter series:").strip().lower()
            with open(csv_path, newline='', encoding='cp1252') as database:
                reader = csv.DictReader(database)
                found = False
                for row in reader:
                    if row['Series'].strip().lower() == series:
                        print(row)
                        found = True
                if not found:
                    print("None found.")
                    search(smash)
        search_by_series(smash)
    elif method == 'tier':
        def search_by_tier(csv_path):
            tier = input("Enter tier:").strip().lower()
            with open(csv_path, newline='', encoding='cp1252') as database:
                reader = csv.DictReader(database)
                found = False
                for row in reader:
                    if row['Tier'].strip().lower() == tier:
                        print(row)
                        found = True
                if not found:
                    print("None found.")
                    search(smash)
        search_by_tier(smash)
    else:
        print("Invalid method. Please enter Number, Name, Series, or Tier")
        search(smash)

def organize(csv_path):
    method = input("Enter organization method (number, name, series, tier):").strip().lower()
    if method == 'name':
        def organize_by_name(csv_path):
            with open(csv_path, newline='', encoding='cp1252') as database:
                reader = csv.DictReader(database)
                rows = list(reader)
                sorted_rows = sorted(rows, key=lambda row: row['Name'].strip().lower())
                for row in sorted_rows:
                    print(row)
        organize_by_name(smash)
    elif method == 'number':
        def organize_by_number(csv_path):
            with open(csv_path, newline='', encoding='cp1252') as database:
                reader = csv.DictReader(database)
                rows = list(reader)
                sorted_rows = sorted(rows, key=lambda row: row['Number'].strip().lower())
                for row in sorted_rows:
                    print(row)
        organize_by_number(smash)
    elif method == 'series':
        def organize_by_series(csv_path):
            with open(csv_path, newline='', encoding='cp1252') as database:
                reader = csv.DictReader(database)
                rows = list(reader)
                sorted_rows = sorted(rows, key=lambda row: row['Series'].strip().lower())
                for row in sorted_rows:
                    print(row)
        organize_by_series(smash)
    elif method == 'tier':
        def organize_by_tier(csv_path):
            with open(csv_path, newline='', encoding='cp1252') as database:
                reader = csv.DictReader(database)
                rows = list(reader)
                sorted_rows = sorted(rows, key=lambda row: row['Tier'].strip().lower())
                for row in sorted_rows:
                    print(row)
        organize_by_tier(smash)
    else:
        print("Invalid method. Please enter Number, Name, Series, or Tier")
        organize(smash)

if __name__ == '__main__':
    print("Run directly.")