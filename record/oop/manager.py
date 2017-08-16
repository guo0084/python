#!/usr/bin/python3.5
from person import person

class manager(person):
    def give_raise(self, percent, bonus=0.1):
        self.pay *= (1.0 + percent + bonus)

    
