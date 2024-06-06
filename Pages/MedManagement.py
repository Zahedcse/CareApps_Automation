from selenium.webdriver.common.by import By

from Pages.utilities import Page


class MedManagement(Page):
    Dashboard = (By.LINK_TEXT, "Dashboard")
    EmarDashboardText = (By.CSS_SELECTOR, "#rc-tabs-22-tab-1")
    ResidentTiles = ()

