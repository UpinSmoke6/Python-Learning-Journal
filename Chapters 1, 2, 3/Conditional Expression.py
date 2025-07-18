user_val = int(input()) # Input a integer

cond_str = 'negative' if (user_val < 0) else 'non-negative' if (user_val >= 0) else 'nothing' # conditional if under 0
# the number is labeled as negative

print(user_val, 'is', cond_str)
