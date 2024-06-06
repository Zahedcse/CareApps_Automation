from selenium.webdriver.common.by import By

from Pages.utilities import Page


class Dashboard(Page):
    DashboardText = (By.XPATH, "//div[contains(text(), 'Dashboard')]")
    DashboardList = (By.XPATH, "//ul/li")

    def verify_dashboard(self):
        self.assert_text("Dashboard", self.DashboardText)

    def click_on_med(self):
        list_of_sections = self.DashboardList
        for section in list_of_sections:
            if section.text == "Med Management ":
                section.click()
            else:
                print(f"{section} section not found")
