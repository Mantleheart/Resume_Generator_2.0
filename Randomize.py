from random import randrange, random, choice
import csv


def getRandomEducation(fileName):
    index = 0
    data = dict()
    pairs = {'school': '',
             'degree': ''
             }
    with open(fileName) as file:
        file.seek(0, 0)
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            index += 1

            data[row[0]] = row[1].split(',')
        keys = data.keys()
        school = choice(list(keys))
        pairs['school'] = school
        pairs['degree'] = choice(data[school])
        return (pairs)


def getRandomSport(school, gender, path):
    genders = {
        'm': [2, 4],
        'f': [3, 5]
    }
    with open(path) as file:
        file.seek(0, 0)
        columns = file.readline().split(',')
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            if row[0] == school:
                select = choice(genders[gender])
                if row[select] == 'Y':
                    return (columns[select])
                else:
                    return (row[select])


def getRandomCity(school,path):
    city = ''
    with open(path) as file:
        file.seek(0, 0)
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            if row[0] == school:
                return (row[6]);


def getRandomAddress(school, path):
    address = ''
    with open(path) as file:
        file.seek(0, 0)
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            if row[0] == school:
                return (choice(row[8:11]));


def getRandomLine(filePath):
    file = open(filePath)
    length = sum(1 for line in file)
    seed = randrange(0, length)
    file.seek(0, 0)
    emails = file.readlines()
    file.close()
    return (emails[seed])


def getNamefromDemoGraphic(source):
    file = open(source)
    length = sum(1 for line in file)
    seed = randrange(0, length)
    file.seek(0, 0)
    names = file.readlines()
    file.close()
    return (names[seed])
    return (names)


def getRandomJob(city, path):
    select = randrange(0, 50)
    job = ''

    with open(path) as file:
        counter = 0
        file.seek(0, 0)
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            if row[0] == city:
                counter += 1
            if row[0] == city and counter >= select:
                return (choice(row[2:3]).replace('*', '•'));


def getAthletics(gender, school, city, sport):
    sex = ''
    if gender == 'f':
        sex = "Women"
    else:
        sex = "Men"
    if sport is None:
        sport = "Soccer"
    seed = randrange(1, 2)
    file = open('templates/sports_template' + str(seed) + '.txt')
    output = file.read()
    file.close()
    output = output.replace('#', sport)
    output = output.replace('$', sex)
    output = output.replace('%', school)
    output = output.replace('&', city)
    output = output.replace("Women's Women's", "Women's")
    output = output.replace("Men's Men's", "Men's")
    output = output.replace("(", "")
    output = output.replace(")", "")
    return (output);


def getRandomExperience(path):
    select = randrange(0, 50)
    job = ''

    with open(path) as file:
        counter = 0
        select = randrange(1, 200)
        file.seek(0, 0)
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            if counter >= select:
                return row[5]
            else:
                counter += 1

