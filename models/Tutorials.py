from services import connect_snowflake


class Tutorial:
    def __init__(self, id, name, date, author, content):
        self.id = id
        self.name = name
        self.date = date
        self.author = author
        self.content = content

    
    def __str__(self):
        return f"Tutorial(ID: {self.id}, Name: '{self.name}', Date: {self.date}, Author: '{self.author}', Content: '{self.content[:30]}...')"

    # Other methods...