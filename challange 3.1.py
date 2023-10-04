"""
write a function called linear _ search_product that takes the list of products and a target product
name as input . the function should perform a linear search to find the terget product in the list and 
return a list of indices of all occurrences of the product if found, or an empty list if the product is not 
found.
"""


def linearSearchproduct(productList,targetProduct):
  indices = []

  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)

  return indices


# Example usage:
products = ["shoes","boot","loafer","shoes","snadal","shoes"]
target = "shoes"
result = linearSearchproduct(products, target)
print(result)


