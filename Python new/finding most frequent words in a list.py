from collections import Counter
text='''
dfkjskjefisej tjeistj isejt isejt iseotjeis tiset iesjt iejtes
est isjti esties hesiuhea iurhaur aurhuawh ruahwruawhra u
njra awurhwauirh uawirhuwar huawrh uawrhuaw
ajiawj eiwhaeiaowhe awhewai hiawe
'''

words=text.split()
counter=Counter(words)
print(counter.most_common(3))       #returns tuple