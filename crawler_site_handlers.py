from crawler_utils import fetch_html, extract_text_lines


def is_saeol_like(url):
    return "eminwon" in url or "saeol" in url


def is_egov_like(url):
    return "bbs" in url or "board" in url


def is_custom_like(url):
    return "list.do" in url or "contents.do" in url


def check_saeol_common(name, url):
    html = fetch_html(url)
    lines = extract_text_lines(html)

    for line in lines:
        if "교섭" in line:
            return {"site": name, "status": "FOUND", "url": url}

    return {"site": name, "status": "NOT_FOUND", "url": url}


def check_egov_common(name, url):
    html = fetch_html(url)
    lines = extract_text_lines(html)

    for line in lines:
        if "교섭" in line:
            return {"site": name, "status": "FOUND", "url": url}

    return {"site": name, "status": "NOT_FOUND", "url": url}


def check_custom_common(name, url):
    html = fetch_html(url)
    lines = extract_text_lines(html)

    for line in lines:
        if "교섭" in line:
            return {"site": name, "status": "FOUND", "url": url}

    return {"site": name, "status": "NOT_FOUND", "url": url}


def check_site(name, url):

    try:

        if is_saeol_like(url):
            return check_saeol_common(name, url)

        if is_egov_like(url):
            return check_egov_common(name, url)

        if is_custom_like(url):
            return check_custom_common(name, url)

        html = fetch_html(url)
        lines = extract_text_lines(html)

        for line in lines:
            if "교섭" in line:
                return {"site": name, "status": "FOUND", "url": url}

        return {"site": name, "status": "NOT_FOUND", "url": url}

    except Exception as e:

        return {
            "site": name,
            "status": "ERROR",
            "error": str(e),
            "url": url
        }
