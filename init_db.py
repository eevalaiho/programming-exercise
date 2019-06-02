import os
import sqlite3

def createDb(path):
    conn = sqlite3.connect(path)
    try:
        c = conn.cursor()
        # Create table
        c.execute('''CREATE TABLE scrapeItem
                    (scrape_time text, url text, pattern text, matches text)''')
        # Save (commit) the changes
        conn.commit()
    except Exception as e:
        conn.close()
        print('Error creating database')
        throw(e)
    conn.close()

if __name__ == "__main__":
    if not os.path.exists('data'):
        os.makedirs('data')
    createDb('data/scraping.db')
