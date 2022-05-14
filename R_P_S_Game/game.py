import random
import json
rck = '''
##########
##########
##########
##########
##########
'''
pap = '''
##########
|        |
|        |
|        |
##########
'''
sci = '''
\     /
 \   /  
   X    
  / \ 
[]   []
'''
vs1 = '''
# #################### #
# \       / ========   #
#  \     /  |          #  
#   \   /   |======|   #
#    \ /           |   #
#     v     =======|   #
# #################### #
'''

vs = [
'      \       / ========        ',
'       \     /  |               ', 
'        \   /   |======|        ',
'         \ /           |        ',
'          v     =======|        ',
]



scores = {
    'Wins': 0,
    'Loses': 0,
    'Ties': 0,
}


choices = {
 'R':{
    'id':'R',
    'Win':'Scissors',
    'Lose':'Paper',
    'art': [
        '##########',
        '##########',
        '##########',
        '##########',
        '##########',
    ]
},
'P':{
    'id':'P',
    'Win':'Rock',
    'Lose':'Scissors',
    'art': [
    '##########',
    '|        |',
    '|        |',
    '|        |',
    '##########',
    ]
},
'S':{
    'id':'S',
    'Win':'Paper',
    'Lose':'Rock',
    'art': [
    '\     /',
    ' \   / ', 
    '   X   ', 
    '  / \  ',
    '[]   []',
    ]
},
}

loop = True
while loop:
    pick = input('Pick R,P,S : ')
    print('############')
    pick = pick.upper();
    opt = ['R','P','S']
    lines = [];
    if pick in opt:
        ran2 = random.randrange(0,3)
        p1 = choices[pick]
        p2 = choices[opt[ran2]]
        for i in range(5):
            line = str(p1['art'][i] + vs[i] + p2['art'][i] + '\n')
            lines.append(line)
            
        #You WIN
        if (p1['Win'] == p2['Lose']):
            print('YOU WIN')
            print('############')
            scores['Wins'] = scores['Wins'] + 1
        #You LOSE
        elif (p1['Lose'] == p2['Win']):
            print('YOU LOSE')
            print('############')
            scores['Loses'] = scores['Loses'] + 1
        #You DRAW
        elif (p1['id'] == p2['id']):
            print('YOU TIE')
            print('############')
            scores['Ties'] = scores['Ties'] + 1
        print('\n')
        text = ''
        for line in lines:
            text = text + str(line)
        print(text)
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






