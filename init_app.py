import sys, os
import sqlite3

def createDb(path):
    conn = sqlite3.connect(path)
    try:
        c = conn.cursor()
        # Create table
        c.execute('''CREATE TABLE scrapeItem
                    (scrape_time text, url text, status text, pattern text, matches text)''')
        # Save (commit) the changes
        conn.commit()
    except Exception as e:
        conn.close()
        print('Error creating database')
        throw(e)
    conn.close()

if __name__ == "__main__":
    # Append program dir to path
    dir = os.path.dirname(os.path.abspath(__file__)) + '/modules'
    if not dir in sys.path:
        sys.path.append(dir)
        print("Appended sys.path")
    print(sys.path)#
    # Create db
    if not os.path.exists('data'):
        os.makedirs('data')
        print('Created dir \'data\'')
    if not os.path.exists('data/scraping.db'):
        createDb('data/scraping.db')
        print('Created database')
