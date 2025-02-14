class Server:
    def __init__(self, size):
        self.size = size  # Maximum number of users allowed
        self.users = [-1] * size  # Initialize server slots as empty (-1 indicates empty)

    def add_user(self, user_id):
        if -1 not in self.users:
            print("The list is full.")
            return

        # Confirm ID before adding
        confirm_id = int(input("Confirm user ID to add: "))
        if confirm_id != user_id:
            print("ID did not match. User not added.")
            return

        # Disconnect existing user with the same ID
        if user_id in self.users:
            print(f"User {user_id} is already connected. Disconnecting the existing user.")
            self.users[self.users.index(user_id)] = -1

        # Add the new user to the first empty slot
        self.users[self.users.index(-1)] = user_id
        print(f"User {user_id} added to the server.")

    def remove_user(self, user_id):
        if user_id not in self.users:
            print(f"User {user_id} is not in the server.")
            return

        # Confirm ID before removing
        confirm_id = int(input("Confirm user ID to remove: "))
        if confirm_id != user_id:
            print("ID did not match. User not removed.")
            return

        # Remove user
        self.users[self.users.index(user_id)] = -1
        print(f"User {user_id} removed from the server.")

    def display_users(self):
        print("Server slots:")
        for i, user in enumerate(self.users):
            print(f"Slot {i + 1}: {'Empty' if user == -1 else f'User ID {user}'}")


# Example usage
server_size = int(input("Enter server size: "))
server = Server(server_size)

while True:
    print("\nOptions: 1. Add User  2. Remove User  3. Display Users  4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        user_id = int(input("Enter user ID to add: "))
        server.add_user(user_id)
    elif choice == 2:
        user_id = int(input("Enter user ID to remove: "))
        server.remove_user(user_id)
    elif choice == 3:
        server.display_users()
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
