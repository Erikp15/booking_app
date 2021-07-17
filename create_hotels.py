import streamlit as st
import pandas as pd
import numpy as np
from tinydb import TinyDB,Query

hotel_db=TinyDB('hotels.json')

hotel_db.insert({'hotel_id':1,'name':'Millennium','stars':5})
hotel_db.insert({'hotel_id':2,'name':'koncheto hut','stars':0})
hotel_db.insert({'hotel_id':3,'name':'thrashen cliffs','stars':0})

