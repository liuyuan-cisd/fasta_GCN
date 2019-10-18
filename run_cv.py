'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-10-18 16:03:45
@LastEditTime: 2019-10-18 21:41:43
@LastEditors: Please set LastEditors
'''
from sklearn.model_selection import StratifiedKFold
#import argparse
import numpy as np
from prepare_data import prepare_data
from build_graph import build_graph
from train import train
import tensorflow as tf
'''
def getopt():

    parse=argparse.ArgumentParser()
    parse.add_argument('-cv','--crossvalidation',type=int,default=5)
    parse.add_argument('-k','--kmer',type=int,default=5)
    parse.add_argument('-fa','--fasta',type=str)
    args=parse.parse_args()
    return args
'''
def split2cv(cv,fasta_path,dataset_name):
    fasta=open(fasta_path,'r')
    seqs_list=[]
    for line in fasta:
        if line.startswith('>'):
            continue
        seqs_list.append(line)
    n_sample=len(seqs_list)
    y=np.array([1]*int(n_sample//2)+[0]*int(n_sample//2))
    X=np.array(seqs_list)

    indices=np.arange(n_sample)
    np.random.shuffle(indices)
    seqs=X[indices]
    labels=y[indices]

    skflod=StratifiedKFold(n_splits=cv)
    i=1
    for train,test in skflod.split(seqs,labels):
        
        train_object=open('./data/corpus/'+dataset_name+'_cv'+str(i)+'.train.txt','w')
        trian_seqs=seqs[train]
        train_object.writelines(trian_seqs)
        train_object.close()
        
        test_object=open('./data/corpus/'+dataset_name+'_cv'+str(i)+'.test.txt','w')
        test_seqs=seqs[test]
        test_object.writelines(test_seqs)
        test_object.close()

        train_labels=open('./data/corpus/'+dataset_name+'_cv'+str(i)+'.train.label','w')
        train_y=labels[train]
        train_labels.writelines([str(e)+'\n' for e in train_y])
        train_labels.close()
        
        test_labels=open('./data/corpus/'+dataset_name+'_cv'+str(i)+'.test.label','w')
        test_y=labels[test]
        test_labels.writelines([str(e)+'\n' for e in test_y])
        test_labels.close()
        i+=1

if __name__ == "__main__":
    
    flags = tf.app.flags
    FLAGS = flags.FLAGS
    
    #args=getopt()
    cv=3
    k=6
    fasta_name='first.txt'

    data_name=fasta_name.split('.')[0]
    split2cv(cv,fasta_name,data_name)
    test_acc=[]
    test_pred=[]
    test_labels=[]
    for i in range (cv):
        temp_data_name=data_name+'_cv'+str(i+1)
        print(temp_data_name)
        prepare_data(temp_data_name,k)
        build_graph(temp_data_name)
        acc,pred,labels=train(temp_data_name)
        test_acc.extend([acc])
        test_labels.extend(labels)
        test_pred.extend(pred)
    print('cv_acc:',np.mean(np.array(test_acc)))
    np.savetxt(data_name+'_cv_acc_result.csv',np.array(test_acc),delimiter=',',fmt='%5f')
    np.savetxt(data_name+'cv_pred.csv',np.array([test_labels,test_pred]).T,delimiter=',',fmt='%d')




        
        


    
    
