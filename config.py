import os
import time
from flask import Flask, request
import telebot
import numpy as np
from matplotlib import pyplot as plt
from datetime import date

from dotenv import load_dotenv
load_dotenv()


# Logging Setup
import logging
logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING
    )

TOKEN = os.getenv('TOKEN')

DEBUG = False
SERVER_URL = os.getenv("SERVER_URL")


bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


import importdir
importdir.do("handlers", globals())

