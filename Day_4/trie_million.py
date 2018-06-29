def add(trie, string):
    if len(string) < 1:
        if '*' not in trie.keys():
            trie['*'] = {}
        return
 
    if string[0] not in trie.keys():
        trie[string[0]] = {}
        
    add(trie[string[0]],string[1:])

def exists(trie, string):
    if len(string) < 1:
        if '*' in trie.keys():
            return True
        else:
            return False

    if string[0] not in trie.keys():
        return False
        
    return exists(trie[string[0]],string[1:])


def test():
    trie = {}

    add(trie,'bananas')
    add(trie,'apples')
    add(trie,'apple_seed')
    add(trie,'oranges')

    print(trie)
    print(exists(trie,'oranges'))
    print(exists(trie,'orange'))
    print(exists(trie,'fart'))

test()