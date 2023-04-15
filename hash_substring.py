# python3

def read_input():
    input_type = input().strip()
    pattern = ''
    text = ''

    if input_type.upper() == 'I':
        #read from keyboard
        pattern = input().rstrip()
        text = input().rstrip()
    elif input_type.upper() == 'F':
        with open("tests/06", 'r') as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
    else:
        print("Invalid input type. Please enter 'I' or 'F'.")
    return pattern, text

def print_occurrences(output):
    """
    Prints the list of integers as a space-separated string.
    
    Args:
    - output: a list of integers to print
    
    Returns:
    - None
    """
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    """
    Finds the occurrences of the pattern in the text using the Rabin-Karp algorithm.
    
    Args:
    - pattern: a string representing the pattern to search for
    - text: a string representing the text to search in
    
    Returns:
    - a list of integers representing the starting indices of the pattern in the text
    """
    p = len(pattern)
    t = len(text)
    q = 101 # prime number used for hashing
    d = 256 # the number of possible characters

    h = d**(p-1) % q # precompute the has for the pattern
    pattern_hash = hash(pattern)
    text_hash = 0
    occurrences = []

    pattern = pattern.lower()
    text = text.lower()

    # compute the hash for the pattern and the first substring of the text
    for i in range(p):
        pattern_hash = (d*pattern_hash + ord(pattern[i])) % q
        text_hash = (d*text_hash + ord(text[i])) % q
    
    #check if the hash values match and if the substrings match character by character
    for i in range(t-p+1):
        if pattern_hash == text_hash:
            if pattern == text[i:i+p].lower():
                occurrences.append(i)
        
        #compute the hash for the next substring
        if i < t-p:
            text_hash = (d*(text_hash - ord(text[i])*h) + ord(text[i+p])) % q
            text_hash = (text_hash + q) % q

    return occurrences

# this part launches the functions
if __name__ == '__main__':
    pattern, text = read_input()
    occurrences = get_occurrences(pattern, text)
    print_occurrences(occurrences)
