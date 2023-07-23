

# Place the code on that folder where you want to download the images
# Open the folder in VS Code. If you dont open the folder, images will not download in your pC
''' Just paste the image link after run the code. as it is running with WHILE loop you can paste as many link as you want'''

import requests

url = 'https://farm66.staticflickr.com/65535/33978196618_632623b4fc_z.jpg'

while True:
    url=input()
    filename = url.split('/')[-1]
    r = requests.get(url, allow_redirects=True)
    open(filename, 'wb').write(r.content)