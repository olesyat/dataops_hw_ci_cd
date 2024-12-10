from hello import app


def test_hello():
    response = app.test_client().get('/')

    assert response.status_code == 200

# def test_missing_config(monkeypatch):
#     # Simulate config.read throwing FileNotFoundError
#     monkeypatch.setattr("configparser.RawConfigParser.read", lambda self, file: None)
#     response = app.test_client().get('/')
#     assert response.data.decode() == "Hello, World!"
#
# def test_hello_message_olesia(monkeypatch):
#     # Simulate feature_12 enabled
#     monkeypatch.setattr("configparser.RawConfigParser.getboolean", lambda self, section, key: key == "feature_12")
#     response = app.test_client().get('/')
#     assert response.data.decode() == "Hello, Olesia!"