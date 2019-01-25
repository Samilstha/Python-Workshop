Q. Program to remove duplicates from Dictionary.
Solution:
    
student = {'id1': 
   {'name': ['Nishesh'], 
    'class': ['BCA'], 
   },
 'id2': 
  {'name': ['Reeshesh'], 
    'class': ['BCA'], 
       },
 'id3': 
    {'name': ['Nishesh'], 
    'class': ['BCA'], 
   },
 'id4': 
   {'name': ['Shrijal'], 
    'class': ['BCA'], 
       },
}

output = {}

for key,value in student.items():
    if value not in output.values():
        output[key] = value

print(output)
