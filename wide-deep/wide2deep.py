import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, PolynomialFeatures, LabelEncoder
from keras.layers import Input, Embedding, Dense, Flatten, Dropout, SpatialDropout1D, Activation, concatenate
from keras.optimizers import Adam, SGD
from keras.layers.advanced_activations import ReLU, PReLU, LeakyReLU, ELU
from keras.layers.normalization import BatchNormalization
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.models import Model
from tensorflow.keras.utils import plot_model

COLUMNS = [
    "age", "workclass", "fnlwgt", "education", "education_num", "marital_status",
    "occupation", "relationship", "race", "gender", "capital_gain", "capital_loss",
    "hours_per_week", "native_country", "income_bracket"
]

LABEL_COLUMN = "label"

CATEGORICAL_COLUMNS = [
    "workclass", "education", "marital_status", "occupation", "relationship",
    "race", "gender", "native_country"
]

CONTINUOUS_COLUMNS = [
    "age", "education_num", "capital_gain", "capital_loss", "hours_per_week"
]


def preprocessing():
    train_data = pd.read_csv('adult.data', names=COLUMNS)
    train_data.dropna(how='any', axis=0)
    test_data = pd.read_csv('adult.test', skiprows=1, names=COLUMNS)
    test_data.dropna(how='any', axis=0)
    all_data = pd.concat([train_data, test_data])
    # 量化标签
    all_data[LABEL_COLUMN] = all_data['income_bracket'].apply(lambda x: ">50K" in x).astype(int)
    all_data.pop('income_bracket')
    y = all_data[LABEL_COLUMN].values
    all_data.pop(LABEL_COLUMN)
    for c in CATEGORICAL_COLUMNS:
        le = LabelEncoder()
        all_data[c] = le.fit_transform(all_data[c])
    train_size = len(train_data)
    x_train = all_data.iloc[:train_size]
    y_train = y[:train_size]
    x_test = all_data.iloc[train_size:]
    y_test = y[train_size:]
    x_train_categ = np.array(x_train[CATEGORICAL_COLUMNS])  # 类别数据
    x_test_categ = np.array(x_test[CATEGORICAL_COLUMNS])
    x_train_conti = np.array(x_train[CONTINUOUS_COLUMNS], dtype='float64')  # 连续数据
    x_test_conti = np.array(x_test[CONTINUOUS_COLUMNS], dtype='float64')
    scaler = StandardScaler()
    x_train_conti = scaler.fit_transform(x_train_conti)  # 通过连续数据训练集的均值和标准差归一化
    x_test_conti = scaler.transform(x_test_conti)
    return [x_train, y_train, x_test, y_test, x_train_categ, x_test_categ, x_train_conti, x_test_conti, all_data]


class Wide_and_Deep:
    def __init__(self, mode='wide and deep'):
        self.mode = mode
        x_train, y_train, x_test, y_test, x_train_categ, x_test_categ, x_train_conti, x_test_conti, all_data \
            = preprocessing()
        self.x_train = x_train
        self.y_train = y_train
        self.x_test = x_test
        self.y_test = y_test
        self.x_train_categ = x_train_categ  # 训练集中的分类数据
        self.x_test_categ = x_test_categ  # 测试集中的类别数据
        self.x_train_conti = x_train_conti  # 训练集中的连续数据
        self.x_test_conti = x_test_conti  # 测试集中的连续数据
        self.all_data = all_data
        self.poly = PolynomialFeatures(degree=2, interaction_only=True)
        # 将类别数据转换cross product化
        self.x_train_categ_poly = self.poly.fit_transform(x_train_categ)
        self.x_test_categ_poly = self.poly.transform(x_test_categ)
        self.categ_inputs = None
        self.conti_input = None
        self.deep_component_outlayer = None
        self.logistic_input = None
        self.model = None

    def deep_component(self):
        categ_inputs = []
        categ_embeds = []
        # 为类别数据的每个要素创建输入层和嵌入层
        for i in range(len(CATEGORICAL_COLUMNS)):
            input_i = Input(shape=(1,), dtype='int32')
            dim = len(np.unique(self.all_data[CATEGORICAL_COLUMNS[i]]))
            embed_dim = int(np.ceil(dim ** 0.25))  # 使输入类别数的第四根成为嵌入维数
            embed_i = Embedding(dim, embed_dim, input_length=1)(input_i)
            flatten_i = Flatten()(embed_i)
            categ_inputs.append(input_i)
            categ_embeds.append(flatten_i)
        # 在全连接层中批量输入连续数据
        conti_input = Input(shape=(len(CONTINUOUS_COLUMNS),))
        conti_dense = Dense(256, use_bias=False)(conti_input)
        # 将每个嵌入的输出与完全连接的层连接
        concat_embeds = concatenate([conti_dense] + categ_embeds)
        concat_embeds = Activation('relu')(concat_embeds)
        bn_concat = BatchNormalization()(concat_embeds)
        # 此外，堆叠3层完全粘合的层。
        fc1 = Dense(512, use_bias=False)(bn_concat)
        ac1 = ReLU()(fc1)
        bn1 = BatchNormalization()(ac1)
        fc2 = Dense(256, use_bias=False)(bn1)
        ac2 = ReLU()(fc2)
        bn2 = BatchNormalization()(ac2)
        fc3 = Dense(128)(bn2)
        ac3 = ReLU()(fc3)

        # 将输入层和最后一层转换为成员变量（用于模型创建）
        self.categ_inputs = categ_inputs
        self.conti_input = conti_input
        self.deep_component_outlayer = ac3

    def wide_component(self):
        # 仅将分类数据放入线性模型
        dim = self.x_train_categ_poly.shape[1]
        self.logistic_input = Input(shape=(dim,))

    def create_model(self):
        self.deep_component()
        self.wide_component()
        if self.mode == 'wide and deep':
            out_layer = concatenate([self.deep_component_outlayer, self.logistic_input])
            inputs = [self.conti_input] + self.categ_inputs + [self.logistic_input]
        elif self.mode == 'deep':
            out_layer = self.deep_component_outlayer
            inputs = [self.conti_input] + self.categ_inputs
        else:
            print('wrong mode')
            return

        output = Dense(1, activation='sigmoid')(out_layer)
        self.model = Model(inputs=inputs, outputs=output)

    def train_model(self, epochs=15, optimizer='adam', batch_size=128):
        if not self.model:
            print('You have to create model first')
            return

        if self.mode == 'wide and deep':
            input_data = [self.x_train_conti] + \
                         [self.x_train_categ[:, i] for i in range(self.x_train_categ.shape[1])] + \
                         [self.x_train_categ_poly]
        elif self.mode == 'deep':
            input_data = [self.x_train_conti] + \
                         [self.x_train_categ[:, i] for i in range(self.x_train_categ.shape[1])]
        else:
            print('wrong mode')
            return

        self.model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])
        self.model.fit(input_data, self.y_train, epochs=epochs, batch_size=batch_size)

    def evaluate_model(self):
        if not self.model:
            print('You have to create model first')
            return

        if self.mode == 'wide and deep':
            input_data = [self.x_test_conti] + \
                         [self.x_test_categ[:, i] for i in range(self.x_test_categ.shape[1])] + \
                         [self.x_test_categ_poly]
        elif self.mode == 'deep':
            input_data = [self.x_test_conti] + \
                         [self.x_test_categ[:, i] for i in range(self.x_test_categ.shape[1])]
        else:
            print('wrong mode')
            return

        loss, acc = self.model.evaluate(input_data, self.y_test)
        print(f'test_loss: {loss} - test_acc: {acc}')

    def save_model(self, filename='wide_and_deep.h5'):
        self.model.save(filename)


if __name__ == '__main__':
    wide_deep_net = Wide_and_Deep()
    wide_deep_net.create_model()
    wide_deep_net.train_model()
    wide_deep_net.evaluate_model()
    wide_deep_net.save_model()
    plot_model(wide_deep_net.model, to_file='model.png', show_shapes=True, show_layer_names=False)