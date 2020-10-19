import time
import random
import uuid
import datetime


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
    email = storename() + '@abc.com'
    return email


def create_uuid_15():
    uid = str(uuid.uuid4().int)
    suid = ''.join(uid.split('-'))
    ssuid = suid[0:15]
    return ssuid


def uuid_32():
    uuid32 = str(uuid.uuid5(uuid.NAMESPACE_DNS, str(uuid.uuid1())))
    return uuid32


def create_sku():
    sku = "sku" + str(random.randint(500, 100000))
    return sku


def get_unique_refid():
    return str(uuid.uuid4())


def get_datetime():
    return datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")


def get_tomorrow():
    return (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%dT%H:00:00.000Z")


def create_receipt_number():
    return "001" + datetime.datetime.now().strftime("%y%m%d%H%M%S") + str(random.randint(1, 9))


def set_cookie__s(cookie, arg):
    cookie["__s"] = arg
    a = []
    c = ""
    for key in cookie:
        a.append(key + "=" + cookie[key])
    for i in a:
        c = c + i + ";"
    return c[0:len(c) - 1]


def set_cookie_sid(arg1, arg2):
    cookie = {"__s": arg2, "sid": arg1}
    a = []
    c = ""
    for key in cookie:
        a.append(key + "=" + cookie[key])
    for i in a:
        c = c + i + ";"
    return c[0:len(c) - 1]


def set_cookie__t(arg1, arg2, arg3):
    cookie = {"__s": arg2, "sid": arg1, "__t": arg3}
    a = []
    c = ""
    for key in cookie:
        a.append(key + "=" + cookie[key])
    for i in a:
        c = c + i + ";"
    return c[0:len(c) - 1]

