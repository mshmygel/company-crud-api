def test_user_creation(user_factory):
    user = user_factory(username="Mike")
    assert user.username == "Mike"
    assert user.is_active is True
