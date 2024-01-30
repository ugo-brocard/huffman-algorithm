import sys
import unittest

sys.path.append("../huffman")

from huffman import Huffman

class TestHuffman(unittest.TestCase):
    def test_encoding(self):
        self.assertEqual(Huffman.encode("Hello World"), "11110101010110111000011001110001")

    def test_decoding(self):
        encoded    = Huffman.encode("Hello World")
        dictionary = Huffman.generate_dictionary("Hello World")

        self.assertEqual(Huffman.decode(encoded, dictionary), "Hello World")