# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for 
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message 
# indicating that the restaurant is open. Make an instance of Restaurant from
# your class. Print the two attributes individually, and then call both 
# methods.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print the restaurant's name and cuisine type."""
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        """Print a message indicating that the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")


my_restaurant = Restaurant("The Great Restaurant", "Italian")
print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create
# three different instances from the class, and call describe_restaurant() for
# each instance.
restaurant1 = Restaurant("Pasta Palace", "Italian")
restaurant2 = Restaurant("Sushi Central", "Japanese")
restaurant3 = Restaurant("Taco Town", "Mexican")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically
# stored in a user profile. Make a method called describe_user() that prints a
# summary of the user's information. Make another method called greet_user()
# that prints a personalized greeting to the user. Create several instances
# representing different users, and call both methods for each user.


class User:
    def __init__(self, first_name, last_name, age, email):
        """Initialize user attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        """Print a summary of the user's information."""
        print("User Profile:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back.")


user1 = User("Alice", "Smith", 30, "alice@example.com")
user2 = User("Bob", "Johnson", 25, "bob@example.com")
user3 = User("Charlie", "Williams", 35, "charlie@example.com")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

# 9-4. Number Served: Start with your program from Exercise 9-1 (page 162). Add
# an attribute called number_served with a default value of 0. Create an
# instance called restaurant from your class. Print the number of customers
# the restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number of
# customers that have been served. Call this method with a new number and print
# the value again. Add a method called increment_number_served() that lets you
# increment the number of customers who’ve been served. Call this method with
# any number you like that could represent how many customers were served in a
# day of business.


class RestaurantWithServed:
    """A class representing a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Print the restaurant's name and cuisine type."""
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def set_number_served(self, number):
        """Set the number of customers served."""
        self.number_served = number

    def increment_number_served(self, additional_customers):
        """Increment the number of customers served."""
        self.number_served += additional_customers

    def open_restaurant(self):
        """Print a message indicating that the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")


restaurant = RestaurantWithServed("The Busy Bistro", "French")
print(f"Number of customers served: {restaurant.number_served}")

restaurant.set_number_served(5)
print(f"Number of customers served: {restaurant.number_served}")

restaurant.increment_number_served(10)
print(f"Number of customers served: {restaurant.number_served}")

# 9-5. Login Attempts: Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 162). Write a method called 
# increment_login_attempts() that increments the value of login_attempts by 1.
# Write another method called reset_login_attempts() that resets the value of
# login_attempts to 0. Make an instance of the User class and call 
# increment_login_attempts() several times. Print the value of login_attempts
# to make sure it was incremented properly, and then call
# reset_login_attempts(). Print login_attempts again to make sure it was
# reset to 0.


class UserWithLoginAttempts:
    def __init__(self, first_name, last_name, age, email):
        """Initialize user attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        """Print a summary of the user's information."""
        print("User Profile:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back.")

    def increment_login_attempts(self):
        """Increment the number of login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the number of login attempts to 0."""
        self.login_attempts = 0


user = UserWithLoginAttempts("Diana", "Brown", 28, "diana@example.com")
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Login attempts: {user.login_attempts}")
user.reset_login_attempts()
print(f"Login attempts after reset: {user.login_attempts}")
