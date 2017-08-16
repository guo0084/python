#!/usr/bin/python3.5
"""
save data base to file use self-defined format;
"""
import sys
import pickle
import shelve


db_file_name = 'shelve_db'
db_pickle_file_name = 'person_pickle'
ENDDB = 'enddb'
ENDREC = 'endrec'
RECSEP = '=>'

def store_dbase(db, file_name=db_file_name):
    file = open(file_name, "w")
    for key in db:
        print(key, file=file)
        for (name, value) in db[key].items():
            print(name + RECSEP + repr(value), file=file)
        print(ENDREC, file=file)
    print(ENDDB, file=file)
    file.close()

def store_dbase_by_pickle(db, file_name=db_pickle_file_name):
    file = open(file_name, "wb")
    pickle.dump(db, file)
    file.close()

    
def load_dbase(file_name=db_file_name):
    file = open(file_name)
    sys.stdin = file
    db = {}
    key = input()
    while key != ENDDB:
        rec = {}
        field = input()
        while field != ENDREC:
            name, value = field.split(RECSEP)
            rec[name] = eval(value)
            field = input()
        db[key] = rec
        key = input()
    return db

def load_dbase_by_pickel(file_name=db_pickle_file_name):
    file = open(file_name, "rb")
    db = pickle.load(file)
    return db

def save_to_shelve(db):
    slv_db = shelve.open("shelve_db")
    for key, value in db.items():
        slv_db[key] = value
    slv_db.close()

    ld_db = shelve.open("shelve_db")
    #print(ld_db)
    ld_db.close()

def load_dbase_from_shelve(file_name):
    db = shelve.open(file_name)
    for name in db:
        print(name, '=>', db[name])
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
            print(person)            
    person_db.close()
    
if __name__ == '__main__':
    #load_dbase_from_shelve(db_file_name)
    find_person(db_file_name)
    #from initdata import db
    #save_to_shelve(db) #test shelve function

    # save every record to seperate file
    #for key, value in db.items():
    #    file = open('' + key + '.pkl', 'wb')
    #    pickle.dump(value, file)
    #    file.close
    #print(db)
    #print('----------------------------------------------')
    #tmp_db = load_dbase_by_pickel()
    #print(tmp_db)
    #store_dbase_by_pickle(db)
    #db = load_dbase(db_file_name)
    #print(db)
    #store_dbase(db, db_file_name)
    
