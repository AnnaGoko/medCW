import os

# Функция для создания новой заметки
def create_note():
    title = input("Введите заголовок заметки: ")
    content = input("Введите текст заметки: ")
    filename = title.lower().replace(" ", "_") + ".txt"
    with open(filename, "w") as file:
        file.write(content)
    print("Заметка успешно создана!")

# Функция для чтения списка заметок
def read_notes():
    notes = os.listdir()
    notes = [note for note in notes if note.endswith(".txt")]
    if not notes:
        print("Список заметок пуст!")
        return
    print("Список заметок:")
    for i, note in enumerate(notes, start=1):
        print(f"{i}. {note[:-4]}")

# Функция для редактирования заметки
def edit_note():
    title = input("Введите заголовок заметки, которую хотите отредактировать: ")
    filename = title.lower().replace(" ", "_") + ".txt"
    if not os.path.exists(filename):
        print("Заметка не найдена!")
        return
    with open(filename, "r") as file:
        content = file.read()
    print(f"Текущий текст заметки:\n{content}")
    new_content = input("Введите новый текст заметки: ")
    with open(filename, "w") as file:
        file.write(new_content)
    print("Заметка успешно отредактирована!")

# Функция для удаления заметки
def delete_note():
    title = input("Введите заголовок заметки, которую хотите удалить: ")
    filename = title.lower().replace(" ", "_") + ".txt"
    if not os.path.exists(filename):
        print("Заметка не найдена!")
        return
    os.remove(filename)
    print("Заметка успешно удалена!")

# Главная функция для выбора действия
def main():
    while True:
        print("\nВыберите действие:")
        print("1. Создать новую заметку")
        print("2. Просмотреть список заметок")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти из программы")
        choice = input("Ваш выбор: ")
        if choice == "1":
            create_note()
        elif choice == "2":
            read_notes()
        elif choice == "3":
            edit_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            break
        else:
            print("Неверный выбор! Попробуйте ещё раз.")

if __name__ == "__main__":
    main()