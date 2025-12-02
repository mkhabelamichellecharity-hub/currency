def decorate_username(username):
    return f"*** {username.upper()} ***"

def mask_password(password):
    return "*" * len(password)

def login_system():
    username = input("Enter username: ")
    password = input("Enter password: ")

    print("\n--- LOGIN SIMULATION ---")
    print(f"Username: {decorate_username(username)}")
    print(f"Password: {mask_password(password)}")

login_system()