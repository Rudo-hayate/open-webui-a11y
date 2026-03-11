import re

from bs4 import BeautifulSoup, NavigableString

LEADING_DECORATIVE_ICON_RE = re.compile(
    r'^(?P<leading>\s*)(?P<icon>[\u2600-\u27BF\U0001F300-\U0001FAFF\uFE0F\u200D]+)(?P<space>\s+)'
)


def hide_decorative_leading_icon(raw_html: str) -> str:
    soup = BeautifulSoup(raw_html, "html.parser")
    item = soup.find("li")

    if item is None:
        return raw_html

    for child in item.contents:
        if not isinstance(child, NavigableString):
            if getattr(child, "get_text", None) and child.get_text(strip=True):
                return str(item)
            continue

        text = str(child)
        if not text.strip():
            continue

        match = LEADING_DECORATIVE_ICON_RE.match(text)
        if match is None:
            return str(item)

        hidden_text = f'{match.group("icon")}{match.group("space")}'
        remainder = text[match.end() :]

        if match.group("leading"):
            child.insert_before(NavigableString(match.group("leading")))

        hidden_icon = soup.new_tag("span")
        hidden_icon["aria-hidden"] = "true"
        hidden_icon.string = hidden_text
        child.insert_before(hidden_icon)

        if remainder:
            child.insert_before(NavigableString(remainder))

        child.extract()
        return str(item)

    return str(item)

