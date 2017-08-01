#!/usr/bin/python3.5
"""
save data base to file use self-defined format;
"""
db_file_name = 'person'
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

    
def load_dbase(file_name=db_file_name):
    file = open(file_name)
    import sys
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

if __name__ == '__main__':
    #from initdata import db
    db = load_dbase(db_file_name)
    print(db)
    store_dbase(db, db_file_name)
    
