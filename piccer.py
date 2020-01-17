import re
import sys

import requests


def main():
    base_url = "https://www.bing.com"
    output_folder = "/media/sax/windows/Users/woefu/Pictures/bingpics/"
    if len(sys.argv) == 1:
        num_pics = 1
    else:
        num_pics = sys.argv[1]

    r = requests.get(f"{base_url}/HPImageArchive.aspx?format=js&idx=0&n={num_pics}")
    if r.status_code != 200:
        raise ValueError("Could not get image information: status code {r.status_code}")
    j = r.json()

    for image_info in j["images"]:
        print(image_info)
        url = base_url + image_info["url"]
        print(image_info["title"])
        filename = output_folder + clean_string(image_info["title"]) + ".jpg"
        get_pic(url, filename)


def get_pic(url, filename):
    r = requests.get(url, allow_redirects=True)
    with open(filename, "wb") as f:
        f.write(r.content)


def clean_string(s):
    s = s.lower().strip().replace(" ", "_")
    s = re.sub(r"(?u)[^-\w.]", "", s)
    return s


if __name__ == "__main__":
    main()
