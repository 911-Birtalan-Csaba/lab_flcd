class HashTable:
    __start_size = 5

    def __init__(self):
        self.__elements = [[] for _ in range(self.__start_size)]
        self.__size = 0
        self.__array_of_elements_size = self.__start_size

    def __compute_hash(self, key: str) -> int:
        """
        Computes the hash value of the given key
        :param key: The key
        :return: The hash value
        """
        char_sum = 0
        for char in key:
            char_sum += ord(char) - ord('0')
        return char_sum % self.__array_of_elements_size

    def __rehash_table(self):
        """
        Rehash the table
        """
        self.__array_of_elements_size *= 2
        new_elements = [[] for _ in range(self.__array_of_elements_size)]
        for list_item in self.__elements:
            for key in list_item:
                hash_value = self.__compute_hash(key)
                new_elements[hash_value].append(key)

    def __check_key_existence(self, key: str, hash_value: int) -> bool:
        """
        Checks if a key is already in the hash table
        :param key: The key to be searched
        :param hash_value: hash value of the key
        :return: True if the key exists, False otherwise
        """
        for keys in self.__elements[hash_value]:
            if key == keys:
                return True
        return False

    def insert(self, key: str):
        """
        Insert a key into the hash table
        :param key: The key to be added
        :exception If the key is already in the hash table
        """
        if self.__size + 1 / self.__array_of_elements_size > 0.6:
            self.__rehash_table()
        hash_value = self.__compute_hash(key)
        # check if the key is not already added
        if not self.__check_key_existence(key, hash_value):
            self.__elements[hash_value].append(key)
            self.__size += 1
        else:
            raise Exception("Key already in the hash table")

    def remove(self, key: str):
        """
        Removes a key from the hash table
        :param key: The key to be removed
        :exception If the key does not exist
        """
        hash_value = self.__compute_hash(key)
        for elem_key in self.__elements[hash_value]:
            if elem_key == key:
                self.__elements[hash_value].remove(key)
                return
        raise Exception("Key does not exist")

    def get(self, key: str):
        """
        Checks whether a key exists or not
        :param key: The key to be checked
        :return: True if it exists, False otherwise
        """
        hash_value = self.__compute_hash(key)
        return key in self.__elements[hash_value]


