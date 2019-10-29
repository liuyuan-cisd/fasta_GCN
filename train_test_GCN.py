'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-10-18 16:03:45
@LastEditTime: 2019-10-21 10:12:05
@LastEditors: Please set LastEditors
'''
from sklearn.model_selection import StratifiedKFold
#import argparse
import numpy as np
from prepare_data_trian_test import prepare_data_trian_test
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

if __name__ == "__main__":
    
    flags = tf.app.flags
    FLAGS = flags.FLAGS
    
    #args=getopt()
    k=9

    train_data='train.data'
    train_label='train.label'
    test_data='test.data'
    test_label='test.label'

    data_name=train_data.split('.')[0]
    prepare_data_trian_test(train_data,train_label,test_data,test_label,data_name,k)
    build_graph(data_name)
    train(data_name)



        
        


    
    
