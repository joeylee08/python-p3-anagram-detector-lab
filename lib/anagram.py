class Anagram:
    def __init__(self, word : str):
        self.word = word

    def match(self, list):
        split_sorted = [*self.word]
        split_sorted.sort()
        print(split_sorted)
        result = []
        for word in list:
            temp_split_sort = [*word]
            temp_split_sort.sort()
            if temp_split_sort == split_sorted:
                result.append(word)
        return result

listen = Anagram("listen")

listen.match(['enlists', 'google', 'inlets', 'banana'])

# python lib/anagram.py