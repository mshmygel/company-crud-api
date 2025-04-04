def test_company_str(company_factory):
    company = company_factory(company_name="Kyrsor")
    assert str(company) == "Kyrsor"
