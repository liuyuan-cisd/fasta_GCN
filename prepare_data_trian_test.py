'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-10-17 11:08:57
@LastEditTime: 2019-10-22 21:31:49
@LastEditors: Please set LastEditors
'''
#!/usr/bin/python
#-*-coding:utf-8-*-
import numpy as np

def split2ngram(sequences,k):
    ngram_sequences=[]
    for line in sequences:
        if line.startswith('>'):
            continue
        line_ngam=''
        for i in range(len(line)):
            if i>(len(line)-k):
                break
            line_ngam=line_ngam+line[i:i+k]+' '
        ngram_sequences.append(line_ngam.strip())
    return ngram_sequences

def prepare_data_trian_test(train_name,train_label,test_data,test_label,dataset_name,k):
    train_txt=open(train_name,'r').readlines()
    train_seqs=[]
    for line in train_txt:
        if line.startswith('>'):
            continue 
        train_seqs.append(line.strip())

    test_txt=open(test_data,'r').readlines()
    test_seqs=[]
    for line in test_txt:
        if line.startswith('>'):
            continue 
        test_seqs.append(line.strip())

    sequences=[]
    sequences.extend(train_seqs)
    sequences.extend(test_seqs)

    n_train=len(train_seqs)

    print (n_train)
    n_test=len(test_seqs)
    print(n_test)
    train_labels_txt=open(train_label,'r').readlines()
    train_labels=[]
    for line in train_labels_txt:
        train_labels.append(line.strip())

    test_labels_txt=open(test_label,'r').readlines()
    test_labels=[]
    for line in test_labels_txt:
        test_labels.append(line.strip())

    labels=[]
    labels.extend(train_labels)
    labels.extend(test_labels)

    train_or_test_list =np.array(['train']*n_train+['test']*n_test).tolist()

    sentences=split2ngram(sequences,k)

    clear_sentence=open('./data/corpus/'+dataset_name+'.clean.txt','w')
    for line in sentences:
        clear_sentence.write(line+'\n')
    clear_sentence.close()

    meta_data_list = []

    for i in range(len(sentences)):
        meta = str(i) + '\t' + train_or_test_list[i] + '\t' + labels[i]
        meta_data_list.append(meta)

    meta_data_str = '\n'.join(meta_data_list)

    f = open('./data/' + dataset_name + '.txt', 'w')
    f.write(meta_data_str)
    f.close()

    corpus_str = '\n'.join(sentences)

    f = open('./data/corpus/' + dataset_name + '.txt', 'w')
    f.write(corpus_str)
    f.close()