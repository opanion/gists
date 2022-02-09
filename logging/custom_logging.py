from locale import format_string
import logging

extra_data = dict(user='Emma')
def main():
    format_str = 'User: %(user)s %(asctime)s: %(levelname)s: %(funcName)s: Line:%(lineno)s %(message)s'
    date_str = '%d-%m-%Y %I:%M:%S %p'
    logging.basicConfig(level=logging.DEBUG, filename='log-output.log',
    filemode='w', format=format_str, datefmt=date_str)

    logging.debug('This is a debug message', extra=extra_data)
    logging.info('This is an info message',  extra=extra_data)
    debugFunc()

def debugFunc():
    logging.debug('This is a debug message',  extra=extra_data)
if __name__ == '__main__': main()