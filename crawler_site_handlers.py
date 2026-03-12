from crawler_utils import fetch_html, extract_text_lines
import re


def clean_text(text: str) -> str:
    if not text:
        return ""
    return re.sub(r"\s+", " ", str(text)).strip()


def is_saeol_like(url: str) -> bool:
    u = (url or "").lower()
    keywords = [
        "selecteminwon",
        "selecteminwonweblist",
        "selecteminwonnoticelist",
        "/saeol/gosi/",
        "/prog/saeolgosi/",
        "/prog/eminwon/",
        "eminwon",
        "saeol",
        "gosi/list.do",
        "selectgosilist",
        "selectgosi",
    ]
    return any(k in u for k in keywords)


def is_egov_like(url: str) -> bool:
    u = (url or "").lower()
    keywords = [
        "selectbbsnttlist",
        "selectboardlist",
        "/bbs/",
        "bbsid=",
        "bbsno=",
        "boardid=",
        "bd_selectbbslist",
        "b000",
    ]
    return any(k in u for k in keywords)


def is_custom_like(url: str) -> bool:
    u = (url or "").lower()
    keywords = [
        "bbsnew",
        "contents.do",
        "page.do",
        "list.do",
        "board/list",
        "boardlist",
        "index.do?menu_id=",
        ".web",
        "/content/boards/",
        "/notice/",
        "/link/",
        "/html/sub",
    ]
    return any(k in u for k in keywords)


def find_keyword_lines(lines, keyword: str = "교섭"):
    matched = []
    for line in lines:
        line = clean_text(line)
        if keyword in line:
            matched.append(line)
    return matched


def extract_best_title(lines, keyword: str = "교섭") -> str:
    matched = find_keyword_lines(lines, keyword=keyword)
    if not matched:
        return ""
    matched.sort(key=len, reverse=True)
    return matched[0][:150]


def check_found_common(name: str, url: str, board_type: str):
    html = fetch_html(url)
    lines = extract_text_lines(html)

    matched = find_keyword_lines(lines, keyword="교섭")
    if matched:
        title = extract_best_title(lines, keyword="교섭")
        return {
            "site": name,
            "status": "FOUND",
            "url": url,
            "board_type": board_type,
            "title": title,
            "matched_count": len(matched),
        }

    return {
        "site": name,
        "status": "NOT_FOUND",
        "url": url,
        "board_type": board_type,
        "title": "",
        "matched_count": 0,
    }


def check_saeol_common(name: str, url: str):
    return check_found_common(name, url, "saeol")


def check_egov_common(name: str, url: str):
    return check_found_common(name, url, "egov")


def check_custom_common(name: str, url: str):
    return check_found_common(name, url, "custom")


def check_fallback(name: str, url: str):
    return check_found_common(name, url, "fallback")


def check_site(name: str, url: str):
    try:
        if is_saeol_like(url):
            return check_saeol_common(name, url)

        if is_egov_like(url):
            return check_egov_common(name, url)

        if is_custom_like(url):
            return check_custom_common(name, url)

        return check_fallback(name, url)

    except Exception as e:
        return {
            "site": name,
            "status": "ERROR",
            "url": url,
            "error": str(e),
            "board_type": "error",
            "title": "",
            "matched_count": 0,
        }
