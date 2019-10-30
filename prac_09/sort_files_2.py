import os


def main():
    os.chdir("FilesToSort2")
    types_of_files = []
    for i, name in enumerate(os.listdir('.')):
        if os.path.isdir(name):
            continue

        file_type = name.split('.')[-1]
        if file_type not in types_of_files:
            folder_type = input("What type of file is a {}".format(file_type))
            types_of_files.append(folder_type)
        print(types_of_files)
        print(i)
        try:
            os.mkdir(file_type)
        except FileExistsError:
            pass
        os.rename(name, "{}/{}".format(types_of_files[(i - 2)], name))


main()
