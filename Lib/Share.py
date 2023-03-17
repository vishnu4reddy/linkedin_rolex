from playwright.sync_api import Page


def run(page: Page):

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
    page1.get_by_label("Password").fill("vishnu16")
    page1.get_by_label("Password").press("CapsLock")
    page1.get_by_label("Password").fill("vishnu16REDDY@")
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
