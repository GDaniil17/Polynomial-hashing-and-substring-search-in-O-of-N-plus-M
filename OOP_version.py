class Hash:
    # Initializes the class with a base value
    def __init__(self, base):
        self.base = base

    # Defines a method for calculating the hash values of a string
    def hash(self, string_to_hash):
        # Initializes a variable to store the current hash value
        hash_value = 0
        # Initializes a list to store the hash values of each character in the string
        hash_list = [0]
        # Initializes a variable to store the current power of the base
        base_power = 1
        # Iterates through the enumerated characters in the string
        for i, character in enumerate(string_to_hash):
            # Calculates the current hash value by adding the ASCII value of the character multiplied by the current base power
            hash_value += ord(character) * base_power
            # Appends the current hash value to the list
            hash_list.append(hash_value)
            # Increases the base power by multiplying it by the base
            base_power *= self.base
        # Returns the list of hash values
        return hash_list

    # Defines a method for unhashing a list of hash values
    def unhash(self, hashes, start_power = 0):
        # Initializes a variable to store the unhashed string
        unhashed_string = ""
        # Initializes a variable to store the current power of the base
        base_power = self.base ** start_power
        # Iterates through the indices of the list of hash values starting at index 1
        for i in range(1, len(hashes)):
            # Calculates the current character by dividing the difference between the current and previous hash values by the base power
            character = chr((hashes[i] - hashes[i-1]) // base_power)
            # Appends the current character to the unhashed string
            unhashed_string += character
            # Increases the base power by multiplying it by the base
            base_power *= self.base
        # Returns the unhashed string
        return unhashed_string

    # Defines a method for finding a substring within a string
    def find_substring(self, long_string_hash, target_string_hash):
        # Calculates the hash value of the target string by subtracting the first character's hash value from the last character's hash value
        target_string_hash_value = target_string_hash[-1] - target_string_hash[0]
        # Iterates through the possible substrings of the long string in reverse order
        for i in range(len(long_string_hash) - len(target_string_hash), 0, -1):
            # Calculates the hash value of the current substring by subtracting the first character's hash value from the last character's hash value
            last = long_string_hash[i + len(target_string_hash) - 1]
            # If the hash value of the current substring is equal to the hash value of the target string, return the start index
            if ((last - long_string_hash[i]) / (self.base ** (i)) == target_string_hash_value):
                return i
        # If no match is found, return -1
        return -1

# Creates an instance of the Hash class with base value 31
hash_helper = Hash(31)

# Declares the long string and target string
long_string = "hellowordfurebidowijspok[worldbjknld"
target_string = "world"

# Calculates the hash values of the long string and the target string
long_string_hash = hash_helper.hash(long_string)
target_string_hash = hash_helper.hash(target_string)

# Prints the hash value of the target string
print(f"We target '{target_string}' with hash {target_string_hash[1:]} in string '{long_string}'\n")

# Finds the start index of the target string in the long string
start_index = hash_helper.find_substring(long_string_hash, target_string_hash)

# If the target string is not found, print a message
if (start_index == -1):
    print(f"String '{long_string}' doesn't contain '{target_string}'")
# If the target string is found, print the start and end indices of the substring
else:
    print(f"String '{long_string}' contains '{target_string}' in substring [{start_index}:{start_index + len(target_string)}]")
