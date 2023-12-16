--Задание 1
-- Выведите все рейсы где actual_arrival не указан.
--SELECT * FROM flights WHERE actual_arrival IS NULL;
-- Выведите имена пассажиров без повторений в алфавитном порядке.
--SELECT passenger_name FROM tickets ORDER BY passenger_name ASC;

-- Задание 2
-- Выбрать количество мест в каждом из самолётов и отсортировать по количеству мест в порядке убывания.
--SELECT aircraft_code, COUNT(*) AS seat_no FROM seats GROUP BY aircraft_code ORDER BY seat_no DESC;
-- Выбрать количество мест в каждом из самолетов по классам обслуживания и отсортировать по полям кода самолета и класса обслуживания в порядке возрастания.
--SELECT aircraft_code, fare_conditions, COUNT(*) AS seat_no FROM seats GROUP BY aircraft_code, fare_conditions ORDER BY aircraft_code ASC, fare_conditions ASC;
-- Выберите минимальную цену полета за каждую дату в таблице bookings.
-- Для того, чтобы сгруппировать только по дате, без учета времени, приведите поле book_date к типу date (::date).
--SELECT DATE(book_date) AS flight_date, MIN(total_amount) AS total_amount FROM bookings GROUP BY flight_date;

-- Задание 3

-- Из таблицы посадочных талонов удалите все записи у рейса с id 9319.
--SELECT * FROM BOARDING_PASSES WHERE FLIGHT_ID = 9319;
--DELETE FROM boarding_passes WHERE flight_id = 9319;