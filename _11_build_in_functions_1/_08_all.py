wifi_enabled: bool = True
has_electricity: bool = True
has_subscription: bool = True

if wifi_enabled and has_subscription and has_electricity:
    print(True)
else:
    print(False)

# Also:

requirements: list[bool] = [wifi_enabled, has_electricity, has_subscription]
if all(requirements):
    print(True)
else:
    print(False)

votes_or_not: list[int] = [1, 1, 1, 0, 1, 0, 0, 1, 1, 1]
print(all(votes_or_not))
