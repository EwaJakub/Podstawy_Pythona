def censor(sentence):
    censored_words = ['Java', 'C#', 'Ruby', 'PHP']
    sentence_list = sentence.split()
    censored_list = [sent if sent not in censored_words else "****" for sent in sentence_list]
    '''
    different solution:
    censored_list = []
    for sent in sentence_list:
         if sent in censored_words:
             censored_list.append("****")
         else:
             censored_list.append(sent)
    '''
    return " ".join(censored_list)

c = censor("Java is the best, but PHP is the bestest!")  # ;-)
print(c)  # **** is the best, but **** is the bestest!

