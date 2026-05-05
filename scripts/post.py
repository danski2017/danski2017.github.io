#!/usr/bin/env python3
"""
Facebook page poster for Atlas Solver Hub and related pages.

Usage:
    python scripts/post.py --page atlas --message "Your post text"
    python scripts/post.py --page atlas --message "Caption" --image images/retained_pair_budget.png
    python scripts/post.py --page atlas --message "Check this out" --link https://danski2017.github.io

Required environment variables (set in .env or your shell):
    FB_PAGE_TOKEN_ATLAS   - Page Access Token for the Atlas Solver Hub page
    FB_PAGE_TOKEN_OTHER   - Page Access Token for your second page
    FB_PAGE_ID_ATLAS      - Numeric Page ID for Atlas Solver Hub
    FB_PAGE_ID_OTHER      - Numeric Page ID for your second page
"""

import argparse
import os
import sys
import requests

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv optional; env vars can be set in the shell directly

GRAPH_API = "https://graph.facebook.com/v19.0"

PAGES = {
    "atlas": {
        "token_env": "FB_PAGE_TOKEN_ATLAS",
        "id_env":    "FB_PAGE_ID_ATLAS",
    },
    "other": {
        "token_env": "FB_PAGE_TOKEN_OTHER",
        "id_env":    "FB_PAGE_ID_OTHER",
    },
}


def get_page_config(page_key):
    if page_key not in PAGES:
        print(f"Error: unknown page '{page_key}'. Choose from: {', '.join(PAGES)}")
        sys.exit(1)
    cfg = PAGES[page_key]
    token = os.getenv(cfg["token_env"])
    page_id = os.getenv(cfg["id_env"])
    if not token:
        print(f"Error: {cfg['token_env']} environment variable is not set.")
        sys.exit(1)
    if not page_id:
        print(f"Error: {cfg['id_env']} environment variable is not set.")
        sys.exit(1)
    return token, page_id


def post_text(token, page_id, message):
    url = f"{GRAPH_API}/{page_id}/feed"
    resp = requests.post(url, data={"message": message, "access_token": token})
    return resp.json()


def post_image(token, page_id, message, image_path):
    if not os.path.exists(image_path):
        print(f"Error: image file not found: {image_path}")
        sys.exit(1)
    url = f"{GRAPH_API}/{page_id}/photos"
    with open(image_path, "rb") as f:
        resp = requests.post(url, data={"caption": message, "access_token": token}, files={"source": f})
    return resp.json()


def post_link(token, page_id, message, link):
    url = f"{GRAPH_API}/{page_id}/feed"
    resp = requests.post(url, data={"message": message, "link": link, "access_token": token})
    return resp.json()


def main():
    parser = argparse.ArgumentParser(description="Post to a Facebook Page via the Graph API.")
    parser.add_argument("--page",    required=True, choices=list(PAGES), help="Which page to post to")
    parser.add_argument("--message", required=True, help="Post text / caption")
    parser.add_argument("--image",   help="Path to an image file to attach")
    parser.add_argument("--link",    help="URL to attach as a link preview")
    args = parser.parse_args()

    token, page_id = get_page_config(args.page)

    if args.image:
        result = post_image(token, page_id, args.message, args.image)
    elif args.link:
        result = post_link(token, page_id, args.message, args.link)
    else:
        result = post_text(token, page_id, args.message)

    if "id" in result:
        print(f"Posted successfully. Post ID: {result['id']}")
    else:
        print(f"Error from Facebook API: {result}")
        sys.exit(1)


if __name__ == "__main__":
    main()
