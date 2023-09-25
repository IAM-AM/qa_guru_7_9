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
def test_github_issue_name_lambda_steps():
    with allure.step("Open github main page"):
        browser.open("https://github.com")

    with allure.step("Search for repository {repo}"):
        s(".search-input").click()
        s('//*[@id="query-builder-test"]').send_keys("eroshenkoam/allure-example").press_enter()

    with allure.step("Follow the repository link"):
        s('[data-testid=results-list]').element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step("Open Issues tab"):
        s('#issues-tab').click()

    with allure.step("Check for the issue 81 {number} is existed"):
        s(by.partial_text('#81')).should(be.visible)



