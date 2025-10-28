class Privileges:
    """A class to store an admin's privileges."""

    def __init__(self, privileges=[]):
        """Initialize the privileges."""
        self.privileges = privileges

    def show_privileges(self):
        """Display the privileges of the administrator."""
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- This user has no privileges.")
