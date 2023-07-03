import pandas as pd
import numpy
import json
import joblib
from sklearn.ensemble import RandomForestClassifier
import os

#判断写入路径是否存在
def is_exist(path):
    return os.path.isdir(path)

#确保写入路径存在
def ensure_exist(path):
    if not is_exist(path):
        os.mkdir(path)

# 相关性矩阵
'''
corr = features_labels.corr()
sns.set_context({'figure.figsize':[100, 100]})
fig = sns.heatmap(corr,
                xticklabels=corr.columns.values,
                yticklabels=corr.columns.values)
heatmap = fig.get_figure()
#heatmap.savefig('C:/Users/sytt0/Desktop/软件杯/work/heatmap.png', dpi=300)
corr
'''
# 各个特征的概率密度函数
'''
feature_names = features.columns.values.tolist()
for name in feature_names:
    fig = plt.figure(figsize=(15, 4), )
    ax = sns.kdeplot(df.loc[(df['label'] == 0), name], color='b', shade=True, label='0')
    ax = sns.kdeplot(df.loc[(df['label'] == 1), name], color='r', shade=True, label='1')
    ax = sns.kdeplot(df.loc[(df['label'] == 2), name], color='g', shade=True, label='2')
    ax = sns.kdeplot(df.loc[(df['label'] == 3), name], color='y', shade=True, label='3')
    ax = sns.kdeplot(df.loc[(df['label'] == 4), name], color='m', shade=True, label='4')
    ax = sns.kdeplot(df.loc[(df['label'] == 5), name], color='c', shade=True, label='5')
    ax.set(xlabel=name, ylabel='频率')
    #plt.title('{} Probabilitydensity function'.format(name))
    #plt.savefig('C:/Users/sytt0/Desktop/软件杯/work/{}的概率密度函数图.png'.format(name))
'''
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RES_DIR = os.path.join(BASE_DIR, 'upload','res')


def read_plit():
    # 获取当前根目录
    ensure_exist(RES_DIR)
    #读取数据
    df = pd.read_csv(os.path.abspath(os.path.join(BASE_DIR + '\\upload\\tests\\test.csv')), index_col=None)
    # 数据标准化
    features = df.iloc[:, 1:-1]
    numeric_features = features.dtypes[features.dtypes != 'object'].index
    features[numeric_features] = features[numeric_features].apply(
        lambda x: (x - x.mean()) / (x.std())
    )
    # 在标准化数据之后，所有均值消失，因此我们可以将缺失值设置为0
    features[numeric_features] = features[numeric_features].fillna(0)
    features_labels = pd.concat([features, df[['label']]], axis=1)
    train_features = pd.concat([df[['sample_id']], features], axis=1)
    train_label = df[['sample_id', 'label']]
    df = pd.concat([train_features, train_label[['label']]], axis=1)
    x = df.drop(['label'], axis=1)

    return x


def data_deal():    # 处理数据集
    ensure_exist(RES_DIR)
    #读取数据
    df = pd.read_csv(os.path.abspath(os.path.join(BASE_DIR + '\\upload\\trains\\train.csv')), index_col=None)
    # 数据标准化
    features = df.iloc[:, 1:-1]
    numeric_features = features.dtypes[features.dtypes != 'object'].index
    features[numeric_features] = features[numeric_features].apply(
        lambda x: (x - x.mean()) / (x.std())
    )
    # 在标准化数据之后，所有均值消失，因此我们可以将缺失值设置为0
    features[numeric_features] = features[numeric_features].fillna(0)
    features_labels = pd.concat([features, df[['label']]], axis=1)
    train_features = pd.concat([df[['sample_id']], features], axis=1)
    train_label = df[['sample_id', 'label']]
    df = pd.concat([train_features, train_label[['label']]], axis=1)

    # 划分数据集
    target_name = 'label'
    x = df.drop(['label'], axis=1)
    y = df[['label']]

    # 实例化随机森林

    rf = RandomForestClassifier(
        criterion='gini',
        n_estimators=50,
        max_depth=None,  # 定义树的深度，可以用来防止过拟合
        min_samples_split=2,  # 定义至少多少个样本的情况下才继续分叉
        min_samples_leaf=0.01  # 定义叶子节点最少需要包含多少个样本（百分比表达），防止过拟合
    )
    # 模型训练
    #rf.fit(x_train, y_train.values.reshape(-1))
    rf.fit(x, y.values.reshape(-1))
    # 先对t_test（DataFrame）进行reshape

    model_path = os.path.join(RES_DIR, 'rf_user.pkl')
    joblib.dump(rf,model_path)





# 指标计算 参数：array
def metrics_calculate(pred, y_test):
    # 获取当前根目录
    ensure_exist(RES_DIR)
    txt_path = os.path.join(RES_DIR, 'result_RandomForest.txt')

    TP = [0, 0, 0, 0, 0, 0]
    FP = [0, 0, 0, 0, 0, 0]
    FN = [0, 0, 0, 0, 0, 0]
    for i in range(len(y_test)):
        if pred[i] == 0 and y_test[i] == 0:
            TP[0] += 1
        if pred[i] != 0 and y_test[i] == 0:
            FN[0] += 1
        if pred[i] == 0 and y_test[i] != 0:
            FP[0] += 1

        if pred[i] == 1 and y_test[i] == 1:
            TP[1] += 1
        if pred[i] != 1 and y_test[i] == 1:
            FN[1] += 1
        if pred[i] == 1 and y_test[i] != 1:
            FP[1] += 1

        if pred[i] == 2 and y_test[i] == 2:
            TP[2] += 1
        if pred[i] != 2 and y_test[i] == 2:
            FN[2] += 1
        if pred[i] == 2 and y_test[i] != 2:
            FP[2] += 1

        if pred[i] == 3 and y_test[i] == 3:
            TP[3] += 1
        if pred[i] != 3 and y_test[i] == 3:
            FN[3] += 1
        if pred[i] == 3 and y_test[i] != 3:
            FP[3] += 1

        if pred[i] == 4 and y_test[i] == 4:
            TP[4] += 1
        if pred[i] != 4 and y_test[i] == 4:
            FN[4] += 1
        if pred[i] == 4 and y_test[i] != 4:
            FP[4] += 1

        if pred[i] == 5 and y_test[i] == 5:
            TP[5] += 1
        if pred[i] != 5 and y_test[i] == 5:
            FN[5] += 1
        if pred[i] == 5 and y_test[i] != 5:
            FP[5] += 1

    Precision = [0, 0, 0, 0, 0, 0]
    Recall = [0, 0, 0, 0, 0, 0]
    F1 = [0, 0, 0, 0, 0, 0]

    if (TP[0] + FP[0]) == 0:
        Precision[0] = 0.0
    else:
        Precision[0] = TP[0] / (TP[0] + FP[0])
    if (TP[1] + FP[1]) == 0:
        Precision[1] = 0.0
    else:
        Precision[1] = TP[1] / (TP[1] + FP[1])
    if (TP[2] + FP[2]) == 0:
        Precision[2] = 0.0
    else:
        Precision[2] = TP[2] / (TP[2] + FP[2])
    if (TP[3] + FP[3]) == 0:
        Precision[3] = 0.0
    else:
        Precision[3] = TP[3] / (TP[3] + FP[3])
    if (TP[4] + FP[4]) == 0:
        Precision[4] = 0.0
    else:
        Precision[4] = TP[4] / (TP[4] + FP[4])
    if (TP[5] + FP[5]) == 0:
        Precision[5] = 0.0
    else:
        Precision[5] = TP[5] / (TP[5] + FP[5])

    # for i in range(6):
    #     print('Precision: {}\n'.format(Precision[i]))

    if (TP[0] + FN[0]) == 0:
        Recall[0] = 0.0
    else:
        Recall[0] = TP[0] / (TP[0] + FN[0])
    if (TP[1] + FN[1]) == 0:
        Recall[1] = 0.0
    else:
        Recall[1] = TP[1] / (TP[1] + FN[1])
    if (TP[2] + FN[2]) == 0:
        Recall[2] = 0.0
    else:
        Recall[2] = TP[2] / (TP[2] + FN[2])
    if (TP[3] + FN[3]) == 0:
        Recall[3] = 0.0
    else:
        Recall[3] = TP[3] / (TP[3] + FN[3])
    if (TP[4] + FN[4]) == 0:
        Recall[4] = 0.0
    else:
        Recall[4] = TP[4] / (TP[4] + FN[4])
    if (TP[5] + FN[5]) == 0:
        Recall[5] = 0.0
    else:
        Recall[5] = TP[5] / (TP[5] + FN[5])

    # for i in range(6):
    #     print('Recall: {}\n'.format(Recall[i]))

    if (Precision[0] + Recall[0]) == 0:
        F1[0] = 0.0
    else:
        F1[0] = (2 * Precision[0] * Recall[0]) / (Precision[0] + Recall[0])
    if (Precision[1] + Recall[1]) == 0:
        F1[1] = 0.0
    else:
        F1[1] = (2 * Precision[1] * Recall[1]) / (Precision[1] + Recall[1])
    if (Precision[2] + Recall[2]) == 0:
        F1[2] = 0.0
    else:
        F1[2] = (2 * Precision[2] * Recall[2]) / (Precision[2] + Recall[2])
    if (Precision[3] + Recall[3]) == 0:
        F1[3] = 0.0
    else:
        F1[3] = (2 * Precision[3] * Recall[3]) / (Precision[3] + Recall[3])
    if (Precision[4] + Recall[4]) == 0:
        F1[4] = 0.0
    else:
        F1[4] = (2 * Precision[4] * Recall[4]) / (Precision[4] + Recall[4])
    if (Precision[5] + Recall[5]) == 0:
        F1[5] = 0.0
    else:
        F1[5] = (2 * Precision[5] * Recall[5]) / (Precision[5] + Recall[5])

    # for i in range(6):
    #     print('F1: {}\n'.format(F1[i]))

    Macro_Precision = sum([Precision[0], Precision[1], Precision[2],
                           Precision[3], Precision[4], Precision[5]]) / 6
    Macro_Recall = sum([Recall[0], Recall[1], Recall[2],
                        Recall[3], Recall[4], Recall[5]]) / 6
    Macro_F1 = sum([F1[0], F1[1], F1[2], F1[3], F1[4], F1[5]]) / 6

    l_sum = sum([TP[0], TP[1], TP[2], TP[3], TP[4], TP[5]])
    m_sum = l_sum + sum([FP[0], FP[1], FP[2], FP[3], FP[4], FP[5]])
    n_sum = l_sum + sum([FN[0], FN[1], FN[2], FN[3], FN[4], FN[5]])

    if m_sum == 0:
        Micro_Precision = 0.0
    else:
        Micro_Precision = l_sum / m_sum
    # print('Micro_Precision: {}\n'.format(Micro_Precision))
    if n_sum == 0:
        Micro_Recall = 0.0
    else:
        Micro_Recall = l_sum / n_sum
    # print('Micro_Recall: {}\n'.format(Micro_Recall))
    if (Micro_Precision + Micro_Recall) == 0:
        Micro_F1 = 0.0
    else:
        Micro_F1 = (2 * Micro_Precision * Micro_Recall) / (Micro_Precision + Micro_Recall)
    # print('Micro_F1: {}\n'.format(Micro_F1))

    if txt_path == None:
        return '%.4f' % Micro_F1
    else:
        f = open(txt_path, 'a', encoding='utf-8')
        for i in range(6):
            f.write('类别{}: '.format(i))
            f.write('\n')
            f.write('Precision: {:.2f}%'.format(Precision[i] * 100))
            f.write('\n')
            f.write('Recall: {:.2f}%'.format(Recall[i] * 100))
            f.write('\n')
            f.write('F1: {:.2f}'.format(F1[i]))
            f.write('\n')
        f.write('Macro_Precision: {:.2f}%'.format(Macro_Precision * 100))
        f.write('\n')
        f.write('Macro_Recall: {:.2f}%'.format(Macro_Recall * 100))
        f.write('\n')
        f.write('Macro_F1: {:.2f}'.format(Macro_F1))
        f.write('\n')
        f.write('Micro_Precision: {:.2f}%'.format(Micro_Precision * 100))
        f.write('\n')
        f.write('Micro_Recall: {:.2f}%'.format(Micro_Recall * 100))
        f.write('\n')
        f.write('Micro_F1: {:.2f}'.format(Micro_F1))
        f.write('\n')
        f.close()



def res_pro(x_test,y_test_use): #获取预测结果
    # 获取当前根目录
    ensure_exist(RES_DIR)
    #csv_path1 = os.path.join(RES_DIR, 'result_pred.csv')
    json_path=os.path.join(RES_DIR, 'result_pred.json')
    file = numpy.stack((x_test.to_numpy()[:, 0], y_test_use), axis=1)
    #pd.DataFrame(file).to_csv(csv_path1)
    dic=dict(zip(x_test.to_numpy()[:, 0],y_test_use))
    json_str = json.dumps(file.tolist(), indent=4)
    with open(json_path, 'w') as json_file:
        json_file.write(json_str)

#保存模型
def use_model(x_test):
    ensure_exist(RES_DIR)
    model_path = os.path.join(RES_DIR, 'rf.pkl')
    rf_new = joblib.load(model_path)
    y_test_use = rf_new.predict(x_test)
    return y_test_use

#读取json文件生成csv文件



'''
output:
Precision: 0.7547169811320755

Precision: 0.7230769230769231

Precision: 0.7387387387387387

Precision: 1.0

Precision: 0.8297872340425532

Precision: 1.0

Recall: 0.9856262833675564

Recall: 0.47474747474747475

Recall: 0.5394736842105263

Recall: 0.3132530120481928

Recall: 0.7358490566037735

Recall: 0.8450704225352113

F1: 0.854853072128228

F1: 0.573170731707317

F1: 0.623574144486692

F1: 0.47706422018348627

F1: 0.78

F1: 0.916030534351145

Micro_Precision: 0.7767195767195767

Micro_Recall: 0.7767195767195767

Micro_F1: 0.7767195767195768
'''
'''
# 随机森林可视化
Estimators = rf.estimators_
class_names = ['0', '1', '2', '3', '4', '5']
feature_names = df.columns[1:-1]
for index, model in enumerate(Estimators):
    dot_data = StringIO()
    sklearn.tree.export_graphviz(model, out_file=dot_data,
                    feature_names=feature_names,
                    class_names=class_names,
                    filled=True, rounded=True,
                    special_characters=True)
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    graph.write_png('work/Rf{}.png'.format(index))
    plt.figure(figsize=(20, 20))
    plt.imshow(plt.imread('work/Rf{}.png'.format(index)))
    plt.axis('off')
'''
