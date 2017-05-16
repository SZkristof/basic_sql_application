import queries


def main():
    print("Press number 1 for mentor names!")
    print("Press number 2 for mentor nicknames!")
    print("Press number 3 for applicant names!")
    print("Press number 4 for lost hat girl!")
    print("Press number 5 for Markus, the new applicant!")
    print("Press number 6 for telephone number change!")
    print("Press number 7 for deleting applicants!")
    user_choice = input("Give: ")
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
    elif int(user_choice) == 5:
        print("\n")
        return queries.new_applicant()
    elif int(user_choice) == 6:
        print("\n")
        return queries.change_phone_number()
    elif int(user_choice) == 7:
        print("\n")
        return queries.delete_applicants()

if __name__ == '__main__':
    main()

