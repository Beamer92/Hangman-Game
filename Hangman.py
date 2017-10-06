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
           

#word = wordgen()
#word2 = wordgen()
#print(word + " " + str(len(word)))
#print(word2 + " " + str(len(word2)))
#noose() 

class Game():
    gameword = ""
    wordlen = 0
    linearr = []

    def __init__(self): # this method creates the class object.
        noose()
        self.gameword = wordgen()
        self.wordlen = len(self.gameword)
        self.linearr = []
    
    def setup_game(self):
        lines = self.wordlen
        xaxis = 10
        while lines > 0:
            letterline = Line(Point(xaxis,420), Point(xaxis + 20,420))
            letterline.draw(win)
            self.linearr.append(xaxis)
            lines -= 1
            xaxis += 30
    
    def find_letters(self, inputchar, word):
            print ([i for i, letter in enumerate(word) if letter == inputchar])

    def game_loop(self):
       # print(self.linearr)
        print(self.gameword)
        input1 = input("Take your first guess: ")
        if input1 in self.gameword:
                print("Yes")
                inst.find_letters(input1, self.gameword)
                lm = Image(Point(5,5), "letter_gifs/" + input1 + ".gif")
                lm.draw(win)
        else:
                 print("NO")

inst = Game()
inst.setup_game()
inst.game_loop()


