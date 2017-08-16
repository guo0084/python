#!/usr/bin/python3.5

import shelve

class person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age  = age
        self.pay  = pay
        self.job  = job

    def __str__(self):
        info  = ('\r\n******** ********')
        info += ('\r\n%8s %8s' % ('name', self.name))
        info += ('\r\n%8s %8d' % ('age', self.age))
        info += ('\r\n%8s %8d' % ('pay', self.pay))
        info += ('\r\n%8s %8s' % ('job', self.job))
        info += ('\r\n******** ********')
        return info

    __repr__ = __str__

    def get_last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay *= (1.0 + percent)

def save_to_shelve(file_name, people):
    db = shelve.open(file_name)
    for person in people:
        db[person] = people[person]
    db.close()

def find_person(shelve_name):
    person_db = shelve.open(shelve_name)
    fields = ['name', 'age', 'job', 'pay']
    max_len = max(len(f) for f in fields)
    while True:
        key = input("\nplease input name you want to query:")
        if not key: break
        try:
            person = person_db[key]
        except:
            print("\nno such person:%s" % key)
        else:
            for field in fields:
                print(field.ljust(max_len), "=>", getattr(person, field))
    person_db.close()
    
    
if __name__ == '__main__':
    from manager import manager
    bob = person('Bob Smith', 42, 30000, 'software')
    sue = person('sue jones', 45, 40000, 'hardware')
    guo = manager('Guo Lingbo', 36, 100000, 'manager')

    people = {}
    people['bob'] = bob
    people['sue'] = sue
    people['guo'] = guo

    save_to_shelve("people", people)
    
    find_person("people")
    
