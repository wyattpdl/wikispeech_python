import sys
import wikipedia as wiki

# get
query = input("wikiwut\n")
result = wiki.page(title=query)
# write
file = open(result.title + ".txt", 'w')
file.write(result.content)
file.close()