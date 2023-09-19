import mysql.connector as myc
mydb=myc.connect(host='localhost',user='root',password='ryan',database='raw')
cur=mydb.cursor()
#name=input('Enter target name: ')
insval="SELECT * FROM humdata" 
try:
    cur.execute(insval)
    result = cur.fetchone()
    print(result)
    mydb.close()
    print('done')
except Exception:
    print('sorry')