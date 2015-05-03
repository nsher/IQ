import re

# string = "who is on the picture?${pic1.txt};a)Victoria b)Niagara Falls с)Abraham Lincoln d)Limba;c"
string = "who is on the picture?${pic1.txt}"
mt = re.match(r".*?(\$\{(pic\d+\.txt)\}).*?", string)
if mt is not None:
    print(mt.group(1))
    print(mt.group(2))
else:
    print('NO')

# mt = re.match(r".*?\$\{(pic\d+\.txt)\}.*?", string)
# print(mt.group(1))       # The entire match 'Isaac Newton'

# m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
# print(m.group(0))       # The entire match 'Isaac Newton'
# print(m.group(1))      # The first parenthesized subgroup.' Isaac'
# print(m.group(2))     # The second parenthesized subgroup. 'Newton'
# print(m.group(1, 2))    # Multiple arguments give us a tuple. ('Isaac', 'Newton')