import tensorflow as tf

# 训练数据，以二元组形式生成数据
def input_fn():
    return {"age":[19, 23, 34, 30, 60, 55, 36],
            "name":["Robert", "David", "Kelly", "Rose", "Hayes", "Luis", "Lili"]}, [0, 0, 1, 1, 0, 0, 1]


# 预测与评估数据， 以Dataset形式生成
def input_fn_predict():
    dataset = tf.data.Dataset.from_tensor_slices(({"age":[23, 33, 58, 20, 59]}, 
                                                    [0, 1, 0, 0, 0]))
    dataset = dataset.batch(10)             # 必须分批，否则会抛出异常
    return dataset



def main(argv):
    # 定义特征对象
    age = tf.feature_column.numeric_column('age')

    # 初始化Estimator对象
    estimator = tf.estimator.DNNClassifier(
        feature_columns=[age],
        hidden_units=[1000]
    )

    # 训练
    estimator.train(input_fn=input_fn, steps=10000)

    # 评估
    evaluation = estimator.evaluate(input_fn=input_fn_predict)
    print('\nAccuracy: {accuracy:0.3f}\n'.format(**evaluation))
    print(evaluation)

    # 预测
    predictions = estimator.predict(input_fn=input_fn_predict)
    for idx, pred_dict in enumerate(predictions):
        class_id = pred_dict['class_ids'][0]
        probability = pred_dict['probabilities'][class_id]
        print("{}: label:{}, prob: {}".format(idx, class_id, probability))


if __name__ == '__main__':
    tf.logging.set_verbosity(tf.logging.INFO)
    tf.app.run(main)
