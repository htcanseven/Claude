import re
src = open('ch1_full.md').read()
# single-pass renumber so nothing is remapped twice
m = {'1.3':'1.1','1.2':'1.2','1.4':'1.3','1.7':'1.4','1.6':'1.5','1.9':'1.6','1.8':'1.7','1.11':'1.8'}
def sub(mo): return 'Figure ' + m[mo.group(1)]
new = re.sub(r'Figure (1\.\d+)', sub, src)
open('ch1_full.md','w').write(new)
print("figure order after renumber:")
for x in re.findall(r'\[Figure (1\.\d+)[^\]]*\]', new): print('  ', x)
