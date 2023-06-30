import pytest

from auth import login_as_superuser


@pytest.mark.only_browser("chromium")
def test_click_back_to_all(page):
    """Opens report detail page and goes back to reports page"""

    login_as_superuser(page)

    page.goto("/form/view")

    with page.expect_navigation():
        page.evaluate("document.querySelector('.td-link').click()")

    assert page.is_visible("#contact-info")

    with page.expect_navigation():
        page.evaluate("document.getElementById('backtoall').click()")

    assert page.is_visible("#contact-email-filter")

    page.goto("/form/dashboard/activity")

    page.evaluate("document.querySelector('select[name=\"assigned_to\"]')[2].click()")
    
    with page.expect_navigation():
        assert page.evaluate("document.querySelector('.td-link')[0].click()")
    
    assert page.is_visible("#contact-info")

    with page.expect_navigation():
        page.evaluate("document.getElementById('backtoall').click()")

    assert page.is_visible("#actions")
