# - The way a taxi ride is priced is as follows:
# 1. Initial charge 1 EUR (as soon as the taxi starts moving)
# 2. .50 EUR per 1/5 th of a mile
# 3. .50 additional EUR between 8PM and 6AM
# 4. 1 EUR additional for busy periods between 4PM and 7PM
# E.g. John gets in the taxi at 1PM (13:00) – not a busy period – and rides for 2 miles. His fare
# is computed as follows:
# 1 EUR + (2 / (1/5)) * .50 EUR = 6 EUR

NIGHT_START_HOUR = '20'
NIGHT_END_HOUR   = '06'
BUSY_START_HOUR  = '16'
BUSY_END_HOUR    = '19'
INITIAL_CHARGE   = 1
COST_PER_MILE    = 0.5 / (1/5)
NIGHT_EXTRA_COST = 0.5
BUSY_EXTRA_COST  = 1
RIDES            = [
    {
        "id": 1,
        "distance": 2,
        "startTime": "2020-06-19T13:01:17.031Z",
        "duration": 9000
    },
    {
        "id": 2,
        "distance": 1,
        "startTime": "2020-06-19T12:01:17.031Z",
        "duration": 6000
    },
    {
        "id": 3,
        "distance": 5,
        "startTime": "2020-06-19T14:01:17.031Z",
        "duration": 7000
    },
    {
        "id": 4,
        "distance": 4,
        "startTime": "2020-06-19T08:32:45.031Z",
        "duration": 6500
    },
    {
        "id": 5,
        "distance": 2,
        "startTime": "2020-10-24T23:06:27.031Z",
        "duration": 3000
    },
        {
        "id": 6,
        "distance": 1,
        "startTime": "2020-10-29T18:35:22.391Z",
        "duration": 9000
    },
    {
        "id": 7,
        "distance": 3,
        "startTime": "2020-11-01T11:28:05.031Z",
        "duration": 5000
    },
    {
        "id": 8,
        "distance": 1,
        "startTime": "2020-11-06T03:55:07.031Z",
        "duration": 7000
    }
]
