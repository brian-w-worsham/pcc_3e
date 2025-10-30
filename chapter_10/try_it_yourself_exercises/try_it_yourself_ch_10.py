from pathlib import Path

# 10-1. Learning Python: Open a blank file in your text editor and write a few
# lines summarizing what you have learned about Python so far. Start each line
# with the phrase In Python you can... Save the file as learning_python.txt in
# same directory as your exercises from this chapter. Write a program that
# reads the file and prints what you wrote two times: print the contents once
# by reading in the entire file, and once by storing the lines in a list and
# then looping over each line.

# Build the path relative to this script's directory, so it works regardless of
# the current working directory when the script is run.
base_dir = Path(__file__).parent
path = base_dir / "learning_python.txt"

# Read entire file contents once
contents = path.read_text(encoding="utf-8")
print("Reading the entire file at once:\n")
print(contents)

# Read lines into a list and loop over them
print("\nReading the file line by line:\n")
lines = contents.splitlines()
for line in lines:
    print(line)


# 10-2. Learning C: You can use teh replace() method to replace any word in a
# string with a different word. Here’s a quick example showing how to replace
# 'dog' with 'cat' in a sentence:
# message = "I really like dogs."
# message = message.replace('dog', 'cat')
# 'I really like cats.'
# Read in the file you just created, learning_python.txt, and replace the word
# 'Python' with the name of another language, such as 'C'. Print the modified
# text to the screen.
modified_contents = contents.replace("Python", "C")
print("\nModified contents with 'Python' replaced by 'C':\n")
print(modified_contents)

# 10-3. Simpler Code: The program file_reader.py in this section uses a
# temporary variable, lines, to show how splitlines() works. You can skip the
# temporary variable and loop directly over the results of splitlines()
# returns:
# for line in contents.splitlines():
# Remove the temporary variable from each of the programs in this section,
# to make them more concise.
print("\nReading the file line by line without a temporary variable:\n")
for line in contents.splitlines():
    print(line)


# 10-4. Guest: Write a program that prompts the user for their name. When they
# respond, write their name to a file called guest.txt.
guest_path = base_dir / "guest.txt"
guest_name = input("Please enter your name: ")
guest_path.write_text(guest_name + "\n", encoding="utf-8")
print(f"Your name has been written to {guest_path}")


# 10-5. Guest Book: Write a while loop that prompts users for their name.
# Collect all the names that are entered, and then write these names to a
# file called guest_book.txt. Make sure each entry appears on a new line in
# the file.
guest_book_path = base_dir / "guest_book.txt"
guest_names = []

while True:
    guest_name = input("Please enter your name (or 'quit' to stop): ")
    if guest_name.lower() == "quit":
        break
    guest_names.append(guest_name)

guest_book_path.write_text("\n".join(guest_names), encoding="utf-8")
print(f"Guest book has been written to {guest_book_path}")


# 10-6. Addition: One common problem when prompting for numerical input occurs
# when people provide text instead of numbers. When you try to convert the
# input to an int, you’ll get a ValueError. Write a program that prompts for
# two numbers. Add them together and print the result. Catch the ValueError if
# either input value is not a number, and print a friendly error message. Test
# your program by entering two numbers and then by entering some text instead
# of a number.

keep_going = True

while keep_going:
    try:
        x = input("Give me a number: ")
        x = int(x)

        y = input("Give me another number: ")
        y = int(y)
    except ValueError:
        print("Sorry, I really needed a number.")
    else:
        sum = x + y
        print(f"The sum of {x} and {y} is {sum}.")
        keep_going = False

# 10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least
# three names of cats in the first file and three names of dogs in the second
# file. Write a program that tries to read these files and print the contents
# of the files to the screen. Wrap each name in a try-except block to catch the
# FileNotFoundError, and print a friendly message if a file is missing. Move
# one of the files to a different location on your system, and make sure the
# code in the except block executes properly.


def read_file(filename):
    """Read and print the contents of a file."""
    try:
        with open(filename) as file:
            contents = file.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        print(contents)


filenames = ["cats.txt", "dogs.txt", "missing.txt"]

for filename in filenames:
    relative_filename = base_dir / filename
    print(f"\nReading file: {relative_filename}")
    read_file(relative_filename)


# 10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to
# fail silently if either file is missing.


def read_file_fail_silent(filename):
    """Read and print the contents of a file."""
    try:
        with open(filename) as file:
            contents = file.read()
    except FileNotFoundError:
        pass
    else:
        print(contents)


filenames = ["cats.txt", "dogs.txt", "missing.txt"]

for filename in filenames:
    relative_filename = base_dir / filename
    print(f"\nReading file: {relative_filename}")
    read_file_fail_silent(relative_filename)



