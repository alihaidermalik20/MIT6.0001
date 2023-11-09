# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

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
    
    
    '''
    if string not broken down to the last char
        keep calling get_permutations(sequence)
    else:
        create an list to store all combinations
        get the last letter of the sequence
        get all the letters except for the last letter
        call the recursion on the sequence with last letter removed and keep doing it till you get only one letter and recursion stops and you can continue with the next lines
        
    create a loop for every letter in the sequence, first sequence that enters here is going to be just one letter
        create an index loop so that you can insert the last letter stored above into every index of the remaining sequence. the loop for the first sequence is going to have one letter sequence and one letter as last
            now insert last letter before the remaining sequence
            append this combination
            On the second loop, insert the last letter in the second position of the remaining sequence of letters before it and append this combination
            third loop, insert it in third position if the index goes till 3 and so on
    then return this list to the recursive function that called it
    
    On the second run after base run, the list is going to have 2 combinations of 2 letter words so you need to go through each one and plug the last letter into each position of this two letter sequence to make 3 letter combinations and append them and return this list
    then this 3 letters list will run and add another last letter to the previous sequence if it was called by the function itself, otherwise it will just return the list and finish
    '''
    # base case
    if len(sequence) == 1:
        return [sequence]
    
    else:  
        permutations_list = []
        last_character = sequence[-1]
        sequence_except_last = sequence[:-1]
        # keep calling itself until broken down to first letter and then continue
        current_permutations_list = get_permutations(sequence_except_last)
        
    # for every permutation in the current list, insert back the last characters into every position of that permutation to make it longer
    for permutation in current_permutations_list:
        for index in range(0,len(permutation) + 1):
            # on first loop, index is at 0 and on last loop, index is at length of the permutations without adding last letter yet
            # first insert last letter in the 0th index, then to the 1st and so on
            # so the prefix to the last character should be upto the index of the current length of permutation not including the current index as last character is added on index position
            # suffix to the last character is everything that is after the index including the index because last letter is not yet in the current permutation
            new_permutation = permutation[:index] + last_character + permutation[index:]
            permutations_list.append(new_permutation)
    
    # transform the current permutations list into set as set doesn't allow duplicates and then back to list to pass on to recursive function that called it or finish and return
    return list(set(permutations_list))

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
    
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
