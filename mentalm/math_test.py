import configparser
from random import randint, choice
from abc_test import *

class MathTest(Test):
    """A math test"""
    def __init__(self, config_file):

        # Read ini file
        self.config_file = config_file
        config = configparser.ConfigParser()
        config.read(self.config_file)

        # Read general
        numq = config.getint('general', 'numq', fallback=9999)
        time_limit = config.getint('general', 'time_limit', fallback=60)

        # Read operations
        self.operations = [key for key in config['operations'] if config.getboolean('operations', key)]

        # Read numbers
        self.low_bound1 = config.getint('number1', 'low_bound')
        self.high_bound1 = config.getint('number1', 'high_bound')
        self.low_bound2 = config.getint('number2', 'low_bound')
        self.high_bound2 = config.getint('number2', 'high_bound')

        super(MathTest, self).__init__(numq, time_limit)
        
    def next_question(self):
        ranum1 = str(randint(self.low_bound1, self.high_bound1))
        op = choice(self.operations)
        ranum2 = str(randint(self.low_bound2, self.high_bound2))

        if ranum2 == '0' and (op == '//' or op == '%'):
            return self.next_question()
        
        return ranum1 + ' ' + op + ' ' + ranum2

    def get_answer(self, question):
        return eval(question)
