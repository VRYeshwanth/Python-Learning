import json
import os

class Password_Manager():
    def __init__(self,file_path):
        self.file_path = file_path
        self.passwords = self.load_passwords()
    
    def load_passwords(self):
        try:
            with open(self.file_path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
    
    def save_password(self):
        with open(self.file_path, "w") as f:
            json.dump(self.passwords, f, indent=4)
    
    def add_password(self, website, username, passw):
        self.passwords[website] = {
            "Username": username,
            "Password": passw
        }
        self.save_password()
        print("---------------------------------------------------------------")
        print("Password Added")
        print("---------------------------------------------------------------")
    
    def delete_password(self, website):
        if website in self.passwords:
            del self.passwords[website]
            self.save_password()
            print("---------------------------------------------------------------")
            print("Website Deleted")
            print("---------------------------------------------------------------")
        else:
            print("---------------------------------------------------------------")
            print("No such website found")
            print("---------------------------------------------------------------")

    def view_passwords(self):
        if not self.passwords:
            print("No passwords available")
        else:
            print("---------------------------------------------------------------")
            for web, data in self.passwords.items():
                print(f"Website = {web}")
                print(f"Username = {data["Username"]}")
                print(f"Password = {data["Password"]}\n")
            print("---------------------------------------------------------------")
            
    
def main():
    file_name = "Passwords.json"
    fp = os.path.dirname(__name__)
    file_path = os.path.join(fp, file_name)

    manager = Password_Manager(file_path)

    while True:
        print("\nPassword Manager Options")
        print("1) Add a new password")
        print("2) Delete a password")
        print("3) View all passwords")
        print("4) Exit")
        ch = int(input())
        if ch == 1:
            web = input("Enter the name of the website : ")
            user = input("Enter the username : ")
            passw = input("Enter your password : ")
            manager.add_password(web,user,passw)
        if ch == 2:
            web = input("Enter the website to delete it : ")
            manager.delete_password(web)
        if ch == 3:
            manager.view_passwords()
        if ch == 4:
            exit(0)

if __name__ == "__main__":
    main()