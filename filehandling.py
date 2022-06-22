import csv


def write_into_csv(info_list):
    with open('Student_administration_info.csv', 'a', newline="") as csv.file:
        writer = csv.writer(csv.file)
        if csv.file.tell() == 0:
            writer.writerow(['Name', 'Age', 'Contact_Number', 'Email'])

        writer.writerow(info_list)


if __name__ == '__main__':
    condition = True

    while condition:
        ask_for_info = input('Enter the student data in this format: (NAME AGE CONTACT_NUMBER Email): ')
        print(f'Student information: {ask_for_info}')

        split_data = ask_for_info.split(' ')
        print(
            f'Name: {split_data[0]}\nAge: {split_data[1]}\nContact_Number: {split_data[2]}\nEmail: {split_data[3]}\n ')
        choice = input('Do you want to confirm the information is right? (Y/N)')

        if choice == 'y':
            write_into_csv(split_data)

            condition_check = input('Enter (Y/N) to fill more student information.')
            if condition_check == 'y':
                condition = True
            elif condition_check == 'n':
                condition = False
        elif choice == 'n':
            print("Re-enter the information.")
