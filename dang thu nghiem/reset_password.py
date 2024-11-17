import hashlib

# Dữ liệu giả lập lưu trữ thông tin tài khoản
users = {
    "user1": {
        "password": hashlib.sha256("password123".encode()).hexdigest(),
        "security_question": "What is your favorite color?",
        "security_answer": hashlib.sha256("blue".encode()).hexdigest()
    }
}

# Hàm mã hóa mật khẩu
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Hàm đăng nhập
def login():
    username = input("Enter username: ")
    if username in users:
        password = input("Enter password: ")
        hashed_password = hash_password(password)
        if hashed_password == users[username]["password"]:
            print("Login successful!")
        else:
            print("Incorrect password.")
    else:
        print("Username not found.")

# Hàm đặt lại mật khẩu
def reset_password():
    username = input("Enter your username: ")
    if username in users:
        print(users[username]["security_question"])
        answer = input("Answer: ")
        hashed_answer = hash_password(answer)
        if hashed_answer == users[username]["security_answer"]:
            new_password = input("Enter new password: ")
            confirm_password = input("Confirm new password: ")
            if new_password == confirm_password:
                users[username]["password"] = hash_password(new_password)
                print("Password has been reset successfully!")
            else:
                print("Passwords do not match.")
        else:
            print("Security answer incorrect.")
    else:
        print("Username not found.")

# Menu chính
def main():
    while True:
        print("\n1. Login")
        print("2. Forgot Password")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            login()
        elif choice == "2":
            reset_password()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
