from typing      import Self
from dataclasses import dataclass, field

@dataclass
class Node:
    character: str = None
    frequency: int = 1

    children: list[Self] = field(default_factory = list)
    code:     str = ""

    def isLeaf(self) -> bool:
        return self.character != None

class Huffman:
    @staticmethod
    def count_letter(string: str, letter) -> int:
        return len([character for character in string if character == letter])

    @staticmethod
    def get_letters_frequency(string: str) -> dict:
        frequencies = {}

        for letter in string:
            frequencies[letter] = Huffman.count_letter(string, letter)

        return dict(sorted(sorted(frequencies.items()), key = lambda x: x[1]))

    @staticmethod
    def generate_tree(string: str) -> Node:
        frequencies = Huffman.get_letters_frequency(string)

        nodes = [Node(frequency[0], frequency[1]) for frequency in frequencies.items()]
        while len(nodes) > 1:
            left  = nodes.pop(0)
            left.code = "0"

            right = nodes.pop(0)
            right.code = "1"

            total = left.frequency + right.frequency

            internal = Node(None, total, [left, right])

            nodes.append(internal)
            nodes = sorted(nodes, key = lambda x: x.frequency)

        return nodes[0]

    @staticmethod
    def calculate_codes(node: Node, value: str = "", codes: dict = {}) -> dict:
        value += node.code
        
        if node.isLeaf():
            codes[node.character] = value

            return codes

        if node.children[0]:
            codes = Huffman.calculate_codes(node.children[0], value, codes)

        if node.children[1]:
            codes = Huffman.calculate_codes(node.children[1], value, codes)

        return codes

    @staticmethod
    def generate_dictionary(string: str) -> dict:
        tree  = Huffman.generate_tree(string)

        return Huffman.calculate_codes(tree)

    @staticmethod
    def encode(string: str) -> str:
        dictionary = Huffman.generate_dictionary(string)

        return "".join([dictionary[letter] for letter in string])

    @staticmethod
    def decode(encoded: str, dictionary: dict) -> str:
        cache   = ""
        decoded = ""

        for character in encoded:
            cache += character

            letters = [key for key, value in dictionary.items() if value == cache]

            if len(letters) == 1:
                decoded += letters[0]
                cache    = ""

        return decoded


dictionary = Huffman.get_letters_frequency("Hello World")
print(dictionary)