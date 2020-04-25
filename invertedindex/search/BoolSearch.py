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
            f_list = self.postingList.get(f_keyword)
            s_list = self.postingList.get(s_keyword)

            complete_list = f_list & s_list
        else:
            print('No matching documents:(')
        print('▒▒ [{}] ---> {}'.format(f_keyword, f_list))
        print('▒▒ [{}] ---> {}'.format(s_keyword, s_list))
        return complete_list

    def search_or(self, f_keyword, s_keyword):
        # Check for documents containing words
        f_list = self.postingList.get(f_keyword)
        s_list = self.postingList.get(s_keyword)

        complete_list = f_list | s_list
        print('▒▒ [{}] ---> {}'.format(f_keyword, f_list))
        print('▒▒ [{}] ---> {}'.format(s_keyword, s_list))
        return complete_list

    def search_notand(self, f_keyword, s_keyword):
        and_list = self.search_and(f_keyword, s_keyword)

        all_list = set()
        for word, doc_list in self.postingList.items():
            # print('{}, {}'.format(word, doc_list))
            all_list.update(doc_list)

        print('▒▒ [ALL docId] ---> {}'.format(all_list))
        print('▒▒ [AND docId] ---> {}'.format(and_list))

        for docId in and_list:
            all_list.remove(docId)
        return all_list
