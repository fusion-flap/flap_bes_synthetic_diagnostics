def event_identification(data_object, base=0, condition=0, length=20, channel=10):
    """
    data_object: 1D signal numpy vector
    base: float, (recommended: signal.mean)
    condition: float, (recommended: signal.std * 2.5)
    length: int, (number of indices, >0; recommended setup: expected filament temporarly length in seconds/dt in seconds)
    """

    signal = data_object.data.T[channel, :]
    sig = copy.deepcopy(signal)

    if base == 0:
        base = signal.mean()

    if condition == 0:
        condition = signal.std() * 2.5

    events_position = []
    events_begin = []
    events_end = []

    peak_value = sig.max()

    while peak_value - base > condition:
        peak_pos = np.argmax(sig)
        events_position.append(peak_pos)

        beginning = max(0, peak_pos - length)
        ending = min(peak_pos + length + 1, len(sig))

        events_begin.append(beginning)
        events_end.append(ending)

        sig[beginning:ending] = base

        peak_value = sig.max()

    return pd.DataFrame(data={'position': events_position, 'begin': events_begin, 'end': events_end})