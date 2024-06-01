from selene import have, browser
import os


class RegistrationPage:
    def open_browser(self):
        browser.open('/automation-practice-form')
        return self

    def fill_name(self, name):
        browser.element('#firstName').type(name)
        return self

    def fill_last_name(self, last_name):
        browser.element('#lastName').type(last_name)
        return self

    def fill_email(self, email):
        browser.element('#userEmail').type(email)
        return self

    def fill_gender(self, gender):
        browser.all('.custom-control-label').element_by(
            have.exact_text(gender)).click()
        return self

    def fill_user_number(self, number):
        browser.element('#userNumber').type(number)
        return self

    def data_birth(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month).click()
        browser.element('.react-datepicker__year-select').type(year).click()
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()
        return self

    def subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()
        return self

    def hobbies(self, hobbies):
        browser.all('.custom-checkbox').element_by(have.exact_text(hobbies)).click()
        return self

    def upload_picture(self, file):
        browser.element('#uploadPicture').send_keys(os.path.abspath(file))
        return self

    def fill_user_address(self, address):
        browser.element('#currentAddress').type(address)
        return self

    def choice_state(self,):
        browser.element('#state').click().element('#react-select-3-option-1').click()
        return self

    def choice_city(self):
        browser.element('#city').click().element('#react-select-4-option-0').click()
        return self

    def submit(self):
        browser.element('#submit').click()
        return self

    def should_user(self, full_name, email, gender, number, date, subjects, hobbies, file, address, state):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                number,
                date,
                subjects,
                hobbies,
                file,
                address,
                state
            )
        )

