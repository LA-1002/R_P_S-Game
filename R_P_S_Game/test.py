import json 
fileR = open('scores.json','r',encoding='utf-8')
js = json.load(fileR)
tot = js['totals']
games = js['games']
fileR.close();

game = {'Wins': 3, 'Loses': 3, 'Ties': 1}

games.append(game)



print(js)

fileW = open('scores.json','w',encoding='utf-8')
json.dump(js,fileW)
fileW.close();




