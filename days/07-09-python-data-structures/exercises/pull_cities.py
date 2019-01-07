from data import us_state_abbrev


def get_list_from_dictionary(states=us_state_abbrev):
    lst=[]
    for key,value in states.items():
        lst.append((key,value))
    return lst



def main():
    dict_of_states = us_state_abbrev
    list_of_states = get_list_from_dictionary()

    # print out the 10th item in each
    print(list_of_states[10])

    states_keys = [state for state in dict_of_states.keys()]
    item10 = states_keys[10]
    print(item10,dict_of_states[item10])

    # print out the 45th key in the dictionary
    print(states_keys[44])

    # print out the 27th value in the dictionary
    states_values = [state for state in dict_of_states.values()]
    print(states_values[26])

    # replace the 15th key in the dictionary with the 28th item in the list
    item28 = list_of_states[27]
    key15 = states_keys[14]

    dict_of_states[item28[0]] = dict_of_states[key15]
    del dict_of_states[key15]
    print('item28=',item28[0])
    print('key15=',key15)
    print(dict_of_states)




if __name__ == '__main__':
    main()

