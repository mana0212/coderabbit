def process_data(users):
  result=[]
  for i in users:
    if i["age"]>18:
      if i["country"]=="India":
        result.append(i)
    return result
