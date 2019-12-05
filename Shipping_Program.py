def ground_shipping(weight):
  flat_charge = 20
  if weight > 10:
    price_per_pound = 4.75
  elif weight > 6:
    price_per_pound = 4
  elif weight > 2:
    price_per_pound = 3
  elif weight > 0:
    price_per_pound = 1.5
    
  total_price = flat_charge + price_per_pound * weight
  return total_price

premium_ground_shipping = 125

def drone_shipping(weight):
  if weight > 10:
    price_per_pound = 14.25
  elif weight > 6:
    price_per_pound = 12
  elif weight > 2:
    price_per_pound = 9
  elif weight > 0:
    price_per_pound = 4.50
  
  total_price = weight * price_per_pound
  return total_price

def best_price(weight):
  ground_shipping_price = ground_shipping(weight)
  drone_shipping_price = drone_shipping(weight)
  
  if ground_shipping_price < premium_ground_shipping and ground_shipping_price < drone_shipping_price:
    print("Ground shipping is the cheapest option. It costs $" + str(ground_shipping_price))
  elif premium_ground_shipping < ground_shipping_price and premium_ground_shipping < drone_shipping_price:
    print("Premium ground shipping is the cheapest option. It costs $" + str(premium_ground_shipping))
  else:
    print("Drone shipping is cheapest. It costs $" + str(drone_shipping_price))
