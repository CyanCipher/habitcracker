# Author: Cyan Cipher
# Date: Sep 02 2025
# License: CLL

from habitcracker import HabitTracker


def main():
    ht = HabitTracker()
    while True:
        usr_choice = input(
            'Display Data(D) | Update Data(U) | Generate Graph(G) | Or EXIT: '
        ).lower()
        if usr_choice == 'd':
            for line in ht.get_queries():
                print(line)

        if usr_choice == 'u':
            ht.update()

        if usr_choice == 'g':
            ht.plot_data()

        if usr_choice == 'exit':
            break


if __name__ == "__main__":
    main()
