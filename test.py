import requests
import json
import names

#https://api.vk.com/method/users.get?user_id=210700286&v=5.52
token = 'aca32f92aca32f92aca32f9207acc9496daaca3aca32f92f06cc73a952c7dcdccf5ebe6'
sec_token= 'e776712380e515f55fb9a9cb51a4c6e7c7a162bdedc2145312c25a4432198aec014ac0396ca730a854ece'



def write_json1(data):
    with open('persons1.json', 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
def write_json2(data):
    with open('persons2.json', 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

def write_tfile(data):
    with open('friends.json', 'w') as file:
        for kek in data:
            json.dump(kek, file, indent=2, ensure_ascii=False)


def get_id():
    #ruk_name=names.zakup('ruk') #Цепляем пул из файла
    user_name= input('Имя: ') #Ввод имени вручную
    all_users = []

    #for name in ruk_name:
        #schetchik = []
    while True:
        r = requests.get('https://api.vk.com/method/users.search', params={'q': user_name,
                                                                           'count': 1000,

                                                                           'fields': 'screen_name',
                                                                           'version': 5.96,
                                                                           'access_token': sec_token})
        write_json1(r.json())
        users = r.json()['response'][1:]
        for id in users:
            all_users.append(id['uid'])
            #schetchik.append(id['uid'])
        if len(all_users) == r.json()['response'][0]:
            break

    return(all_users)


def get_friend_id():
    #zak_name=names.zakup('zak') #Цепляем пул из файла
    user_name = input('Имя 2: ') #Ввод имени вручную
    all_users = []
    #for name in zak_name:
    while True:
        r = requests.get('https://api.vk.com/method/users.search', params={'q': user_name,
                                                                           'count': 1000,
                                                                           'fields': 'screen_name',
                                                                           'version': 5.96,
                                                                           'access_token': sec_token})
        try:
            users = r.json()['response'][1:]
            for id in users:
                all_users.append(id['uid'])
            #write_json2(r.json())
            if len(all_users) == r.json()['response'][0]:
                break
        except KeyError:
            pass
    return(all_users)

def friends():
    all_users= get_id()
    friend=[]

    for user_id in all_users:
        r = requests.get('https://api.vk.com/method/friends.get', params={'user_id' : user_id,
                                                                          'order' : 'name',
                                                                          'count' : 1000,
                                                                          #'offset' : 5,
                                                                          'fields' : 'city',
                                                                          'ins' : 'ins',
                                                                          'version': 5.96,
                                                                          'access_token': token})
        try:
            users = r.json()['response']
            friend.extend(users)
        except KeyError:
            pass
    #write_tfile(friend)
    return(friend)

def friends_finder():
    all_friends = friends()
    one_friend_id = get_friend_id()

    for pers_id in one_friend_id:
        for friend in all_friends:
            if pers_id == friend["uid"]:
                print(pers_id)


def main():
    print((friends_finder()))


if __name__ == '__main__':
    main()