import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' : "https://faceattendancerealtimeusingai-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "456456" :
        {
            "Name" : "Lalit Malik",
            "Major" : "CSE",
            "Starting_Year" : 2023,
            "Total_Attendance" : 10,
            "Standing" : "G",
            "Year" : 3,
            "Last_Attendance_Time" : "2025-10-30 00:54:34",

        },
    "852741" :
        {
            "Name" : "Emily Blunt",
            "Major" : "IT",
            "Starting_Year" : 2023,
            "Total_Attendance" : 8,
            "Standing" : "G",
            "Year" : 3,
            "Last_Attendance_Time" : "2025-10-20 00:54:34",

        },
    "963852" :
        {
            "Name" : "Elon Musk",
            "Major" : "ECE",
            "Starting_Year" : 2023,
            "Total_Attendance" : 4,
            "Standing" : "B",
            "Year" : 3,
            "Last_Attendance_Time" : "2025-09-01 00:54:34",

        }

}

for key, value in data.items():
    ref.child(key).set(value)