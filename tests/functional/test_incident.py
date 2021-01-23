def test_file_incident(selenium):
    selenium.get("http://localhost:5000/incident")
    selenium.find_element_by_id("description").send_keys(
        "reporting an incident"
    )
    selenium.find_element_by_id("submit").click()
    assert "http://localhost:5000/" == selenium.current_url
