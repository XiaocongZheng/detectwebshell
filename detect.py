import os
from sklearn.feature_extraction.text import CountVectorizer
import sys
import numpy as np
from sklearn import cross_validation
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


def load_file(file_path):
    t=""
    with open(file_path) as f:
        for line in f:
            line=line.strip('\n')
            t+=line
    return t


def load_files(path):
    files_list=[]
    for r, d, files in os.walk(path):
        for file in files:
            if file.endswith('.php'):
                file_path=path+file
                #print "Load %s" % file_path
                t=load_file(file_path)
                files_list.append(t)
    return  files_list



if __name__ == '__main__':

    #bigram_vectorizer = CountVectorizer(ngram_range=(2, 2),token_pattern = r'\b\w+\b', min_df = 1)
    webshell_bigram_vectorizer = CountVectorizer(ngram_range=(2, 2), decode_error="ignore",
                                        token_pattern = r'\b\w+\b',min_df=1)
    webshell_files_list=load_files("D:/xampp/htdocs/simple/xiaoma/")
    x1=webshell_bigram_vectorizer.fit_transform(webshell_files_list).toarray()
    y1=[1]*len(x1)
    vocabulary=webshell_bigram_vectorizer.vocabulary_
    wp_bigram_vectorizer = CountVectorizer(ngram_range=(2, 2), decode_error="ignore",
                                        token_pattern = r'\b\w+\b',min_df=1,vocabulary=vocabulary)
    wp_files_list=load_files("D:/xampp/htdocs/simple/wordpress/")
    x2=wp_bigram_vectorizer.fit_transform(wp_files_list).toarray()
    y2=[0]*len(x2)
    x=np.concatenate((x1,x2))
    y=np.concatenate((y1, y2))
    clf = GaussianNB()
    clf.fit(x,y)
    #scores=cross_validation.cross_val_score(clf, x, y, n_jobs=-1,cv=3)
    test_bigram_vectorizer = CountVectorizer(ngram_range=(2, 2), decode_error="ignore",
                                        token_pattern = r'\b\w+\b',min_df=1,vocabulary=vocabulary)
    paths="D:/xampp/htdocs/upload/"
    count=0
    for fn in os.listdir(paths):
       count = count+1
    count1=str(count)
    paths1=paths+count1+"/"
    print paths1
    test_files_list=load_files(paths1)
    x3=test_bigram_vectorizer.fit_transform(test_files_list).toarray()
    a=clf.predict(x3)
    for number in a:
        print number
    #print scores
    #print np.mean(scores)