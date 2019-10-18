# fasta_GCN
使用图卷积对生物序列进行分类

需要准备平衡的数据集，前一半为正例，后一半为反例，只需要fasta格式文件即可执行本程序

## 使用方法
 
  首先安装依赖：Python 3.6,Tensorflow >= 1.4.0,sklearn, numpy,nltk
 
  直接将整个项目的文件夹放到服务器上
  
  把fasta文件放在项目的根目录，即和代码相同的路径下
  
  打开run_cv.py 修改三个参数：
  
  cv= 交叉验证的折数
  
  k=Kmer中的k
  
  fasta_name=fasta文件的文件名
  
  保存后运行python run_cv.py
 
 ## 运行结果：
 
    程序运行结束会打印交叉验证的ACC，并且把每一个模型的ACC保存在了后缀result.csv的文件里。
    
    程序的预测结果保存在后缀为pred.csv文件里，第一列为正确lables,第二列为预测值
    
    (注意这时的顺序可能已经被打乱了，和输入fasta的顺序不同)
