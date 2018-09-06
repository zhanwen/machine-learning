from datetime import datetime
import pandas as pd
from matplotlib import pyplot
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder

# 数据预处理
# 加载并解析原始数据,转变成需要的数据集
def resolveData():
    def parse(x):
        return datetime.strptime(x, '%Y %m %d %H')
    dataset = pd.read_csv('raw.csv', parse_dates=[['year', 'month', 'day', 'hour']], index_col=0, date_parser=parse)
    dataset.drop('No', axis=1, inplace=True)
    del dataset['PRES']
    del dataset['cbwd']
    dataset.columns = ['pollution', 'dew', 'temp', 'wnd_spd', 'snow', 'rain']
    dataset.index.name = 'date'
    dataset['pollution'].fillna(0, inplace=True)
    dataset = dataset[24:]
    print(dataset.head(10))
    dataset.to_csv('repollution.csv')

# 去除不需要的数据
# 包括压强和风向
def removeData():
    dataset = pd.read_csv("pollution.csv")
    dataset = dataset.iloc[:, [0, 1, 2, 3, 6, 7, 8]]
    dataset.columns = ['date', 'pollution', 'dew', 'temp', 'wnd_spd', 'snow', 'rain']
    dataset.index.name = 'date'
    dataset = dataset.values
    print(dataset)
    # dataset.to_csv('pollution2.csv')


# 折线图展示
# 将数据以时间序列展示,这里时间选取前 1000h
# 由于将所有的数据同时展示，空间比较小，可以选择每次处理其中一组数据
def display():
    dataset = pd.read_csv('pollution.csv', header=0, index_col=0)
    values = dataset.values
    groups = [1, 2, 3, 4, 5, 6]
    i = 1
    pyplot.figure()
    for group in groups:
        pyplot.subplot(len(groups), 1, i)
        pyplot.plot(values[:1000, group])
        pyplot.title(dataset.columns[group], y=0.5, loc='right')
        i += 1
    pyplot.show()

# 转化为监督学习所需要的数据
def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
    n_vars = 1 if type(data) is list else data.shape[1]
    df = pd.DataFrame(data)
    cols, names = list(), list()
    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
        names += [('var%d(t-%d)' % (j + 1, i)) for j in range(n_vars)]
        # forecast sequence (t, t+1, ... t+n)
    for i in range(0, n_out):
        cols.append(df.shift(-i))
        if i == 0:
            names += [('var%d(t)' % (j + 1)) for j in range(n_vars)]
        else:
            names += [('var%d(t+%d)' % (j + 1, i)) for j in range(n_vars)]
            # put it all together
    agg = pd.concat(cols, axis=1)
    agg.columns = names
    # drop rows with NaN values
    if dropnan:
        agg.dropna(inplace=True)
    return agg

def reframed_data(n_in, n_out):
    dataset = pd.read_csv('pollution.csv', header=0, index_col=0)
    values = dataset.values
    encoder = LabelEncoder()
    values[:, 4] = encoder.fit_transform(values[:, 4])
    values = values.astype('float32')
    scaler = MinMaxScaler(feature_range=(0,1))
    scaled = scaler.fit_transform(values)
    reframed = series_to_supervised(scaled, n_in, n_out)
    return reframed.values, scaler, values

def minmaxData():
    dataset = pd.read_csv('pollution.csv', header=0, index_col=0)
    values = dataset.values
    encoder = LabelEncoder()
    values[:, 4] = encoder.fit_transform(values[:, 4])
    values = values.astype('float32')
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled = scaler.fit_transform(values)
    return values, scaled, scaler

def get_data():
    dataset = pd.read_csv('pollution.csv', header=0, index_col=0)
    values = dataset.values
    encoder = LabelEncoder()
    values[:, 4] = encoder.fit_transform(values[:, 4])
    values = values.astype('float32')
    return values

def get_finally_data(day):
    dataset = pd.read_csv('pollution.csv', header=0, index_col=0)
    values = dataset.values
    n_train_hours = 24 * day
    train = values[:n_train_hours, :]
    test = values[n_train_hours:, :]
    train_X, train_y = train[:, :-1], train[:, -1]
    test_X, test_y = test[:, :-1], test[:, -1]
    train_X = train_X.reshape((train_X.shape[0], 1, train_X.shape[1]))
    test_X = test_X.reshape((test_X.shape[0], 1, test_X.shape[1]))
    print(train_X.shape, train_y.shape, test_X.shape, test_y.shape)
    return train_X, train_y, test_X, test_y

if __name__ == '__main__':
    # resolveData()
    # removeData()
    # display()
    # reframed_data(5, 3)
    # get_data()
    # minmaxData()
    get_finally_data(36)