def get_significant_other_name():
    while True:
        significant_other_name = input("Enter the name of the target person's significant other (if applicable): ")
        if ' ' not in significant_other_name:
            return significant_other_name
        else:
            print("Invalid input. Please enter a word without spaces.")

def get_first_name():
    while True:
        first_name = input("Enter the target's first name (no spaces allowed): ")
        if ' ' not in first_name:
            return first_name
        else:
            print("Invalid input. Please enter a word without spaces.")

def get_last_name():
    while True:
        last_name = input("Enter the target's last name (no spaces allowed): ")
        if ' ' not in last_name:
            return last_name
        else:
            print("Invalid input. Please enter a word without spaces.")

def get_pet_names():
    num_pets = int(input("How many pets does the target person have? (Enter a number): "))

    pet_names = []

    for i in range(num_pets):
        while True:
            pet_name = input(f"Enter the name of pet {i+1}: ")
            if ' ' not in pet_name:
                pet_names.append(pet_name)
                break
            else:
                print("Invalid input. Please enter a word without spaces.")

    return pet_names

def get_children_names():
    num_children = int(input("How many children does the target person have? (Enter a number): "))

    children_names = []

    for i in range(num_children):
        while True:
            child_name = input(f"Enter the name of child {i+1}: ")
            if ' ' not in child_name:
                children_names.append(child_name)
                break
            else:
                print("Invalid input. Please enter a word without spaces.")

    return children_names

def get_favorite_thing():
    while True:
        favorite_thing = input("Enter the target's favorite thing. For example a sports team, food, game, etc. No spaces allowed: ")
        if ' ' not in favorite_thing:
            return favorite_thing
        else:
            print("Invalid input. Please enter a word without spaces.")

def generate_passwords(first_name, last_name, significant_other_name, pet_names, children_names, favorite_thing):
    passwords = []
    special_char = "<>?!@#$%^&*()_-+=~[{]}\|"

    for i in range(10000):
        number = str(i)
        number_with_zeros = f"{i:04}"
        password = f"{first_name}{number}\n"
        passwords.append(password)
        password = f"{number}{first_name}\n"
        passwords.append(password)
        password = f"{last_name}{number}\n"
        passwords.append(password)
        password = f"{number}{last_name}\n"
        passwords.append(password)
        password = f"{first_name}{number_with_zeros}\n"
        passwords.append(password)
        password = f"{number_with_zeros}{first_name}\n"
        passwords.append(password)
        password = f"{last_name}{number_with_zeros}\n"
        passwords.append(password)
        password = f"{number_with_zeros}{last_name}\n"
        for char in special_char:
            password = f"{char}{number}{first_name}\n"
            passwords.append(password)
            password = f"{number}{char}{first_name}\n"
            passwords.append(password)
            password = f"{number}{first_name}{char}\n"
            passwords.append(password)
            password = f"{char}{number}{first_name}{char}\n"
            passwords.append(password)
            password = f"{char}{first_name}{number}\n"
            passwords.append(password)
            password = f"{first_name}{char}{number}\n"
            passwords.append(password)
            password = f"{first_name}{number}{char}\n"
            passwords.append(password)
            password = f"{char}{first_name}{number}{char}\n"
            passwords.append(password)
            password = f"{char}{last_name}{number}\n"
            passwords.append(password)
            password = f"{last_name}{char}{number}\n"
            passwords.append(password)
            password = f"{last_name}{number}{char}\n"
            passwords.append(password)
            password = f"{char}{last_name}{number}{char}\n"
            passwords.append(password)
            password = f"{char}{number}{last_name}\n"
            passwords.append(password)
            password = f"{number}{char}{last_name}\n"
            passwords.append(password)
            password = f"{number}{last_name}{char}\n"
            passwords.append(password)
            password = f"{char}{number}{last_name}{char}\n"
            passwords.append(password)
            if i < 1000:
                password = f"{char}{first_name}{number_with_zeros}\n"
                passwords.append(password)
                password = f"{first_name}{char}{number_with_zeros}\n"
                passwords.append(password)
                password = f"{first_name}{number_with_zeros}{char}\n"
                passwords.append(password)
                password = f"{char}{first_name}{number_with_zeros}{char}\n"
                passwords.append(password)
                password = f"{char}{last_name}{number_with_zeros}\n"
                passwords.append(password)
                password = f"{last_name}{char}{number_with_zeros}\n"
                passwords.append(password)
                password = f"{last_name}{number_with_zeros}{char}\n"
                passwords.append(password)
                password = f"{char}{last_name}{number_with_zeros}{char}\n"
                passwords.append(password)
                password = f"{char}{number_with_zeros}{first_name}\n"
                passwords.append(password)
                password = f"{number_with_zeros}{char}{first_name}\n"
                passwords.append(password)
                password = f"{number_with_zeros}{first_name}{char}\n"
                passwords.append(password)
                password = f"{char}{number_with_zeros}{first_name}{char}\n"
                passwords.append(password)
                password = f"{char}{number_with_zeros}{last_name}\n"
                passwords.append(password)
                password = f"{number_with_zeros}{char}{last_name}\n"
                passwords.append(password)
                password = f"{number_with_zeros}{last_name}{char}\n"
                passwords.append(password)
                password = f"{char}{number_with_zeros}{last_name}{char}\n"
                passwords.append(password)
        
        if significant_other_name:
            password = f"{significant_other_name}{number}\n"
            passwords.append(password)
            password = f"{number}{significant_other_name}\n"
            passwords.append(password)
            password = f"{significant_other_name}{number_with_zeros}\n"
            passwords.append(password)
            password = f"{number_with_zeros}{significant_other_name}\n"
            for char in special_char:
                password = f"{char}{number}{significant_other_name}\n"
                passwords.append(password)
                password = f"{number}{char}{significant_other_name}\n"
                passwords.append(password)
                password = f"{number}{significant_other_name}{char}\n"
                passwords.append(password)
                password = f"{char}{number}{significant_other_name}{char}\n"
                passwords.append(password)
                password = f"{char}{significant_other_name}{number}\n"
                passwords.append(password)
                password = f"{significant_other_name}{char}{number}\n"
                passwords.append(password)
                password = f"{significant_other_name}{number}{char}\n"
                passwords.append(password)
                password = f"{char}{significant_other_name}{number}{char}\n"
                passwords.append(password)
                
                if i < 1000:
                    password = f"{char}{significant_other_name}{number_with_zeros}\n"
                    passwords.append(password)
                    password = f"{significant_other_name}{char}{number_with_zeros}\n"
                    passwords.append(password)
                    password = f"{significant_other_name}{number_with_zeros}{char}\n"
                    passwords.append(password)
                    password = f"{char}{significant_other_name}{number_with_zeros}{char}\n"
                    passwords.append(password)
                    password = f"{char}{number_with_zeros}{significant_other_name}\n"
                    passwords.append(password)
                    password = f"{number_with_zeros}{char}{significant_other_name}\n"
                    passwords.append(password)
                    password = f"{number_with_zeros}{significant_other_name}{char}\n"
                    passwords.append(password)
                    password = f"{char}{number_with_zeros}{significant_other_name}{char}\n"
                    passwords.append(password)
        
        for pet_name in pet_names:
            password = f"{pet_name}{number}\n"
            passwords.append(password)
            password = f"{pet_name}{number_with_zeros}\n"
            passwords.append(password)
            for char in special_char:
                password = f"{char}{number}{pet_name}\n"
                passwords.append(password)
                password = f"{number}{char}{pet_name}\n"
                passwords.append(password)
                password = f"{number}{pet_name}{char}\n"
                passwords.append(password)
                password = f"{char}{number}{pet_name}{char}\n"
                passwords.append(password)
                password = f"{char}{pet_name}{number}\n"
                passwords.append(password)
                password = f"{pet_name}{char}{number}\n"
                passwords.append(password)
                password = f"{pet_name}{number}{char}\n"
                passwords.append(password)
                password = f"{char}{pet_name}{number}{char}\n"
                passwords.append(password)
                if i < 1000:
                    password = f"{char}{pet_name}{number_with_zeros}\n"
                    passwords.append(password)
                    password = f"{pet_name}{char}{number_with_zeros}\n"
                    passwords.append(password)
                    password = f"{pet_name}{number_with_zeros}{char}\n"
                    passwords.append(password)
                    password = f"{char}{pet_name}{number_with_zeros}{char}\n"
                    passwords.append(password)
                    password = f"{char}{number_with_zeros}{pet_name}\n"
                    passwords.append(password)
                    password = f"{number_with_zeros}{char}{pet_name}\n"
                    passwords.append(password)
                    password = f"{number_with_zeros}{pet_name}{char}\n"
                    passwords.append(password)
                    password = f"{char}{number_with_zeros}{pet_name}{char}\n"
                    passwords.append(password)
        
        for child_name in children_names:
            password = f"{child_name}{number}\n"
            passwords.append(password)
            password = f"{child_name}{number_with_zeros}\n"
            passwords.append(password)
            for char in special_char:
                password = f"{char}{number}{child_name}\n"
                passwords.append(password)
                password = f"{number}{char}{child_name}\n"
                passwords.append(password)
                password = f"{number}{child_name}{char}\n"
                passwords.append(password)
                password = f"{char}{number}{child_name}{char}\n"
                passwords.append(password)
                password = f"{char}{child_name}{number}\n"
                passwords.append(password)
                password = f"{child_name}{char}{number}\n"
                passwords.append(password)
                password = f"{child_name}{number}{char}\n"
                passwords.append(password)
                password = f"{char}{child_name}{number}{char}\n"
                passwords.append(password)
                if i < 1000:
                    password = f"{char}{child_name}{number_with_zeros}\n"
                    passwords.append(password)
                    password = f"{child_name}{char}{number_with_zeros}\n"
                    passwords.append(password)
                    password = f"{child_name}{number_with_zeros}{char}\n"
                    passwords.append(password)
                    password = f"{char}{child_name}{number_with_zeros}{char}\n"
                    passwords.append(password)
                    password = f"{char}{number_with_zeros}{child_name}\n"
                    passwords.append(password)
                    password = f"{number_with_zeros}{char}{child_name}\n"
                    passwords.append(password)
                    password = f"{number_with_zeros}{child_name}{char}\n"
                    passwords.append(password)
                    password = f"{char}{number_with_zeros}{child_name}{char}\n"
                    passwords.append(password)
        
        password = f"{favorite_thing}{number}\n"
        passwords.append(password)
        password = f"{favorite_thing}{number_with_zeros}\n"
        passwords.append(password)
        for char in special_char:
            password = f"{char}{number}{favorite_thing}\n"
            passwords.append(password)
            password = f"{number}{char}{favorite_thing}\n"
            passwords.append(password)
            password = f"{number}{favorite_thing}{char}\n"
            passwords.append(password)
            password = f"{char}{number}{favorite_thing}{char}\n"
            passwords.append(password)
            password = f"{char}{favorite_thing}{number}\n"
            passwords.append(password)
            password = f"{favorite_thing}{char}{number}\n"
            passwords.append(password)
            password = f"{favorite_thing}{number}{char}\n"
            passwords.append(password)
            password = f"{char}{favorite_thing}{number}{char}\n"
            passwords.append(password)
            if i < 1000:
                password = f"{char}{favorite_thing}{number_with_zeros}\n"
                passwords.append(password)
                password = f"{favorite_thing}{char}{number_with_zeros}\n"
                passwords.append(password)
                password = f"{favorite_thing}{number_with_zeros}{char}\n"
                passwords.append(password)
                password = f"{char}{favorite_thing}{number_with_zeros}{char}\n"
                passwords.append(password)
                password = f"{char}{number_with_zeros}{favorite_thing}\n"
                passwords.append(password)
                password = f"{number_with_zeros}{char}{favorite_thing}\n"
                passwords.append(password)
                password = f"{number_with_zeros}{favorite_thing}{char}\n"
                passwords.append(password)
                password = f"{char}{number_with_zeros}{favorite_thing}{char}\n"
                passwords.append(password)

    return passwords
    
def file_name(passwords, first_name):
    file_name = f"{first_name}.txt"
    with open(file_name, "w") as file:
        file.write("".join(passwords))
    return file_name

significant_other_name = get_significant_other_name()
first_name = get_first_name()
last_name = get_last_name()
pet_names = get_pet_names()
children_names = get_children_names()
favorite_thing = get_favorite_thing()

combined_passwords = generate_passwords(first_name, last_name, significant_other_name, pet_names, children_names, favorite_thing)
file_name = file_name(combined_passwords, first_name)

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
