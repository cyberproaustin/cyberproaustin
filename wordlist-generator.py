import calendar
import os

def get_company_name():
    while True:
        company_name = input("Enter the name of the company. If the company name is more than one word, use the acronym or type the words with no spaces: ")
        if ' ' in company_name:
            print("Company name cannot contain spaces. Please try again.")
        else:
            return company_name

def get_company_info():
    street_name = input("Enter the name of the street (no spaces): ")
    while ' ' in street_name:
        print("Street name cannot contain spaces.")
        street_name = input("Enter the name of the street (no spaces): ")

    street_number = input("Enter the number of the street: ")

    company_description = input("What is the most popular item the company sells? (no spaces): ")
    while ' ' in company_description:
        print("This cannot contain spaces.")
        company_description = input("What is the most popular item the company sells? (no spaces): ")

    return street_name, street_number, company_description


def generate_month_passwords(current_year):
    passwords = []

    # Generate passwords using names of months and seasons
    for year in range(current_year - 75, current_year + 75):
        last_2_digits_year = str(year)[-2:]

        for month in range(1, 13):
            month_name = calendar.month_name[month]
            passwords.append(f"{month_name}{year}")
            passwords.append(f"{year}{month_name}")
            passwords.append(f"{month_name}{last_2_digits_year}")
            passwords.append(f"{last_2_digits_year}{month_name}")

            for special_char in "!@#$%^&*?~+=_-":
                passwords.append(f"{month_name}{special_char}{year}")
                passwords.append(f"{month_name}{special_char}{last_2_digits_year}")
                passwords.append(f"{special_char}{month_name}{year}")
                passwords.append(f"{special_char}{month_name}{last_2_digits_year}")
                passwords.append(f"{month_name}{year}{special_char}")
                passwords.append(f"{month_name}{last_2_digits_year}{special_char}")

        # Add seasons
        seasons = ["Winter", "Spring", "Summer", "Autumn", "Fall"]
        for season in seasons:
            passwords.append(f"{season}{year}")
            passwords.append(f"{year}{season}")
            passwords.append(f"{season}{last_2_digits_year}")
            passwords.append(f"{last_2_digits_year}{season}")

            for special_char in "!@#$%^&*?~+=_-":
                passwords.append(f"{season}{special_char}{year}")
                passwords.append(f"{season}{special_char}{last_2_digits_year}")
                passwords.append(f"{special_char}{season}{year}")
                passwords.append(f"{special_char}{season}{last_2_digits_year}")
                passwords.append(f"{season}{year}{special_char}")
                passwords.append(f"{season}{last_2_digits_year}{special_char}")

    # Add lowercase versions
    lowercase_passwords = [password.lower() for password in passwords]

    return lowercase_passwords + passwords

def generate_company_passwords(current_year, company_name):
    passwords = []


    last_2_digits_year = str(current_year)[-2:]
    passwords.append(f"{company_name}{current_year}")
    passwords.append(f"{current_year}{company_name}")
    passwords.append(f"{company_name}{last_2_digits_year}")
    passwords.append(f"{last_2_digits_year}{company_name}")

    for special_char in "!@#$%^&*?~+=_-":
        passwords.append(f"{company_name}{special_char}{current_year}")
        passwords.append(f"{company_name}{special_char}{last_2_digits_year}")
        passwords.append(f"{special_char}{company_name}{current_year}")
        passwords.append(f"{special_char}{company_name}{last_2_digits_year}")
        passwords.append(f"{company_name}{current_year}{special_char}")
        passwords.append(f"{company_name}{last_2_digits_year}{special_char}")

    # Add lowercase versions
    lowercase_passwords = [password.lower() for password in passwords]

    return lowercase_passwords + passwords


def generate_street_passwords(street_name, street_number):
    passwords = []

    special_chars = "!@#$%^&*?~+=_-"

    # Add combinations without special characters
    combinations = [
        f"{street_name}{street_number}",
        f"{street_number}{street_name}",
    ]

    passwords.extend(combinations)

    # Add combinations with special characters
    for special_char in special_chars:
        passwords.append(f"{street_name}{street_number}{special_char}")
        passwords.append(f"{street_number}{street_name}{special_char}")
        passwords.append(f"{special_char}{street_name}{street_number}")
        passwords.append(f"{special_char}{street_number}{street_name}")
        passwords.append(f"{street_name}{special_char}{street_number}")
        passwords.append(f"{street_number}{special_char}{street_name}")
        passwords.append(f"{street_number}{street_name}{special_char}")
        passwords.append(f"{street_name}{special_char}{street_number}")
        passwords.append(f"{street_name}{special_char}")
        passwords.append(f"{street_number}{special_char}")
        passwords.append(f"{special_char}{street_name}")
        passwords.append(f"{special_char}{street_number}")

   # Add lowercase versions
    lowercase_passwords = [password.lower() for password in passwords]

    return passwords + lowercase_passwords
    
def generate_descriptor_passwords(company_description, street_name, street_number, company_name, current_year):
    passwords = []

    special_chars = "!@#$%^&*?~+=_-"

    last_2_digits_year = str(current_year)[-2:]
    combinations = [
        f"{company_description}{street_number}",
        f"{company_description}{street_name}",
        f"{company_description}{company_name}",
        f"{company_description}{current_year}",
        f"{company_description}{last_2_digits_year}",
        f"{street_number}{company_description}",
        f"{street_name}{company_description}",
        f"{company_name}{company_description}",
        f"{current_year}{company_description}",
        f"{last_2_digits_year}{company_description}"
    ]

    for special_char in special_chars:
        passwords.append(f"{special_char}{company_description}{street_number}")
        passwords.append(f"{company_description}{special_char}{street_name}")
        passwords.append(f"{company_description}{company_name}{special_char}")
        passwords.append(f"{special_char}{company_description}{current_year}")
        passwords.append(f"{street_number}{special_char}{company_description}")
        passwords.append(f"{street_name}{company_description}{special_char}")
        passwords.append(f"{special_char}{company_name}{company_description}")
        passwords.append(f"{current_year}{special_char}{company_description}")
        passwords.append(f"{last_2_digits_year}{special_char}{company_description}")
        passwords.append(f"{company_description}{street_number}{special_char}")
        passwords.append(f"{special_char}{company_description}{street_name}")
        passwords.append(f"{company_description}{special_char}{company_name}")
        passwords.append(f"{company_description}{current_year}{special_char}")
        passwords.append(f"{company_description}{last_2_digits_year}{special_char}")
        passwords.append(f"{special_char}{street_number}{company_description}")
        passwords.append(f"{street_name}{special_char}{company_description}")
        passwords.append(f"{company_name}{company_description}{special_char}")
        passwords.append(f"{special_char}{current_year}{company_description}")
        passwords.append(f"{special_char}{last_2_digits_year}{company_description}")
        passwords.append(f"{company_description}{special_char}{street_number}")
        passwords.append(f"{company_description}{street_name}{special_char}")
        passwords.append(f"{special_char}{company_description}{company_name}")
        passwords.append(f"{company_description}{special_char}{current_year}")
        passwords.append(f"{company_description}{special_char}{last_2_digits_year}")
        passwords.append(f"{street_number}{company_description}{special_char}")
        passwords.append(f"{special_char}{street_name}{company_description}")
        passwords.append(f"{company_name}{special_char}{company_description}")
        passwords.append(f"{current_year}{company_description}{special_char}")
        passwords.append(f"{last_2_digits_year}{company_description}{special_char}")

    # Add lowercase versions
    lowercase_passwords = [password.lower() for password in passwords]

    return lowercase_passwords + passwords


# Main script
company_name = get_company_name()
current_year = int(input("Enter the current year: "))
street_name, street_number, company_description = get_company_info()

# Generate passwords based on month
month_passwords = generate_month_passwords(current_year)

# Generate passwords based on company name
company_passwords = generate_company_passwords(current_year, company_name)

# Generate passwords based on street information
street_passwords = generate_street_passwords(street_name, street_number)

# Generate passwords based on company descriptor
descriptor_passwords = generate_descriptor_passwords(company_description, street_name, street_number, company_name, current_year)

# Combine original and modified passwords
combined_passwords = month_passwords + company_passwords + street_passwords + descriptor_passwords

# Create a file with the passwords
file_name = ""
if len(company_name) == 1:
    file_name = company_name[0].replace(' ', '') + ".txt"
else:
    acronym = ''.join([name[0].upper() for name in company_name])
    file_name = acronym + ".txt"

# Write the original passwords to the file
with open(file_name, 'w') as file:
    file.write('\n'.join(combined_passwords))

# Replace 'A' with '4'
a_and_4_passwords = [password.replace('A', '4') for password in combined_passwords]

# Create a new temporary file with modified passwords
a_and_4_temp_file_name = file_name.replace('.txt', '_temp_a4.txt')
with open(a_and_4_temp_file_name, 'w') as file:
    file.write('\n'.join(a_and_4_passwords))

# Replace 'B' with '8'
b_and_8_passwords = [password.replace('B', '8') for password in combined_passwords]

# Create a new temporary file with modified passwords
b_and_8_temp_file_name = file_name.replace('.txt', '_temp_b8.txt')
with open(b_and_8_temp_file_name, 'w') as file:
    file.write('\n'.join(b_and_8_passwords))

# Replace 'E' with '3' (uppercase) and 'e' with '3' (lowercase)
e_and_3_passwords = [password.replace('E', '3').replace('e', '3') for password in combined_passwords]

# Create a new temporary file with modified passwords
e_and_3_temp_file_name = file_name.replace('.txt', '_temp_e3.txt')
with open(e_and_3_temp_file_name, 'w') as file:
    file.write('\n'.join(e_and_3_passwords))

# Replace 'I' with '1' (uppercase) and 'l' with '1' (lowercase)
i_and_1_passwords = [password.replace('I', '1').replace('l', '1') for password in combined_passwords]

# Create a new temporary file with modified passwords
i_and_1_temp_file_name = file_name.replace('.txt', '_temp_i1.txt')
with open(i_and_1_temp_file_name, 'w') as file:
    file.write('\n'.join(i_and_1_passwords))

# Replace '0' with 'o' and 'O'
o_and_0_passwords = [password.replace('o', '0').replace('O', '0') for password in combined_passwords]

# Create a new temporary file with modified passwords
o_and_0_temp_file_name = file_name.replace('.txt', '_temp_o0.txt')
with open(o_and_0_temp_file_name, 'w') as file:
    file.write('\n'.join(o_and_0_passwords))

# Replace 'T' with '7'
t_and_7_passwords = [password.replace('T', '7') for password in combined_passwords]

# Create a new temporary file with modified passwords
t_and_7_temp_file_name = file_name.replace('.txt', '_temp_t7.txt')
with open(t_and_7_temp_file_name, 'w') as file:
    file.write('\n'.join(t_and_7_passwords))

# Replace 's' with '5' (lowercase) and 'S' with '5' (uppercase)
s_and_5_passwords = [password.replace('s', '5').replace('S', '5') for password in combined_passwords]

# Create a new temporary file with modified passwords
s_and_5_temp_file_name = file_name.replace('.txt', '_temp_s5.txt')
with open(s_and_5_temp_file_name, 'w') as file:
    file.write('\n'.join(s_and_5_passwords))

# Replace 'A' with '4', 'a' with '@', 'B' with '8', 'E' with '3', 'e' with '3', 
# 'I' with '1' (uppercase), 'l' with '1' (lowercase), 'T' with '7', 's' with '5' (lowercase), 'S' with '5' (uppercase), 'o' and 'O' with '0'
combined_replacements_passwords = [password.replace('A', '4').replace('a', '@').replace('B', '8').replace('E', '3').replace('e', '3')
                                  .replace('I', '1').replace('l', '1').replace('T', '7').replace('s', '5').replace('S', '5').replace('o', '0').replace('O', '0')
                                  for password in combined_passwords]

# Create a new temporary file with modified passwords
combined_replacements_temp_file_name = file_name.replace('.txt', '_temp_combined.txt')
with open(combined_replacements_temp_file_name, 'w') as file:
    file.write('\n'.join(combined_replacements_passwords))
    
# Concatenate the original file with the modified passwords
with open(file_name, 'a') as file:
    with open(a_and_4_temp_file_name, 'r') as a4_file:
        file.write(a4_file.read())

    with open(b_and_8_temp_file_name, 'r') as b8_file:
        file.write(b8_file.read())

    with open(e_and_3_temp_file_name, 'r') as e3_file:
        file.write(e3_file.read())

    with open(i_and_1_temp_file_name, 'r') as i1_file:
        file.write(i1_file.read())

    with open(o_and_0_temp_file_name, 'r') as o0_file:
        file.write(o0_file.read())

    with open(t_and_7_temp_file_name, 'r') as t7_file:
        file.write(t7_file.read())

    with open(s_and_5_temp_file_name, 'r') as s5_file:
        file.write(s5_file.read())
        
    with open(combined_replacements_temp_file_name, 'r') as combined_file:
        file.write(combined_file.read())

#Get the modified passwords
modified_passwords = a_and_4_passwords + b_and_8_passwords + i_and_1_passwords + t_and_7_passwords + s_and_5_passwords + e_and_3_passwords + o_and_0_passwords + combined_replacements_passwords

# Remove duplicates
unique_modified_passwords = modified_passwords

# Remove temporary files
os.remove(a_and_4_temp_file_name)
os.remove(b_and_8_temp_file_name)
os.remove(i_and_1_temp_file_name)
os.remove(o_and_0_temp_file_name)
os.remove(t_and_7_temp_file_name)
os.remove(s_and_5_temp_file_name)
os.remove(e_and_3_temp_file_name)
os.remove(combined_replacements_temp_file_name)

# Write the final passwords to the file
with open(file_name, 'a') as file:
    file.write('\n'.join(unique_modified_passwords))

print(f"Generated {len(unique_modified_passwords)} passwords. Passwords saved to {file_name}.")
