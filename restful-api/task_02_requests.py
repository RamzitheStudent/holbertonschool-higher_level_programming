#!/usr/bin/python3
"""Fetches posts from JSONPlaceholder and processes them."""

import requests
import csv


def fetch_and_print_posts():
    """Fetches all posts and prints the titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print("Status Code:", response.status_code)

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """Fetches all posts and saves them into a CSV file."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        data_to_save = []
        for post in posts:
            data_to_save.append({
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            })

        # Save to CSV
        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data_to_save)


if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
