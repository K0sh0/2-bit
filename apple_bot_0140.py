##
## SQLITE DATABASE
## GET GIF
## BOTS ON
## QUEUE
## TRIVIA
## ROULETTE
## REGISTER
## POKER
## FUNCTION FOR GIFS
## ROCK PAPER SCISSORS
## BALANCE SHEET
## HIGH CARD
## TAROT CARDS
## 


from discord.ext import commands
import discord
import random
import sqlite3
import time
from datetime import datetime
import json
import asyncio
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

global rps_state
global long_list
global long_color
global long_oe
global riley
global kimo
global conn
global black_swan
global c
global cluu
global fin_set
global cat_set
global ans_set
global amount
global payday
global cur_deck
global pot
global flop
global players
global active_table
global cur_player
global kosho_auth
global host_auth
global host_on

active_table = False
payday = []
ans_set = []
cluu = []
fin_set = []
cat_set = []
amount = []
queue = []
tracker = 0
confirm = "☻☻☻☻☻☻☻☻ ΦΦ ☻☻☻☻☻☻☻☻"
rps_state = 0
TOKEN ="NjU5OTY2MjY2MTI3MTU1MjE5.XmxlPA.4Xll7rDj2hODK_mF9McjRX8NGSE"
bot = commands.Bot('.')
bot.remove_command('help')
kosho_id = 436061310225088512
amounts = {}
long_list= []
long_color = []
long_oe = []
eo = "empty"
host_on = False

class User:
  def __init__(self, userid, amount):
    self.userid = userid
    self.amount = amount

#########################################################################################
#########################################################################################
##      SQLITE DATABASE
##
try:
  conn = sqlite3.connect('users')
  c = conn.cursor()
  c.execute("""CREATE TABLE users ( 
              userid text,
              amount integer)""")
except sqlite3.OperationalError:
  space = 1

def insert_user(user):
  with conn:
    c.execute("INSERT INTO users Values (:userid, :amount)",
             {'userid': user.userid,
              'amount': user.amount})

def get_by_userid(userid):
  c.execute("SELECT * FROM users WHERE userid = :userid", {'userid': userid})
  return c.fetchone()

def get_full_list(db):
  c.execute("SELECT * FROM users")
  return c.fetchall()

def remove_user(userid):
  with conn:
    c.execute("DELETE from users WHERE userid = :userid",
             {'userid': userid})

def update_pay(idx_new):
  user_db = '''UPDATE users
               SET amount = ?
               WHERE userid = ?'''
  with conn:
    c.execute(user_db, idx_new)

def display_list(db_id):
  with conn:
    x = get_full_list(db_id)
    return x

now = datetime.now()
timestamp = datetime.timestamp(now)
print("timestamp =", timestamp)

##########################################################################################
##########################################################################################
##      GET GIF
##
robbie = ['https://imgur.com/o0SC0o6']
fe = ['https://imgur.com/U65srcp']
frames = ['https://imgur.com/TJUkNMa']
foot = ['https://imgur.com/zAdnegZ']
slick = ['https://imgur.com/CicYjkP']
david = ['https://imgur.com/kWQ46Mq', 'https://imgur.com/GzwafH8',
               'https://imgur.com/7dh17F8','https://imgur.com/WrSIVt6',
               'https://imgur.com/upE1zN2', 'https://imgur.com/sz5wXL6']
black_swan = ['https://imgur.com/8Y3Y9Lm']#, 'https://imgur.com/HPzyIyz']
riley = ["https://imgur.com/a/VP2qKMK", "https://imgur.com/a/qHsPmMf",
             "https://imgur.com/a/uMTeWbW", "https://imgur.com/a/ZdsTL5t",
             "https://imgur.com/a/A73o0Xr", "https://imgur.com/a/Pgyqdd6",
             "https://imgur.com/a/8vVHqKI", "https://imgur.com/a/4AY4MD9"]
kimo = ["https://imgur.com/a/eygCEXJ", "https://imgur.com/a/lIHAZz2",
            "https://imgur.com/a/ywizxSi", "https://imgur.com/a/Jg9iOiU",
            "https://imgur.com/a/wE6Sp6x", "https://imgur.com/a/m4vCar1",
            "https://imgur.com/a/cvYVH5P", "https://imgur.com/a/rKtPuJQ",
            "https://imgur.com/a/ecETRAM", "https://imgur.com/a/4PMrUYl",
            "https://imgur.com/a/iMCbTa9", "https://imgur.com/a/LdL3Wlj",
            "https://imgur.com/a/ZmBDpTj", "https://imgur.com/a/RbVOMP2",
            "https://imgur.com/a/iqo85g2", "https://imgur.com/a/HaJsymY",
            "https://imgur.com/a/eG9aR4L", "https://imgur.com/a/rKpSkX0",
            "https://imgur.com/a/lNs7ddC", "https://imgur.com/a/E35MWhp",
            "https://imgur.com/a/l1xIEmt", "https://imgur.com/a/DYsMiTZ",
            "https://imgur.com/a/xfONicX", "https://imgur.com/a/r9tc1XF",
            "https://imgur.com/a/3iBqhXJ", "https://imgur.com/a/cCaKE00",
            "https://imgur.com/a/cCaKE00", "https://imgur.com/a/3nY2Baj",
            "https://imgur.com/a/CGjX7Yv", "https://imgur.com/a/inddCJj"]
bebe = ["https://imgur.com/a/yJKlkzN", "https://imgur.com/a/UH3wdQ4",
              "https://imgur.com/a/DSlE6Gz", "https://imgur.com/a/1aIteL7"]
trish = ["https://imgur.com/a/4AY4MD9"]
dawn = ["https://imgur.com/a/Afn7kw6", "https://imgur.com/a/4ohejfS",
               "https://imgur.com/a/wiOPotF", "https://imgur.com/a/Vfn6oAy"]
gem = ["https://imgur.com/a/trBqKST", "https://imgur.com/a/V8tvMIP"]
vd = ["https://imgur.com/a/trBqKST"]
grim = ["https://imgur.com/a/Zlnagg4", "https://imgur.com/a/XY9aRK1",
             "https://imgur.com/a/pguNXeN", "https://imgur.com/a/i34BLEe"]
louis = ["https://imgur.com/a/3nnNTlR", "https://imgur.com/a/3TOczvs",
             "https://imgur.com/a/Ywh2SYg"]
nathan = ['https://imgur.com/Xje8Jli', 'https://imgur.com/4vvCJkB',
                 'https://imgur.com/OKlHm6C', 'https://imgur.com/GbHdqJj',
                 'https://imgur.com/kFhGd89']
rig = ["https://imgur.com/a/GDa0RHd"]
scott = ["https://imgur.com/a/zZRy2Wu",
              "https://imgur.com/a/TH671AO"]
kosho = ["https://imgur.com/a/WzXwdo7", "https://imgur.com/a/H5xRvpx"]
curved = ['https://imgur.com/fiufH5X', 'https://imgur.com/vcNcl70']
matt = ["https://imgur.com/a/gywcFKc", "https://imgur.com/a/SqSMJVN",
            "https://imgur.com/a/ye3jWQb", "https://imgur.com/a/YTO0sTp",
            "https://imgur.com/a/bnMEtrF", "https://imgur.com/a/oLe2HMY",
            "https://imgur.com/a/fCn7deI", "https://imgur.com/a/Z47ZuoF",
            "https://imgur.com/a/OTiedKK", "https://imgur.com/a/T1Fc38H",
            "https://imgur.com/a/ZCLJ9eQ" ]
rand = ["https://imgur.com/a/eygCEXJ", "https://imgur.com/a/lIHAZz2",
             "https://imgur.com/a/ywizxSi", "https://imgur.com/a/Jg9iOiU",
             "https://imgur.com/a/wE6Sp6x", "https://imgur.com/a/m4vCar1",
             "https://imgur.com/a/cvYVH5P", "https://imgur.com/a/rKtPuJQ",
             "https://imgur.com/a/ecETRAM", "https://imgur.com/a/4PMrUYl",
             "https://imgur.com/a/iMCbTa9", "https://imgur.com/a/LdL3Wlj",
             "https://imgur.com/a/ZmBDpTj", "https://imgur.com/a/RbVOMP2",
             "https://imgur.com/a/iqo85g2", "https://imgur.com/a/HaJsymY",
             "https://imgur.com/a/eG9aR4L", "https://imgur.com/a/rKpSkX0",
             "https://imgur.com/a/lNs7ddC", "https://imgur.com/a/E35MWhp",
             "https://imgur.com/a/l1xIEmt", "https://imgur.com/a/DYsMiTZ",
             "https://imgur.com/a/xfONicX", "https://imgur.com/a/r9tc1XF",
             "https://imgur.com/a/3iBqhXJ", "https://imgur.com/a/cCaKE00",
             "https://imgur.com/a/cCaKE00", "https://imgur.com/a/3nY2Baj",
             "https://imgur.com/a/CGjX7Yv", "https://imgur.com/a/inddCJj",
             "https://imgur.com/a/VP2qKMK", "https://imgur.com/a/qHsPmMf",
             "https://imgur.com/a/uMTeWbW" ,"https://imgur.com/a/ZdsTL5t",
             "https://imgur.com/a/A73o0Xr" ,"https://imgur.com/a/Pgyqdd6",
             "https://imgur.com/a/8vVHqKI", "https://imgur.com/a/4AY4MD9"]
tarot_deck = ["https://imgur.com/a/bKUpcWn", "https://imgur.com/a/koeh9Ho",
                      "https://imgur.com/a/rOuHTod", "https://imgur.com/a/M6kZpcC",
                      "https://imgur.com/a/xnseP0f", "https://imgur.com/a/VGPtIYA",
                      "https://imgur.com/a/VGPtIYA", "https://imgur.com/a/uPUborJ",
                      "https://imgur.com/a/Asac03l", "https://imgur.com/a/Asac03l",
                      "https://imgur.com/a/BxR65A8", "https://imgur.com/a/PZ8x6zW"]
play_cards = ['300/2_of_clubs_300.png', '300/3_of_clubs_300.png',
                       '300/4_of_clubs_300.png', '300/5_of_clubs_300.png',
                       '300/6_of_clubs_300.png', '300/7_of_clubs_300.png',
                       '300/8_of_clubs_300.png', '300/9_of_clubs_300.png',
                       '300/10_of_clubs_300.png', '300/jack_of_clubs_300.png',
                       '300/queen_of_clubs_300.png', '300/king_of_clubs_300.png',
                       '300/ace_of_clubs_300.png', '300/2_of_hearts_300.png',
                       '300/3_of_hearts_300.png', '300/4_of_hearts_300.png',
                       '300/5_of_hearts_300.png', '300/6_of_hearts_300.png',
                       '300/7_of_hearts_300.png', '300/8_of_hearts_300.png',
                       '300/9_of_hearts_300.png', '300/10_of_hearts_300.png',
                       '300/jack_of_hearts_300.png', '300/queen_of_hearts_300.png',
                       '300/king_of_hearts_300.png', '300/ace_of_hearts_300.png',
                       '300/2_of_spades_300.png', '300/3_of_spades_300.png',
                       '300/4_of_spades_300.png', '300/5_of_spades_300.png',
                       '300/6_of_spades_300.png', '300/7_of_spades_300.png',
                       '300/8_of_spades_300.png', '300/9_of_spades_300.png',
                       '300/10_of_spades_300.png', '300/jack_of_spades_300.png',
                       '300/queen_of_spades_300.png', '300/king_of_spades_300.png',
                       '300/ace_of_spades_300.png', '300/2_of_diamonds_300.png',
                       '300/3_of_diamonds_300.png', '300/4_of_diamonds_300.png',
                       '300/5_of_diamonds_300.png','300/6_of_diamonds_300.png',
                       '300/7_of_diamonds_300.png', '300/8_of_diamonds_300.png',
                       '300/9_of_diamonds_300.png', '300/10_of_diamonds_300.png',
                       '300/jack_of_diamonds_300.png', '300/queen_of_diamonds_300.png',
                       '300/king_of_diamonds_300.png', '300/ace_of_diamonds_300.png' ]

pcards = ["file:///F:/TOP%20GUN/New%205/Cards/Playing%20Cards/SVG-cards-1.3/jack_of_spades2.svg"]

##########
##  GET GIF
##
def get_gif(var):
  if(var == 'robbie'):
    xlen = len(robbie)
    xpos = random.randrange(0,xlen,1)
    gif = robbie[xpos]
  if(var == 'fe'):
    xlen = len(fe)
    xpos = random.randrange(0,xlen,1)
    gif = fe[xpos]
  if(var == 'frames'):
    xlen = len(frames)
    xpos = random.randrange(0,xlen,1)
    gif = frames[xpos]
  if(var == 'foot'):
    xlen = len(foot)
    xpos = random.randrange(0,xlen,1)
    gif = foot[xpos]
  if(var == 'slick'):
    xlen = len(slick)
    xpos = random.randrange(0,xlen,1)
    gif = slick[xpos]
  if(var == 'david'):
    xlen = len(david)
    xpos = random.randrange(0,xlen,1)
    gif = david[xpos]
  if(var == 'curved'):
    xlen = len(curved)
    xpos = random.randrange(0,xlen,1)
    gif = curved[xpos]
  if(var == 'nathan'):
    xlen = len(nathan)
    xpos = random.randrange(0,xlen,1)
    gif = nathan[xpos]
  if(var == 'blackswan'):
    xlen = len(black_swan)
    xpos = random.randrange(0,xlen,1)
    gif = black_swan[xpos]
  if(var == 'riley'):
    xlen = len(riley)
    xpos = random.randrange(0,xlen,1)
    gif = riley[xpos]
  if(var == 'kimo'):
    xlen = len(kimo)
    xpos = random.randrange(0,xlen,1)
    gif = kimo[xpos]
  if(var == 'bebe'):
    xlen = len(bebe)
    xpos = random.randrange(0,xlen,1)
    gif = bebe[xpos]
  if(var == 'trish'):
    xlen = len(trish)
    xpos = random.randrange(0,xlen,1)
    gif = trish[xpos]
  if(var == 'dawn'):
    xlen = len(dawn)
    xpos = random.randrange(0,xlen,1)
    gif = dawn[xpos]
  if(var == 'gem'):
    xlen = len(gem)
    xpos = random.randrange(0,xlen,1)
    gif = gem[xpos]
  if(var == 'grim'):
    xlen = len(grim)
    xpos = random.randrange(0,xlen,1)
    gif = grim[xpos]
  if(var == 'vd'):
    xlen = len(vd)
    xpos = random.randrange(0,xlen,1)
    gif = vd[xpos]
  if(var == 'louis'):
    xlen = len(louis)
    xpos = random.randrange(0,xlen,1)
    gif = louis[xpos]
  if(var == 'scott'):
    xlen = len(scott)
    xpos = random.randrange(0,xlen,1)
    gif = scott[xpos]
  if(var == 'rig'):
    xlen = len(rig)
    xpos = random.randrange(0,xlen,1)
    gif = rig[xpos]
  if(var == 'kosho'):
    xlen = len(kosho)
    xpos = random.randrange(0,xlen,1)
    gif = kosho[xpos]
  if(var == 'matt'):
    xlen = len(matt)
    xpos = random.randrange(0,xlen,1)
    gif = matt[xpos]
  if(var == 'rand'):
    xlen = len(rand)
    xpos = random.randrange(0,xlen,1)
    gif = rand[xpos]
  if(var == 'onetime'):
    gif = pcards[0]
  return gif

###########################################################################################
###########################################################################################
###    BOTS ON
##
@bot.event
async def on_ready():
  global kosho_auth
  kosho_auth = bot.get_user(kosho_id)
  print(bot.user.name)
  print(bot.user.id)
  print(time.ctime())
  print('------')

##########
###   HELP
###
@bot.command(pass_context=True)
async def help(ctx):
  author = ctx.message.author
  test_e = discord.Embed(
                 colour=discord.Colour.orange()
    )
  test_e.set_author(name='Bot prefix:   .')
  test_e.add_field(name='REGISTER YOUR ACCOUNT',
                                  value='.reg (After you call this function, you can now gain prize money)',
                                  inline=False)
  test_e.add_field(name='PRESENT TRIVIA CLUES',
                                  value='.trivia  (Will Post One Question) \n .trivia [# of rounds] [# of clues]',
                                  inline=False)
  test_e.add_field(name='ROULETTE',
                                  value='''.rou [bet amount] [bet][bet category] 
                                                 .rou 100 black color
                                                  - Categories -
                                                  'num' - Guess by number 
                                                  'eo' ---- Guess by 'even' or 'odd' 
                                                  'half' -- Guess by '1st' OR '2nd' half 
                                                  'row' -- Guess by '1st' OR '2nd' or '3rd' row 
                                                  '12s' --- Guess by '1st' OR '2nd' OR '3rd' set of 12 mumbers''',
                                  inline=False)
  test_e.add_field(name='ROCK PAPER SCISSORS',
                                  value= " .rps [the user you're challenging] ",
                                  inline=False)
  test_e.add_field(name='MEMES & GIFS',
                                  value=' .gif [username]',
                                  inline=False)
  await author.send(embed=test_e)

###########################################################################################
###########################################################################################
##      QUEUE
##
@bot.command()          ####
async def q(ctx):           ##### add to queue
  un = ctx.author.name  ####
  #await ctx.message.delete()
  if not un in queue:
    queue.append(un)
    msg1 = await ctx.send(confirm)
    #await asyncio.sleep(7)
    #await msg1.delete()

##########################
##  REMOVE
##
@bot.command()           ######
async def p(ctx):            #### remove user to queue
    un = ctx.author.name ######
    if un in queue:
      queue.remove(un)
      #await asyncio.sleep(7)
      #await ctx.message.delete()      

################################
##  QUEUE LIST
##
@bot.command()                    #######
async def list(ctx, queue=queue): ### display list
  tracker = len(queue)            ########
  #await ctx.message.delete()
  msg1 = await ctx.send("Queue")
  msg2 = []
  for i in range(tracker):
    tracker_i = i+1
    tracker_str = str(tracker_i)
    new_str = tracker_str + ") " + queue[i]
    msg = await ctx.send(new_str)
    msg2.append(msg)
  #await asyncio.sleep(15)
  #await msg1.delete()
  msg_len = len(msg2)
  #for i in range(msg_len):
    #await msg2[i].delete()
    
#############
# remove other users
#############
@bot.command()
async def p1(ctx, other: discord.Member):
  roles = ctx.author.roles
  msg = await ctx.send(roles)
  await asyncio.sleep(7)
  await msg.delete()

###########################################################################################
###########################################################################################
###    TRIVIA
###
@bot.command(description='Trivia')
async def popcorn(ctx):
  print(ctx)
  
@bot.command(description='Trivia')
async def trivia(ctx, rounds: int = 1, clues: int = 1):
  stop = False
  def get_cat(clue, list_clues):
    new = []
    cat = clue['category']
    len_list = len(list_clues)
    for i in range(len_list):
      if(list_clues[i]['category'] == cat):
        new.append(list_clues[i])
    return new

  def check(m):
    return 1

  with open('jeo_0147.json') as f:
    copy = json.load(f)
  len_copy = len(copy)
  for i in range(rounds):
    rand_clue = random.randrange(0, len_copy, 1)
    list_cat = get_cat(copy[rand_clue], copy) # produce the list of clues of given category
    len_list = len(list_cat)
    if(len_list >= clues):
      clues_set = []
      for j in range(clues):
        rand_clues = random.randrange(0, len_list, 1)
        if(rand_clues not in clues_set):
          clues_set.append(rand_clues)
          msg_1 = await ctx.send('Round:  ' + list_cat[rand_clues]['category'])
          str_amount = str(list_cat[rand_clues]['amount'])
          msg_2 = await ctx.send('$' + str_amount)
          msg_3 = await ctx.send(list_cat[rand_clues]['clue'])

          start_time = time.time()
          diff = 0
          winners = []
          while(diff < 20 and stop == False):
            msg = await bot.wait_for('message', check=check)
            guess = msg.content
            fuzzy_check = fuzz.token_set_ratio(list_cat[rand_clues]['answer'], guess)
            curr_time = time.time()
            if(fuzzy_check > 75):
              print(fuzzy_check)
              #curr_time = time.time()
              #curr_time = curr_time + 30
              diff = 25
              temp_id = msg.author.id
              name = msg.author.mention
              str_amount = str(list_cat[rand_clues]['amount'])
              msg_10 = await ctx.send(name + ' wins ' + str_amount)
              search_id = get_by_userid(temp_id)
              if(search_id not in winners):
                winners.append(search_id)
                len_wins = len(winners)
                for i in range(len_wins):
                  try:
                    new_val = list_cat[rand_clues]['amount'] + search_id[1]
                    update_pay((new_val, search_id[0]))
                  except:
                    break
            else:
              curr_time = time.time()
              diff = curr_time - start_time
          msg_4 = await ctx.send('-' + list_cat[rand_clues]['answer'])
          await asyncio.sleep(2)
          #await msg_1.delete()
          #await msg_2.delete()
          await asyncio.sleep(3)
          #await msg_3.delete()
          #await msg_4.delete()
          #try:
            #await msg_10.delete()
          #except:
            #print('No mes_10')
          await asyncio.sleep(3)
        elif(rand_clues in clues_set):
          j = j - 1

@bot.command(description='auth')
async def host(ctx):
  global host_on
  if(host_on == False):
    global host_auth
    host_auth = ctx.message.author
    host_on = True
    
################
###  LIVE TRIVIA
###
@bot.command(description='Trivia')
async def ready(ctx, rounds: int = 1, clues: int = 1, cat_10 = 0):
  global host_auth
  host_id = host_auth.id
  primary_id = ctx.author.id
  global cat_set
  if(cat_10 == 0):
    cat_12 = 'for_evo.json'
  elif(cat_10 == 1):
    cat_12 = 'fe_0150.json'
  elif(cat_10 == 2):
    cat_12 = 'TIME.json'
  elif(cat_10 == 3):
    cat_12 = 'AUSTRALIA.json'
  elif(cat_10 == 4):
    cat_12 = 'globe.json'
  elif(cat_10 == 5):
    cat_12 = 'history.json'
  cat_set = []
  if(host_id == primary_id):
    def get_cat(clue, list_clues):
      new = []
      cat = clue['category']
      len_list = len(list_clues)
      for i in range(len_list):
        if(list_clues[i]['category'] == cat):
          new.append(list_clues[i])
      return new
    def check(m):
      return 1
    with open(cat_12) as f:
      copy = json.load(f)
    len_copy = len(copy)
    for i in range(rounds):
      rand_clue = random.randrange(0, len_copy, 1)
      list_cat = get_cat(copy[rand_clue], copy) # produce the list of clues of given category
      len_list = len(list_cat)
      if(len_list >= clues):
        clues_set = []
        for j in range(clues):
          rand_clues = random.randrange(0, len_list, 1)
          if(rand_clues not in clues_set):
            clues_set.append(rand_clues)
            cluu.append(list_cat[rand_clues])
    len_1 = len(cluu)
    for i in range(len_1):
      i_ = str(i)
      i_ = '------------- ( ' + i_ + ' )'
      len_1 = len(cluu)
      rand_r = random.randrange(0, len_1, 1)
      #print('CATEGORY : ' + cluu[rand_r]['category'], i_)
     # print(cluu[rand_r]['amount'])
     # print('CLUE : ' + cluu[rand_r]['clue'])
     # print('ANSWER : ' +  cluu[rand_r]['answer'])
      fin_set.append(cluu[rand_r])
      ans_set.append(cluu[rand_r]['answer'])
      if(cluu[rand_r]['category'] not in cat_set):
        cat_set.append(cluu[rand_r]['category'])
      del cluu[rand_r]

#############
##  NEXT CLUE
##
@bot.command(pass_context=True)
async def next(ctx):
  global host_auth
  host_id = host_auth.id
  primary_id = ctx.author.id
  secs = 200.0
  global m_1
  kosho = get_by_userid(kosho_id)
  kosho = int(kosho[0])
  kosho = bot.get_user(kosho)
  go = 0
  if primary_id == host_id:
    if(not amount):
      amount.append(fin_set[0]['amount'])
    else:
      amount[0] = fin_set[0]['amount']
    await ctx.send(fin_set[0]['category'])
    new_amount = fin_set[0]['amount'] * 3
    str_amount = str(new_amount)
    await ctx.send('$' + str_amount)
    print('CATEGORY : ' + fin_set[0]['category'])
    await host_auth.send('CATEGORY : ' + fin_set[0]['category'])
    print(fin_set[0]['amount'])
    await host_auth.send(fin_set[0]['amount'])
    print('CLUE : ' + fin_set[0]['clue'])
    await host_auth.send('CLUE : ' + fin_set[0]['clue'])
    print('ANSWER : ' +  fin_set[0]['answer'])
    await host_auth.send('ANSWER : ' +  fin_set[0]['answer'])
    len_fin_ = len(fin_set)
    print(len_fin_)
    await host_auth.send(len_fin_)
    await ctx.send(':diamonds::diamonds::diamonds::diamonds::diamonds::diamonds::diamonds::diamonds::diamonds::diamonds::diamonds:')
    def check(message):
      global m_1
      m_1 = '0'
      if(message.content == 'x' or message.content == 'X' and message.author != kosho):
        return 1
      elif(message.author.id == host_id):
        m_1 = message.content
        return m_1
      #else:
        #return 0
      
    while(go != 1):
      go_1 = 0
      try:
        msg = await bot.wait_for('message', timeout=secs, check=check)
        this_guy = msg.author
        this_guy_id = msg.author.id
        this_nick = msg.author.nick
        if(this_guy_id == host_id and msg.content == 'f'):
          await ctx.send(fin_set[0]['answer'])
          go = 1
          go_1 = 1
          del fin_set[0]
          break
        else:
          try:
            await ctx.send(msg.author.nick)
            print(msg.author.nick)
            await host_auth.send(msg.author.nick)
          except:
            await ctx.send(msg.author.name)
            print(msg.author.name)
            await host_auth.send(msg.author.name)
      except asyncio.TimeoutError:
        await ctx.send(fin_set[0]['answer'])
        go = 1
        go_1 = 1
        del fin_set[0]
        break
      while(go_1 != 1):
        msg_1 = await bot.wait_for('message', check=check)
        if( msg_1.author.id == host_id and m_1 == 'a'):
          mult = 3
          id_ = []
          len_payday = len(payday)
          for i in range(len_payday):
            id_.append(payday[i]['id'])
          pay = mult * amount[0]
          pay_str  = str(pay)
          if(this_guy_id not in id_):
            payday.append({'id':this_guy_id, 'amount':pay})
          else:
            for i in range(len_payday):
              if(payday[i]['id'] == this_guy_id):
                new_pay = payday[i]['amount'] + pay
                payday[i]['amount'] = new_pay
          await ctx.send('Paid $' + pay_str)
          await ctx.send(fin_set[0]['answer'])
          go_1 = 1
          go = 1
          del fin_set[0]
          break
        elif(msg_1.author.id == host_id and m_1 == 's'):
          #secs = 30.0
          mult = 3
          id_ = []
          len_payday = len(payday)
          for i in range(len_payday):
            id_.append(payday[i]['id'])
          pay = mult * amount[0] * -1
          pay_str  = str(pay)
          if(this_guy_id not in id_):
            payday.append({'id':this_guy_id, 'amount':pay})
          else:
            for i in range(len_payday):
              if(payday[i]['id'] == this_guy_id):
                new_pay = payday[i]['amount'] + pay
                payday[i]['amount'] = new_pay
          await ctx.send('Paid $' + pay_str)
          await ctx.send(':diamonds::diamonds::diamonds::diamonds::diamonds::diamonds::diamonds::diamonds::diamonds::diamonds::diamonds:')
          go_1 = 1
        elif(m_1 == 'f'):
          await ctx.send(fin_set[0]['answer'])
          go = 1
          go_1 = 1
          del fin_set[0]
          break

########### 
##  ROUNDS
##    
@bot.command(pass_context=True)
async def rounds(ctx):
  global host_auth
  global cat_set
  primary_id = host_auth.id
  primary_id = ctx.message.author.id
  if primary_id == host_auth.id:
    len_r = len(cat_set)
    cat_2 = cat_set
    for i in range(len_r):
      await ctx.send(cat_set[i])

############
##  ANSWERS
##
@bot.command(pass_context=True)
async def answer(ctx):
  primary_id = ctx.message.author.id
  if primary_id == kosho_id:
    await ctx.send(ans_set[0])
    del ans_set[0]

#########
##  SHOW
##
@bot.command(pass_context=True)
async def show(ctx):
  global host_auth
  primary_id = host_auth.id
  len_payday = len(payday)
  id_ = []
  for i in range(len_payday):
    id_1 = payday[i]['id']
    id_2 = int(id_1)
    id_.append(id_2)
  for i in range(len_payday):
    name = bot.get_user(id_[i])
    amount = payday[i]['amount']
    name = str(name)
    amount = str(amount)
    await ctx.send(name + ' - $' + amount)

################
##  TRANSACTION
##
@bot.command(pass_context=True)
async def trans(ctx):
  len_payday = len(payday)
  id_ = []
  for i in range(len_payday):
    id_1 = payday[i]['id']
    id_2 = int(id_1)
    id_.append(id_2)
  for i in range(len_payday):
    name = get_by_userid(id_[i])
    amount = payday[i]['amount']
    amount = int(amount)
    if(amount > 0):
      amount_ = int(name[1])
      pay = amount_ + amount
      update_pay((pay, name[0]))
    payday[i]['amount'] = 0

###########################################################################################
###########################################################################################
##  ROULETTE 
##
def play_rou(xspin):
  global spin
  global str_even_odd
  global row
  global twelve
  global half
  global tables
  tables = [ ]
  row = [ ]
  """Roulette."""
  g ="Green"
  r = "Red"
  b ="Black"
  spin = [g, r, b, r, b, r, b,
              r, b, r, b, b, r, b,
              r, b, r, b, r, r, b,
              r, b, r, b, r, b, r,
              b, b, r, b, r, b, r,
              b, r ]
  str_xsp = str(xspin)
  even_odd = xspin%2
  str_even_odd = " "
  if(even_odd == 0):
    if(xspin != 0):
      str_even_odd = "Even"
  else:
    str_even_odd = "Odd"
  row = [" ", "1st Row", "2nd Row", "3rd Row","1st Row", "2nd Row",
              "3rd Row","1st Row", "2nd Row", "3rd Row", "1st Row",
              "2nd Row", "3rd Row","1st Row", "2nd Row", "3rd Row",
              "1st Row", "2nd Row", "3rd Row","1st Row", "2nd Row",
              "3rd Row","1st Row", "2nd Row", "3rd Row", "1st Row",
              "2nd Row", "3rd Row","1st Row", "2nd Row", "3rd Row",
              "1st Row", "2nd Row", "3rd Row","1st Row", "2nd Row",
              "3rd Row"]
  twelve = [" ", "1st 12", "1st 12", "1st 12", "1st 12", "1st 12",
                 "1st 12", "1st 12", "1st 12", "1st 12", "1st 12",
                 "1st 12", "1st 12", "2nd 12", "2nd 12", "2nd 12",
                 "2nd 12", "2nd 12", "2nd 12", "2nd 12", "2nd 12",
                 "2nd 12", "2nd 12", "2nd 12", "2nd 12", "3rd 12",
                 "3rd 12", "3rd 12", "3rd 12", "3rd 12", "3rd 12",
                 "3rd 12", "3rd 12", "3rd 12", "3rd 12", "3rd 12",
                 "3rd 12"]
  half = [" ", "1st Half", "1st Half", "1st Half", "1st Half", "1st Half",
               "1st Half", "1st Half", "1st Half", "1st Half", "1st Half",
               "1st Half", "1st Half", "1st Half", "1st Half", "1st Half",
               "1st Half", "1st Half", "1st Half", "2nd Half", "2nd Half",
               "2nd Half", "2nd Half", "2nd Half", "2nd Half", "2nd Half",
               "2nd Half", "2nd Half", "2nd Half", "2nd Half", "2nd Half",
               "2nd Half", "2nd Half", "2nd Half", "2nd Half", "2nd Half",
               "2nd Half"]
  tables = ['https://imgur.com/a/bQZWVDz', 'https://imgur.com/a/WmToAd0',
                'https://imgur.com/a/HeaoOjb', 'https://imgur.com/a/ynMuxrl',
                'https://imgur.com/a/rWiqZVP', 'https://imgur.com/a/1Qykabr',
                'https://imgur.com/a/fRikYDZ', 'https://imgur.com/a/UDdiquk',
                'https://imgur.com/a/kgWJGCU', 'https://imgur.com/a/wGNGbTj',
                'https://imgur.com/a/uMtOmLu', 'https://imgur.com/a/09UXSBP',
                'https://imgur.com/a/LzXI9bj', 'https://imgur.com/a/IJtJHlL',
                'https://imgur.com/a/6pbJS2N', 'https://imgur.com/a/6pbJS2N',
                'https://imgur.com/a/ZVgqQks', 'https://imgur.com/a/npbBuUa',
                'https://imgur.com/a/FyZ9AfA', 'https://imgur.com/a/RXFxPiI',
                'https://imgur.com/a/3VzlCxv', 'https://imgur.com/a/rn4O7lM',
                'https://imgur.com/a/71TFonl', 'https://imgur.com/a/WzimMh4',
                'https://imgur.com/a/PnzdFjO', 'https://imgur.com/a/RrxNqrA',
                'https://imgur.com/a/nN5nfzi', 'https://imgur.com/a/6jvDvWW',
                'https://imgur.com/a/XEkr9ib', 'https://imgur.com/a/I9PN0XT',
                'https://imgur.com/a/13yHNO3', 'https://imgur.com/a/ixOGL5I',
                'https://imgur.com/a/446LPNn', 'https://imgur.com/a/8kzqQpe',
                'https://imgur.com/a/YFIkQix', 'https://imgur.com/a/yRI0TLO',
                'https://imgur.com/a/ssMBGZv']
  str_res_1 = str_xsp + " " + spin[xspin] + " " + str_even_odd + " "
  str_res_2 = half[xspin]  +   "  - " + row[xspin] + " " + twelve[xspin]
  str_res = str_res_1 + str_res_2
  return str_res

############
##  ROULETTE
##
long_list = []
long_color = []
long_oe = []

############
##  ROULETTE
##
@bot.command(description='Roulette')
async def rou(ctx, bet:int, guess, style:str = 'num' ):
  temp_id = ctx.message.author.id
  search_id = get_by_userid(temp_id)
  if(search_id[1] >= bet and bet >= 0):
    xspin = random.randrange(0,36,1)
    str_res = play_rou(xspin)
    #about to display the message
    long_list.append(xspin)
    long_color.append(spin[xspin])
    long_oe.append(str_even_odd)
    #displays neat box with answer
    emb = (discord.Embed(description=" ", color=0x3DF270))
    emb.set_author(name=str_res)
    #displays answer
    msg_5 = await ctx.send(tables[xspin])
    msg_6 = await ctx.send(embed=emb)
    #If Winner or Loser
    #betting numbers
  if(style == 'num' and search_id[1] >= bet and bet > 0):
    if(guess == xspin):
      await ctx.send("Winner!")
      win_val = 35 * bet
      new_val = search_id[1] + win_val
      win2_val = bet + win_val
      new_str_num = "+ $ " + str(win2_val)
      msg_7 = await ctx.send(new_str_num)
    else:
      new_val = search_id[1] - bet
  #betting color
  if(style == 'color' and search_id[1] >= bet and bet > 0):
    new_col = spin[xspin].lower()
    if(guess == new_col):
      await ctx.send("Winner!")
      win_val = bet
      new_val = search_id[1] + win_val
      win2_val = bet + win_val
      new_str_col = "+ $ " + str(win2_val)
      msg_7 = await ctx.send(new_str_col)
    else:
      new_val = search_id[1] - bet
  #betting even or odd
  if(style == 'eo' and search_id[1] >= bet and bet > 0):
    new_eo = str_even_odd.lower()
    if(guess == new_eo):
      await ctx.send("Winner!")
      win_val = bet
      new_val = search_id[1] + win_val
      win2_val = bet + win_val
      new_str_eo = "+ $ " + str(win2_val)
      msg_7 = await ctx.send(new_str_eo)
    else:
       new_val = search_id[1] - bet
  #betting on half
  if(style == 'half' and search_id[1] >= bet and bet > 0):
    new_half = half[xspin][:3]
    if(guess == new_half):
      await ctx.send("Winner!")
      win_val = bet
      new_val = search_id[1] + win_val
      win2_val = bet + win_val
      new_str_half = "+ $ " + str(win2_val)
      msg_7 = await ctx.send(new_str_half)
    else:
      new_val = search_id[1] - bet
  #betting on rows
  if(style == 'row' and search_id[1] >= bet and bet > 0):
    new_row = row[xspin][:3]
    if(guess == new_row):
      await ctx.send("Winner!")
      win_val = bet * 2
      new_val = search_id[1] + win_val
      win2_val = bet + win_val
      new_str_row = "+ $ " + str(win2_val)
      msg_7 = await ctx.send(new_str_row)
    else:
      new_val = search_id[1] - bet
   #betting on 12
  if(style == '12s' and search_id[1] >= bet and bet > 0):
    new_12 = twelve[xspin][:3]
    if(guess == new_12):
      await ctx.send("Winner!")
      win_val = bet * 2
      new_val = search_id[1] + win_val
      win2_val = bet + win_val
      new_str_12 = "+ $ " + str(win2_val)
      msg_7 = await ctx.send(new_str_12)
    else:
      new_val = search_id[1] - bet
  if(search_id[1] >= bet and bet > 0):
    update_pay((new_val, search_id[0]))
  await asyncio.sleep(8)
  try:
    await msg_5.delete()
  except:
    print('no msg_5')
  try:
    await msg_6.delete()
  except:
    print('no msg_6')
  try:
    await msg_7.delete()
  except:
    print('no msg_7')

########################
# STATS FOR ROULETTE
#
@bot.command(description='Roulette Stats')
async def rlist(ctx, long_list = long_list):
  await ctx.send(long_list)

@bot.command(description='Roulette Stats Color')
async def rcol(ctx, long_color = long_color):
  await ctx.send(long_color)

@bot.command(description='Roulette Stats')
async def roe(ctx, long_oe = long_oe):
  await ctx.send(long_oe)

@bot.command(description='Les Grossman')
async def les(ctx):
  await ctx.send('https://imgur.com/a/XCKY1YN')

###########################################################################################
###########################################################################################
##      REGISTER
##
@bot.command(pass_context=True)
async def reg(ctx):
  temp_id = ctx.message.author.id
  search_id = get_by_userid(temp_id)
  if not search_id:
    new_user = User(temp_id, 1000)
    insert_user(new_user)
    msg_1 = await ctx.send("You are now registered.")
  else:
    msg_1 = await ctx.send("You already have an account.")
  await asyncio.sleep(7)
  await msg_1.delete()

######################
##    REGISTER SOMEONE
##
@bot.command(pass_context=True)
async def regg(ctx, other: discord.Member):
  temp_id = other.id
  search_id = get_by_userid(temp_id)
  if ctx.message.author.id == kosho_id:
    if not search_id:
      new_user = User(temp_id, 1000)
      insert_user(new_user)
      msg_1 = await ctx.send("User is now registered.")
    else:
      msg_1 = await ctx.send("They already have an account.")
  else:
      msg_1 = await ctx.send("Nice try.  You don't have permission to do that.")
  await asyncio.sleep(7)
  await msg_1.delete()

################
##    MY BALANCE
##
@bot.command(pass_context=True)
async def bal(ctx):
  temp_id = ctx.message.author.id
  search_id = get_by_userid(temp_id)
  user_list = get_full_list(temp_id)
  #print(user_list)
  if search_id:
    msg_1 = await ctx.send("You have {} coins in the bank.".format(search_id[1]))
  else:
    msg_1 = await ctx.send("You do not have an account.")
  await asyncio.sleep(7)
  await msg_1.delete()

##############################
##   LOOK AT SOMEONE ELSES BAL
##
@bot.command(pass_context=True)
async def hisbal(ctx, other: discord.Member):
  temp_id = other.id
  search_id = get_by_userid(temp_id)
  if search_id:
    await ctx.send("They have {} in the bank".format(search_id[1]))
  else:
     await ctx.send("They do not have an account")

########################
##      GIVES USERS MONEY
##
@bot.command(pass_context=True)
async def give(ctx, amount: int, other: discord.Member):
  primary_id = ctx.message.author.id
  other_id = other.id
  search_id = get_by_userid(other_id)
  if not search_id:
    await ctx.send("Someone isn't registered yet.")
  else:
    if primary_id == kosho_id:
      temp_val = search_id[1] + amount
      str_amounts = str(temp_val)
      str_member = str(other)
      str_new = str_member + " has " + str_amounts

      update_pay((temp_val, search_id[0]))
      await ctx.send("Transaction complete")
      await ctx.send(str_new)
    else:
      await ctx.send("Nice try.  You don't have permission to do that.")

###########################################################################################
###########################################################################################
###   POKER
###
@bot.command(pass_context=True)
async def poker(ctx):
  global active_table
  global players
  global cur_deck
  user_id = ctx.message.author.id        ##  current user and user ID
  search_id = get_by_userid(user_id)
  user_name = bot.get_user(user_id)
  if(active_table != True):                      ##  is there a current table
    active_table = True
    players = []
    players.append(user_name)
  elif(active_table == True and user_name not in players):
    players.append(user_name)
  len_players = len(players)
  for i in range(len_players):
    await ctx.send(players[i].name)
  cur_deck = []
  #await ctx.send(ctx.message.author)
  #await ctx.send(players[0])
  def deal_cards(player):
    len_players = len(players)
    for i in range(len_players):
       players[i]
    test_e = discord.Embed(
        colour=discord.Colour.orange()
    )
    test_e.set_author(name='Bot prefix:   .')
    test_e.add_field(name='REGISTER YOUR ACCOUNT',
                                  value='.reg (After you call this function, you can now gain prize money)',
                                  inline=False)

##########################################################################################
##########################################################################################
##     FUNCTIONS FOR GIFS
##
@bot.command(description='Gifs')
async def gif(ctx, var:str = rand, ):
  now = datetime.now()
  timestamp = datetime.timestamp(now)
  print("timestamp =", timestamp)
  var1 = var
  giffer = get_gif(var1)
  await ctx.send(giffer)

###########################################################################################
###########################################################################################
##     ROCK PAPER SCISSORS
##
#@bot.command(description='Rock Paper Scissors')
@bot.command(pass_context=True)
async def rps(ctx, other: discord.Member, wager = 100, rps_state:bool = rps_state):
  if(rps_state == 0):
    #var
    rps_state = 1
    other_a = other.mention
    auth = ctx.message.author.mention
    this_id = ctx.message.author.id
    this_id_id = get_by_userid(this_id)
    other_id = other.id
    other_id_id = get_by_userid(other_id)
    str_wager = str(wager)
    #adress users
    compl_str_1 = other_a + ", " + auth + " challenged you to some ROSHAMBO! for " + str_wager  
    compl_str_2 = ". ```||R|| for Rock \n||P|| for Paper \n||S|| for Scissors \n(Add the bars or just right click the letter and select Mark As Spoiler) \nOr Q to quit```"
    await ctx.send(compl_str_1 + compl_str_2)
    #displays neat box with answer
    global emb
    emb = (discord.Embed(description=" ", color=0x3DF270))
    global weapon
    weapon = '_'
    weapons = [' ', ' ']
    go0 = 0
    go1 = 0
    go = 0
    res0 ="Blank"
    res1 = "Blank"
     
    def check(m):
      if(m.content == '||R||' or m.content == '||r||' or m.content == 'R' or m.content == 'r'):
        return 1
      elif(m.content == '||P||' or m.content == '||p||' or m.content == 'P' or m.content == 'p'):
        return 1
      elif(m.content == '||S||' or m.content == '||s||' or m.content == 'S' or m.content == 's'):
        return 1
      elif(m.content == 'q' or m.content == 'Q' or m.content == '||Q||' or m.content == '||q||'):
        return 1

    while(go <= 1):
      msg = await bot.wait_for('message', check=check)
      if(msg.content == 'q' or msg.content == 'Q'):
        await ctx.send(msg.author.mention + " quit.")
        go = 3
        rps_state = 0
        return 0
      elif(msg.author.id == this_id and go0 == 0 and go <= 1):
        weapons[0] = msg.content
        go0 = 1
        go = go + 1
        await msg.delete()
        #await ctx.send(emd)
        #emb.set_author(name=str_res)
        #displays answer
        #await ctx.send(lv.tables[xspin])
        #await ctx.send(embed=emb)
        if(go1 == 0):
          await ctx.send("Waiting on " + other_a)
      elif(msg.author.id == other_id and go1 == 0 and go <= 1):
        weapons[1] = msg.content
        go1 = 1
        go = go + 1
        await msg.delete()
        if(go0 == 0):
          await ctx.send("Waiting on " + auth)
    if(weapons[0] == '||r||' or weapons[0] == '||R||' or weapons[0] == 'r' or weapons[0] == 'R'):
      if(weapons[1] == '||r||' or weapons[1] == '||R||' or weapons[1] == 'r' or weapons[1] == 'R'):
        await ctx.send("Draw! Keep your money.")
        res0 = "Rock"
        res1 = "Rock"
    if(weapons[0] == '||s||' or weapons[0] == '||S||' or weapons[0] == 's' or weapons[0] == 'S'):
      if(weapons[1] == '||s||' or weapons[1] == '||S||' or weapons[1] == 's' or weapons[1] == 'S'):
        await ctx.send("Draw! Keep your money.")
        res0 = "Scissors"
        res1 = "Scissors"
    if(weapons[0] == '||p||' or weapons[0] == '||P||' or weapons[0] == 'p' or weapons[0] == 'P'):
      if(weapons[1] == '||p||' or weapons[1] == '||P||' or weapons[1] == 'p' or weapons[1] == 'P'):
        await ctx.send("Draw! Keep your money.")
        res0 = "Paper"
        res1 = "Paper"
    if(weapons[0] == '||r||' or weapons[0] == '||R||' or weapons[0] == 'r' or weapons[0] == 'R'):
      if(weapons[1] == '||s||' or weapons[1] == '||S||' or weapons[1] == 's' or weapons[1] == 'S'):
        npay = this_id_id[1] + wager
        mpay = other_id_id[1] - wager
        update_pay((npay, this_id_id[0]))
        update_pay((mpay, other_id_id[0]))
        str_this = str(this_id_id[1])
        await ctx.send(auth + " WINS! \n Balance : $" + str_this)
        res0 = 'Rock'
        res1 = 'Scissors'
      elif(weapons[1] == '||p||' or weapons[1] == '||P||' or weapons[1] == 'p' or weapons[1] == 'P'):
        npay = this_id_id[1] - wager
        mpay = other_id_id[1] + wager
        update_pay((npay, this_id_id[0]))
        update_pay((mpay, other_id_id[0]))
        str_this = str(other_id_id[1])
        await ctx.send(other_a + " WINS! \n Balance : $" + str_this)
        res0 = 'Rock'
        res1 = 'Paper'
    if(weapons[1] == '||R||' or weapons[1] == '||r||' or weapons[1] == 'R' or weapons[1] == 'r'):
      if(weapons[0] == '||s||' or weapons[0] == '||S||' or weapons[0] == 's' or weapons[0] == 'S'):
        npay = this_id_id[1] - wager
        mpay = other_id_id[1] + wager
        update_pay((npay, this_id_id[0]))
        update_pay((mpay, other_id_id[0]))
        str_this = str(other_id_id[1])
        await ctx.send(other_a + " WINS! \n Balance : $" + str_this)
        res1 = 'Rock'
        res0 = 'Scissors'
      elif(weapons[0] == '||p||' or weapons[0] == '||P||' or weapons[0] == 'p' or weapons[0] == 'P'):
        npay = this_id_id[1] + wager
        mpay = other_id_id[1] - wager
        update_pay((npay, this_id_id[0]))
        update_pay((mpay, other_id_id[0]))
        str_this = str(this_id_id[1])
        await ctx.send(auth + " WINS! \n Balance : $" + str_this)
        res1 = 'Rock'
        res0 = 'Paper'
    if(weapons[1] == '||s||' or weapons[1] == '||S||' or weapons[1] == 's' or weapons[1] == 'S'):
      if(weapons[0] == '||p||' or weapons[0] == '||P||' or weapons[0] == 'p' or weapons[0] == 'P'):
        npay = this_id_id[1] - wager
        mpay = other_id_id[1] + wager
        update_pay((npay, this_id_id[0]))
        update_pay((mpay, other_id_id[0]))
        str_this = str(other_id_id[1])
        await ctx.send(other_a + " WINS!  \n Balance : $" + str_this)
        res0 = 'Paper'
        res1 = 'Scissors'
    elif(weapons[0] == '||p||' or weapons[0] == '||P||' or weapons[0] == 'p' or weapons[0] == 'P'):
      if(weapons[1] == '||r||' or weapons[1] == '||R||' or weapons[1] == 'r' or weapons[1] == 'R'):
        npay = this_id_id[1] + wager
        mpay = other_id_id[1] - wager
        update_pay((npay, this_id_id[0]))
        update_pay((mpay, other_id_id[0]))
        str_this = str(this_id_id[1])
        await ctx.send(auth + " WINS! \n Balance : $" + str_this )
        res1 = 'Rock'
        res0 = 'Paper'
    await ctx.send(auth + " : " + res0 + "\n" + other_a + " : " + res1)
    rps_state = 0

############################################################################################
############################################################################################
##    BALANCE LIST
##
@bot.command(description='Balance Sheet')
async def rich(ctx, len_list = 5, wait = 15):
  this_id = ctx.message.author.id
  bal_list = display_list(this_id)
  howlong = len(bal_list)
  print(howlong)
  this_list = []
  def my_func(e):
    return e[1]
  bal_list.sort(reverse=True, key=my_func)
  t_ = 'ALL-TIME BALANCE \n'
  for i in range(len_list):
    id_ = int(bal_list[i][0])
    name_ = bot.get_user(id_)
    name_ = str(name_)
    bal_ = str(bal_list[i][1])
    num_ = str(i + 1)
    this_ = (num_ + ') ' + name_ + ' --- $' + bal_)
    t_ = t_ + '\n' + this_
  msg_1 = await ctx.send(t_)
  await asyncio.sleep(wait)
  await msg_1.delete()

############################################################################################  
############################################################################################
##    TAROT FUNCTIONS
##
@bot.command(description='Tarot')
async def tarot(ctx, quant:int = 3):
  cards = []
  fulldeck = []
  full_deck = tarot_deck
  for i in range(quant):
    tarot_len = len(full_deck)
    index = random.randrange(0,tarot_len,1)    
    cards.append(full_deck[index])
    full_deck.remove(full_deck[index])
    await ctx.send(cards[i])

############################################################################################
############################################################################################
##   HIGH CARD
##
@bot.command(description='Draw Card')
async def cards(ctx, bet = 100):
  temp_id = ctx.message.author.id
  search_id = get_by_userid(temp_id)
  def mod_13(num):
    if(num >= 39):
      mult = 3
    elif(num >= 26):
      mult = 2
    elif(num >= 13):
      mult = 1
    else:
      mult = 0
    sub = 13 * mult
    return num - sub
  if(search_id[1] >= bet and bet >= 0):
    cards = []
    cards = play_cards
    cards_1 = play_cards
    xlen = len(cards)
    xpos = random.randrange(0,xlen,1)
    xpos_1 = xpos
    while(xpos_1 == xpos):
          xpos_1 = random.randrange(0,xlen,1)
    await ctx.send(file=discord.File(cards[xpos]))
    await asyncio.sleep(3.5)
    await ctx.send(file=discord.File(cards[xpos_1]))
    my_num = mod_13(xpos)
    house_num = mod_13(xpos_1)
    if(house_num > my_num):
      my_val = search_id[1]
      my_val = my_val - bet
      update_pay((my_val, search_id[0]))
      await ctx.send('Loser.')
    elif(my_num > house_num):
      my_val = search_id[1]
      my_val = my_val + bet
      update_pay((my_val, search_id[0]))
      await ctx.send('Winner!')
    else:
      await ctx.send('Draw.')

#########
##  TESTER
##
@bot.command(description='Draw Card')
async def test(ctx, other:discord.Member):
  temp_id = other.id
  search_id = get_by_userid(temp_id)
  test = bot.get_user(temp_id)
  await test.send('Ace of Spades' + ' \n ' + 'King of Spades')
  
###############
##  RUN THE BOT
##
bot.run(TOKEN)
