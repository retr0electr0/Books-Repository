from utils import database

USER_CHOICE = """
Enter:
- 'a' to add  new book ➕
- 'l' to list all books 📄
- 'r' to mark a book as read ✔️
- 'd' to delete a book ➖️
- 'q' to quit ✖️

Your choice: """


def menu():
    database.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print('Unknown command. Please try again')

        user_input = input(USER_CHOICE)


def prompt_add_book():
    name = input('\nEnter the new book name: ')
    author = input('\nEnter the new book author: ')

    database.add_book(name, author)


class InfIter:
    """Infinite iterator"""

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        num = self.num
        self.num += 1
        return num


numbers_gen = iter(InfIter())
next(numbers_gen)

# numbers_gen = (x for x in ['1.','2.','3.','4.','5.']) ## old variant


def list_books():
    books = database.get_all_books()
    for book in books:
        read = 'Yes' if book['read'] == '1' else 'No'
        print(next(numbers_gen))
        print(f"{book['name']} by {book['author']}, read: {read}")


def prompt_read_book():
    name = input('\nFinished reading a book? Enter its name: ')

    database.mark_book_as_read(name)


def prompt_delete_book():
    name = input('\nWant to delete a book? Enter its name: ')

    database.delete_book(name)


menu()