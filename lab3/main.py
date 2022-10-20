from hash_table import HashTable

if __name__ == '__main__':
    symbol_table = HashTable()
    symbol_table.insert("test")
    assert (symbol_table.get("test") is True)
    assert (symbol_table.get("testNotExist") is False)
    symbol_table.remove("test")
    assert (symbol_table.get("test") is False)
