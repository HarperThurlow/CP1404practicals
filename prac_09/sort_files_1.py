import os


def main():
    os.chdir("FilesToSort")
    for name in os.listdir('.'):
        if os.path.isdir(name):
            continue
        file_type = name.split('.')[-1]
        try:
            os.mkdir(file_type)
        except FileExistsError:
            pass
        os.rename(name, "{}/{}".format(file_type, name))


main()
