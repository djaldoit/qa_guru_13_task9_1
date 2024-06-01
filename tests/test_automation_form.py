from data.user import User
from pages.registration_page import RegistrationPage


def test_user_form():
    page = RegistrationPage()
    user = User('Piter',
                'Parker',
                'spiderman@gmail.com',
                'Male',
                '1234567890',
                '12',
                'May',
                '1995',
                'English',
                'Music',
                '111.jpg',
                'Vladimir street 12',
                'Uttar Pradesh',
                'Agra'
                )

    page.open_browser()
    page.register_user(user)
    page.submit()
    page.should_user(user)




