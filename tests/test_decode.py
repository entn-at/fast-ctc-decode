#!/usr/env/bin python3

import numpy as np
from unittest import TestCase, main
from fast_ctc_decode import beam_search


class Tests(TestCase):

    def setUp(self):
        self.beam_size = 5
        self.alphabet = "NACGT"
        self.beam_cut_threshold = 0.1
        self.probs = np.random.rand(100, 5).astype(np.float32)

    def test_beam_search(self):
        """ simple beam search test with the canonical alphabet"""
        seq = beam_search(self.probs, self.alphabet, self.beam_size, self.beam_cut_threshold)
        self.assertEqual(len(set(seq)), len(self.alphabet) - 1)

    def test_beam_search_alphabet(self):
        """ simple beam search test with different alphabet"""
        seq = beam_search(self.probs, "NRUST", self.beam_size, self.beam_cut_threshold)
        self.assertEqual(len(set(seq)), len(self.alphabet) - 1)


if __name__ == '__main__':
    main()
