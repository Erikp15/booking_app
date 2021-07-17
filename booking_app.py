import streamlit as st
import pandas as pd
import numpy as np
from tinydb import TinyDB,Query

user_db=TinyDB('users.json')
hotel_db=TinyDB('hotels.json')
booking_db=TinyDB('bookings.json')
id_db=TinyDB('id.json')

q=Query()

id_range=id_db.search(q.type=='user')
booking_id=id_db.search(q.type=='booking')

user_id=st.number_input(
    "select your user id",
    min_value=1,
    max_value=id_range[0]['id']-1,
)

hotels=[]
for hotel in hotel_db:
    hotels.append(hotel['name'])

hotel_picked=st.selectbox(
    "select your desired hotel",
    options=hotels
)

start_date=st.text_input(
    'input start date',
    max_chars=10,
)

end_date=st.text_input(
    'input end date',
    max_chars=10,
)

if st.button('confirm booking'):
    booking_db.insert({'booking_id':booking_id[0]['id'],'user_id':user_id,'hotel_picked':hotel_picked,'start_date':start_date,'end_date':end_date})
    id_db.update({'id':booking_id[0]['id']+1},q.type=='booking')
    st.write('booking confirmed from user',user_id,'at hotel',hotel_picked,', starting on',start_date,'and ending on',end_date)