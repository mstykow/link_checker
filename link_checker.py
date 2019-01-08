#! python3
# Program lists all broken links within a given URL.

import requests, bs4

def complete_URL(hrefValue, parent):
    if hrefValue.startswith('http'):
        return hrefValue
    else:
        return parent + hrefValue

print('Enter the URL you wish to check for dead links:')
checksite = input()
print('Checking...')

# Get URL contents and collect all links.
ro = requests.get(checksite)
try:
    ro.raise_for_status()
except Exception as err:
    print('There was a problem: %s' % (exc))

soup = bs4.BeautifulSoup(ro.text, "html.parser")
matchList = soup.select('a[href]')

# Collect only dead links in a list.
deadlinks = []
for match in matchList:
    link = match.get('href')
    try:
        matchRequest = requests.get(complete_URL(link, checksite))
        matchRequest.raise_for_status()
    except:
        deadlinks.append(link)

# Print out the list if non-empty.
print('Check complete.')
if deadlinks == []:
    print('No dead links found in this page.')
else:
    print('There were %s broken links on this page.' % str(len(deadlinks)) )
    print('List of broken links:')
    for link in deadlinks:
        print(link)
