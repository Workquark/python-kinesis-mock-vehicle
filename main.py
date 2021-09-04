from taskscheduler.schedule import schedule
import os

if __name__ == '__main__':
    os.environ['AWS_DEFAULT_REGION'] = 'ap-south-1'
    schedule()

