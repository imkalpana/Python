class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, key):
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value
    
    def add(self, key, value):
        hash_value = self.hash(key)
        if hash_value not in self.collection:
            self.collection[hash_value] = {}

        self.collection[hash_value][key] = value
        
    def remove(self, key):
        if self.hash(key) in self.collection and key in self.collection[self.hash(key)]:
            del self.collection[self.hash(key)][key]
        
    
    def lookup(self, key):
        hash_value = self.hash(key)
        if hash_value in self.collection and key in self.collection[hash_value]:
            return self.collection[hash_value][key]
        else:
            None


my_table = HashTable()
print(my_table.hash('golf'))
my_table.add('golf', 'sport')
print(my_table.collection)
my_table.add('dear', 'friend')
my_table.add('read', 'book')
print(my_table.collection)
my_table.remove('read')
print(my_table.collection)
print(my_table.lookup('golf'))
