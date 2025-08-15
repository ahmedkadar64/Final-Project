# Create an idea for a database to use
# Create a module that showcases database based off user input

import sys
sys.path.append(r"C:\Users\HP\PycharmProjects\Final-Project")

import csv
companies = r"C:\Users\HP\PycharmProjects\Final-Project\companies.csv"

def show_all(csv_path):
    with open(csv_path, newline='', encoding='cp1252') as database:
        reader = csv.DictReader(database)
        for row in reader:
            print(row)

show_all(companies)

def search(csv_path):
    method = input("Enter search method:").strip().lower()
    if method == 'rank':
        rank = input("Enter the rank:").strip().lower()
        with open(csv_path, newline='', encoding='cp1252') as database:
            reader = csv.DictReader(database)
            for row in reader:
                if row['Rank'].strip().lower() == rank:
                    print(row)
    elif method == 'name':
        name = input("Enter the name:").strip().lower()
        with open(csv_path, newline='', encoding='cp1252') as database:
            reader = csv.DictReader(database)
            for row in reader:
                if row['Name'].strip().lower() == name:
                    print(row)
    elif method == 'industry':
        industry = input("Enter the industry:").strip().lower()
        with open(csv_path, newline='', encoding='cp1252') as database:
            reader = csv.DictReader(database)
            for row in reader:
                if row['Industry'].strip().lower() == industry:
                    print(row)
    else:
        print("Invalid method. Please try again.")
        search(companies)

# python
def organize(csv_path):
    method = input("Enter organization method (rank, name, industry, revenue, growth, employees, headquarters):").strip().lower()
    with open(csv_path, newline='', encoding='cp1252') as database:
        reader = csv.DictReader(database)
        rows = list(reader)
    if method == 'rank':
        sorted_rows = sorted(rows, key=lambda x: int(x['Rank']))
        for row in sorted_rows:
            print('Rank:', row['Rank'], 'Name:', row['Name'], 'Industry:', row['Industry'])
    elif method == 'name':
        sorted_rows = sorted(rows, key=lambda x: x['Name'].strip().lower())
        for row in sorted_rows:
            print('Name:', row['Name'], 'Rank:', row['Rank'], 'Industry:', row['Industry'])
    elif method == 'industry':
        sorted_rows = sorted(rows, key=lambda x: x['Industry'].strip().lower())
        for row in sorted_rows:
            print('Industry:', row['Industry'], 'Name:', row['Name'], 'Rank:', row['Rank'])
    elif method == 'revenue':
        sorted_rows = sorted(rows, key=lambda x: float(x['Revenue'].replace('$', '').replace(',', '')))
        for row in sorted_rows:
            print('Revenue:', row['Revenue'], 'Name:', row['Name'], 'Rank:', row['Rank'])
    elif method == 'growth':
        sorted_rows = sorted(rows, key=lambda x: float(x['Revenue growth'].replace('%', '')))
        for row in sorted_rows:
            print('Revenue growth:', row['Revenue growth'], 'Name:', row['Name'], 'Rank:', row['Rank'])
    elif method == 'employees':
        sorted_rows = sorted(rows, key=lambda x: int(x['Employees'].replace(',', '')))
        for row in sorted_rows:
            print('Employees:', row['Employees'], 'Name:', row['Name'], 'Rank:', row['Rank'])
    elif method == 'headquarters':
        sorted_rows = sorted(rows, key=lambda x: x['Headquarters'].strip().lower())
        for row in sorted_rows:
            print('Headquarters:', row['Headquarters'], 'Name:', row['Name'], 'Rank:', row['Rank'])
    else:
        print("Invalid method. Please try again.")
        organize(csv_path)

organize(companies)
if __name__ == '__main__':
    print("Run directly.")