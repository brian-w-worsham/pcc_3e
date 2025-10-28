import user

"""Create an administrator class."""


class Admin(user.User):
    """Represent an administrator."""

    def __init__(self, first_name, last_name, age, email, location):
        """Initialize an administrator."""
        super().__init__(first_name, last_name, age, email, location)
        self.privileges = []

    def show_privileges(self):
        """Display the privileges of the administrator."""
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")
