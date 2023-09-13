from selene import browser, by, be
import allure


def test_github():
    browser.open("https://github.com")

    browser.element(".search-input").click()
    browser.element(".QueryBuilder-InputWrapper").type(
        'eroshenkoam/allure-example').press_enter()

    browser.element('[data-testid=results-list]').element(
        by.link_text('eroshenkoam/allure-example')).click()

    browser.element('#issues-tab').click()

    browser.element(by.partial_text('#81')).should(be.visible)