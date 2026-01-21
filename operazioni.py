def somma ( a:float, b:float ):
  if isinstance(a, (int,float) ) and isinstance(b, (int,float) ):
    return a + b
  else:
    #raise TypeError("a e b devono essere numeri")
    # print("a e b devono essere numeri")
    #return TypeError("a e b devono essere numeri")
    return None
  
def sottrazione(a: float, b: float):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a / b
    else:
        return None