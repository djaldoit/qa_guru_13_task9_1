from selene import have
from page.registration_page import RegistrationPage

page = RegistrationPage()
user1 = page.user_registration('Piter',
                               'Parker',
                               'spiderman@example.com',
                               'Male',
                               '1234567890',
                               28,
                               'May',
                               '1995',
                               'Reading',
                               './images/111.jpg',
                               'Vladimir Street 12',
                               'Haryana',
                               'Karnal'
                               )


def test_automation_form():
    page.open_browser()
    page.user_registration(*user1)
    page.submit()
    page.should_user().should(have.exact_texts(*user1))





