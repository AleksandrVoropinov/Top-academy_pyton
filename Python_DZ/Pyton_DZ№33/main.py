# Создать таблицу с 10 космическими кораблями из API: https://swapi.dev/api/starships/{id}/
# Используя потоки и семафор.
import sqlite3
import requests
from multiprocessing import Pool, Lock


def create_table():
    conn = sqlite3.connect('starships.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS starships
                (id INTEGER PRIMARY KEY,
                name TEXT,
                model TEXT,
                manufacturer TEXT,
                cost_in_credits TEXT,
                length TEXT,
                crew TEXT,
                passengers TEXT,
                cargo_capacity TEXT,
                starship_class TEXT)''')

    conn.commit()
    conn.close()


def get_starship(id):
    response = requests.get(f'https://swapi.dev/api/starships/{id}/')
    starship = response.json()

    return (starship['id'], starship['name'], starship['model'], starship['manufacturer'], starship['cost_in_credits'],
            starship['length'], starship['crew'], starship['passengers'], starship['cargo_capacity'],
            starship['starship_class'])


def insert_starship(starship):
    conn = sqlite3.connect('starships.db')
    c = conn.cursor()
    c.execute('INSERT INTO starships VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', starship)
    conn.commit()
    conn.close()


def get_starships():
    start_id = 1
    end_id = 11

    lock = Lock()

    with Pool() as pool:
        for id in range(start_id, end_id + 1):
            starship = pool.apply_async(get_starship, args=(id,))
            insert_starship(starship.get())


if __name__ == '__main__':
    create_table()
    get_starships()
