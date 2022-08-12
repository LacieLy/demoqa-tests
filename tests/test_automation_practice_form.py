from selene import have, command
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss


def test_practice_form():
    browser.open('/automation-practice-form')

#General info
    s('#firstName').type('Lacie')
    s('#lastName').type('Lyn')
    s('#userEmail').type('Lyn@gmail.com')
    # s('//*[contains(@class, "custom-radio")][contains (.//text(), "Female")]')
    ss('.custom-radio').element_by(have.exact_text('Female')).click()
    s('#userNumber').type('6666666666')

#Date of Birth
    s('#dateOfBirthInput').click()
    s('.react-datepicker__month-select').type('January')
    s('.react-datepicker__year-select').type('1993')
    s('.react-datepicker__day--013').click()

#Subjects
    s('#subjectsInput').type('English').press_enter()
    s('#subjectsInput').type('Computer Science').press_enter()

#Hobbies
    ss('.custom-checkbox').element_by(have.exact_text('Reading')).click()
    ss('.custom-checkbox').element_by(have.exact_text('Music')).click()

#Picture


#Address
    s('#currentAddress').type('SPB')
    s('#react-select-3-input').type('NCR').press_enter()
    s('#react-select-4-input').type('Delhi').press_enter()

    s('#submit').perform(command.js.click)

#Assert
    ss(".table-responsive").should(have.texts(
        'Lacie Lyn',
        'Lyn@gmail.com'
    ))