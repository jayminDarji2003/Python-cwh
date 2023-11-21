# request module in python
"""
    There are lots of other function we can use it to achieve the web scripting tasks

        1. get
        2. post
        3. delete
        4. update
        
"""

import requests

response = requests.get("https://www.google.com")
print(response.text)
