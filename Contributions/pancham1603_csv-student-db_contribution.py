'''
Write a program to display the following: Menu driven program

- add data
- read the entire file
- Search for a specific record (ask for the roll number)
- Update the record (ask for the roll number)
- Delete
- Exit
The above should be able to perform the functionality on a dictionary STUDENTDATA(having roll number and stream). 
Also the end of file and file not found error should be handled.
'''

import csv


def add_data(data):
  try:
      with open('STUDENTDATA.csv', 'r') as file:
          for row in file.readlines():
              if str(row[0]) == str(data[0]):
                  return f'[ERROR] Roll number already exists try using update to delete'
  except FileNotFoundError:
      with open('STUDENTDATA.csv', 'w') as file:
          write = csv.writer(file)
          write.writerow(data)
          return f'[ADDED] {data}'
  with open('STUDENTDATA.csv', 'a', newline='') as file:
      write = csv.writer(file)
      write.writerow(data)
      return f'[ADDED] {data}'

    
def read():
  filedata = []
  try:
      with open('STUDENTDATA.csv', 'r') as file:
          reader = csv.reader(file)
          for row in reader:
              if len(row) >0 and row != ' ' and row != '\n' :
                  filedata.append(row)
  except FileNotFoundError:
      with open('STUDENTDATA.csv', 'w') as file:
          return f'[ERROR] No data found, try adding some data'
  return filedata


def search(rollno):
  STUDENT_DATA = {}
  try:
      with open('STUDENTDATA.csv', 'r') as file:
          reader = csv.reader(file)
          for row in reader:
              if len(row) > 0 and row != ' ' and row != '\n' :
                  if str(row[0]) == str(rollno):
                      STUDENT_DATA[row[0]] = row[1]
  except FileNotFoundError:
      with open('STUDENTDATA.csv', 'w') as file:
          return f'[ERROR] No data found, try adding some data'
  return STUDENT_DATA


def update(data):
  STUDENT_DATA = {}
  try:
      with open('STUDENTDATA.csv', 'r') as file:
          reader = csv.reader(file)
          for row in reader:
              if len(row) > 0 and row != ' ' and row != '\n' :
                  STUDENT_DATA[row[0]] = row[1]
  except FileNotFoundError:
      with open('STUDENTDATA.csv', 'w') as file:
          return f'[ERROR] No data found, try adding some data'
  STUDENT_DATA[data[0]] = data[1]
  with open('STUDENTDATA.csv', 'w', newline='') as file:
      writer = csv.writer(file)
      for key in STUDENT_DATA.keys():
          writer.writerow([key, STUDENT_DATA[key]])
  updated = {data[0]:data[1]}
  return f'[UPDATED] {updated}'


def delete(rollno):
  STUDENT_DATA = {}
  try:
      with open('STUDENTDATA.csv', 'r') as file:
          reader = csv.reader(file)
          for row in reader:
              if len(row) >0 and row != ' ' and row != '\n' :
                  STUDENT_DATA[row[0]] = row[1]
  except FileNotFoundError:
      with open('STUDENTDATA.csv', 'w') as file:
          return f'[ERROR] No data found, try adding some data'
 
  try:
      deleted = {rollno:STUDENT_DATA[rollno]}
      del STUDENT_DATA[rollno]
  except KeyError:
      return f'[ERROR] No such student found'
  with open('STUDENTDATA.csv', 'w', newline='') as file:
      writer = csv.writer(file)
      for key in STUDENT_DATA.keys():
          writer.writerow([key, STUDENT_DATA[key]])
  return f'[DELETED] {deleted}'


def exit():
  quit()

  
while True:
  ask = input("What would you like to do? (enter h for help)\n")
  if ask == 'h':
      print('''1) Add data, do -> add (rollno) (stream)
2) Read file -> read
3) Search using roll number -> search (roll no.)
4) Update -> update (roll no.) (new stream)
5) Delete -> del (roll no.)
6) Quit/Exit -> exit''')
 
  if ask.startswith('add'):
      print(add_data([ask.split()[1], ask.split()[2]]))

  elif ask.startswith('read'):
      data = read()
      if data:
          for record in data:
              print(record)
      else:
          print(f'No data found, try adding some data')

  elif ask.startswith('search'):
      result = search(ask.split()[1])
      if result:
          print(f'[RESULT] {result}')
      else:
          print('No such student found')
 
  elif ask.startswith('update'):
      print(update([ask.split()[1], ask.split()[2]]))

  elif ask.startswith('del'):
      print(delete(ask.split()[1]))

  elif ask.startswith('exit'):
      exit()
