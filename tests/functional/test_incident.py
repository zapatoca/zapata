def test_file_incident(selenium):
    selenium.get("https://localhost:8443/incident")
    selenium.find_element_by_id("description").send_keys(
        "reporting an incident"
    )
    selenium.find_element_by_id("submit").click()
    assert "https://localhost:8443/" == selenium.current_url
