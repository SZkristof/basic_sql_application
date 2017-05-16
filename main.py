import queries


def main():
    print("Press number 1 for mentor names!")
    print("Press number 2 for mentor nicknames!")
    user_choice = input("")
    if int(user_choice) == 1:
        print("\n")
        return queries.mentor_names()
    elif int(user_choice) == 2:
        print("\n")
        return queries.mentor_nicks()


if __name__ == '__main__':
    main()
