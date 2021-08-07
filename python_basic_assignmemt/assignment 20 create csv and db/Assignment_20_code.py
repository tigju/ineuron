### 1 ###
test1 = "This is a test of the emergency text system"
file = open("test.txt", "w")
file.write(test1)
file.close()
# ### ###

# ### 2 ###
reading = open('test.txt', 'r')
test2 = reading.read()
reading.close()

print(test1 == test2)
### ###

### 3 ###
import csv
books = [
    {'title': 'The Weirdstone of Brisingamen', 'author': 'Alan Garner', 'year': 1960}, 
    {'title': 'Perdido Street Station', 'author': 'China Miéville', 'year': 2000}, 
    {'title': 'Thud!', 'author': 'Terry Pratchett', 'year': 2005}, 
    {'title': 'The Spellman Files', 'author': 'Lisa Lutz', 'year': 2007}, 
    {'title': 'Small Gods', 'author': 'Terry Pratchett', 'year': 1992}
]
with open('books.csv', 'w', newline='') as file:
    book = csv.DictWriter(file, ['title', 'author', 'year'])
    book.writeheader()
    book.writerows(books)
### ###

### 4 ###
import sqlite3
conn = sqlite3.connect('books.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE books (title VARCHAR(50), author VARCHAR(50), year INT)''')
## ###

## 5 ###
with open('books.csv', 'r') as file:
    reading = csv.reader(file)
    # skip header
    next(reading, None)
    curs.executemany("INSERT INTO books VALUES(?, ?, ?)", reading)
conn.commit()
conn.close()
### ###

### 6 ###
conn = sqlite3.connect('books.db')
curs = conn.execute('''SELECT title from books
                        ORDER BY title''')
# returns list of tuples
fetched_titles = curs.fetchall()

# unpack to one list
titles = [title for tpl in fetched_titles for title in tpl]

print(titles)
###

### 7 ###
conn = sqlite3.connect('books.db')
curs = conn.execute('''SELECT * from books
                        ORDER BY year''')
# returns list of tuples
fetched_rows = curs.fetchall()

rows = [row for row in fetched_rows]

for r in rows:
    print(r)
###  ###

### 8 ###
import sqlalchemy
engine = sqlalchemy.create_engine('sqlite:///books.db')
### ###

### 9 ###
import redis
redis_host = 'localhost'
redis_port = 6379

r = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)
r.hmset("test", mapping={"count": 1, "name":  "Fester Bestertester"})
hsh = r.hgetall("test")
print(hsh)
### ###

### 10 ###
r.hincrby("test", "count", amount=1)
hsh_incr = r.hgetall("test")
print(hsh_incr)
### ###

