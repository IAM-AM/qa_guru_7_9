import allure
from selene import browser, by, be
from selene.support.shared.jquery_style import s
from allure_commons.types import Severity


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.feature("Issues in Repository")
@allure.story("Created issue is shown")
@allure.link("https://github.com/", name='Testing')
@allure.label('owner', 'IAM-AM')
def test_github_issue_selene():
    browser.open("https://github.com")

    s(".search-input").click()
    s('//*[@id="query-builder-test"]').type("eroshenkoam/allure-example").press_enter()

    s('[data-testid=results-list]').element(by.link_text('eroshenkoam/allure-example')).click()

    s('#issues-tab').click()

    s(by.partial_text('#81')).should(be.visible)
