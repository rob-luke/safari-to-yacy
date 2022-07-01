#!/usr/bin/env python3
"""Send current Safari URL to Yacy

This script will extract the url from the foremost
window of Safari and send it to be indexed in the
Yacy search engine.
"""

from subprocess import PIPE
import subprocess
from pydantic import BaseSettings
import requests
from requests.auth import HTTPDigestAuth


class Settings(BaseSettings):
    """Settings with defaults."""

    yacy_url: str = ""
    verbose: bool = True
    yacy_auth_username: str = ""
    yacy_auth_password: str = ""


def generate_search_string(
    yacy_url: str, crawlingURL: str, crawlingMode: str = "url", crawlingDepth: int = 0
) -> str:
    """Create search string in yacy format."""

    url = (
        f"{yacy_url}/Crawler_p.html?crawlingURL={crawlingURL}"
        f"&crawlingMode={crawlingMode}"
        f"&crawlingDepth={crawlingDepth}"
        f"&crawlingstart="
    )

    return url


def get_safari_url() -> str:
    """Get URL of current tab in Safari."""
    cmd = "osascript -e 'tell application \"Safari\" to URL of document 1'"
    pipe = subprocess.Popen(cmd, shell=True, stdout=PIPE).stdout
    url = pipe.readlines()[0].decode("UTF-8")  # type: ignore
    return url


def main() -> None:
    """Main program loop."""

    settings = Settings()
    site_url = get_safari_url()
    query_url = generate_search_string(settings.yacy_url, site_url)

    if settings.verbose:
        print(settings.dict())
        print(site_url)
        print(query_url)

    _ = requests.get(
        url=query_url,
        auth=HTTPDigestAuth(settings.yacy_auth_username, settings.yacy_auth_password),
    )

    return None


if __name__ == "__main__":
    main()
