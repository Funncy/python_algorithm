
#1번째
def reverser(words, start=0, end=None):
    if len(words) < 2 :
        return words
    # end = end or len(words)-1
    if end is None:
        end = len(words)-1

    #스위칭    
    while start < end:
        words[start], words[end] = words[end], words[start]
        start += 1
        end -= 1

def reversing_word_sentence_logic(words):
    #전체회전
    reverser(words)

    p = 0
    start = 0
    while p < len(words):
        if words[p] == u"\u0020":
            #띄어쓰기 찾기
            reverser(words, start, p-1)
            start = p+1
        p += 1
    
    #마지막 단어 reverse
    reverser(words, start, p-1)
    return "".join(words)


str1 = "파이썬 알고리즘 정말 재미있다"
str2 = reversing_word_sentence_logic(list(str1))
print(str2)


#반복문 하나로 처리
def reverse_words_brute(words):
    word, sentence = [], []
    for character in words:
        if character != " ":
            word.append(character)
        else:
            if word:
                sentence.append("".join(word))
            word = []
    
    if word != "":
        sentence.append("".join(word))
    sentence.reverse()
    return " ".join(sentence)

str1 = "파이썬 알고리즘 정말 재미있다"
str2 = reverse_words_brute(str1)
print(str2)

#list, slice 사용
def reversing_word_slice(sentence):
    new_word = []
    words = sentence.split(" ")
    
    for word in words[::-1]:
        new_word.append(word)
    return " ".join(new_word)

str1 = "파이썬 알고리즘 정말 재미있다"
str2 = reversing_word_slice(str1)
print(str2)

#내장 시퀀스 사용
def reversing_words(sentence):
    words = sentence.split(" ")
    rev_set = " ".join(reversed(words))
    return rev_set

str1 = "파이썬 알고리즘 정말 재미있다"
str2 = reversing_words(str1)
print(str2)