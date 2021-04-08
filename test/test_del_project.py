import random
from model.project import Project


def test_dell_project(app, db):
    app.session.login("administrator", "root")
    app.project.open_project_page()
    if len(db.get_project_list()) == 0:
        app.project.create_new_project(Project(name="Project to delete"))
    old_project = db.get_project_list()
    project = random.choice(old_project)
    app.project.delete_project_by_name(project.name)
    new_project = db.get_project_list()
    old_project.remove(project)
    assert sorted(old_project, key=Project.id_or_max) == sorted(new_project, key=Project.id_or_max)