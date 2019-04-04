import configparser,os

cf = configparser.ConfigParser()
data = cf.read('por.ini')
# print(data)
print(cf.get('mysql','name'))