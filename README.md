wordcount
=========

A simple python wordcount which can be run with unix pipes. 
Sample text file included is available from Project Gutenberg, for the use of everyone with no cost or restrictions. 

possible usage
% cat frankenstein.txt | ./wc_map.py | sort | ./wc_reduce.py | sort -n -K2
or
% ./wc_map.py frankenstein.txt | ./wc_red.py | sort -n -K2


todo: 
*implement Counter (available from python 2.7)


