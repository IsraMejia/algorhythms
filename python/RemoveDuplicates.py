class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        # 'slow' inicia en 0 porque el primer elemento siempre es único
        slow = 0
        
        # 'fast' recorre todo el arreglo empezando desde el segundo elemento
        for fast in range(1, len(nums)):
            # Si encontramos un valor diferente al que tiene 'slow'
            if nums[fast] != nums[slow]:
                # Movemos slow un espacio y actualizamos su valor
                slow += 1
                nums[slow] = nums[fast]
        
        # Retornamos k, que es la cantidad de elementos únicos. 
        # Como slow es un índice (empieza en 0), sumamos 1.
        return slow + 1