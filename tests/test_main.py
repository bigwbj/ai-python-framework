import os

def test_project_structure():
    # Check if .gitignore exists
    assert os.path.isfile('.gitignore'), ".gitignore file is missing."

    # Check if docs/requirements.txt exists
    assert os.path.isfile('docs/requirements.txt'), "docs/requirements.txt file is missing."

    # check if folder requirements exists
    assert os.path.exists('requirements'), "requirements folder is missing."
    assert os.path.exists('use_case'), "use_case folder is missing."
    assert os.path.exists('unit_test'), "unit_test folder is missing."
    assert os.path.exists('src'), "src folder is missing."
    assert os .path.exists('tests'), "tests folder is missing."
    assert os.path.exists('docs'), "docs folder is missing." 
