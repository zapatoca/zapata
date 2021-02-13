def test_new_project(selenium):
    selenium.get("http://localhost:5000/projects/new")
    assert (
        selenium.find_element_by_class_name("card-header").text
        == "New Project"
    )
