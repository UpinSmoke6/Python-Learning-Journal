num_users = int(input())
update_direction = int(input())

num_users = num_users + 1 if update_direction == 3 else num_users -1 # Increment plus on if update_direct equals 3
                                                                     # otherwise decrement.

print('New value is:', num_users)