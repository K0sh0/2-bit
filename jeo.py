import requests
from bs4 import BeautifulSoup
import json
import re

     ##  VARIABLES
big_data = []
eps = 1
master_site = 'http://www.j-archive.com/showgame.php?game_id='

     ##  FUNCTIONS
# GET CLUES
def get_clues(soup_):
  clues = []
  for h in range(2):
    for i in range(6):
      for j in range(5):
        col = i + 1
        row = j + 1
        if(h == 0):
          round_ =  'J'
        elif(h == 1):
          round_ = 'DJ'
        clue = soup.find('td', {'id': 'clue_' + round_ + '_' + str(col) +'_' + str(row)})
        if(clue == None):
          clue = 'Empty'
        clues.append(clue)
  clue = soup.find('td', {'id' : 'clue_FJ'})
  clues.append(clue)
  return clues

#  GET ANSWERS
def get_answers(soup_, clues):
  answers = []
  for i in range(61):
    j = i
    if(i == 60):
      onmouseout = "togglestick('clue_FJ_stuck')"
    else:
      if(j >= 30):
        j = j - 30
        round_ = 'DJ'
      else:
        round_ = 'J'
      col = (j / 5) + 1
      col = int(col)
      col = str(col)
      row = (j % 5) + 1
      row = str(row)
      onmouseout = "togglestick('clue_" + round_ + "_" + col + "_" + row + "_stuck')"
    _div = soup.find('div', {'onclick' : onmouseout})
    if(clues[i] == 'Empty'):
      _div = 'Empty'
      answer = 'Empty'
    else:
      _omo = _div['onmouseover']
      if( i == 60):
        try:
          text_start = _omo.index('"><i>')
          text_start = int(text_start)
          text_start = text_start + 5
          text_finish = _omo.index('</i>')
          text_finish = int(text_finish)
          answer = _omo[text_start:text_finish]
        except:
          answer = 'Empty'
      else:
        text_start = _omo.index('nse">')
        text_start = int(text_start)
        text_start = text_start + 5
        text_finish = _omo.index('</em><br')
        text_finish = int(text_finish)
        answer = _omo[text_start:text_finish]
    answers.append(answer)
  len_answers = len(answers)
  answers_ = []
  for i in range(len_answers):
    res = answers[i]
    if('<i>' in res):
      if(res.index('<i>') == 0):
        res = re.sub('<i>', ' ', res)
      if(res.endswith('</i>')):
        res = re.sub('</i>', ' ', res)
    answers_.append(res)    
  return answers_

# GET AMOUNTS
def get_amounts():
  amounts = []
  for h in range(2):
    for i in range(6):
      for j in range(5):
        amount = (h+1) * (j+1) * 100
        amounts.append(amount)
  amounts.append(0)
  return amounts

# GET CATEGORIES
def get_categories(soup_):
  categories_ = []
  all_good = True
  categories = soup.find_all('td', {'class', 'category_name'})
  for h in range(2):
    for i in range(6):
      for j in range(5):
        if(h == 0):
          categories_.append(categories[i].text)
          if(categories[i] == 'None'):
           all_good = False
        elif(h == 1):
          categories_.append(categories[i + 6].text)
          if(categories[i + 6] == 'None'):
            all_good = False
  categories_.append(categories[12].text)
  return categories_

# FINAL FORMATTING
def format_lib(answers, row_col, show_num,
                          show_url, categories, clues, amounts = 0,
                          audio = False, image = False, video = False,
                          big_data = big_data):
  with open('jeo.json') as f:
    big_data = json.load(f)
  #w_show = 'whole_show_' + title
  #big_data['questions'] = []#w_show] = {}
  for i in range(61):
    typo = type(clues[i])
    if(clues[i] != 'Empty' and typo != str):
      clues[i] = clues[i].text
      #big_data[w_show][row_col[i]]
      big_data.append({'code' : row_col[i], 'clue' : clues[i],
                                     'show_number' : show_num,
                                    'show_url' : show_url, 'category' : categories[i],
                                    'answer' : answers[i], 'amount' : amounts[i],
                                    'audio' : audio[i], 'image' : image[i],
                                    'video' : video[i]})
  big_data = json.dumps(big_data, indent=1)
  return big_data

#  ROW & COLUMN FORMATTER
def get_row_col(title):
  array = []
  for h in range(2):
    for i in range(6):
      for j in range(5):
        if(h == 0):
          round_ = 'J'
        else:
          round_ = 'DJ'
        row = j + 1
        col = i + 1
        row = str(row)
        col = str(col)
        compl_string = title + '_' + round_ + '_' + col +  '_' + row
        array.append(compl_string)
  fj_format = title + '_FJ'
  array.append(fj_format)
  return array

##    PICS,  AUDIO,  VIDEO
# FIND AUDIO
def find_audio(soup_):
  audio_ = []
  for h in range(2):
    for i in range(6):
      for j in range(5):
        col = i + 1
        row = j + 1
        if(h == 0):
          round_ =  'J'
        elif(h == 1):
          round_ = 'DJ'
        clue = soup.find('td', {'id': 'clue_' + round_ + '_' + str(col) +'_' + str(row)})
        clue_ = str(clue)
        try:
          audio = clue_.index('mp3')
        except:
          audio = False
        audio_.append(audio)
  clue = soup.find('td', {'id' : 'clue_FJ'})
  clue_ = str(clue)
  try:
    audio = clue_.index('mp3')
  except:
    audio = False
  audio_.append(audio)
  return audio_

# FIND PICTURES
def find_pics(soup_):
  pics = []
  for h in range(2):
    for i in range(6):
      for j in range(5):
        col = i + 1
        row = j + 1
        if(h == 0):
          round_ =  'J'
        elif(h == 1):
          round_ = 'DJ'
        clue = soup.find('td', {'id': 'clue_' + round_ + '_' + str(col) +'_' + str(row)})
        clue_ = str(clue)
        try:
          pic = clue_.index('jpg')
        except:
          pic = False
        pics.append(pic)
  clue = soup.find('td', {'id' : 'clue_FJ'})
  clue_ = str(clue)
  try:
    pic = clue_.index('jpg')
  except:
    pic = False
  pics.append(pic)
  return pics

# FIND VIDEOS
def find_vids(soup_):
  vids = []
  for h in range(2):
    for i in range(6):
      for j in range(5):
        col = i + 1
        row = j + 1
        if(h == 0):
          round_ =  'J'
        elif(h == 1):
          round_ = 'DJ'
        clue = soup.find('td', {'id': 'clue_' + round_ + '_' + str(col) +'_' + str(row)})
        clue_ = str(clue)
        try:
          vid = clue_.index('mp4')
        except:
          vid = False
        vids.append(vid)
  clue = soup.find('td', {'id' : 'clue_FJ'})
  clue_ = str(clue)
  try:
    vid = clue_.vid('mp4')
  except:
    vid = False
  vids.append(vid)
  return vids

     ##  EXTRACT 
for ep in range(6700, 8000):
  url = master_site + str(ep)
  pull = requests.get(url)
  soup = BeautifulSoup(pull.text, 'html.parser')
  test = soup.find('div', {'id':'content'})
  test = test.text[0] + test.text[1] + test.text[2]
# TEST IF EMPTY
  if(test == 'ERR'):
    print('Empty')
  else:
    try:
      # print(soup)
      title = soup.find('title')
      title = title.text[19:-18]
      row_col = get_row_col(title)
      categories = get_categories(soup)
      clues = get_clues(soup)
      answers = get_answers(soup, clues)
      amounts = get_amounts()
      audio = find_audio(soup)
      pics = find_pics(soup)
      vids = find_vids(soup)
      show_ready = format_lib(answers, row_col, title, url, categories, clues, amounts, audio, pics, vids)
      print(title, ep)
      with open('jeo.json', 'w') as outfile:
        outfile.write(show_ready)
      outfile.close()
    except:
      print('empty')
  

