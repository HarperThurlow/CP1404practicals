"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Make a new directory
    # The next time you run this, it will crash if the directory exists
    # TODO: Use exception handling to avoid the crash (just pass)
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))

        # TODO: Try these options one at a time
        # Option 1: rename file to new name - in place

        # os.rename(filename, new_name)

        # Option 2: move file to new place, with new name
        # shutil.move(filename, 'temp/' + new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    saved_string = ""
    previous_character = ""
    filename = filename.rstrip("txt")
    filename = filename.rstrip("TXT")
    for character in filename:

        if previous_character.islower() and character.isupper():
            saved_string += "_"

        elif previous_character.isupper() and character.isupper():
            saved_string += "_"

        elif character == "_" or character.isspace():
            saved_string += "_"

        elif character.islower() and saved_string[-1] == "_":
            saved_string += character.capitalize()

        elif character.islower():
            if previous_character == "_":
                character.capitalize()
            saved_string += character

        if character.isupper():
            saved_string += character
        print(saved_string)

        previous_character = character

    saved_string += ".txt"
    return saved_string


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')

    for directory_name, subdirectories, filenames in os.walk('.'):
        # os.path.join(directory_name, filename)
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        # TODO: add a loop to rename the files
        try:
            for filename in filenames:
                old_name = os.path.join(directory_name, filename)
                new_name = os.path.join(directory_name, get_fixed_filename(filename))
                # os.rename(old_name, new_name)
        except FileExistsError:
            pass


main()
# demo_walk()
