
'''
The primary memory of a computer is composed of bits of information, and those bits are typ- ically grouped into larger units: byte

memory address. In effect, each byte of memory is associated with a unique number that serves as its address

In this sense, we say that a computer’s main mem- ory performs as random access memory (RAM). That is, it is just as easy to retrieve byte #8675309 as it is to retrieve byte #309.

We will refer to each location within an array as a cell, and will use an integer index to describe its location within the array, with cells numbered starting with 0, 1, 2, and so on.

Each cell of an array must use the same number of bytes.

 Python internally represents each Unicode character with 16 bits (i.e., 2 bytes). Therefore, a six-character string, such as   SAMPLE , would be stored in 12 consecutive bytes of memory,
