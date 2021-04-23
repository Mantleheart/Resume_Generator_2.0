from os import path
import glob
import random

def checkPath(dir, fName):
    if path.exists(dir + "/" + fName):
        if fName[-1].isdigit():
            newName = fName[:-1]
            fName = newName + str(int(fName[-1]) + 1)
            return(fName)
        else:
            return(fName + '1')
    else:
        return(fName)
    
def countFiles(dir, fName):
    return(len(glob.glob1(dir, fName + "*")))

def correctDates(input, start, finish, startMonth, finishMonth):
    monthVals = {
    "January": 1,
    "February":2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "Septemeber": 9,
    "October": 10,
    "November": 11,
    "December": 12
    }
    valMonths = {
    1:"January",
    2:"February",
    3:"March",
    4:"April",
    5:"May",
    6:"June",
    7:"July",
    8:"August",
    9:"Septemeber",
    10:"October",
    11:"November",
    12:"December"
    }

    
    isInternship = False
    internshipWords = ["internship", "Internship","Intern", "intern"]
    year = str(random.randint(int(start),int(finish)))
    
    #Use has-key method to find the month that appears in the resume and replace it.
    if input != None:
        words = input.split(' ')
        month = ''
        dateFound = ''
        secondFound = ''
        for index, word in enumerate(words):
            if word[0:2] == '20':
                    if word in internshipWords:
                        isInternship = True
                    words[index] = year
            
        return(' '.join(words))
        

