import ConfigParser
import os

def lerEnv():
    Config = ConfigParser.ConfigParser()
    Config.read(os.getcwd() + "/env/env.ini")
    
    return Config