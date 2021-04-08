import random
from model.project import Project


def test_dell_project(app, db, json_project):
    username = "administrator"
    password = "root"
    app.session.login(username, password)
    if len(db.get_project_list()) == 0:
        app.project.create_new_project(json_project)
    app.project.open_project_page()
    old_project = app.soap.get_list_project(username, password)
    project = random.choice(old_project)
    app.project.delete_project_by_name(project.name)
    new_project = app.soap.get_list_project("administrator", "root")
    old_project.remove(project)
    assert sorted(old_project, key=Project.id_or_max) == sorted(new_project, key=Project.id_or_max)