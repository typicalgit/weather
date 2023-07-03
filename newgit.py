import requests

def create_github_account(username, password, email):
    # Create a new GitHub account
    url = 'https://api.github.com/user'
    payload = {
        'login': username,
        'password': password,
        'email': email
    }
    response = requests.post(url, json=payload)

    # Check the response status code
    if response.status_code == 201:
        print('GitHub account created successfully!')
    else:
        print(f'Error: {response.status_code} - {response.text}')

# Usage example
username = 'joethegitrepo'
password = 'IamZMoon123'
email = 'zmoonmoozn@gmail.com'

create_github_account(username, password, email)
