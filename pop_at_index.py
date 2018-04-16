def pop_at_index(seq, index):
    # Fill in your code here
    return seq[:index]+seq[index+1:] if index!=-1 else seq[:index]
