# Initialize counter
numlines = 0

# Get contents of README
with open("README.md","r") as f:
    for line in f:
        numlines+=1

# Create HTML data
html_page = f'<html>\n<head></head>\n<body><p>Number of lines in README.md is {numlines}</p></body>\n</html>'

# Create html
with open("lines.html","w") as f:
    f.write(html_page)
