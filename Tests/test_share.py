from playwright.sync_api import Page


def test_run(page: Page):

    page.goto("https://www.google.com/")
    page.get_by_role("combobox", name="Search").click()
    page.get_by_role("combobox", name="Search").fill("rolex")
    page.get_by_role("combobox", name="Search").press("Enter")
    page.get_by_role("link", name="The Rolex® Collection").click()
    with page.expect_popup() as page1_info:
        page.get_by_role(
            "button", name="Share this page on Linkedin New tab").click()
    page1 = page1_info.value
    page1.get_by_label("Email or Phone").fill("8247548679")
    page1.get_by_label("Email or Phone").press("Tab")
    page1.get_by_label("Password").fill("vishnu161999")
    page1.get_by_role("button", name="Sign in", exact=True).click()
    page1.get_by_role("button", name="Share in a post").click()
    page1.get_by_role("button", name="Post", exact=True).click()
    with page1.expect_popup() as page2_info:
        page1.get_by_role("link", name="Continue to LinkedIn").click()
    page2 = page2_info.value
    page2.get_by_role("button", name="vishnu vardhan reddy usirike Me").click()
    page2.get_by_role("link", name="Sign Out").click()
    page2.get_by_role("button", name="Sign out", exact=True).click()
    page2.close()

# home_page.py
# class HomePage:
#     def __init__(self, page):
#         self.page = page
#         self.search_box = page.get_by_role("combobox", name="Search")
#         self.rolex_link = page.locator(
#             "//h3[normalize-space()='Official Rolex Website - Swiss Luxury Watches']")

#     def search_for(self, query):
#         self.search_box.fill(query)
#         self.search_box.press("Enter")

#     def click_rolex_link(self):
#         self.rolex_link.click()

# # login_page.py


# class LoginPage:
#     def __init__(self, page):
#         self.page = page
#         self.email_field = page.get_by_label("Email or Phone")
#         self.password_field = page.get_by_label("Password")
#         self.sign_in_button = page.locator(
#             "#organic-div form").get_by_role("button", name="Sign in")

#     def login(self, email, password):
#         self.email_field.fill(email)
#         self.password_field.fill(password)
#         self.sign_in_button.click()

# # share_page.py


# class SharePage:
#     def __init__(self, page):
#         self.page = page
#         self.continue_link = page.get_by_role(
#             "link", name="Continue to LinkedIn")
#         self.post_button = page.get_by_role(
#             "button", name="vishnu vardhan reddy usirike Me")
#         self.sign_out_link = page.get_by_role("link", name="Sign Out")

#     def click_continue_link(self):
#         self.continue_link.click()

#     def share_post(self):
#         self.post_button.click()

#     def sign_out(self):
#         self.sign_out_link.click()

# # test_case.py


# class TestShareOnLinkedin:
#     def __init__(self, browser):
#         self.browser = browser

#     def run(self, query, email, password):
#         home_page = HomePage(self.browser)
#         home_page.page.goto("https://www.linkedin.com/")
#         home_page.search_for(query)
#         home_page.click_rolex_link()

#         login_page = LoginPage(home_page.page.expect_popup())
#         login_page.login(email, password)

#         share_page = SharePage(login_page.page.expect_popup())
#         share_page.click_continue_link()
#         share_page.share_post()
#         share_page.sign_out()
