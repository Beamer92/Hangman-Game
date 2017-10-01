from graphics import *
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
    
    
    
    
noose()    
    
