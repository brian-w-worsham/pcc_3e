import admin

"""Module top practice importing classess from another module."""


my_admin = admin.Admin("Diana", "Brown", 28, "diana@example.com", "texas")
my_admin.privileges = ["can add post", "can delete post", "can ban user"]
my_admin.show_privileges()
