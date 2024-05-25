import time
from selene import have, browser
import os


class RegistrationPage:
    def __init__(self):
        pass

    def open_browser(self):
        browser.open('/automation-practice-form')

    def full_name_and_email(self, name, last_name, email):
        browser.element('#firstName').type(name)
        browser.element('#lastName').type(last_name)
        browser.element('#userEmail').type(email)

    def gender(self, gender):
        if gender == 'Male':
            browser.element('[for="gender-radio-1"]').click()
        elif gender == 'Female':
            browser.element('[for="gender-radio-2"]').click()
        else:
            browser.element('[for="gender-radio-3"]').click()

    def user_number(self, number):
        browser.element('#userNumber').type(number)

    def data_birth(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month).click()
        browser.element('.react-datepicker__year-select').type(year).click()
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()

    def subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def hobbies(self, *values):
        for value in values:
            if value == 'Sports':
                browser.all('.custom-checkbox').element_by(have.exact_text('Sport')).click()
            elif value == 'Reading':
                browser.all('.custom-checkbox').element_by(have.exact_text('Reading')).click()
            elif value == 'Music':
                browser.all('.custom-checkbox').element_by(have.exact_text('Music')).click()

    def file_download_dir(self, dir):
        browser.element('#uploadPicture').send_keys(os.path.abspath(dir))

    def user_address(self, address, state, cities):
        browser.element('#currentAddress').type(address)
        if state == 'NCR':
            browser.element('#state').click().element('#react-select-3-option-0').click()
            if cities == 'Delhi':
                browser.element('#city').click().element('#react-select-4-option-0').click()
            if cities == 'Gurgaon':
                browser.element('#city').click().element('#react-select-4-option-1').click()
            if cities == 'Noida':
                browser.element('#city').click().element('#react-select-4-option-2').click()
        elif state == 'Uttar Pradesh':
            browser.element('#state').click().element('#react-select-3-option-1').click()
            if cities == 'Agra':
                browser.element('#city').click().element('#react-select-4-option-0').click()
            if cities == 'Lucknow':
                browser.element('#city').click().element('#react-select-4-option-1').click()
            if cities == 'Merrut':
                browser.element('#city').click().element('#react-select-4-option-2').click()
        elif state == 'Haryana':
            browser.element('#state').click().element('#react-select-3-option-2').click()
            if cities == 'Karnal':
                browser.element('#city').click().element('#react-select-4-option-0').click()
            if cities == 'Panipat':
                browser.element('#city').click().element('#react-select-4-option-1').click()
        elif state == 'Rajasthan':
            browser.element('#state').click().element('#react-select-3-option-3').click()
            if cities == 'Jaipur':
                browser.element('#city').click().element('#react-select-4-option-0').click()
            if cities == 'Jaiselmer':
                browser.element('#city').click().element('#react-select-4-option-1').click()

    def submit(self):
        return browser.element('#submit').press_enter()

    def should_user(self):
        return browser.element('.table').all('td').even

    def browser_close(self):
        return browser.element('#closeLargeModal').click()


def test_automation_form():
    page = RegistrationPage()
    page.open_browser()
    page.full_name_and_email('Piter', 'Parker', 'spiderman@example.com')
    page.gender('Male')
    page.user_number('1234567890')
    page.data_birth(25, 'May', '1994')
    page.subjects('Arts')
    page.hobbies('Sport', 'Music')  # Не выбирает чекбокс спорт, а вот читать выбирает
    page.file_download_dir('./images/111.jpg')
    page.user_address('Vladimir Street 12', 'Haryana', 'Karnal')
    page.submit()
    time.sleep(2)
    page.should_user().should(
        have.exact_texts(
            'Piter Parker',
            'spiderman@example.com',
            'Male',
            '1234567890',
            '25 May,1994',
            'Arts',
            'Music',
            '111.jpg',
            'Vladimir Street 12',
            'Haryana Karnal'
        )
    )

    page.browser_close()





