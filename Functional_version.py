# Declares a base value to be used in the hashing function
base = 31

# Defines a function 'hash' which takes a string 'string_to_hash' as input
def hash(string_to_hash):
    # Initializes a variable 'hash_value' to be 0
    hash_value = 0
    # Initializes a list 'hash_list' to contain a single element, 0
    hash_list = [0]
    # Initializes a variable 'base_power' to be 1
    base_power = 1
    # Iterates through the enumerated characters in the string 'string_to_hash'
    for i, character in enumerate(string_to_hash):
        # Adds the ASCII value of the character 'character' multiplied by 'base_power' to 'hash_value'
        hash_value += ord(character) * base_power
        # Appends the value of 'hash_value' to the list 'hash_list'
        hash_list.append(hash_value)
        # Multiplies 'base_power' by 'base'
        base_power *= base
    # Returns the list 'hash_list'
    return hash_list

# Defines a function 'unhash' which takes a list of hashes 'hashes' and an optional integer 'start_power'
def unhash(hashes, start_power = 0):
    # Initializes an empty string 'unhashed_string'
    unhashed_string = ""
    # Initializes 'base_power' to be 'base' to the power of 'start_power'
    base_power = base ** start_power
    # Iterates through the indices of the list 'hashes' starting at 1
    for i in range(1, len(hashes)):
        # Concatenates the character corresponding to the result of dividing the difference between the current element in 'hashes' and the previous element by 'base_power' to 'unhashed_string'
        unhashed_string += chr((hashes[i] - hashes[i-1]) // base_power)
        # Multiplies 'base_power' by 'base'
        base_power *= base
    # Returns the string 'unhashed_string'
    return unhashed_string

# Defines a function 'find_substring' which takes two lists of hashes 'long_string_hash' and 'target_string_hash'
def find_substring(long_string_hash, target_string_hash):
    # Calculate the hash value of the target string by subtracting the first character's hash value
    # from the last character's hash value
    target_string_hash_value = target_string_hash[-1] - target_string_hash[0]

    # Iterate through the possible substrings of the long string in reverse order
    for i in range(len(long_string_hash) - len(target_string_hash), 0, -1):
        # Calculate the hash value of the current substring by subtracting the first character's hash value
        # from the last character's hash value
        last = long_string_hash[i + len(target_string_hash) - 1]
        # If the hash value of the current substring is equal to the hash value of the target string, return the start index
        if ((last - long_string_hash[i]) / (base ** (i)) == target_string_hash_value):
            return i
    # If no match is found, return -1
    return -1

long_string = "hellowordfurebidowijspok[worldbjknld"
target_string = "world"

# Calculate the hash values of the long string and the target string
long_string_hash = hash(long_string)
target_string_hash = hash(target_string)

print(f"We target '{target_string}' with hash {target_string_hash[1:]}")

# Find the start index of the target string in the long string
start_index = find_substring(long_string_hash, target_string_hash)

# If the target string is not found, print a message
if (start_index == -1):
    print(f"String '{long_string}' doesn't contain '{target_string}'")
# If the target string is found, print the start and end indices of the substring
else:
    print(f"String '{long_string}' contains '{target_string}' in substring [{start_index}:{start_index + len(target_string)}]")
