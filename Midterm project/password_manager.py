import json
import random
import string
import base64
import os

class PasswordManager:
    def __init__(self):
        # Get the directory where this script is located
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Create a "password data" folder inside the script directory
        self.data_folder = os.path.join(self.script_dir, "password data")
        
        # Files will be created in the "password data" folder
        self.master_file = os.path.join(self.script_dir, "master.json")
        self.passwords_file = os.path.join(self.data_folder, "passwords.json")
        
        self.master_username = None
        self.master_password = None
        self.logged_in = False

        # Creating "password data" if it doesdn't exist
        if not os.path.exists(self.data_folder):
            os.makedirs(self.data_folder)
    
    def simple_encrypt(self, text):
        """Simple encryption using base64"""
        return base64.b64encode(text.encode()).decode()
    
    def simple_decrypt(self, encrypted_text):
        """Simple decryption using base64"""
        return base64.b64decode(encrypted_text.encode()).decode()
    
    def setup_master_credentials(self):
        """Setup master username and password for first time use"""
        print("=== Setup Master Credentials ===")
        self.master_username = input("Create master username: ")
        self.master_password = input("Create master password: ")
        
        # Save master credentials in main folder
        master_data = {
            "username": self.master_username,
            "password": self.master_password
        }
        with open(self.master_file, "w") as f:
            json.dump(master_data, f)
        
        # Initialize empty password storage in data folder
        with open(self.passwords_file, "w") as f:
            json.dump({}, f)
        
        print("Master credentials setup complete!")
        print(f"Master file: {self.master_file}")
        print(f"Password data: {self.passwords_file}")
        self.logged_in = True
    
    def login(self):
        """Login with master username and password"""
        try:
            with open(self.master_file, "r") as f:
                master_data = json.load(f)
        except:
            self.setup_master_credentials()
            return
        
        print("=== Login ===")
        username = input("Master username: ")
        password = input("Master password: ")
        
        if username == master_data["username"] and password == master_data["password"]:
            self.master_username = username
            self.master_password = password
            self.logged_in = True
            print("Login successful!")
        else:
            print("Invalid credentials!")
            exit()
    
    def load_passwords(self):
        """Load encrypted passwords from file"""
        try:
            with open(self.passwords_file, "r") as f:
                encrypted_data = json.load(f)
            
            # Decrypt all passwords
            decrypted_data = {}
            for domain, data in encrypted_data.items():
                decrypted_data[domain] = {
                    "username": self.simple_decrypt(data["username"]),
                    "password": self.simple_decrypt(data["password"])
                }
            return decrypted_data
        except:
            return {}
    
    def save_passwords(self, passwords):
        """Encrypt and save passwords to file"""
        encrypted_data = {}
        for domain, data in passwords.items():
            encrypted_data[domain] = {
                "username": self.simple_encrypt(data["username"]),
                "password": self.simple_encrypt(data["password"])
            }
        
        with open(self.passwords_file, "w") as f:
            json.dump(encrypted_data, f, indent=2)
    
    def generate_password(self):
        """Generate computer-generated password"""
        length = 12
        characters = string.ascii_letters + string.digits + "!@#$%"
        return ''.join(random.choice(characters) for _ in range(length))
    
    def find_password(self):
        """Option 1: Find password for domain/application"""
        print("\n--- FIND PASSWORD ---")
        domain = input("Enter domain/application name: ")
        
        passwords = self.load_passwords()
        
        if domain in passwords:
            data = passwords[domain]
            print(f"\nDomain: {domain}")
            print(f"Username: {data['username']}")
            print(f"Password: {data['password']}")
        else:
            print(f"No entry found for '{domain}'")
    
    def add_password(self):
        """Option 2: Add new password entry"""
        print("\n--- ADD PASSWORD ---")
        domain = input("Enter domain/application name: ")
        
        passwords = self.load_passwords()
        
        if domain in passwords:
            print(f"Error: '{domain}' already exists!")
            return
        
        username = input("Enter username: ")
        
        print("\nPassword options:")
        print("1. Computer-generated password")
        print("2. Type my own password")
        choice = input("Choose option (1 or 2): ")
        
        if choice == "1":
            password = self.generate_password()
            print(f"Generated password: {password}")
        else:
            password = input("Enter your password: ")
        
        passwords[domain] = {
            "username": username,
            "password": password
        }
        
        self.save_passwords(passwords)
        print(f"Password for '{domain}' added successfully!")
    
    def change_password(self):
        """Option 3: Change password for existing domain"""
        print("\n--- CHANGE PASSWORD ---")
        domain = input("Enter domain/application name: ")
        
        passwords = self.load_passwords()
        
        if domain not in passwords:
            print(f"Error: '{domain}' not found!")
            return
        
        print(f"Current username: {passwords[domain]['username']}")
        
        print("\nPassword options:")
        print("1. Computer-generated password")
        print("2. Type my own password")
        choice = input("Choose option (1 or 2): ")
        
        if choice == "1":
            new_password = self.generate_password()
            print(f"Generated password: {new_password}")
        else:
            new_password = input("Enter new password: ")
        
        passwords[domain]["password"] = new_password
        self.save_passwords(passwords)
        print(f"Password for '{domain}' updated successfully!")
    
    def run(self):
        """Main application loop"""
        self.login()
        
        while self.logged_in:
            print("\n=== PASSWORD MANAGER ===")
            print("1. Find password")
            print("2. Add password")
            print("3. Change password")
            print("4. Exit")
            
            choice = input("Select option (1-4): ")
            
            if choice == "1":
                self.find_password()
            elif choice == "2":
                self.add_password()
            elif choice == "3":
                self.change_password()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid option! Please choose 1-4.")

# Run the application
if __name__ == "__main__":
    manager = PasswordManager()
    manager.run()