import logging

def main():
    logging.basicConfig(level=logging.DEBUG, filename='output.log',
    filemode='w')

    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')

    logging.info('Here is a {} variable and an int:'.format('string', 5))

if __name__ == '__main__': main()