class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        
class Solution:
    def reverse(self, x: int) -> int:
        resultList = []
        x = int(x)
        # Проверяем, находится ли число в допустимом диапазоне
        if -2**31 <= x <= 2**31 - 1:
            x = str(x)
            x = list(x)
            if x[0] == "-":  # Если число отрицательное
                # Добавляем минус в результат
                resultList += x[0]
                # Удаляем минус из списка
                x.remove(x[0])
                # Реверсируем список символов без минуса
                x = self.reverse(x)
                # Добавляем реверсированные символы в результат
                for i in x:
                    resultList += i
                return int(''.join(resultList))  # Возвращаем целое число из результата
            else:
                # Число положительное
                # Реверсируем список символов
                x = self.reverse(x)
                # Добавляем реверсированные символы в результат
                for i in x:
                    resultList += i
                return int(''.join(resultList))  # Возвращаем целое число из результата
        else:
            # Число выходит за допустимый диапазон
            return 0
