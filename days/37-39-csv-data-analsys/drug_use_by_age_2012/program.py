import csv
import research

def main():
    print('Drug Use By Age')
    research.init()

    print("Highest Percentage of those in a age group who used marijuana in the past 12 months")
    data = research.highest_marijuana_use()
    for idx, r in enumerate(data[:5],1):
        print(f'{idx}. % of age group: {r.age} who used marijuana in the past 12 months: {r.marijuana_use} %')



if __name__ == '__main__':
    main()