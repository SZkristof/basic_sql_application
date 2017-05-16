import queries


def main():
    print("Press number 1 for mentor names!")
    print("Press number 2 for mentor nicknames!")
    print("Press number 3 for applicant names!")
    print("Press number 4 for lost hat girl!")
    user_choice = input("")
    if int(user_choice) == 1:
        print("\n")
        return queries.mentor_names()
    elif int(user_choice) == 2:
        print("\n")
        return queries.mentor_nicks()
    elif int(user_choice) == 3:
        print("\n")
        return queries.finding_carol()
    elif int(user_choice) == 4:
        print("\n")
        return queries.the_lost_hat()


if __name__ == '__main__':
    main()
