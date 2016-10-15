from datetime import datetime, timedelta

coffee_time = datetime(year=2016, month=10, day=16, hour=8, minute=0)
stop_time = coffee_time + timedelta(minutes=30)

class Config(object):

    JOBS = [
        {
            'id': 'turn_on',
            'func': 'jobs:make_coffee',
	    'trigger': 'date',
	    'run_date': coffee_time.strftime('%Y-%m-%dT%H:%M'),
        },
        {
            'id': 'turn_off',
            'func': 'jobs:stop_coffee',
	    'trigger': 'date',
	    'run_date': stop_time.strftime('%Y-%m-%dT%H:%M'),
	    # 'trigger': 'interval',
	    # 'seconds': 5,
        },
    ]

    SCHEDULER_VIEWS_ENABLED = True
