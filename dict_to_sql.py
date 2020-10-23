import sqlite3


def test():
	dict_data = {
	'filename' : 'test.txt',
	'size' : '200'
	}

	

	table_name = 'test'
	attrib_names = ", ".join(dict_data.keys())
	attrib_values = ", ".join("?" * len(dict_data.keys()))
	sql = f"INSERT INTO {table_name} ({attrib_names}) VALUES ({attrib_values})"

	conn = sqlite3.connect('rview_app.db')
	c = conn.cursor()
	c.execute(sql, list(dict_data.values()))

	conn.commit()
	conn.close()


def addtable():
	conn = sqlite3.connect('rview_app.db')
	c = conn.cursor()
	c.execute("""CREATE TABLE test (
		filename text,
		size integer
		)""")
	conn.commit()
	conn.close()

def show():
	conn = sqlite3.connect('rview_app.db')
	c = conn.cursor()
	c.execute("SELECT * FROM test")
	records = c.fetchall()
	print (records)
	conn.commit()
	conn.close()

test()
show()
