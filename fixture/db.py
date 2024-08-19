import pymysql.cursors
from model.group import Group
from model.contact import Contact
import random

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, email, email2, email3 from addressbook WHERE deprecated IS NULL")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, email, email2, email3) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address,
                                  homenomber=home, mobilenomber=mobile, worknomber=work, email=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return list

    def is_contact_in_group(self, contact_id, group_id):
        cursor = self.connection.cursor()
        try:
            cursor.execute(f"SELECT * FROM address_in_groups WHERE id = {contact_id} AND group_id = {group_id}")
            result = cursor.fetchone()
        finally:
            cursor.close()
        return result is not None

    def destroy(self):
        self.connection.close()
