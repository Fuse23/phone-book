# Телефонный справочник
Это приложение командной строки для управления телефонным справочником.
Оно позволяет пользователям добавлять, просматривать, редактировать и искать контакты в телефонной книге.

## Возможности:
1. **Просмотр контактов**: Пользователи могут просматривать все контакты, хранящиеся в телефонной книге.
2. **Добавление контакта**: Позволяет пользователям добавить новый контакт в телефонную книгу, вводя данные о контакте.
3. **Редактирование контакта**: Пользователи могут отредактировать существующий контакт, предоставив новые данные.
4. **Поиск контакта**: Позволяет пользователям искать контакт по определенным критериям, таким как имя, фамилия, номер телефона и т. д.

## Использование:
**Запуск программы**: Запустите основной файл phone_book как исполняемый файл или используя интерпретатор Python.

**Выбор действия**: После запуска программы выберите одно из действий, введя соответствующий номер или ключевое слово:
- 0 или menu: Показать меню с доступными действиями.
- 1 или show: Просмотр контактов.
- 2 или add: Добавить новый контакт.
- 3 или edit: Редактировать существующий контакт.
- 4 или search: Поиск контакта.
Ввод данных: Следуйте инструкциям в консоли, чтобы добавить, отредактировать или найти контакты.

## Запуск:
Запустите create_executed_file.sh с правами суперпользователя для создания исполняемого файла phone_book
```bash
sudo sh create_executed_file.sh
```

Или запустите с помощью Python
```bash
python3 phone_book
```

## Запуск тестов:
```bash
poetry install
poetry run pytest
```

Или используйте pip для установки pytest
```bash
python3 -m pip install pytest
python3 -m pytest
```