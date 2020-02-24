import requests
import json
import random as ran
import html
print ('You gonna play quiz now!')
input ('To start on "Easy" press enter:')
counter = 0
while True:
    print ('-----------------------------------')
    r = requests.get ('https://opentdb.com/api.php?amount=1&difficulty=easy')
    if (r.status_code != 200):
        print ('Sorry, server is unavailable, check your connection and re-execute code!')
        break
    questik = json.loads (r.text)
    quest = questik['results']
    q = quest[0]
    print ('Category is ' + '"' + html.unescape(q['category']) + '"' + '.')
    print ('Your question is: \n' + html.unescape(q['question']))
    if q['type'] == 'boolean':
        ans = input ('\nIf you agree type "True", either type "False": ')
        if ans == html.unescape(q['correct_answer']):
            print ('You are absolutely right!')
            counter += 1
        else:
            print ('Oh no! It is incorrect answer, go to next question.')
    else:
        answers = html.unescape(q['incorrect_answers'])
        place = ran.randint(0, len(answers))
        answers.insert(place, html.unescape(q['correct_answer']))
        print ('\nHere are available answers:')
        keks = 0
        for answer in answers:
            keks += 1
            print (str(keks) + ' - ' + html.unescape(answer))
        ans = input ('\nChoose the number of the correct answer: ')
        if int(ans) - 1 == place:
            print ('You are absolutely right!')
            counter += 1
        else:
            print ('Oh no! It is incorrect answer, the correct was : ' + str(place + 1) + ' - ' + html.unescape(q['correct_answer']) + '.')
    print ('Your score now is: ' + str(counter))
    go = input ('To continue press enter. If you want to stop - type "stop": ')
    if go.lower() == 'stop':
        break

            
            
        
