from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, address=None, company=None, homenomber=None,
                         worknomber=None, mobilenomber=None, fax=None, email=None, bday=None, bmonth=None, byear=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.address = address
        self.company = company
        self.homenomber = homenomber
        self.worknomber = worknomber
        self.mobilenomber = mobilenomber
        self.fax = fax
        self.email = email
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.firstname)

    def __eq__(self, other):
        return self.id == other.id and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
