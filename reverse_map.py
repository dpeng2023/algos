import pprint

time_to_dest = {'05:00PM': 'Freeport',
                '05:55PM': 'Rock Sound',
                '07:00PM': 'West End',
                '09:35AM': 'Freeport',
                '09:55AM': 'West End',
                '10:45AM': 'Treasure Cay',
                '11:45AM': 'Rock Sound',
                '12:00PM': 'Treasure Cay'}

# dict_comp of a list_comp
dest_to_time = { dest: [ k
                         for k,v in time_to_dest.items()
                         if v == dest ]
                 for dest in set(time_to_dest.values())
                }

pprint.pprint(dest_to_time)

