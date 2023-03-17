class SharePage:
    def __init__(self, page):
        self.page = page
        self.continue_link = page.get_by_role(
            "link", name="Continue to LinkedIn")
        self.post_button = page.get_by_role(
            "button", name="vishnu vardhan reddy usirike Me")
        self.sign_out_link = page.get_by_role("link", name="Sign Out")

    def click_continue_link(self):
        self.continue_link.click()

    def share_post(self):
        self.post_button.click()

    def sign_out(self):
        self.sign_out_link.click()