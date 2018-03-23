def copy_tree(tree):
    if tree==():
        return ()
    elif type(tree) is not tuple:
        return tree
    else:
        return (copy_tree(tree[0]),)+copy_tree(tree[1:])


print(copy_tree((1,2,(3,4,(5,6)),7,8)))
