def test_dict():
    """
    test the classifier based on Sentiment Dict
    """
    print("DictClassifier")
    print("---" * 45)

    from spa.classifiers import DictClassifier

    ds = DictClassifier()

    # 对一个单句进行情感分析
    #a_sentence = "剁椒鸡蛋好咸,土豆丝很好吃"    # result值: 修改前(1)/修改后(1)
    #a_sentence = "要是米饭再多点儿就好了"    # result值: 修改前(1)/修改后(0)
    #a_sentence = "要是米饭再多点儿就更好了"    # result值: 修改前(0)/修改后(0)
    # a_sentence = "不太好吃，相当难吃，要是米饭再多点儿就好了"    # result值: 修改前(1)/修改后(0)
    #result = ds.analyse_sentence(a_sentence)
    #print(result)

    # 对一个文件内语料进行情感分析
    count = 6001
    flag = 0
    corpus_filepath = "fileInput/jdnew1.txt"
    for i in range(0,3000):
        count += 1
        if count%300 == 0:
            print(count)
            flag += 1
            runout_filepath_ = "f_runout/relsultAppleMac%s.txt" % flag
            pos_results = ds.analysis_file(corpus_filepath, runout_filepath_, start=count, end=count+300)
    #
    # corpus_filepath = "D:/My Data/NLP/SA/waimai/negative_corpus_v1.txt"
    # runout_filepath_ = "f_runout/f_dict-negative_test.txt"
    # neg_results = ds.analysis_file(corpus_filepath, runout_filepath_, start=3000, end=4000-1)
    #
    # origin_labels = [1] * 1000 + [0] * 1000
    # classify_labels = pos_results + neg_results
    #
    # print(len(classify_labels))
    #
    # filepath = "f_runout/Dict-waimai-%s.xls" % (
    #     datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
    # results = get_accuracy(origin_labels, classify_labels, [1000, 1000, 0])
    #
    # Write2File.write_contents(filepath, results)


if __name__ == "__main__":
    test_dict()