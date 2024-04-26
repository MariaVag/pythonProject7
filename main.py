import requests as rq
import logging

logger = logging.getLogger('RequestsLogger')

sites = ['https://www.youtube.com/', 'https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
         'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com', 'https://tiktok.com',
         'https://www.ozon.ru']

logging.basicConfig(level=logging.INFO)

error_handler = logging.FileHandler('success_responses.log',
                    mode='w',
                    encoding='UTF8',
                    )
error_handler.setLevel(logging.ERROR)


error_handler2 = logging.FileHandler('bad_responses.log',
                    mode='w',
                    encoding='UTF8')
error_handler2.setLevel(logging.INFO)



error_handler3 = logging.FileHandler('blocked_responses.log',
                    mode='w',
                    encoding='UTF8')
error_handler3.setLevel(logging.WARNING)



logger.error('ERROR')
logger.info('INFO')
logger.warning('WARNING')

formatter = logging.Formatter('%(levelname)s: %(message)s')
error_handler.setFormatter(formatter)
error_handler2.setFormatter(formatter)
error_handler3.setFormatter(formatter)

logger.addHandler(error_handler)
logger.addHandler(error_handler2)
logger.addHandler(error_handler3)


for site in sites:
    try:
        response = rq.get(site, timeout=3)
        print(response)
        if response.status_code == 200:
            logger.info(f'INFO: {site} {response.status_code}')
        else:
            logger.warning(f'WARNING: {site} {response.status_code}')
    except Exception as e:
        logger.error(f'ERROR: {site}. Exception: {str(e)}')

logging.info('wow')
for handler in logger.handlers:
    handler.close()

