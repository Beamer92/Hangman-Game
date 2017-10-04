from graphics import *
import requests
import keys
import json
import random

win = GraphWin('Hangman', 500, 500)

def noose():
#draw the hangman's noose to start
    leg1 = Line(Point(430,430), Point(480, 480))
    leg1.draw(win)

    midbar = Line(Point(430,430), Point(399,430))
    midbar.draw(win)

    leg2 = Line(Point(399,430), Point(349,480))
    leg2.draw(win)

    pole = Line(Point(415,430), Point(415, 50))
    pole.draw(win)

    cross = Line(Point(415,50), Point(315,50))
    cross.draw(win)

    drop = Line(Point(315,50), Point(315,80))
    drop.draw(win)
    
    brace = Line(Point(415,80), Point(385, 50))
    brace.draw(win) 
       

def wordgen():
    #One way to do without an API, produces words nobody would know 99% of the time
    #word = requests.get('http://setgetgo.com/randomword/get.php').text
    #print(word)

    #uses API key from wordnik, grabs 26 words between 7-10 characters that have at least 15 dictionary entries(?) so they're knowable words
    #randomly select number between 0-25 and returns that word
    ker = keys.api_key
    urlstring = "http://api.wordnik.com/v4/words.json/randomWords?minCorpusCount=10000&minDictionaryCount=15&excludePartOfSpeech=proper-noun,proper-noun-plural,proper-noun-posessive,suffix,family-name,idiom,affix&hasDictionaryDef=true&includePartOfSpeech=noun,verb,adjective,definite-article,conjunction&limit=26&maxLength=10&minLength=7&api_key="
    callstring = urlstring + ker
    response = requests.get(callstring)
    wordlist =  response.json()
    wordnum = random.randint(0,25)
    wordchoice = wordlist[wordnum]['word']
    return (wordchoice)

noose() 
wordgen()