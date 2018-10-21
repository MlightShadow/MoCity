# -*- coding: UTF-8 -*-

person = {
    'name': 'xiaoPang',
    'hp': 100,
    'food': 100,
    'water': 100,
    'ap': 5.0,
    'position': '1-1',
    'bag': []
}

item = {
    '0001': {
        'name': 'item0001'
    },
    '0002': {
        'name': 'item0002'
    },
    '0003': {
        'name': 'item0003'
    },
}

op = 0

# 人物属性修改方法
def attribute(type, num):
    person[type] = person[type] + num
    print(type, num)




def search():

    print('find a taotao, sweet')

def turnEnd():
    person['ap'] = 5.0
    print('end turn')



def isDead():
    if person['hp'] <= 0:
        print('you dead')
        exit()

def life():
    if person['food'] < -30 or person['water'] < -10:
        attribute('hp', -10)
        isDead()

def turnStart():
    attribute('food', -10)
    attribute('water', -10)
    life()
    print('hp%d, food%d, water%d' % (person['hp'], person['food'], person['water']))

def doSomeThing():
    while(person['ap'] > 0):
        op = input('lets do some thing ')
        if op == 'search':
            search() 
            attribute('ap', -1)


while(1):
    turnStart()
    doSomeThing()
    turnEnd()