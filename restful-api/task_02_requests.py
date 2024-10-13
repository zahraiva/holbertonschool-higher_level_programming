import requests
import csv

def fetch_and_print_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status Code: {}".format(r.status_code))
    if r.status_code == 200:
        posts = r.json()
        for p in posts:
            print(p['title'])

def fetch_and_save_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    if r.status_code == 200:
        posts = r.json()
        p_data = []
        for post in posts:
            p_info = {"id": post["id"], "title": post["title"], "body": post["body"]}
            p_data.append(p_info)
        with open("posts.csv", mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(p_data)
        print("Data has been written to posts.csv")

def main():
    fetch_and_print_posts()
    fetch_and_save_posts()

if __name__ == "__main__":
    main()
