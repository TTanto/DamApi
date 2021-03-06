#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import logging
import os

from sqlalchemy.sql import text

import db
import settings
from db.models import SQLAlchemyBase, User, GenereEnum, UserToken, UserInstruments, Instruments
from settings import DEFAULT_LANGUAGE

# LOGGING
mylogger = logging.getLogger(__name__)
settings.configure_logging()


def execute_sql_file(sql_file):
    sql_folder_path = os.path.join(os.path.dirname(__file__), "sql")
    sql_file_path = open(os.path.join(sql_folder_path, sql_file), encoding="utf-8")
    sql_command = text(sql_file_path.read())
    db_session.execute(sql_command)
    db_session.commit()
    sql_file_path.close()


if __name__ == "__main__":
    settings.configure_logging()

    db_session = db.create_db_session()

    # -------------------- REMOVE AND CREATE TABLES --------------------
    mylogger.info("Removing database...")
    SQLAlchemyBase.metadata.drop_all(db.DB_ENGINE)
    mylogger.info("Creating database...")
    SQLAlchemyBase.metadata.create_all(db.DB_ENGINE)



    # -------------------- CREATE USERS --------------------
    mylogger.info("Creating default users...")
    # noinspection PyArgumentList
    user_admin = User(
        created_at=datetime.datetime(2020, 1, 1, 0, 1, 1),
        username="admin",
        email="admin@damcore.com",
        name="Administrator",
        surname="DamCore",
        genere=GenereEnum.male,
        gps="42.090205,1.1504",
        description="hola",

    )
    user_admin.set_password("DAMCoure")

    # noinspection PyArgumentList
    user_1= User(
        created_at=datetime.datetime(2020, 1, 1, 0, 1, 1),
        username="usuari1",
        email="usuari1@gmail.com",
        name="usuari",
        surname="1",
        birthdate=datetime.datetime(1989, 1, 1),
        genere=GenereEnum.male,
        gps="42.390205,3.1504",
    )
    user_1.set_password("a1s2d3f4")
    user_1.tokens.append(UserToken(token="656e50e154865a5dc469b80437ed2f963b8f58c8857b66c9bf"))

    # noinspection PyArgumentList
    user_2 = User(
        created_at=datetime.datetime(2020, 1, 1, 0, 1, 1),
        username="user2",
        email="user2@gmail.com",
        name="user",
        surname="2",
        birthdate=datetime.datetime(2017, 1, 1),
        genere=GenereEnum.male,
        gps="40.390205,2.5504",

    )
    user_2.set_password("r45tgt")
    user_2.tokens.append(UserToken(token="0a821f8ce58965eadc5ef884cf6f7ad99e0e7f58f429f584b2"))


    # -------------------- CREATE Instruments --------------------
    mylogger.info("Creating instrumets data...")
    # noinspection PyArgumentList
    instrument1 = Instruments(
        id_instrument=1,
        name="Guitarra"
    )
    instrument2 = Instruments(
        id_instrument=2,
        name="Trompeta"
    )
    instrument3 = Instruments(
        id_instrument=3,
        name="Piano"
    )
    instrument4 = Instruments(
        id_instrument=4,
        name="Maracas"
    )
    

    db_session.add(user_admin)
    db_session.add(user_1)
    db_session.add(user_2)

    #----Adding Instruments----#
    db_session.add(instrument1)
    db_session.add(instrument2)
    db_session.add(instrument3)
    db_session.add(instrument4)

    
    db_session.commit()
    db_session.close()
