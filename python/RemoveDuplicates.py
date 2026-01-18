class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums: return 0  # Caso base: si la lista está vacía.

        slow = 0 # El primer elemento (índice 0) siempre es único.
        
        for fast in range(1, len(nums)): # Empezamos a explorar desde el segundo (índice 1).
            if nums[fast] != nums[slow]: # ¿El explorador encontró algo diferente al último único?
                slow += 1                # ¡Sí! Entonces movemos el "escritor" a la siguiente casilla.
                nums[slow] = nums[fast]  # Escribimos el nuevo valor único ahí.
                
        return slow + 1 # Retornamos la cantidad (si el índice es 4, hay 5 elementos).