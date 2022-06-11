class HashTable:
    def __init__(self, size = 7):
        self.data_map  = [None] * size

    def __hash(self, key): 
        my_hash  = 0
        for letter in key:
            my_hash  =  (my_hash + ord(letter) * 23 ) % len(self.data_map)
        return my_hash

    def print_table(self):
        for key , value in enumerate(self.data_map):
            print(key , ":", value)
        print('')

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index]  == None:
            self.data_map[index] = []
        self.data_map[index].append([key,value])

    def get_item(self, key):
        index  = self.__hash(key) 
        if self.data_map[index] is None:
            return None
        address = self.data_map[index]
        for pair in address:
            if key == pair[0]:
                return pair[1]

    def get_item_authors_solution(self, key):
        index  = self.__hash(key) 
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        temp  = []
        for address in self.data_map:
            if address is not None:
                for pair in address:
                    temp.append(pair[0])
        if temp:
            return temp
        return None

    def keys_authors_solution(self):
        all_keys  = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

if __name__ == "__main__":
    ht = HashTable()
    ht.print_table()
    ht.set_item('bolts', 1400)
    ht.set_item('washers', 50)
    ht.set_item('lumber', 70)

    ht.print_table()
    print(ht.get_item('washers') )
    print(ht.get_item('bolts') )
    print(ht.get_item('pins') )
    print(ht.get_item_authors_solution('washers') )
    print(ht.keys())
    print(ht.keys_authors_solution())
