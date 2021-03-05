def test_new_project(selenium):
    selenium.get("https://localhost:8443/projects/new")
    assert (
        selenium.find_element_by_class_name("card-header").text
        == "New Project"
    )
