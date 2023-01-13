# -*- coding: utf-8 -*-

from model.contact import Contact

def test_add_contact(app):
    contact1 = Contact(first_name="f_name1",
                       middle_name="m_name1",
                       last_name="l_name1",
                       nickname="nickname1",
                       photo_path="C:\\fakepath\\1.jpg",
                       title="title1",
                       company="company1",
                       address="address1",
                       home="home1",
                       mobile="mobile1",
                       work="work1",
                       fax="fax1",
                       email="emaill1", email2="emaill2", email3="emaill3",
                       homepage="homepage1",
                       birthday_day="1",
                       birthday_month="January",
                       birthday_year="2000",
                       anniversary_day="5",
                       anniversary_month="July",
                       anniversary_year="2000",
                       group="group1",
                       secondary_address="sec_addr1",
                       secondary_home="sec_home1",
                       secondary_notes="sec_notes1")
    app.session.login(username="admin", password="secret")
    app.contact.create(contact1)
    app.open_home_page()
    app.session.logout()




