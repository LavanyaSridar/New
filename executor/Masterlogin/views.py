from django.shortcuts import render
from datetime import datetime
from Masterlogin.models import CalculationLog



# Create your views here.
from django.shortcuts import render
import mysql.connector as sql

ema=''
pwod=''
# Create your views here.
def Mastlogin(request):
    global ema,pwod
    if request.method=="POST":
        s=sql.connect(host="localhost",user="root",passwd="admin",database='website')
        cursor=s.cursor()
        c=request.POST
        for key,value in c.items():
            if key=="email":
                ema=value
            if key=="password":
                pwod=value
        
        e="select * from Mastsign where email='{}' and password='{}'".format(ema,pwod)
        cursor.execute(e)
        f=tuple(cursor.fetchall())
        if f==():
            return render(request,'error.html')
        else:
            return render(request,"welcome.html")

    return render(request,'Masterlogin.html')




def zero(func=None, *args):
    return func(0, *args) if func else 0


def one(func=None, *args):
    return func(1, *args) if func else 1


def two(func=None, *args):
    return func(2, *args) if func else 2


def three(func=None, *args):
    return func(3, *args) if func else 3


def four(func=None, *args):
    return func(4, *args) if func else 4


def five(func=None, *args):
    return func(5, *args) if func else 5


def six(func=None, *args):
    return func(6, *args) if func else 6


def seven(func=None, *args):
    return func(7, *args) if func else 7


def eight(func=None, *args):
    return func(8, *args) if func else 8


def nine(func=None, *args):
    return func(9, *args) if func else 9


def plus(num):
    return lambda x: x + num


def minus(num):
    return lambda x: x - num


def times(num):
    return lambda x: x * num


def divided_by(num):
    return lambda x: x // num


def calculate(request):
    result = ''  # Define the result variable outside the if statement
    if request.method == 'POST':
        expression = request.POST.get('expression', '')  # assuming the input field name is 'expression'
        result = eval(expression)
        log_entry = CalculationLog(expression='expression', result=result)
        log_entry.save()
    context = {'result': result}
    return render(request, 'result.html', context)
    

def show_logs(request):
    logs = CalculationLog.objects.all()
    context = {'logs': logs}
    return render(request, 'log.html', context)
