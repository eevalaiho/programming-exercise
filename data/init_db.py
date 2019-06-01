import sqlite3
conn = sqlite3.connect('../data/scraping.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE items
             (time text, url text, pattern text, content text)''')

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()