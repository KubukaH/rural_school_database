import sqlite3 as sq3
import os

def create_db(name):
  connection_string = os.path.realpath(f"data_base/{name}.db")

  con = sq3.connect(
    connection_string, detect_types=sq3.PARSE_DECLTYPES | sq3.PARSE_COLNAMES
  )
  cur = con.cursor()
  cur.executescript(
    '''
      BEGIN;
      CREATE TABLE IF NOT EXISTS staff(
        user_id PRIMARY KEY UNIQUE,
        user_name TEXT UNIQUE,
        password TEXT,
        name TEXT,
        surname TEXT,
        email TEXT,
        phone_number TEXT,
        home_address TEXT,
        position TEXT,
        roles TEXT,
        created TIMESTAMP,
        updated TIMESTAMP,
        accessed TIMESTAMP,
        ts TIMESTAMP
      );
      CREATE TABLE IF NOT EXISTS cookies(
        cookie_id PRIMARY KEY UNIQUE, 
        cookie_owner_id TEXT, 
        cookie_owner_username TEXT, 
        cookie_owner_name TEXT,
        cookie_owner_surname TEXT,
        cookie_owner_email TEXT,
        cookie_owner_phonenumber TEXT,
        cookie_owner_homeaddress TEXT,
        cookie_owner_position TEXT,
        cookie_owner_roles TEXT,
        ts TIMESTAMP, 
        cookie_expire_time TIMESTAMP,
        cookie_owner_ts TIMESTAMP,
        cookie_owner_last_updated TIMESTAMP,
        cookie_owner_accessed TIMESTAMP,
        cookie_expired BOOLEAN
      );
      CREATE TABLE IF NOT EXISTS keys(
        key_id PRIMARY KEY UNIQUE,
        key_data TEXT,
        session_key TEXT
      );
      CREATE TABLE IF NOT EXISTS students(
        school_id PRIMARY KEY UNIQUE,
        names TEXT,
        date_of_birth TEXT,
        entry_number TEXT,
        gender TEXT,
        address TEXT,
        class TEXT,
        parent_names TEXT,
        parent_phone_number TEXT,
        sports TEXT,
        other_details TEXT,
        created TIMESTAMP,
        last_updated TIMESTAMP
      );
      COMMIT;
    '''
  )

  return 