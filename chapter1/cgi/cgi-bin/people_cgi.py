#!/usr/bin/python3.5

import cgi, shelve, os, sys

shelve_name = 'people'
field_names = ['name', 'age', 'job', 'pay']


form = cgi.FieldStorage()
print('content-type:text/html')
sys.path.insert(0, os.getcwd())
sys.path.append('/home/glb/python/chapter1/oop')
from person import person


reply_html = """
<html>
<title>People Input form</title>
<body>
<form method=POST action="people_cgi.py">
    <table>
        <tr><th>Key<td><input type=text name=key value="%(key)s">
        $ROWS$
    </table>
        $TEST$
</form>
</body>
</html>
"""

row_html = '<tr><th>%s<td><input type=text name=%s value="%%(%s)s">\n'
rows_html=""
for field_name in field_names:
    rows_html += (row_html % ((field_name,) * 3))
reply_html = reply_html.replace('$ROWS$', rows_html)

def htmlize(adict):
    new = adict.copy()
    for field in field_names:
        value = new[field]
        new[field] = cgi.escape(repr(value))
    return new

def fetch_record(db, form):
    try:
        key = form['key'].value
        record = db[key]
        fields = record.__dict__
        fields['key'] = key
    except:
        fields = dict.fromkeys(field_names, '?')
        fields['key'] = form['key'].value
    return fields

def update_record(db, form):
    if not 'key' in form:
        fields = dict.fromkeys(field_names, '?')
        fields['key'] = 'Missing key input!'
    else:
        key = form['key'].value
        if key in db:
            record = db[key]
        else:
            record = person(name='?', age='?')
        for field in field_name:
            setattr(record, field, eval(form[field].value))
        db[key] = record
        fields = record.__dict__
        fields[key] = key
    return fields

db = shelve.open(shelve_name)
action = form['action'].value if 'action' in form else None
if action == 'Fetch':
    fields = fetch_record(db, form)
elif action == 'Update':
    fields = update_record(db, form)
else:
    fields = dict.fromkeys(field_names, '?')
    fields['key'] = 'Missing key input!'

reply_html = reply_html.replace('$TEST$', repr(db[form['key'].value]))
#print(reply_html)
print(reply_html % htmlize(fields))
db.close()
