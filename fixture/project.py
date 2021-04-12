from selenium.webdriver.support.ui import Select
from model.project import Project


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def open_project_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def create_project(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()

    def fill_in_project(self, Project):
        wd = self.app.wd
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(Project.name)
        wd.find_element_by_name("status").click()
        Select(wd.find_element_by_name("status")).select_by_visible_text(Project.status)
        wd.find_element_by_name("view_state").click()
        Select(wd.find_element_by_name("view_state")).select_by_visible_text(Project.view)
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(Project.description)

    def save_project(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def create_new_project(self, project):
        self.open_project_page()
        self.create_project()
        self.fill_in_project(project)
        self.save_project()

    def dell_project(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()

    def delete_project_by_name(self, name):
        wd = self.app.wd
        wd.find_element_by_link_text(name).click()
        self.dell_project()