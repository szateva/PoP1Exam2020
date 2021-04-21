""" Given a non-empty string s, its atom is a string s1 such that s is equal to s1 con-
catenated with itself some number of times, i.e., s == s1 or s == s1 + ... + s1.
Implement the function:
shortest_atom(s)
which takes a non-empty string s as a parameter and returns its shortest atom, i.e., an
atom s1 of s such that no string strictly shorter than s1 is an atom of s. Importing
any libraries is NOT allowed.
Indicative test cases:
shortest_atom("ababab") = "ab"
shortest_atom("abcabc") = "abc"
shortest_atom("abcab") = "abcab"
 """