class HomePage:
    def __init__(self, page):
        self.page = page
        self.search_box = page.get_by_role("combobox", name="Search")
        self.rolex_link = page.locator(
            "//h3[normalize-space()='Official Rolex Website - Swiss Luxury Watches']")

    def search_for(self, query):
        self.search_box.fill(query)
        self.search_box.press("Enter")

    def click_rolex_link(self):
        self.rolex_link.click()