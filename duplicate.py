def Find_duplicates(items):
  duplicates - []

for item in items:
  if items.count(item) > 1:
    duplicates.append(item)

return duplicates
