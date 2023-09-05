def get_population():
  keys = ['col', 'bol']
  values = [300,400]
  return keys, values

def population(data, country):
  result = list(filter(lambda item: item['country']==country, data))
  return result
