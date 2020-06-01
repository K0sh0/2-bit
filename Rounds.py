from discord.ext import commands
import discord
import random
import sqlite3
import time
from datetime import datetime
import json
import asyncio

with open('jeo_0150.json') as f:
  copy = json.load(f)

cat = []
len_copy = len(copy)
for i in range(len_copy):
  dog = copy[i]['category']
  if(i % 10000 == 0):
    print(len_copy - i)
  if('HISTORY' in dog):
    cat.append(copy[i])
cat_ = json.dumps(cat, indent=1)
print(len(cat_))

with open('histiry.json', 'w') as outfile:
  outfile.write(cat_)
outfile.close()
