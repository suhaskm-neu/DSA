class HashMap:
    """
    A simple implementation of a hash map.

    Attributes:
        size (int): The size of the hash table.
        hash_table (list): The hash table to store key-value pairs.

    Methods:
        __init__(): Initializes the hash map.
        _hash(key): Hashes the given key to an index in the hash table.
        put(key, value): Inserts a key-value pair into the hash map.
        get(key): Retrieves the value associated with the given key.
        remove(key): Removes the key-value pair with the given key from the hash map.
        contains(key): Checks if the hash map contains the given key.
    """

    def __init__(self):
        """
        Initializes the hash map.

        The hash map is implemented as a list of lists, where each inner list represents a bucket.
        Each bucket contains key-value pairs that have the same hash value.
        """
        self.size = 26  # Assuming only lowercase letters are used
        self.hash_table = [[] for _ in range(self.size)]

    def _hash(self, key):
        """
        Hashes the given key to an index in the hash table.

        Args:
            key (str): The key to be hashed.

        Returns:
            int: The index in the hash table corresponding to the hashed key.
        """
        return ord(key[0].lower()) - ord('a')

    def put(self, key, value):
        """
        Inserts a key-value pair into the hash map.

        If a key-value pair with the same key already exists in the hash map, the value is updated.

        Args:
            key (str): The key of the pair to be inserted.
            value (any): The value of the pair to be inserted.
        """
        index = self._hash(key)
        for pair in self.hash_table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.hash_table[index].append([key, value])

    def get(self, key):
        """
        Retrieves the value associated with the given key.

        Args:
            key (str): The key of the pair to be retrieved.

        Returns:
            any: The value associated with the given key, or None if the key is not found.
        """
        index = self._hash(key)
        for pair in self.hash_table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def remove(self, key):
        """
        Removes the key-value pair with the given key from the hash map.

        Args:
            key (str): The key of the pair to be removed.
        """
        index = self._hash(key)
        for i, pair in enumerate(self.hash_table[index]):
            if pair[0] == key:
                del self.hash_table[index][i]
                return

    def contains(self, key):
        """
        Checks if the hash map contains the given key.

        Args:
            key (str): The key to be checked.

        Returns:
            bool: True if the hash map contains the given key, False otherwise.
        """
        index = self._hash(key)
        for pair in self.hash_table[index]:
            if pair[0] == key:
                return True
        return False