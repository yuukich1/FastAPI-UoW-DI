import logging
from logging.handlers import TimedRotatingFileHandler
import os
from datetime import date



def setup_loger():
    log_folder = './logs'
    os.makedirs(log_folder, exist_ok=True)

    log_format = "%(asctime)s %(levelname)s %(message)s"

    log_filename = os.path.join(log_folder, f'{date.today()}.log')
    handler = TimedRotatingFileHandler(log_filename, when="midnight", interval=1, encoding='utf-8')

    handler.setFormatter(logging.Formatter(log_format))

    # Устанавливаем уровень логирования
    logging.basicConfig(level=logging.INFO, handlers=[handler])

