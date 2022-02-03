import re

"""
https://www.w3schools.com/python/python_regex.asp
"""

txt = '''
<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">

<channel>
<title>{{ title }}</title>
<link>{{ site_url }}/</link>
<description>Grow with Technology</description>

{{ content }}

</channel>
</rss>
'''

expre = '{{\s*([^}\s]+)\s*}}'
resp = re.findall(expre, txt)
print(resp)