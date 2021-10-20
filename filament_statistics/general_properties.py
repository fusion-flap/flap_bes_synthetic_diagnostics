def skewness_calculation(dataobj):
    skewness = []
    ch = []
    for channel in range(dataobj.data.shape[1]):
        data = dataobj.data.T[channel, :]
        sk = skew(data)
        skewness.append(sk)
        ch.append(channel)
    return pd.DataFrame(data={'channel': ch, 'skewness': skewness})


def kurtosis_calculation(dataobj):
    kurt = []
    ch = []
    for channel in range(dataobj.data.shape[1]):
        data = dataobj.data.T[channel, :]
        ku = kurtosis(data)
        kurt.append(ku)
        ch.append(channel)
    return pd.DataFrame(data={'channel': ch, 'kurtosis': kurt})
