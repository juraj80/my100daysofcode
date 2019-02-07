import csv
import os
from collections import namedtuple
from typing import List

import logbook

research_log = logbook.Logger('Research')

data = []

Record = namedtuple('Record', 'age,n,alcohol_use,alcohol_frequency,marijuana_use,marijuana_frequency,cocaine_use,'
                              'cocaine_frequency,crack_use,crack_frequency,heroin_use,heroin_frequency,hallucinogen_use,'
                              'hallucinogen_frequency,inhalant_use,inhalant_frequency,pain_releiver_use,'
                              'pain_releiver_frequency,oxycontin_use,oxycontin_frequency,tranquilizer_use,'
                              'tranquilizer_frequency,stimulant_use,stimulant_frequency,meth_use,meth_frequency,'
                              'sedative_use,sedative_frequency')


def init():
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, 'data', 'drug-use-by-age.csv')

    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)

        data.clear()
        for row in reader:
            for key, value in row.items():
                if value == '-':
                    row[key] = 0
            record = parse_row(row)
            data.append(record)

    research_log.trace(f'Loading a CSV file {filename} and parsing of data successful')


def parse_row(row):
    row['n'] = int(row['n'])
    row['alcohol-use'] = float(row['alcohol-use'])
    row['alcohol-frequency'] = float(row['alcohol-frequency'])
    row['marijuana-use'] = float(row['marijuana-use'])
    row['marijuana-frequency'] = float(row['marijuana-frequency'])
    row['cocaine-use'] = float(row['cocaine-use'])
    row['cocaine-frequency'] = float(row['cocaine-frequency'])
    row['crack-use'] = float(row['crack-use'])
    row['crack-frequency'] = float(row['crack-frequency'])
    row['heroin-use'] = float(row['heroin-use'])
    row['heroin-frequency'] = float(row['heroin-frequency'])
    row['hallucinogen-use'] = float(row['hallucinogen-use'])
    row['hallucinogen-frequency'] = float(row['hallucinogen-frequency'])
    row['inhalant-use'] = float(row['inhalant-use'])
    row['inhalant-frequency'] = float(row['inhalant-frequency'])
    row['pain-releiver-use'] = float(row['pain-releiver-use'])
    row['pain-releiver-frequency'] = float(row['pain-releiver-frequency'])
    row['oxycontin-use'] = float(row['oxycontin-use'])
    row['oxycontin-frequency'] = float(row['oxycontin-frequency'])
    row['tranquilizer-use'] = float(row['tranquilizer-use'])
    row['tranquilizer-frequency'] = float(row['tranquilizer-frequency'])
    row['stimulant-use'] = float(row['stimulant-use'])
    row['stimulant-frequency'] = float(row['stimulant-frequency'])
    row['meth-use'] = float(row['meth-use'])
    row['meth-frequency'] = float(row['meth-frequency'])
    row['sedative-use'] = float(row['sedative-use'])
    row['sedative-frequency'] = float(row['sedative-frequency'])

    record = Record(age=row['age'], n=row['n'], alcohol_use=row['alcohol-use'],
                    alcohol_frequency=row['alcohol-frequency'], marijuana_use=row['marijuana-use'],
                    marijuana_frequency=row['marijuana-frequency'],
                    cocaine_use=row['cocaine-use'], cocaine_frequency=row['cocaine-frequency'],
                    crack_use=row['crack-use'], crack_frequency=row['crack-frequency'], heroin_use=row['heroin-use'],
                    heroin_frequency=row['heroin-frequency'], hallucinogen_use=row['hallucinogen-use'],
                    hallucinogen_frequency=row['hallucinogen-frequency'], inhalant_use=row['inhalant-use'],
                    inhalant_frequency=row['inhalant-frequency'], pain_releiver_use=row['pain-releiver-use'],
                    pain_releiver_frequency=row['pain-releiver-frequency'], oxycontin_use=row['oxycontin-use'],
                    oxycontin_frequency=row['oxycontin-frequency'], tranquilizer_use=row['tranquilizer-use'],
                    tranquilizer_frequency=row['tranquilizer-frequency'], stimulant_use=row['stimulant-use'],
                    stimulant_frequency=row['stimulant-frequency'], meth_use=row['meth-use'],
                    meth_frequency=row['meth-frequency'], sedative_use=row['sedative-use'],
                    sedative_frequency=row['sedative-frequency'])

    return record


def highest_alcohol_use() -> List[Record]:
    return sorted(data, key=lambda r: r.alcohol_use, reverse=True)


def highest_marijuana_use() -> List[Record]:
    return sorted(data, key=lambda r: r.marijuana_use, reverse=True)


def highest_cocaine_use() -> List[Record]:
    return sorted(data, key=lambda r: r.cocaine_use, reverse=True)
