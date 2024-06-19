from django.shortcuts import render
from datetime import *
def home(request):
    current_time = datetime.now()
    past_time = current_time - timedelta(days=2, hours=5)
    context = {
        'employee': {
            'name': 'Md Abdullah All Mamun',
            'age': 22,
            'experience': 2,
            'intro':"I'm mamun"
        },
        'problems': {
            'capfirst': 'mamun all',
            'center': 'Mamun',
            'cut': 'abdullah all mamun',
            'date': datetime(2024, 6, 18),
            'default1':'hello',
            'default':'',
            'dictsort':[
                {'name':'md','age':12},
                {'name':'abdullah','age':13},
                {'name':'mamun','age':14},
            ],
            'divisibleby':21,
            'escape':'<script>alert("Hello, world!");</script>',
            'filesizeformat':3253151,
            'array':[1,2,3,4,5,6,7],
            'linenumbers':"""One
                Two
                Three
                Four""",
            'line':"hamba hamba o hamba goru ailo re",
            'cu_date':current_time,
            'comment_date':past_time,
        },
        'Earthly':{
            'array':[1,2,3,4,5,6,5,4,6],
            'date':datetime(2024, 6, 18),
            'default':'',
            'num':12,
            'name':'md abdullah all mamun',
            'students':[
                                
                {'name':'tinni','age':22,'id':58},
                {'name':'mamun','age':22,'id':75},
                {'name':'nahian','age':22,'id':78},
                {'name':'trisha','age':22,'id':56},
                {'name':'nahid','age':22,'id':35},
                {'name':'niloy','age':22,'id':51},

            ]
            ,
            'escape':'<script>alert("Hello, world!");</script>',
            'lines':"""one
            two 
            three 
            four
            get on the 
            dance floor
            """,
            'time':datetime.now(),
        },
        'Departments':['Cse','EEE','Civil'],

    }
    return render(request, "index.html", context)
