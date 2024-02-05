import sqlite3 as sql
import os
import secrets
from datetime import datetime, timedelta

# modules from local modifications
from extras.time_code import time_stuff
from extras.named_tupple import namedtuple_factory
from extras.secrets import hashed_id, hash_sign, verify

@time_stuff
def create_account(db_name, user_id, user_name, password, name, surname, email, phone_number, home_address, position, roles, ts=datetime.now()):
  mode = ''
  secret_pwd = hash_sign(user_name, password)
  con = sql.connect(os.path.relpath(f'data_base/{db_name}.db'))
  try:
    with con:
      cur = con.cursor()
      cur.execute(
        '''
          INSERT INTO staff VALUES(
          :user_id,
          :user_name,
          :password,
          :name,
          :surname,
          :email,
          :phone_number,
          :home_address,
          :position,
          :roles,
          :created,
          :updated,
          :accessed,
          :ts
          )
        ''', {
          "user_id": user_id, "user_name":user_name, "password": secret_pwd, "name": name, "surname": surname, "email": email, "phone_number": phone_number, "home_address": home_address, "position": position, "roles": roles, "created": ts, "updated": ts, "accessed": ts, "ts": ts
        }
      )
      del password, secret_pwd
      con.commit()
      mode = 'success'
  except Exception as ep:
    mode = ep
    
  return mode

@time_stuff
def login(db_name, user_name, password):
  cookie = ''
  temp = ''
  pwd = hash_sign(user_name, password)
  expire_time = datetime.now() + timedelta(hours=8)
  con = sql.connect(os.path.relpath(f'data_base/{db_name}.db'))
  try:
    con.row_factory = namedtuple_factory
    cur = con.cursor()
    cur.execute(
      '''
        SELECT * FROM staff WHERE user_name = :user_name
      ''', {
        "user_name": user_name
      }
    )
    temp = cur.fetchone()
    if temp is not None and verify(user_name, temp.password, password) is True:
      cur.execute(
      '''
        INSERT INTO cookies VALUES(
        :cookie_id, 
        :cookie_owner_id, 
        :cookie_owner_username, 
        :cookie_owner_name,
        :cookie_owner_surname,
        :cookie_owner_email,
        :cookie_owner_phonenumber,
        :cookie_owner_homeaddress,
        :cookie_owner_position,
        :cookie_owner_roles,
        :ts, 
        :cookie_expire_time,
        :cookie_owner_ts,
        :cookie_owner_last_updated,
        :cookie_owner_accessed,
        :cookie_expired
        )
      ''', {
        "cookie_id": hashed_id(secrets.token_bytes(24)), 
        "cookie_owner_id": temp.user_id, 
        "cookie_owner_username": temp.user_name, 
        "cookie_owner_name": temp.name,
        "cookie_owner_surname": temp.surname,
        "cookie_owner_email": temp.email,
        "cookie_owner_phonenumber": temp.phone_number,
        "cookie_owner_homeaddress": temp.home_address,
        "cookie_owner_position": temp.position,
        "cookie_owner_roles": temp.roles,
        "ts": datetime.now(), 
        "cookie_expire_time": expire_time,
        "cookie_owner_ts": temp.ts,
        "cookie_owner_last_updated": temp.updated,
        "cookie_owner_accessed": temp.accessed,
        "cookie_expired": False
      }
      )
      cur.execute(
        '''SELECT * FROM cookies WHERE cookie_expired = :cookie_expired''', { "cookie_expired": False }
      )
      cookie = cur.fetchone()
    else:
      cookie = temp
    del password
    con.commit()
    con.close()
  except Exception as ep:
    cookie = ep

  return cookie

@time_stuff
def logout(db_name, cookie_id):
  con = sql.connect(os.path.relpath(f'data_base/{db_name}.db'))
  try:
    with con:
      cur = con.cursor()
      cur.execute('''SELECT * FROM cookies''')
      cur.execute('''UPDATE cookies SET cookie_expired = :cookie_expired WHERE cookie_id = :cookie_id''', {'cookie_expired': True, 'cookie_id': cookie_id})
  except Exception as ep:
    print(ep)

@time_stuff
def verify_cookie(db_name):
  con = sql.connect(os.path.relpath(f'data_base/{db_name}.db'))
  cookie = None
  try:
    con.row_factory = namedtuple_factory
    cur = con.cursor()
    cur.execute(
      '''SELECT * FROM cookies WHERE cookie_expired = :cookie_expired''', { 'cookie_expired': False }
    )
    cookie = cur.fetchone()
  except Exception as ep:
    print(f"error: {ep}")
  
  return cookie

@time_stuff
def student_enrolment(db_name,names, school_id, date_of_birth, entry_number, gender, address, class_grade, parent_names, parent_phone_number, sports, other_details, ts):
  mode = ''
  con = sql.connect(os.path.relpath(f'data_base/{db_name}.db'))

  try:
    con.row_factory = namedtuple_factory
    cur = con.cursor()
    cur.execute(
      '''
        INSERT INTO students VALUES(
        :school_id,
        :names,
        :date_of_birth,
        :entry_number,
        :gender,
        :address,
        :class,
        :parent_names,
        :parent_phone_number,
        :sports,
        :other_details,
        :created,
        :last_updated
        )
      ''', {
        "school_id": school_id, "names": names, "date_of_birth": date_of_birth, "entry_number": entry_number, "gender": gender, "address": address, "class": class_grade, "parent_names": parent_names, "parent_phone_number": parent_phone_number, "sports": sports, "other_details": other_details, "created": ts, "last_updated": ts
      }
    )
    mode = 'success'
    con.commit()
    con.close()
  except Exception as ep:
    mode = ep

  return mode

@time_stuff
def search_student(db_name, sid):
  con = sql.connect(os.path.relpath(f'data_base/{db_name}.db'))
  srecord = ''
  try:
    con.row_factory = namedtuple_factory
    cur = con.cursor()
    cur.execute("""SELECT * FROM students WHERE school_id = :school_id""", { "school_id": sid })
    srecord = cur.fetchone()
  except Exception as ep:
    print(ep)

  return srecord

@time_stuff
def get_all_students(db_name):
  con = sql.connect(os.path.relpath(f'data_base/{db_name}.db'))
  cur = con.cursor()
  cur.execute('''SELECT * FROM students''')
  sts = cur.fetchall()
  con.close()
  return sts
