class SomeClass:
    def Substring(self, s):
        max_len = 0
        zero = []
        null = []
        new_list = list(s)
        reverse_list = new_list.reverse()
        for i in new_list:
            if i in zero:
                if len(zero) > max_len:
                    max_len = len(zero)
                zero.clear()
                zero.append(i)
                print(zero)
                continue
            else:
                zero.append(i)
                print(zero)
        if len(zero) > max_len:
            print(len(zero))
        else:
            print(max_len)
            
        for j in reverse_list:
            if j in null:
                if len(null) > max_len:
                    max_len = len(null)
                null.clear()
                null.append(i)
                print(null)
                continue
            else:
                null.append(i)
                print(null)
        if len(null) > max_len:
            print(len(null))
        else:
            print(max_len)
        
obj = SomeClass()
result = obj.Substring('pwwkew')
print(result)