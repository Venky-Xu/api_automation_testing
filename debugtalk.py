
import time
import random
import uuid
from datetime import datetime


def sleep(n_secs):
    time.sleep(n_secs)


def random_1_10000():
    number = random.randint(1, 10000)
    return number


def hook_print(result):
    print(result)


def storename():
    store_name = 'venky' + str(random_1_10000())
    return store_name


def mail():
    email = storename()+'@abc.com'
    return email


def create_uuid_15():
    uid = str(uuid.uuid4().int)
    suid = ''.join(uid.split('-'))
    ssuid = suid[0:15]
    return ssuid

def get_unique_refid():
    return str(uuid.uuid4())

def get_datetime():
    return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")

def create_sku():
<<<<<<< HEAD
    sku= "sku" + str(random.randint(500,100000))
    return sku
=======
    return "sku" + str(random.randint(500,100000))

def create_unique_refid():
    return str(uuid.uuid4())
    
>>>>>>> Added Pricebook test cases
