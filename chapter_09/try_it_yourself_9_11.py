from try_it_yourself import User, Privileges, Admin

"""Module top practice importing classess from another module."""


# 9-10. Imported Admin: Start with your work from Exercise 9-8 (page 173).
# Store the classes User, Privileges and Admin in one module. Create a separate
# file, make an Admin instance, and call show_privileges() to show that
# everything works correctly.


my_admin = Admin("Diana", "Brown", 28, "diana@example.com")
my_admin.privileges = ["can add post", "can delete post", "can ban user"]
my_admin.show_privileges()
