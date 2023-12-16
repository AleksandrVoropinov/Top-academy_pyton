-- Задание 1
--CREATE DATABASE Birds;
-- Задание 2
--ALTER DATABASE Birds RENAME TO Cats;
-- Задание 3
--DROP DATABASE Cats;
-- Задание 4
--CREATE DATABASE "Овощи и фрукты";
--CREATE TABLE Food (
--    Name VARCHAR(100),
--    Type VARCHAR(20),
--    Color VARCHAR(20),
--    Calories INT,
--    Description VARCHAR(200)
--);
--Заполнение таблицы:
--INSERT INTO Food (Name, Type, Color, Calories, Description)
--VALUES
--('яблоко','фрукт','красный',52,'Сладкий и сочный фрукт'),
--('банан','фрукт','желтый',96,'Энергетический фрукт'),
--('груша','фрукт','зеленый',57,'Сочный и ароматный фрукт'),
--('арбуз','фрукт','зеленый',30,'Освежающий и сочный фрукт'),
--('огурец','овощ','зеленый',17,'Сочный овощ с нежным вкусом'),
--('помидор','овощ','красный',18,'Сочный и ароматный овощ');
-- Задание 5
-- Отображение всей информации из таблицы с овощами и фруктами
--SELECT * FROM Food;

-- Отображение всех овощей
--SELECT * FROM Food WHERE Type = 'овощ';

-- Отображение всех фруктов
--SELECT * FROM Food WHERE Type = 'фрукт';

-- Отображение всех названий овощей и фруктов
--SELECT Name FROM Food;

-- Отображение всех цветов. Цвета должны быть уникальными
--SELECT DISTINCT Color FROM Food;

-- Отображение фруктов конкретного цвета
--SELECT * FROM Food WHERE Type = 'фрукт' AND Color = 'красный';

-- Отображение овощей конкретного цвета
--SELECT * FROM Food WHERE Type = 'овощ' AND Color = 'зеленый';
