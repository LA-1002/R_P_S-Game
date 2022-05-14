import random
import json
rck = '##########\n##########\n##########\n##########\n##########'

pap = '##########\n|        |\n|        |\n|        |\n##########'
     
sci = '\       /\n\   /  \n  X    \n/    \\n[]      []\n'

scores = {
    'Wins': 0,
    'Loses': 0,
    'Ties': 0
}


choices = {
 'R':{
    'id':'R',
    'Win':'Scissors',
    'Lose':'Paper'
},
'P':{
    'id':'P',
    'Win':'Rock',
    'Lose':'Scissors'
},
'S':{
    'id':'S',
    'Win':'Paper',
    'Lose':'Rock'
},
}

loop = True
while loop:
    pick = input('Pick R,P,S : ')
    opt = ['R','P','S']
    pick = pick.upper();
    if pick in opt:
        ran2 = random.randrange(0,3)
        p1 = choices[pick]
        p2 = choices[opt[ran2]]
        #You WIN
        if (p1['Win'] == p2['Lose']):
            print('############')
            print('YOU WON')
            scores['Wins'] = scores['Wins'] + 1
        #You LOSE
        elif (p1['Lose'] == p2['Win']):
            print('############')
            print('YOU LOSE')
            scores['Loses'] = scores['Loses'] + 1
        #You DRAW
        elif (p1['id'] == p2['id']):
            print('############')
            print('YOU DRAW')
            scores['Ties'] = scores['Ties'] + 1
        print('############')
        out = input('AGAIN Y/N : ')
        print('############')
        if out.upper() == 'N':
            loop = False

print(scores)
fileR = open('scores.json','r',encoding='utf-8')
js = json.load(fileR)
tot = js['totals']
games = js['games']
fileR.close();

tot['Wins'] = int(tot['Wins']) + scores['Wins']
tot['Loses'] = int(tot['Loses']) + scores['Loses']
tot['Ties'] = int(tot['Ties']) + scores['Ties']
games.append(scores)

fileW = open('scores.json','w',encoding='utf-8')
json.dump(js,fileW)
fileW.close();






