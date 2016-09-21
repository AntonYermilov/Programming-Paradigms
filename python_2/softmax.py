def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    e = np.exp(x)
    return e / np.sum(e, axis=0)
