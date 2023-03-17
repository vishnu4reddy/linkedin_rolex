from Lib.home_page import HomePage
from Lib.share_page import SharePage
from Lib.login_page import LoginPage


class TestShareOnLinkedin:
    def __init__(self, browser):
        self.browser = browser

    def run(self, query, email, password):
        home_page = HomePage(self.browser)
        home_page.page.goto("https://www.linkedin.com/")
        home_page.search_for(query)
        home_page.click_rolex_link()

        login_page = LoginPage(home_page.page.expect_popup())
        login_page.login(email, password)

        share_page = SharePage(login_page.page.expect_popup())
        share_page.click_continue_link()
        share_page.share_post()
        share_page.sign_out()




# from Lib.home_page import HomePage
# from playwright.sync_api import Page


# def test_homePage(page:Page):
#     homepage = HomePage(page)
#     homepage.