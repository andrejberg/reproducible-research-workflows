#!/usr/bin/env python3
# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///
"""Fill in your Git name and email from your Jupyter4NFDI account, where you have not set them.

The lab runs this at every start, and setup_module.py runs it before its first commit. It
asks the hub who you are and sets only a value that is missing, so a name or email you set
yourself always stays. If the hub does not answer, nothing changes.

Your email goes into every commit you make. To use another name or email, set it yourself
in a terminal; it is kept in work/ and replaces the one from your account:

    git config --global user.name "Your Name"
    git config --global user.email "you@example.org"
"""

import http.client
import json
import os
import subprocess
import urllib.request

KEYS = ("user.name", "user.email")
TIMEOUT = 3  # seconds; the lab must start even when the hub does not answer


def configured(key):
    """Return the value Git has for key, or an empty string."""
    result = subprocess.run(["git", "config", "--global", "--get", key], capture_output=True, text=True)
    return result.stdout.strip() if result.returncode == 0 else ""


def usable(value):
    return (isinstance(value, str) and value.strip() and len(value) < 256
            and value.isprintable())


def from_hub():
    """Return the name and email the hub has for this lab's user, as far as it has them."""
    url, token = os.environ.get("JUPYTERHUB_API_URL"), os.environ.get("JUPYTERHUB_API_TOKEN")
    if not (url and token):
        return {}
    request = urllib.request.Request(url.rstrip("/") + "/user", headers={"Authorization": f"token {token}"})
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
            user = json.load(response)
    except (OSError, ValueError, http.client.HTTPException):
        return {}
    info = user.get("user_info") if isinstance(user, dict) else None
    if not isinstance(info, dict):
        return {}
    name, email = info.get("display_name"), info.get("email")
    values = {}
    if usable(name):
        values["user.name"] = name.strip()
    if usable(email) and "@" in email and " " not in email.strip():
        values["user.email"] = email.strip()
    return values


def fill_in():
    """Set the missing ones of user.name and user.email from the hub; return what was set."""
    missing = [key for key in KEYS if not configured(key)]
    if not missing:
        return {}
    values = from_hub()
    written = {}
    for key in missing:
        if key in values:
            result = subprocess.run(["git", "config", "--global", key, values[key]], capture_output=True, text=True)
            if result.returncode == 0:
                written[key] = values[key]
    return written


if __name__ == "__main__":
    for key in fill_in():
        print(f"Git {key} set from your Jupyter4NFDI account.")
