import wikipedia


def main():
    user_input = input(">> ")
    while user_input != "":
        try:
            x = wikipedia.page(user_input)
            print("{}\n{}\n{]".format(x.title, x.summary, x.url()))
        except wikipedia.exceptions.DisambiguationError:
            pass

        user_input = input(">> ")

main()
