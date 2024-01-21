import psycopg2

# Подключение к базе данных PostgreSQL

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="Vorop",
    password="1"
)

# Создание курсора для выполнения SQL-запросов

cur = conn.cursor()

# Функция для ввода имени и фамилии студента


def enter_student():
    first_name = input("Введите имя студента: ")
    last_name = input("Введите фамилию студента: ")

    # Выполнение SQL-запроса для добавления студента в базу данных

    cur.execute("INSERT INTO Students (FirstName, LastName) VALUES (%s, %s)", (first_name, last_name))
    conn.commit()
    print("Студент успешно добавлен в журнал")


# Функция для добавления оценки студенту

def add_grade():
    student_id = int(input("Введите ID студента: "))
    subject = input("Введите предмет: ")
    grade = int(input("Введите оценку: "))

    # Выполнение SQL-запроса для добавления оценки студенту в базу данных

    cur.execute("INSERT INTO Grades (StudentID, Subject, Grade) VALUES (%s, %s, %s)", (student_id, subject, grade))
    conn.commit()
    print("Оценка успешно добавлена в журнал")


# Основной цикл программы

while True:

    print("Выберите действие:")
    print("1 - Ввести имя и фамилию студента")
    print("2 - Поставить оценку студенту по его ID")
    print("3 - Закончить работу приложения")
    choice = input("Ваш выбор: ")

    if choice == '1':
        enter_student()

    elif choice == '2':
        add_grade()

    elif choice == '3':
        break
    else:
        print("Некорректный выбор. Попробуйте ещё раз.")

# Закрытие курсора и соединение с базой данных

cur.close()
conn.close()
