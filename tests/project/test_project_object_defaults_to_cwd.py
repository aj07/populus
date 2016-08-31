from populus.utils.filesystem import is_same_path
from populus.project import Project


def test_project_dir_defaults_to_cwd(project_dir):
    project = Project()

    assert is_same_path(project.project_dir, project_dir)
