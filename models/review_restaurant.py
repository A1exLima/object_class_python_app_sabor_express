class Review_restaurant:
  def __init__(self, client, rating):
    self._client = client
    self._rating = rating
  
  def __str__(self):
    return f'Cliente: {self._client:10} | Nota: {self._rating}'
