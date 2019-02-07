import csv
import research

def main():
    print('Drug Use By Age')
    research.init()

    print("Highest Percentage of those in a age group who used marijuana in the past 12 months")
    print()
    data = research.highest_marijuana_use()
    for idx, r in enumerate(data[:5],1):
        print(f'{idx}. {r.marijuana_use} % of age group: {r.age} years used marijuana {int(r.marijuana_frequency)} number of times (median)')
    print()
    print("Highest Percentage of those in a age group who used cocaine in the past 12 months")
    print()
    data = research.highest_cocaine_use()
    for idx, r in enumerate(data[:5],1):
        print(f'{idx}. {r.cocaine_use} % of age group: {r.age} years used cocaine {int(r.cocaine_frequency)} number of times (median)')






if __name__ == '__main__':
    main()