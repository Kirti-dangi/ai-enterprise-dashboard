users = {"admin": "admin123"}

def login_user(username, password):
    return username in users and users[username] == password

def register_user(username, password):
    if username not in users:
        users[username] = password
        return True
    return False