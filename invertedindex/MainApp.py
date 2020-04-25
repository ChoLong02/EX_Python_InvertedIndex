import index.CreateIndex as index
import search.BoolSearch as search

f_keyword = 'unit'  # Search Keyword1
s_keyword = 'year'  # Search Keyword2
s_option = 'NOT AND'  # Search Option


csvFile = 'dataset/lyrl2004_tokens_train.csv'
if __name__ == '__main__':
    try:
        cIndex = index.CreateIndex() # Create Object
        cIndex.import_csv(csvFile) # IMPORT [CSV File]
        cIndex.index_create()  # Create InvertedIndex

        boolS = search.BoolSearch(cIndex.dictList, cIndex.postingList)

        print('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒')
        print('▒▒ SEARCH [{}] {} [{}]'.format(f_keyword, s_option, s_keyword))
        print('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒')
        if s_option == 'AND':
            complete_list = boolS.search_and(f_keyword, s_keyword)
        elif s_option == 'OR':
            complete_list = boolS.search_or(f_keyword, s_keyword)
        elif s_option == 'NOT AND':
            complete_list = boolS.search_notand(f_keyword, s_keyword)
        print('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒')
        print('▒▒ Search Result: [{},{}] ---> {}'.format(f_keyword, s_keyword, complete_list))
        print('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒')

    except Exception as e:
        print('>> Exception :(')
        print('>>', e)
    finally:
        pass
