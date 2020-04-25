class BoolSearch:
    fKeyword = ''         # Search Keyword1
    sKeyword = ''         # Search Keyword2
    dict_list = {}        # Dictonary list of Invertedindex
    posting_list = {}     # Posting list of Invertedindex
    standard_keyword = '' # Words with fewer documents
    complete_list = []    # Search Result(docId)

    def __init__(self, dict_list, posting_list):
        # Get the list of created inverted index
        self.dictList = dict_list
        self.postingList = posting_list

    def search_and(self, f_keyword, s_keyword):
        # Check for documents containing words
        f_bool = f_keyword in self.postingList
        s_bool = s_keyword in self.postingList

        if f_bool and s_bool:
            if f_bool > s_bool:
                big_keyword = f_keyword
                small_keyword = s_keyword
            else:
                big_keyword = s_keyword
                small_keyword = f_keyword
        else:
            print('No matching documents:(')

        small_list = self.postingList.get(small_keyword)
        big_list = self.postingList.get(big_keyword)
        print('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒')
        print('▒▒ SEARCH [{}] AND [{}]'.format(f_keyword, s_keyword))
        print('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒')
        print('▒▒ [{}] ---> {}'.format(f_keyword, small_list))
        print('▒▒ [{}] ---> {}'.format(s_keyword, big_list))
        print('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒')

        for i in range(len(small_list)):
            if small_list[i] in big_list:
                self.complete_list.append(small_list[i])
        print('▒▒ Search Result: [{},{}] ---> {}'.format(f_keyword, s_keyword, self.complete_list))
        print('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒')

        return self.complete_list

    def search_or(self, f_keyword, s_keyword):
        # Check for documents containing words
        print('zz')
        f_list = self.postingList.get(f_keyword)
        s_list = self.postingList.get(s_keyword)

        temp_list = f_list + s_list
        complete_list = list(set(temp_list))
        complete_list.sort()
        print(
            '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒')
        print('▒▒ SEARCH [{}] OR [{}]'.format(f_keyword, s_keyword))
        print(
            '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒')
        print('▒▒ [{}] ---> {}'.format(f_keyword, f_list))
        print('▒▒ [{}] ---> {}'.format(s_keyword, s_list))
        print('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒')
        print('▒▒ Search Result: [{},{}] ---> {}'.format(f_keyword, s_keyword, complete_list))
        print('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒')



    def search_nad(self, f_keyword, s_keyword):
        and_list = self.search_and(f_keyword, s_keyword)

        print(self.postingList)

        for word, doc_list in self.postingList.items():
            # print('{}, {}'.format(word, doc_list))
            all_list.update()
