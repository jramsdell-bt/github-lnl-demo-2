import configparser
config = configparser.ConfigParser()
config.read('config.ini')

print("Printing contents of config.ini")
for (section_name, params) in config.items():
    for (k,v) in params.items():
        print("{}: {}".format(k, v))
