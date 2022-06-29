import hashlib


# Test passwords. the below code opens and read a password text file in this project folder
with open('nist_10000.txt', newline='') as bad_passwords:
    password_samples = bad_passwords.read().split('\n')

# This is a sample of data {user:{username, role, md5_hash}} pulled off from a database
users_table = {
    'kalip': {
        'username': 'kalip',
        'role': 'subscriber',
        'md5': '8289a2f789053c777becfd6c8c9487ea'
    }, 
    'folorunsho': {
        'username': 'folorunsho',
        'role': 'administrator',
        'md5': '92472f0a6a0534f201e806384d4e7b29'
    }, 
    'gbenro': {
        'username': 'gbenro',
        'role': 'subscriber',
        'md5': 'cb0eef2644ac22a55a363fadc6ca8db9'
    }, 
    'leye': {
        'username': 'leye',
        'role': 'employee',
        'md5': '8ef17701ea56ec9c98a13199d9290f76'
    },
    'paul': {
        'username': 'paul',
        'role': 'employee',
        'md5': '3d087d60bc3cdc24e1d23ce373b7f194'
    },
}


# Initialize an empty object
rainbow_table = {}

# Run a for loop through each word in the password list and hash word by word everything in the password_samples
for passes in password_samples:
    hashes = hashlib.md5(passes.encode()).hexdigest()
    rainbow_table[hashes] = passes

# Print results of each user and the password from each broken has through the password list. If a md5_hash doesn't match the md5_hash for the password list, print('Not found')
for user in users_table.keys():
    try:
        print(f"User: {user} \t\t Password: {rainbow_table[users_table[user]['md5']]}")
    
    except KeyError:
        print(f"User: {user} \t\t Password: Not found")