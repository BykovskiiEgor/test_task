class ConsoleInterface:
    @staticmethod
    def display_books(books):
        if not books:
            print("Библиотека пуста.")
        for book in books:
            print(f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, Статус: {book.status}")

    @staticmethod
    def display_message(message):
        print(message)

    @staticmethod
    def prompt_input(prompt):
        return input(prompt)
