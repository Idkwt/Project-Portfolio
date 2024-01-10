import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://facial-attendance-system-a4bc2-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "43":
        {
            "name": "Sahil Saeed",
            "major": "Computer Science",
            "starting_year":2021,
            "total_attendance":6,
            "Grade": "A",
            "Year": 3,
            "last_attendance_time": "2023-11-05 00:54:34"
            
        },
       "73":
        {
            "name": "Syed Mustufa Iqbal",
            "major": "Computer Science",
            "starting_year":2021,
            "total_attendance":8,
            "Grade": "B",
            "Year": 3,
            "last_attendance_time": "2023-11-05 00:54:34"
            
        },
       "D04":
        {
            "name": "Subhan Khan",
            "major": "Computer Science",
            "starting_year":2021,
            "total_attendance":4,
            "Grade": "C",
            "Year": 3,
            "last_attendance_time": "2023-11-05 00:54:34"
            
        }        
}

for key, value in data.items():
    ref.child(key).set(value)