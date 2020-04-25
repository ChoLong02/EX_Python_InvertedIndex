import csv
import nltk


class CreateIndex:
    count = 0        # Test를 위해 문서 몇건만 사용(제한적으로)
    docList = []     # CSV파일 자연어처리가 후 저장될 리스트
    dictList = {}    # 역색인(사전 >> 단어:빈도수)
    postingList = {} # 역색인(포스팅 >> 단어:문서)

    def __init__(self):
        pass

    def import_csv(self, csvFile):

        # 1.rcv1 엑셀데이터 호출
        with open(csvFile, 'r') as f:
            reader = csv.reader(f)

            # 2.rcv1 데이터 한건씩 반복돌면서 자연어처리
            for id, txt in reader:
                if self.count < 10:
                    # 3.소문자 변경
                    content = txt.lower()

                    # 3.토크나이징 및 중복 단어제거
                    wordList = list(set(nltk.word_tokenize(content)))
                    for word in wordList:
                        pair = [word, id]
                        #print(pair)
                        self.docList.append(pair)
                    self.count+=1

        # 5.배열 사이즈 확인
        print('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒')
        print('▒▒ AFTER NLP Preprocessing List Size: {}'.format(len(self.docList)))

        # 6.배열 정렬
        self.docList.sort()

    def index_create(self):
        inverted = {}  # 중간 저장소

        for word, idx in self.docList:
            locations = inverted.setdefault(word, [])
            locations.append(idx)

            # print('{}, {}, {}'.format(word, len(locations), locations))
            # 7. 단어:[문서들] - 포스팅목록 생성
            self.postingList[word] = set(locations)
            # 8. 단어:빈도수 - 사전목록 생성
            self.dictList[word] = len(locations)
        # print(postingList)
        # print(dictList)
        # print(len(postingList))

        # 9.전체 단어 수
        print('▒▒ INVERTED INDEX Size: {}'.format(len(self.dictList)))
        print('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒')

        # 10.생성된 사전,포스팅목록의 단어, 빈도수, 문서번호 출력
        for word, freq in self.dictList.items():
            print('{}, {}, {}'.format(word, freq, self.postingList.get(word)))
        print('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒')
