import streamlit as st
import pandas as pd
import numpy as np
from tinydb import TinyDB,Query

user_db=TinyDB('users.json')
id_db=TinyDB('id.json')
q=Query()

if(st.button('create new user')):
    id=id_db.search(q.type=='user')
    user_db.insert({'user_id':id[0]['id']})
    id_db.update({'id':id[0]['id']+1},q.type=='user')
    'your user key is',id[0]['id']

