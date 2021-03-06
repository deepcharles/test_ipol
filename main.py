#!/usr/bin/python3
import matplotlib
matplotlib.use("Agg")
import argparse

import numpy as np
import matplotlib.pyplot as plt


def main(n_samples, sigma):
    for rep in range(5):
        signal = np.random.normal(scale=sigma, size=n_samples)
        fig, ax = plt.subplots(figsize=(20, 10))

        ax.plot(signal)
        fig.savefig("signal_{}.png".format(rep))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Display random signal')
    parser.add_argument("-input", "--i",
                        help='input')
    parser.add_argument("-n_samples", "--n",
                        help='Number of samples')
    parser.add_argument("-sigma", "--s",
                        help='noise std')

    args = parser.parse_args()
    main(int(args.n), float(args.s))
