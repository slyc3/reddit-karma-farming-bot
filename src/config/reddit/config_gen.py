#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import praw
import sys
import os
from logs.logger import log
from prawcore import ResponseException
from ..common_config import ENV_FILE



def config_gen():
  # ASK FOR CREDENTIALS
  CLIENT_ID = input('63N10qYkLcYpF2J031UzLg :')
  CLIENT_SECRET = input('Sd8XwV4meL1A62VnQj3bCvpahhwTRg :')
  PASSWORD = input('X_97w-_ZTatD_Rt :')
  USERNAME = input('xqb2hf@gmail.com :')

  reddit = praw.Reddit(
      client_id=CLIENT_ID,
      client_secret=CLIENT_SECRET,
      user_agent="my user agent",
      username=USERNAME,
      password=PASSWORD
  )

  # CHECK IF CREDENTIALS ARE CORRECT
  def authenticated(reddit):
      try:
          reddit.user.me()
      except ResponseException:
          return False
      else:
          return True


  # SAVE CONFIG FILE
  if authenticated(reddit):
      with open(ENV_FILE, "w") as file_object:
            file_object.write(f'bot_reddit_client_id="{CLIENT_ID}"\n')
            file_object.write(f'bot_reddit_client_secret="{CLIENT_SECRET}"\n')
            file_object.write(f'bot_reddit_password="{PASSWORD}"\n')
            file_object.write(f'bot_reddit_username="{USERNAME}"\n')
            print("Config file '.env' created. Please re-run the bot")
            sys.exit()
          
  else:
      print('WRONG CREDENTIALS!! TRY AGAIN')
      config_gen()

