# Hash-Compare

PROBLEM:
You have 2 hashes. You are looking for the difference between the 2. What was added or removed or if the hash is the same.

Hash only have string keys
Hash only have string, boolean, number, array or hash as value
Compare should have an option for deep or shallow compare
Compare should list the difference for keys and values

SUMMARY
I try to make the code more user-friendly by adding detailed comment to explain each line of the code.

*The code has two functions compare_hashes_deep and compare_hashes_shallow that can compare two hashes and return the differences between them. 
*The compare_hashes_deep function performs a deep comparison, which checks for differences in the nested hashes and lists, while the compare_hashes_shallow function only checks for differences in the top level keys and values.
*It checks if the keys are present in both the hashes, if not it will consider the key removed or added.
*It also checks if the values are of same type and then if the values are different it will consider the value changed or type changed.
*It also lists the differences for keys and values. And it also handles the nested lists and hashes using the compare_lists function.
*It also handles the edge cases like empty lists and empty hashes.
*In addition, the code also only compares the keys and values with the type of strings, boolean, numbers, arrays or hashes, And the keys of the hashes must be strings.

*It also returns the results in a more structured format, where the differences are returned as a list of dictionaries, each containing information about the change, such as the key/index that changed, the old value, and the new value.


CONCLUSION:
The hash-compare code can be used to compare two versions of a configuration file to identify which elements have been added, removed or changed. It could also be used to compare two lists of products in an e-commerce website to track what items have been added or removed from the inventory.

Additionally, it can be used in version control systems to find the differences between different versions of the same file. It can also be used in any application that needs to compare lists to see if any changes have been made to them.
