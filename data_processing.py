import csv
import sqlite3

con = sqlite3.connect("billboard.db")
cur = con.cursor()
cur.execute("CREATE TABLE billboard (url, week_id, week_position, song, performer, song_id, instance, previous_week_position, peak_position, weeks_on_chart);")

with open('billboard.csv', 'r') as file:
    dictReader = csv.DictReader(file)
    to_db = [(i['url'], i['week_id'],
              i['week_position'], i['song'], i['performer'], i['song_id'], i['instance'], i['previous_week_position'], i['peak_position'], i['weeks_on_chart']) for i in dictReader]

cur.executemany("INSERT INTO billboard (url, week_id, week_position, song, performer, song_id, instance, previous_week_position, peak_position, weeks_on_chart) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
con.commit()
con.close()
