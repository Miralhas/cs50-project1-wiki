def quick(array):

    if not array:
          return array

    else:
        pivot = array[0]
        menores = [i for i in array[1:] if i <= pivot]
        maiores = [i for i in array[1:] if i > pivot]

        return quick(menores) + [pviot] + quick[maiores]





`quick([5,3,7,5,8,6,1,2])`