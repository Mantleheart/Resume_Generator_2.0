from random import randrange, random, choice
from Generator import *
import numpy

# variables:

stats = {'w': 0,
         'b': 0,
         'h': 0,
         'a': 0,
         }


def generateRace(params):
    race = ''
    total = float(params["White"]) + float(params["Asian"]) + float(params["Black"]) + float(params["Hispanic"])
    white = int((float(params["White"])/total) * 25)
    black = int((float(params["Black"])/total) * 25)
    asian = int((float(params["Asian"])/total) * 25)
    hispanic = (float(params["Hispanic"])/total) * 25
    
    
    seed = int(random() * total * 25)
    if 0 <= seed < white:
        race = 'w'
    if white <= seed < white + black:
        race = 'b'
    if white + black <= seed < white + black + hispanic:
        race = 'h'
    if white + black + hispanic <= seed <= white + black + hispanic + asian:
        race = 'a'
    return race


def generateSex(params):
    seed = numpy.random.uniform(0.0,1.0);
    if seed < float(params["GenderRatio"]):
       return('m')
    else:
        return('f')
    
    
    

# path is the primary data file
def getPair(path,params):
    return generate(generateRace(params), generateSex(params), path, params)
