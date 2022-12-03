def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string
    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  
    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.
    Returns: a list of all permutations of sequence
    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    

    if len(sequence) <= 1:
        return [sequence]
    else:
        perms = list()
        first_char = sequence[0]
        rest_chars = sequence[1:]

        rest_perms = get_permutations(rest_chars)

        for perm in rest_perms:
            for i in range(len(rest_chars) + 1):
                new_seq = perm[0:i] + first_char + perm[i:len(perm)]
                perms.append(new_seq)
        return perms

print(get_permutations('abc'))