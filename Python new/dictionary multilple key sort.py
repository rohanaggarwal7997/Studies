from operator import itemgetter

users=[
    {'fname':'rohan','lname':'garwal'},
{'fname':'rohan','lname':'aggarl'},
{'fname':'roan','lname':'awal'},
{'fname':'ran','lname':'aggwal'},
{'fname':'rhan','lname':'aggawal'},
{'fname':'rohana','lname':'aggrwal'},
{'fname':'rohan','lname':'agwal'},
]


for x in sorted(users,key=itemgetter('fname')):
    print(x)

    #doesnt sort lname accordingly
print('-------------------------------')

for x in sorted(users,key=itemgetter('fname','lname')):     #sort according to first then according to last
    print(x)