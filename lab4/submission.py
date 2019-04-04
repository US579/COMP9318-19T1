## import modules here

################# Question 1 #################
from collections import Counter
import pandas as pd

raw_data = pd.read_csv('./asset/data.txt', sep='\t')
raw_data.head()


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

print(training_data)
sms = 'I am not spam'
a = get_freq_of_tokens(sms)
#caculate the probility of P(class) the class is category here which has two classes
#one is "ham" and another one is "spam"
class_disturbution = {}
for item in training_data:
    if item[1] not in class_disturbution:
        class_disturbution[item[1]] = 1
    else:
        class_disturbution[item[1]] += 1
#the probility of "ham" occur in the whole document
P_ham = class_disturbution['ham']/float(sum(class_disturbution.values()))
#the probility of "spam" occur in the whole document
P_spam = class_disturbution['spam']/float(sum(class_disturbution.values()))

#gather all the word occur in one class and store its the number of occurrences
for key in training_data:




def multinomial_nb(training_data, sms):# do not change the heading of the function
    pass # **replace** this line with your code