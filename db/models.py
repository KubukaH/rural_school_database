import sqlite3 as sql
import os
import secrets
from datetime import datetime, timedelta

# modules from local modifications
from extras.time_code import time_stuff
from extras.named_tupple import namedtuple_factory
from extras.secrets import hashed_id, hash_sign, verify
from .get_db_name import get_db_name

@time_stuff
def create_account(user_id, user_name, password, name, surname, email, phone_number, home_address, position, roles,db_name=get_db_name(), ts=datetime.now()):
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
def login(user_name, password, db_name=get_db_name()):
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
def logout(cookie_id, db_name=get_db_name()):
  res = ''
  con = sql.connect(os.path.relpath(f'data_base/{db_name}.db'))
  try:
    with con:
      cur = con.cursor()
      cur.execute('''SELECT * FROM cookies''')
      cur.execute('''UPDATE cookies SET cookie_expired = :cookie_expired WHERE cookie_id = :cookie_id''', {'cookie_expired': True, 'cookie_id': cookie_id})
      res = 'done'
  except Exception as ep:
    res = ep
  return res

@time_stuff
def verify_cookie(db_name=get_db_name()):
  con = sql.connect(os.path.relpath(f'data_base/{db_name}.db'))
  cookie = ''
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
def student_enrolment(first_name, last_name, added_names, school_id, date_of_birth, birth_entry_number, gender, permanent_address, current_address, student_class, parent_names, parent_phone_number, sports, other_details, ts, db_name=get_db_name()):
  mode = ''
  con = sql.connect(os.path.relpath(f'data_base/{db_name}.db'))

  try:
    con.row_factory = namedtuple_factory
    cur = con.cursor()
    cur.execute(
      '''
        INSERT INTO students VALUES(
        :school_id,
        :last_name,
        :first_name,
        :added_names,
        :gender,
        :date_of_birth,
        :birth_entry_number,
        :permanent_address,
        :current_address,
        :other_details,
        :parent_names,
        :parent_phone_number,
        :student_class,
        :sports,
        :created,
        :last_updated
        )
      ''', {
        "school_id": school_id, "last_name": last_name, "first_name": first_name, "added_names": added_names, "date_of_birth": date_of_birth, "birth_entry_number": birth_entry_number, "gender": gender, "permanent_address": permanent_address, "current_address": current_address, "student_class": student_class, "parent_names": parent_names, "parent_phone_number": parent_phone_number, "sports": sports, "other_details": other_details, "created": ts, "last_updated": ts
      }
    )
    mode = 'success'
    con.commit()
    con.close()
  except Exception as ep:
    mode = ep

  return mode

@time_stuff
def search_student(sid, db_name=get_db_name()):
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
def get_all_students(db_name=get_db_name()):
  con = sql.connect(os.path.relpath(f'data_base/{db_name}.db'))
  cur = con.cursor()
  cur.execute('''SELECT * FROM students''')
  sts = cur.fetchall()
  con.close()
  return sts

@time_stuff
def delete_std_record(school_id, db_name=get_db_name()):
  res = ''
  con = sql.connect(os.path.relpath(f'data_base/{db_name}.db'))
  try:
    with con:
      cur = con.cursor()
      cur.execute('''SELECT * FROM students''')
      cur.execute('''DELETE FROM students WHERE school_id = :school_id''', {"school_id": school_id})
      res = 'okay'
  except Exception as ep:
    res = ep
  return res

@time_stuff
def get_last_transaction():
  res = ''
  con = sql.connect(os.path.relpath(f'data_base/{get_db_name()}.db'))
  try:
    with con:
      cur = con.cursor()
      res = cur.execute("SELECT * FROM students ORDER BY created DESC")
  except Exception as ep:
    res = ep
  return res.fetchone()