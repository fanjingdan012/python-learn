import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="Initial0", db="test")
c = db.cursor()
max_price = 5
c.execute("""SELECT * FROM user""")
#c.execute('create table user1 (id varchar(20) primary key, name varchar(20))')
c.execute('insert into user1 (id, name) values (%s, %s)', ['1', 'Michael'])
c.rowcount
db.commit()
c.execute('select * from user1 where id = %s', ('1',))
values = c.fetchall()
print(values)
r = c.fetchone()
print(r)
c.close()
db.close()