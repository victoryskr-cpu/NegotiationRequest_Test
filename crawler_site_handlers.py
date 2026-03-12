
from crawler_utils import fetch_html, extract_text_lines

def check_site(name, url):
    try:
        html = fetch_html(url)
        lines = extract_text_lines(html)

        found = False
        for line in lines:
            if "교섭" in line:
                found = True
                break

        if found:
            return {
                "site": name,
                "status": "FOUND",
                "url": url
            }
        else:
            return {
                "site": name,
                "status": "NOT_FOUND",
                "url": url
            }

    except Exception as e:
        return {
            "site": name,
            "status": "ERROR",
            "error": str(e),
            "url": url
        }
