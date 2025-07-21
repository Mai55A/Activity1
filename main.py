# main.py

from my_sites import sites, open_site

# 1) Print menu
print("Choose a website to open:\n")
for number, (name, _) in sites.items():
    print(f"{number}. {name}")

# 2) Ask user for input
try:
    choice = int(input("\nEnter the number of the website: "))
    
    if choice in sites:
        _, url = sites[choice]
        open_site(url)
        print(f"Opening {url}...")
    else:
        print("Invalid number. Please try again.")
except ValueError:
    print("Invalid input. Please enter a number.")
