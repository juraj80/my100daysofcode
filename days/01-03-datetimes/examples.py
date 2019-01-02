from datetime import datetime
import re

line = 'INFO 2014-07-03T23:27:51 supybot Shutdown complete'
loglines = ['ERROR 2014-07-03T23:24:31 supybot Invalid user dictionary file',
            'INFO 2016-10-03T10:12:00 supybot Shutdown initiated.',
            'INFO 2016-10-03T10:15:31 supybot Shutdown initiated.']

SHUTDOWN_EVENT = 'Shutdown initiated'

# for you to code:

def convert_to_datetime(line):
    '''TODO 1:
       Given a log line extract its timestamp and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)'''
    words = line.split(" ")
    timestr = re.split("[T \-:]+",words[1])
    year = int(timestr[0])
    month = int(timestr[1])
    day = int(timestr[2])
    hour = int(timestr[3])
    minute = int(timestr[4])
    seconds = int(timestr[5])
    return datetime(year,month,day,hour,minute,seconds)

def time_between_shutdowns(loglines):
    '''TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and calculate the
       timedelta between the first and last one.
       Return this datetime.timedelta object.'''
    result = []
    for line in loglines:
        if SHUTDOWN_EVENT in line:
            timestamp = convert_to_datetime(line)
            result.append(timestamp)
    start =result[0]
    end = result[-1]
    timediff = end - start
    return timediff

def test_convert_to_datetime():
    line1 = 'ERROR 2014-07-03T23:24:31 supybot Invalid user dictionary file'
    line2 = 'INFO 2015-10-03T10:12:51 supybot Shutdown initiated.'
    line3 = 'INFO 2016-09-03T02:11:22 supybot Shutdown complete.'
    assert convert_to_datetime(line1) == datetime(2014, 7, 3, 23, 24, 31)
    assert convert_to_datetime(line2) == datetime(2015, 10, 3, 10, 12, 51)
    assert convert_to_datetime(line3) == datetime(2016, 9, 3, 2, 11, 22)


def test_time_between_events():
    diff = time_between_shutdowns(loglines)
    assert type(diff) == timedelta
    assert str(diff) == '0:03:31'

def main():
    test_convert_to_datetime()
    time_between_shutdowns(loglines)

if __name__ == '__main__':
    main()