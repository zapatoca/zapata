from zapata.app.models.fee import Fee


def test_Fee():
    fee = Fee(
        Apartment=1,
        Fee_type=2,
        Amount=1000,
        project=1,
    )
    assert fee.Jan == 0
    assert fee.Feb == 0
    assert fee.Balance == 0
    assert fee.Alert is True
