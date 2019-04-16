from sqlalchemy import Column, String
from sql_helpers import SESSION, BASE


class PMPermit(BASE):
    __tablename__ = "pmpermit"
    chat_id = Column(String(14), primary_key=True)
    reason = Column(String(127))

    def __init__(self, chat_id, reason=""):
        self.chat_id = chat_id
        self.reason = reason


PMPermit.__table__.create(checkfirst=True)


def is_approved(chat_id):
    try:
        return SESSION.query(PMPermit).filter(PMPermit.chat_id == str(chat_id)).one()
    except:
        return None
    finally:
        SESSION.close()


def approve(chat_id, reason):
    adder = PMPermit(str(chat_id), str(reason))
    SESSION.add(adder)
    SESSION.commit()


def disapprove(chat_id):
    rem = SESSION.query(PMPermit).get(str(chat_id))
    if rem:
        SESSION.delete(rem)
        SESSION.commit()


def get_all_approved():
    rem = SESSION.query(PMPermit).all()
    SESSION.close()
    return rem#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       untitled.py
#       
#       Copyright 2019  <>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#       
#       



def main():
	
	return 0

if __name__ == '__main__':
	main()

