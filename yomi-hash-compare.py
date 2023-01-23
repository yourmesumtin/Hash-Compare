def compare_lists(lst1, lst2):
    # Initialize an empty list to store the differences
    item = []
    for num,(i,j) in enumerate(zip(lst1, lst2)):
        if isinstance(i, list) and isinstance(j, list):
            # If the values are lists, recursively compare the lists
            item.extend(compare_lists(i, j))
        else:
            if isinstance(i, type(j)):
                if i != j:
                    # If the values are different, append a string with the index and change
                    item.append(f"index.{num} changed")
            else:
                # If the types are different, append a string with the index and change
                item.append(f"index.{num} type changed")

    # checking if any element is left in lst1 or lst2
    if len(lst1) > len(lst2):
        for i in range(len(lst1) - len(lst2)):
            # If an element is present in lst1 but not in lst2, it has been removed
            item.append(f"index.{len(lst2) + i} removed")
    elif len(lst1) < len(lst2):
        for i in range(len(lst2) - len(lst1)):
            # If an element is present in lst2 but not in lst1, it has been added
            item.append(f"index.{len(lst1) + i} added")
    return item

def compare_hashes_deep(hash1, hash2):
    # Initialize an empty list to store the differences
    differences = []

    # Compare keys in both hashes
    for key in hash1:
        if key not in hash2:
            # If a key is present in hash1 but not in hash2, it has been removed
            differences.append(f"key {key} removed")
    for key in hash2:
        if key not in hash1:
            # If a key is present in hash2 but not in hash1, it has been added
            differences.append(f"key {key} added")
        else:
            if isinstance(hash1[key], dict) and isinstance(hash2[key], dict):

                # If the values are nested dictionaries, recursively compare the nested hashes
                nested_differences = compare_hashes_deep(hash1[key], hash2[key])
                for nested_difference in nested_differences:
                    differences.append(f"{key}.{nested_difference}")
            elif isinstance(hash1[key], list) and isinstance(hash2[key], list):
                # If the values are lists, compare the nested lists
                if hash1[key] != hash2[key]:
                    differences.extend(compare_lists(hash1[key], hash2[key]))
            elif isinstance(hash1[key], type(hash2[key])):
                if hash1[key] != hash2[key]:
                    # If the values are not equal, append a string with the key and change
                    differences.append(f"key {key} changed")
            else:
                # If the types are different, append a string with the key and change
                differences.append(f"key {key} type changed")
    return differences

def compare_hashes_shallow(hash1, hash2):
    # Initialize an empty list to store the differences
    differences = []

    # Compare keys in both hashes
    for key in hash1:
        if key not in hash2:
             # If a key is present in hash1 but not in hash2, it has been removed
            differences.append(f"key {key} removed")
    for key in hash2:
        if key not in hash1:
            # If a key is present in hash2 but not in hash1, it has been added
            differences.append(f"key {key} added")
        else:
            if hash1[key] != hash2[key]:
                # If the values are not equal, append a string with the key and change
                differences.append(f"key {key} changed")
    return differences



# TESTING (This is just my own simple way of testing the code)

hash1 = {
"first-key": True,
"second-key": "python3",
"third-key": [1,2,3,4],
"fourth-key": {"sub-first": 1, "sub-second": 2}
}

hash2 = {
"first-key": False,
"second-key": "python",
"third-key": [1,2,3,4,5,6,7],
"fourth-key": {"sub-first": 3, "sub-second": 4}
}

#perform a deep comparison, Enzyme can be ignored
print("Enzyme Deep Comparison:")
print(compare_hashes_deep(hash1, hash2))

#perform a shallow comparison,Yomi can also be ignored 
print("Yomi Shallow Comparison:")
print(compare_hashes_shallow(hash1, hash2))