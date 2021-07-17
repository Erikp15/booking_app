import streamlit as st
import pandas as pd
import numpy as np
from tinydb import TinyDB,Query

user_db=TinyDB('users.json')
hotel_db=TinyDB('hotels.json')
booking_db=TinyDB('bookings.json')
id_db=TinyDB('id.json')

id_db.truncate()
hotel_db.truncate()
user_db.truncate()
booking_db.truncate()
id_db.insert({'id':1,'type':'user'})
id_db.insert({'id':1,'type':'booking'})