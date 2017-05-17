import queries
import printing


def main():
    printing.menu()
    running = True
    while running:
        user_choice = input("Choose a number from 1 to 7: ")
        if user_choice == "1":
            return queries.mentor_names()
        elif user_choice == "2":
            return queries.mentor_nicks()
        elif user_choice == "3":
            return queries.finding_carol()
        elif user_choice == "4":
            return queries.the_lost_hat()
        elif user_choice == "5":
            return queries.new_applicant()
        elif user_choice == "6":
            return queries.change_phone_number()
        elif user_choice == "7":
            return queries.delete_applicants()
        elif user_choice == "q":
            break
        else:
            printing.typo()


if __name__ == '__main__':
    main()

