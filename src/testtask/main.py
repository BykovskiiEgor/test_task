from adapters.file_repository import FileBookRepository
from adapters.console_interface import ConsoleInterface
from application.use_case import AddBook, DeleteBook, SearchBook, DisplayBooks, UpdateStatus

def main():
    repository = FileBookRepository("library.json")
    interface = ConsoleInterface()

    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Поиск книги")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("0. Выйти")

        choice = interface.prompt_input("Выберите действие: ")

        if choice == "1":
            title = interface.prompt_input("Введите название книги: ")
            author = interface.prompt_input("Введите автора книги: ")
            year = int(interface.prompt_input("Введите год издания: "))
            use_case = AddBook(repository)
            book = use_case.execute(title, author, year)
            interface.display_message(f"Книга добавлена: {book}")
        elif choice == "2":
            book_id = int(interface.prompt_input("Введите ID книги для удаления: "))
            use_case = DeleteBook(repository)
            if use_case.execute(book_id):
                interface.display_message("Книга удалена.")
            else:
                interface.display_message("Книга не найдена.")
        elif choice == "3":
            field = interface.prompt_input("По какому полю искать? (title, author, year): ")
            query = interface.prompt_input("Введите запрос: ")
            use_case = SearchBook(repository)
            books = use_case.execute(query, field)
            interface.display_books(books)
        elif choice == "4":
            use_case = DisplayBooks(repository)
            books = use_case.execute()
            interface.display_books(books)
        elif choice == "5":
            book_id = int(interface.prompt_input("Введите ID книги: "))
            status = interface.prompt_input("Введите новый статус ('в наличии' или 'выдана'): ")
            use_case = UpdateStatus(repository)
            book = use_case.execute(book_id, status)
            if book:
                interface.display_message(f"Статус обновлен: {book}")
            else:
                interface.display_message("Книга не найдена.")
        elif choice == "0":
            interface.display_message("Выход из программы.")
            break
        else:
            interface.display_message("Некорректный выбор.")

if __name__ == "__main__":
    main()
