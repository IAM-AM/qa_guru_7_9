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
def test_github_issue_decorator_steps():
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_issue_tab()
    should_see_issue_number("#81")


@allure.step("Open github main page")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Search for repository {repo}")
def search_for_repository(repo):
    s(".search-input").click()
    s('//*[@id="query-builder-test"]').send_keys(repo).press_enter()


@allure.step("Follow the repository link")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Open Issues tab")
def open_issue_tab():
    s('#issues-tab').click()


@allure.step("Check for the issue 81 {number} is existed")
def should_see_issue_number(number):
    s(by.partial_text(number)).should(be.visible)