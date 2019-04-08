import configparser

##https://docs.python.org/zh-cn/3/library/configparser.html

config = configparser.ConfigParser()
print(config.sections()) #Return a list of section names

config.read('config.ini',encoding='utf-8')

print(config.sections())
