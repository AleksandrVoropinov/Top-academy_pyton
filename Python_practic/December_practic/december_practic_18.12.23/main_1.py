# import threading
# import time
# import requests as requests
#
# from debestr import StarWarsDataBase
# import logging
#
#
# logger = logging.getLogger('main_1')
# logging.basicConfig(level='INFO')
#
# lock = threading.Semaphore(1)
#
#
# def insert_human_to_db(human):
#     try:
#         lock.acquire(True)
#         logger.info(f'Insert {human["name"]} to db...')
#         db.insert_human_to_table(human)
#         logger.info(f'Insert {human["name"]} to db...SUCCESS')
#     finally:
#         lock.release()
#
#     # logger.exception(f'Insert {human["name"]} to db...ERROR')
#
#
# def get_human(human_id):
#     response = requests.get(f'https://swapi.dev/api/people/{human_id}/')
#     insert_human_to_db(response.json())
#
#
# def consequent_loading():
#     start = time.time()
#     for i in range(1, 10):
#         try:
#             logger.info(f'Getting {i} human...')
#             get_human(i)
#             logger.info(f'Getting {i} human ... SUCCESS')
#         except BaseException:
#             logger.error(f'Getting {i} human...ERROR')
#     logger.info(f'Consequent loading takes {time.time() - start} sec.')
#
#
# def parallel_loading():
#     start = time.time()
#     tasks = []
#     for i in range(1, 10):
#         task = threading.Thread(target=get_human, args=(i, ))
#         task.name = f'Getting {i} human...'
#         logger.info(task.name)
#         task.start()
#         tasks.append(task)
#     for i_task in tasks:
#         i_task.join()
#         logger.info(i_task.name + 'SUCCESS')
#     logger.info(f'Parallel loading takes {time.time() - start}')
#
#
# if __name__ == '__main__':
#     db = StarWarsDataBase()
#     try:
#         consequent_loading()
#         # parallel_loading()
#     finally:
#         db.close_connection()
