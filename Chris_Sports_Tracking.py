import csv
import os

count  = 1
##Loops 3 times, assigns the name and win for each sport to variables.
while  count  <= 3:
    print('Who are we counting for?')
    person = input()
    sport = "MLB"
    mlb_win = input('How many ' + sport + ' wins for ' + person + '? ')
    mlb_loses = input('How many ' + sport + ' loses for ' + person + '? ')
    mlb_pushes = input('How many ' + sport + ' pushes for ' + person + '? ')
    sport = "NFL"
    nfl_win = input('How many ' + sport + ' wins for ' + person + '? ')
    nfl_loses = input('How many ' + sport + ' loses for ' + person + '? ')
    nfl_pushes = input('How many ' + sport + ' pushes for ' + person + '? ')
    sport = "NCAA"
    ncaa_win = input('How many ' + sport + ' wins for ' + person + '? ')
    ncaa_loses = input('How many ' + sport + ' loses for ' + person + '? ')
    ncaa_pushes = input('How many ' + sport + ' pushes for ' + person + '? ')
    print('----')
#Assigns print output to variables MLB wins and the person
    mlb_win_output = (person + "'s MLB wins = " + mlb_win + '\n')
    mlb_loses_output = (person + "'s MLB loses = " + mlb_loses + '\n')
    mlb_pushes_output = (person + "'s MLB pushes = " + mlb_pushes + '\n')
    mlb_output = (mlb_win_output + mlb_loses_output + mlb_pushes_output)
#Assigns print output to variables NFL wins and the person
    nfl_win_output = (person + "'s NFL wins = " + nfl_win + '\n')
    nfl_loses_output = (person + "'s NFL loses = " + nfl_loses + '\n')
    nfl_pushes_output = (person + "'s NFL pushes = " + nfl_pushes + '\n')
    nfl_output = (nfl_win_output + nfl_loses_output + nfl_pushes_output)
#Assigns print output to variables NCAA wins and the person
    ncaa_win_output = (person + "'s NCAA wins = " + ncaa_win + '\n')
    ncaa_loses_output = (person + "'s NCAA loses = " + ncaa_loses + '\n')
    ncaa_pushes_output = (person + "'s NCAA pushes = " + ncaa_pushes + '\n')
    ncaa_output = (ncaa_win_output + ncaa_loses_output + ncaa_pushes_output)

#Prints user and sport wins in user friendly text
    print(mlb_output)
    print(nfl_output)
    print(ncaa_output)
##Saves output variable to a .txt file that matches the person variable
    with open(person + '.txt', 'w')as f:
        f.write('--------------------------------------- \n' + mlb_output + '--------------------------------------- \n' + nfl_output + '--------------------------------------- \n'+ ncaa_output)
        f.close
    print('Wrote results to ' + person + '.txt')
    count += 1
    continue
#check to see if all.txt exists, if it does it will delete the file
import os
try:
    os.remove('summary.txt')
    print('Removed summary.txt')
except:
     print('File summary.txt does not exist.')
#Opens Chris.txt, George.txt, Carlos.txt, assigns the file contents to variables, then writes those variable to a file called summary./t
with open('Chris.txt', 'r')as f:
    chris_file =f.read()
    f.close
with open('George.txt', 'r')as f:
    george_file =f.read()
    f.close
with open('Carlos.txt', 'r')as f:
    carlos_file =f.read()
    f.close

with open('summary.txt', 'w')as f:
    f.write(chris_file + george_file + carlos_file)
    f.close
print('Wrote results to ' +  'summary.txt')
print('Press any key to close prompt.')
input()
