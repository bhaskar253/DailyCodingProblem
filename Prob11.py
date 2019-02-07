# Problem Stmt.:
# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings,
# return all strings in the set that have s as a prefix. For example, given the query string de and the set
# of strings [dog, deer, deal], return [deer, deal].
# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

def autocomplete(setOfString, string):
    class Node:
        def __init__(self):
            self.childrens = {}
            self.isLast = False
    class Trie:
        def __init__(self):
            self.root = Node()
        def formTrie(self,keys):
            for key in keys:
                self.insert(key)
        def insert(self,key):
            node = self.root
            for ch in list(key):
                if ch not in node.childrens:
                    node.childrens[ch] = Node()
                node = node.childrens[ch]
            node.isLast = True
    
    def suggestionsRec(node, word, words):
        if node.isLast:
            words.append(word)
        for ch, nd in node.childrens.items():
            suggestionsRec(nd, word+ch, words)

    trie = Trie()
    trie.formTrie(setOfString)
    words = []
    node,found,word = trie.root,True,''
    for ch in list(string):
        if ch not in node.childrens:
            found = False
            break
        word += ch
        node = node.childrens[ch]
    if not found or (node.isLast and not node.childrens):
        return words
    suggestionsRec(node, word, words)
    return words

if __name__ == "__main__": 
    print(autocomplete(["hello", "dog", "hell", "cat", "a", "hel", "help", "helps", "helping"],"hel"))
