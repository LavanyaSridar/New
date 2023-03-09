from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import mysql.connector as sql
fname=''
lname=''
sex=''
ema=''
pwod=''
# Create your views here.
def Mastsignup(request):
    global fname,lname,sex,ema,pwod
    if request.method=="POST":
        s=sql.connect(host="localhost",user="root",passwd="admin",database='website')
        cursor=s.cursor()
        c=request.POST
        for key,value in c.items():
            if key=="first_name":
                fname=value
            if key=="last_name":
                lname=value
            if key=="sex":
                sex=value
            if key=="email":
                ema=value
            if key=="password":
                pwod=value
        
        e="insert into Mastsign Values('{}','{}','{}','{}','{}')".format(fname,lname,sex,ema,pwod)
        cursor.execute(e)
        s.commit()

    return render(request,'Mastersignup.html')

