def person_is_seller(person):
    if person[len(person)-1] == 'm':
        return True
    return False


def search_seller_of_mango(dict):
    from collections import deque
    search_queue = deque()
    search_queue += dict['you']
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + ' is seller mango')
                return True
            else:
                if person in dict.keys():
                    search_queue += dict[person]
                    searched.append(person)
    return False 

my_friends = {'you':['julia', 'german', 'valya'],
            'julia':['lera', 'john'],
            'german':['dmitr', 'hamam'],
            'valya':['chup']}
search_seller_of_mango(my_friends)
print( float("inf"))