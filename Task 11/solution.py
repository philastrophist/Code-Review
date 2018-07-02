from scipy.stats import gaussian_kde
import numpy as np


def get_distribution(data):
    return gaussian_kde(data).pdf


def resample_pdf_distribution(probability_distribution, resample_parent, n):
    """
    Creates a sample of size `n` derived from `resample_parent` with the same distribution as probability_distribution
    probability_distribution: callable which returns the pdf for a given set of points
    resample_parent: np.array {shape = (nobjects, ndimensions)}
    n: int
    returns: array of indices for selecting the resampled distribution: np.array {shape = (nobjects, )}
    """
    probabilities = probability_distribution(resample_parent)
    probabilities /= probabilities.sum()
    return np.random.choice(len(resample_parent), p=probabilities, replace=False, size=n)
