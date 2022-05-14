# finalproject1
The url for the admin page
http://127.0.0.1:8000/admin/


libraryapi:

1.get all data
request:http://127.0.0.1:8000/bookapi/
response:[
    {
        "id": 6,
        "nameofbook": "HARRY POTTER",
        "statusofbook": "NOT BURROWED",
        "rollnoburrower": 0
    },
    {
        "id": 8,
        "nameofbook": "I CAN AND I WILL",
        "statusofbook": "not BURROWED",
        "rollnoburrower": 210047709
    },
    {
        "id": 9,
        "nameofbook": "HOW TO WIN FRIENDS AND INFLUENCE PEOPLE",
        "statusofbook": "BURROWED",
        "rollnoburrower": 200070056
    },
    {
        "id": 10,
        "nameofbook": "BELIEVE IN YOURSELF",
        "statusofbook": "BURROWED",
        "rollnoburrower": 210020008
    },
    {
        "id": 11,
        "nameofbook": "STOP OVERTHINKING",
        "statusofbook": "BURROWED",
        "rollnoburrower": 200046576
    },
    {
        "id": 12,
        "nameofbook": "THE POWER OF POSITIVE THINKING",
        "statusofbook": "BURROWED",
        "rollnoburrower": 210046076
    }
]

2.get single data
request:http://127.0.0.1:8000/bookapi/8
response:{
    "id": 8,
    "nameofbook": "I CAN AND I WILL",
    "statusofbook": "not BURROWED",
    "rollnoburrower": 210047709
}


3.post some new data
request:http://127.0.0.1:8000/bookapi/
response:{
    "msg": "Data created"
}


4.delete some data
request:http://127.0.0.1:8000/bookapi/7
response:{
    "msg": "Data DELETED"
}

5.PUT SOME DATA
REQUEST:http://127.0.0.1:8000/bookapi/<int:pk>
RESPONSE:{
    "msg": "Data Updated"
}


6.PATCH SOME DATA
REQUEST :http://127.0.0.1:8000/bookapi/<int:pk>
RESPONSE:{
    "msg": "Data Updated PARTIALLY"
}
