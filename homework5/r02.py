import logging
import functools






def dec(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kw):
        logger = logging.getLogger()
        fh = logging.FileHandler('test.log', encoding='utf-8')
        ch = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logger.level=logging.INFO
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        logger.addHandler(fh)
        logger.addHandler(ch)
        logger.info(fn.__name__)
        fn()
    return wrapper

@dec
def test():
    print('over')

test()





