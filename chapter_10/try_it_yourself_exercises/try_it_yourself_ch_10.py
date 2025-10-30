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
