from page.registration_page import RegistrationPage


def test_automation_form():
    page = RegistrationPage()
    (
        page.open_browser()
        .fill_name('Piter')
        .fill_last_name('Parker')
        .fill_email('spiderman@gmail.com')
        .fill_gender('Male')
        .fill_user_number('1234567890')
        .data_birth('28', 'May', '1995')
        .subjects('English')
        .hobbies('Sports')
        .upload_picture('./images/111.jpg')
        .fill_user_address('Vladimir street 12')
        .choice_state()
        .choice_city()
        .submit()
        .should_user(
            'Piter Parker',
            'spiderman@gmail.com',
            'Male',
            '1234567890',
            '28 May,1995',
            'English',
            'Sports',
            '111.jpg',
            'Vladimir street 12',
            'Uttar Pradesh Agra')

        )






