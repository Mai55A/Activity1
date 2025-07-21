# my_sites.py

import webbrowser

# 1) Dictionary: {number: (site_name, site_url)}
sites = {
    1: ("Google", "https://www.google.com"),
    2: ("YouTube", "https://www.youtube.com"),
    3: ("GitHub", "https://www.github.com"),
    4: ("Wikipedia", "https://www.wikipedia.org")
}

# 2) Function to open a website
def open_site(url):
    webbrowser.open(url)
