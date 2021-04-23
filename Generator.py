from Randomize import *
import csv
import datetime
from util import correctDates

def generate(race, sex, path, param):
    graduates = {'control':
        {
            'email': '',
            'address': '',
            'number': '',
            'fname': '',
            'gender': '',
            'lname': '',
            'email': '',
            'school': '',
            'degree': '',
            'city': '',
            'work1': '',
            'work2': '',
            'work3': '',
            'skills': '',
            'race':'',
            'sex':''
        }
        ,

        'test':
            {
                'email': '',
                'address': '',
                'number': '',
                'fname': '',
                'gender': '',
                'lname': '',
                'email': '',
                'school': '',
                'degree': '',
                'sport': '',
                'city': '',
                'work1': '',
                'work2': '',
                'work3': '',
                'skills': '',
                'race':'',
                'sex':''
            }
    }

    school = getRandomEducation(path)

    #
    #  CONTROL CASE
    #
    graduates['control']['sex'] = sex
    graduates['control']['race'] = race
    graduates['control']['email'] = getRandomLine('emails/' + race + 'email.txt').strip()
    graduates['control']['fname'] = (getRandomLine('names/' + sex + graduates['control']['email'][0] + race + 'names.txt')).strip()
    graduates['control']['lname'] = graduates['control']['email'][2:(len(graduates['control']['email']) - 16)]
    graduates['control']['gender'] = sex
    graduates['control']['school'] = school['school']
    graduates['control']['degree'] = school['degree']
    graduates['control']['city'] = getRandomCity(school['school'], path)
    graduates['control']['work1'] = getRandomJob(graduates['control']['city'], param["workPath"])
    graduates['control']['work1'] = correctDates(graduates['control']['work1'], param["BeginYear"], param["EndYear"], param["BeginMonth"], param["EndMonth"])
    
    graduates['control']['work2'] = getRandomJob(graduates['control']['city'], param["workPath"])
    
    graduates['control']['work2'] = correctDates(graduates['control']['work2'], param["BeginYear"], param["EndYear"], param["BeginMonth"], param["EndMonth"])
    
    graduates['control']['work3'] = correctDates(graduates['control']['work3'], param["BeginYear"], param["EndYear"], param["BeginMonth"], param["EndMonth"])
    
    
    graduates['control']['skills'] = getRandomExperience(param["workPath"])
    graduates['control']['address'] = getRandomAddress(school['school'], path)
    graduates['control']['number'] = '(414) 368-0558'
    #
    #  TEST CASE
    #

    WorkParagraph = getRandomJob(graduates['test']['city'],path)

    graduates['test']['sex'] = sex
    graduates['test']['race'] = race
    graduates['test']['email'] = getRandomLine('emails/' + race + 'email.txt').strip()
    graduates['test']['fname'] = (getRandomLine('names/' + sex + graduates['test']['email'][0] + race + 'names.txt')).strip()
    graduates['test']['lname'] = graduates['test']['email'][2:(len(graduates['test']['email']) - 16)]
    graduates['test']['gender'] = sex
    graduates['test']['school'] = school['school']
    graduates['test']['degree'] = school['degree']
    graduates['test']['sport'] = getRandomSport(school['school'], graduates['test']['gender'], path)
    
    graduates['test']['work1'] = getAthletics(sex,school['school'],getRandomCity(school['school'],path),graduates['test']['sport'])
    graduates['test']['work1'] = correctDates(graduates['test']['work1'], param["BeginYear"], param["EndYear"], param["BeginMonth"], param["EndMonth"])
    graduates['test']['city'] = getRandomCity(school['school'], path)
    graduates['test']['work2'] = correctDates(WorkParagraph, param["BeginYear"], param["EndYear"], param["BeginMonth"], param["EndMonth"])
    graduates['test']['skills'] = getRandomExperience(param["workPath"])
    graduates['test']['address'] = getRandomAddress(school['school'].replace('\r', ', '), path)
    graduates['test']['number'] = '267-281-4278'

    return graduates
