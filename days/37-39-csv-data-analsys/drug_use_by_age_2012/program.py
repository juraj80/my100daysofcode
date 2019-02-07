import csv
import sys

import logbook as logbook
import research

app_log = logbook.Logger('App')

def main():
    print('Drug Use By Age')
    research.init()

    print()

    msg = "Highest Percentage of those in a age group who used alcohol in the past 12 months"
    print(msg)
    print()
    data = research.highest_alcohol_use()
    for idx, r in enumerate(data[:5],1):
        print(f'{idx}. {r.alcohol_use} % of age group: {r.age} years used alcohol {int(r.alcohol_frequency)} number of times (median)')
    app_log.trace(f'QUERY: {msg}')
    print()

    msg = "Highest Percentage of those in a age group who used marijuana in the past 12 months"
    print(msg)
    print()
    data = research.highest_marijuana_use()
    for idx, r in enumerate(data[:5],1):
        print(f'{idx}. {r.marijuana_use} % of age group: {r.age} years used marijuana {int(r.marijuana_frequency)} number of times (median)')
    app_log.trace(f'QUERY:{msg}')
    print()
    msg = "Highest Percentage of those in a age group who used cocaine in the past 12 months"
    print(msg)
    print()
    data = research.highest_cocaine_use()
    for idx, r in enumerate(data[:5],1):
        print(f'{idx}. {r.cocaine_use} % of age group: {r.age} years used cocaine {int(r.cocaine_frequency)} number of times (median)')
    app_log.trace(f'QUERY:{msg}')


def init_logging(filename: str = None):
    level = logbook.TRACE

    if filename:
        logbook.TimedRotatingFileHandler(filename, level=level).push_application()
    else:
        logbook.StreamHandler(sys.stdout, level=level).push_application()

    msg = f'Logging initialized, level: {level}, mode: {"stdout mode" if not filename else "file mode: " + filename}'
    logger = logbook.Logger('Startup')
    logger.notice(msg)



if __name__ == '__main__':
    init_logging('research-app.log')
    main()