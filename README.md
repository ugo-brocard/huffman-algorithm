# huffman-algorithm
<div align="center">
    Huffman algorithm is a python implementation of the **huffman algorithm** it's an efficient encoding algorithm for text.
    <br>
    <br>
    <img alt="GitHub License" src="https://img.shields.io/github/license/ugo-brocard/matrices-py"/>
    <img alt="GitHub Workflow Status (with event)" src="https://img.shields.io/github/actions/workflow/status/ugo-brocard/matrices-py/publish.yml"/>
    <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/matrices-py"/>
    <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/ugo-brocard/matrices-py"/>
</div>

## ✨ Key features
- [x] Count letters
- [x] Tree generation
- [x] Dictionary generation
- [x] Letter frequency calculation
- [x] String encoding
- [x] String decoding
  
- [ ] Tree visualisation

It works with python 3.12 or later

***

## 🔧 Installation

It should work on any python3 version after the 1.10 but it's always good to have the latest version since it will be the one I'm sure it works on :)

### ⚙ Using PyPi

``` bash
$ pip install huffman-algorithm
```

## 📚 Usage

### 📕 Dictionary generation
```py
from huffman import Huffman

dictionary = Huffman.generate_dictionary("Hello World")

# How to see the dictionary ?
print(dictionary)    # Output: {'W': '000', 'd': '001', 'e': '010', 'r': '011', 'l': '10', 'o': '110', ' ': '1110', 'H': '1111'}
```

### 🌳 Tree generation
```py
from huffman import Huffman

tree = Huffman.generate_tree("Hello World")

# How to see the tree ?
print(tree)    # Output: Node(character=None, frequency=11, children=[Node(character=None, frequency=4, children=[...]])
```

### 🔢 Letter frequency calculation
```py
from huffman import Huffman

frequencies = Huffman.get_letters_frequency("Hello World")

# How to see the encoded string ?
print(frequencies)    # Output: {' ': 1, 'H': 1, 'W': 1, 'd': 1, 'e': 1, 'r': 1, 'o': 2, 'l': 3}
```

### ⚙️ String encoding
```py
from huffman import Huffman

encoded = Huffman.encode("Hello World")

# How to see the encoded string ?
print(encoded)    # Output: '11110101010110111000011001110001'
```

### ⚙️ String decoding
```py
from huffman import Huffman

encoded = Huffman.encode("Hello World")
dictionary = Huffman.generate_dictionary("Hello World")

decoded = Huffman.decode(encoded, dictionary)

# How to see the decoded string ?
print(decoded)    # Output: 'Hello World'
```

## 🍕 Contributing
All contribution are welcomed so consider looking at the source code on [GitHub](https://github.com/ugo-brocard/huffman-algorithm)

## 🛡 License

This project is licensed under the [MIT License](https://github.com/ugo-brocard/huffman-algorithm/blob/main/LICENSE)