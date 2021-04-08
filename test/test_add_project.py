from model.project import Project


def test_add_project(app, db, json_project):
    project = json_project
    app.session.login("administrator", "root")
    old_project = db.get_project_list()
    app.project.create_new_project(json_project)
    new_project = db.get_project_list()
    old_project.append(project)
    assert sorted(old_project, key=Project.id_or_max) == sorted(new_project, key=Project.id_or_max)