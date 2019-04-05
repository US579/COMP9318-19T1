## import modules here
from collections import Counter
import pandas as pd

################# Question 1 #################
raw_data = pd.read_csv('./asset/data.txt', sep='\t')
def tokenize(sms):
    return sms.split(' ')

def get_freq_of_tokens(sms):
    tokens = {}
    for token in tokenize(sms):
        if token not in tokens:
            tokens[token] = 1
        else:
            tokens[token] += 1
    return tokens
training_data = []
for index in range(len(raw_data)):
    training_data.append((get_freq_of_tokens(raw_data.iloc[index].text), raw_data.iloc[index].category))


#caculate the probility of P(class) the class is category here which has two classes
#one is "ham" and another one is "spam"
def multinomial_nb(training_data, sms):# do not change the heading of the function
    class_disturbution = dict()
    for item in training_data:
        if item[1] not in class_disturbution:
            class_disturbution[item[1]] = 1
        else:
            class_disturbution[item[1]] += 1
    # the probility of "ham" ,"spam"occur in the whole document
    P_ham ,P_spam = class_disturbution['ham'] / sum(class_disturbution.values()),class_disturbution['spam'] / sum(class_disturbution.values())
    # gather all the words occur in one class(in this case we have two classes) and store its the number of occurrences
    word_occurances = dict()
    for key in training_data:
        if key[1] not in word_occurances:
            word_occurances[key[1]] = key[0]
        else:
            word_occurances[key[1]] = Counter(word_occurances[key[1]]) + Counter(key[0])

    V_num = len(set.union(set(word_occurances['spam'].keys()), set(word_occurances['ham'].keys())))
    # the likelihood of P(W|C)
    def P_w_c(count_w_c, count_c, V):
        return (count_w_c + 1) / (count_c + V)
    conditional_Pro_ham ,conditional_Pro_spam = dict() , dict()
    for word in sms:
        if word not in word_occurances['ham'] and word not in word_occurances['spam']:
            continue
        category_ham = word_occurances['ham']
        if word not in category_ham.keys():
            a = 0
        else:
            a = category_ham[word]
        b = sum(category_ham.values())
        pro_ham = P_w_c(a, b, V_num)
        conditional_Pro_ham[word] = pro_ham

        category_spam = word_occurances['spam']
        if word not in category_spam.keys():
            x = 0
        else:
            x = category_spam[word]
        y = sum(category_spam.values())
        pro_spam = P_w_c(x, y, V_num)
        conditional_Pro_spam[word] = pro_spam

    def get_freqs(sms):
        tokens = {}
        for token in sms:
            if token not in tokens:
                tokens[token] = 1
            else:
                tokens[token] += 1
        return tokens
    word_fre = get_freqs(sms)
    pham ,pspam = 1 , 1
    for k, v in word_fre.items():
        try:
            pham *= conditional_Pro_ham[k] ** v
            pspam *= conditional_Pro_spam[k] ** v
        except KeyError:
            pass
    ratio = (pspam * P_spam) / (pham * P_ham)
    return ratio


sms = 'I am not spam'
sms =tokenize(sms)
print(multinomial_nb(training_data, sms))

'''
the answer is : 0.23427672955974846
'''