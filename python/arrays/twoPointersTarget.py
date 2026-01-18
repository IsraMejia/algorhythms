from typing import List, Optional

def two_sum(nums: List[int], target: int) -> Optional[List[int]]:
    """
    Busca dos índices en la lista 'nums' cuya suma sea igual al 'target'.
    """ 
    nums_map = {} 
    for p, num in enumerate(nums): 
        
        if num in nums_map: 
            return [nums_map[num], p]
        else: 
            number_to_find = target - num 
            nums_map[number_to_find] = p

    return None

# Ejemplo de uso:
# print(two_sum([2, 7, 11, 15], 9))  # Salida: [0, 1]