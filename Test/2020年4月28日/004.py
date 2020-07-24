import logging
logging.basicConfig(
    filename='test.log',
    filemode='w',
    level=logging.DEBUG,
    datefmt='%Y/%m/%d %H:%M:%S',
    format='%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(module)s - %(message)s'
)
logging.debug('debug level: 10')
logging.info('info level: 20')
logging.warning('warning level: 30')
logging.error('error level: 40')
logging.critical('critical level: 50')