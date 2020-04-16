
import time
import random


def sleep(n_secs):
    time.sleep(n_secs)


def random_1_10000():
    number = random.randint(1, 10000)
    return number


def storename():
    store_name = 'venky' + str(random_1_10000())
    return store_name


def mail():
    email = storename()+'@abc.com'
    return email
