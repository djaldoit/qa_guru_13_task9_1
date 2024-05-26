import os
from selene import browser, have


class RegistrationPage:

    # Open
    def open_browser(self):
        browser.open('/automation-practice-form')

    # Registration
    def user_registration(self,
                          first_name,
                          last_name,
                          email,
                          gender,
                          number,
                          day,
                          month,
                          year,
                          subject,
                          direct,
                          address,
                          state,
                          city,
                          ):

        # Full name, email
        browser.element('#firstName').type(first_name)
        browser.element('#lastName').type(last_name)
        browser.element('#userEmail').type(email)

        # Gender
        if gender == 'Male':
            browser.element('[for="gender-radio-1"]').click()
        elif gender == 'Female':
            browser.element('[for="gender-radio-2"]').click()
        else:
            browser.element('[for="gender-radio-3"]').click()

        # Date of birth
        browser.element('#userNumber').type(number)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month).click()
        browser.element('.react-datepicker__year-select').type(year).click()
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()

        # Subjects
        browser.element('#subjectsInput').type(subject).press_enter()
        for value in subject:
            if value == 'Sports':
                browser.all('.custom-checkbox').element_by(have.exact_text('Sport')).click()
            elif value == 'Reading':
                browser.all('.custom-checkbox').element_by(have.exact_text('Reading')).click()
            elif value == 'Music':
                browser.all('.custom-checkbox').element_by(have.exact_text('Music')).click()

        # Directory file
        browser.element('#uploadPicture').send_keys(os.path.abspath(direct))

        # Address
        browser.element('#currentAddress').type(address)

        # State and city
        if state == 'NCR':
            browser.element('#state').click().element('#react-select-3-option-0').click()
            if city == 'Delhi':
                browser.element('#city').click().element('#react-select-4-option-0').click()
            if city == 'Gurgaon':
                browser.element('#city').click().element('#react-select-4-option-1').click()
            if city == 'Noida':
                browser.element('#city').click().element('#react-select-4-option-2').click()
        elif state == 'Uttar Pradesh':
            browser.element('#state').click().element('#react-select-3-option-1').click()
            if city == 'Agra':
                browser.element('#city').click().element('#react-select-4-option-0').click()
            if city == 'Lucknow':
                browser.element('#city').click().element('#react-select-4-option-1').click()
            if city == 'Merrut':
                browser.element('#city').click().element('#react-select-4-option-2').click()
        elif state == 'Haryana':
            browser.element('#state').click().element('#react-select-3-option-2').click()
            if city == 'Karnal':
                browser.element('#city').click().element('#react-select-4-option-0').click()
            if city == 'Panipat':
                browser.element('#city').click().element('#react-select-4-option-1').click()
        elif state == 'Rajasthan':
            browser.element('#state').click().element('#react-select-3-option-3').click()
            if city == 'Jaipur':
                browser.element('#city').click().element('#react-select-4-option-0').click()
            if city == 'Jaiselmer':
                browser.element('#city').click().element('#react-select-4-option-1').click()

    # Submit
    def submit(self):
        return browser.element('#submit').press_enter()

    # Should
    def should_user(self):
        return browser.element('.table').all('td').even