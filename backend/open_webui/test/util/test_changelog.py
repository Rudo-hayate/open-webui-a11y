from open_webui.utils.changelog import hide_decorative_leading_icon


def test_hide_decorative_leading_icon_wraps_leading_emoji():
    raw_html = '<li>🔐 <strong>Custom OIDC logout endpoint.</strong> Added support.</li>'

    result = hide_decorative_leading_icon(raw_html)

    assert 'aria-hidden="true"' in result
    assert '<span aria-hidden="true">🔐 </span>' in result
    assert '<strong>Custom OIDC logout endpoint.</strong> Added support.' in result


def test_hide_decorative_leading_icon_leaves_non_icon_prefix_unchanged():
    raw_html = '<li><strong>Custom OIDC logout endpoint.</strong> Added support.</li>'

    result = hide_decorative_leading_icon(raw_html)

    assert result == raw_html

