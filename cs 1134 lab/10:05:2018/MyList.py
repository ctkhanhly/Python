import ctypes  # provides low-level arrays


def make_array(n):
    return (n * ctypes.py_object)()


class MyList:
    def __init__(self):
        self.data = make_array(1)
        self.n = 0
        self.capacity = 1

    def __len__(self):
        return self.n

    def append(self, val):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data[self.n] = val
        self.n += 1

    def resize(self, new_capacity):
        new_data = make_array(new_capacity)
        for i in range(self.n):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def __getitem__(self, ind):
        if not (-self.n <= ind <= (self.n - 1)):
            raise IndexError(str(ind) + " is out of range")
        if(-self.n <= ind < 0):
            ind = self.n + ind
        return self.data[ind]

    def __setitem__(self, ind, value):
        if not (-self.n <= ind <= (self.n - 1)):
            raise IndexError(str(ind) + " is out of range")
        '''
        if(-self.n <= ind < 0):
            ind = self.n + ind
        '''
        self.data[ind] = value

    def __iter__(self):
        for i in range(self.n):
            yield self.data[i]

    def extend(self, other):
        for elem in other:
            self.append(elem)

    def __repr__(self):

        str_lst = [0] * (self.n + 2)
        str_lst[0] = "["
        str_lst[len(str_lst) - 1] = "]"
        str_lst = MyList()
        str_lst.append("[")
        for i in range(self.n):
            if(i == self.n - 1):
                # str_lst[i + 1] = f'{self.data[i]}'
                str_lst.append(f'{self.data[i]}')
            else:
                # str_lst[i + 1] = f'{self.data[i]}, '
                str_lst.append(f'{self.data[i]}, ')
        #str_lst.extend([str(self.data[i]) for i in tange(self.n) if i == self.n-1 else str(self.data[i])+ ", "])

        str_lst.append("]")
        # str(int)
        #str = "[" + "".join(self) + "]"
        return "".join(str_lst)

    def __add__(self, other):
        new_list = MyList()
        # cannot set of length <index
        for i in range(self.n + other.n):
            if(i < self.n):
                new_list.append(self.data[i])
            else:
                new_list.append(other.data[i - self.n])
        return new_list

    def __iadd__(self, other):
        for i in range(other.n):
            self.append(other.data[i])
        return self

    def __mul__(self, num):
        new_list = MyList()
        for m in range(num):
            new_list.extend(self)
        return new_list

    def __rmul__(self, num):
        new_list = MyList()
        for m in range(num):
            new_list.extend(self)
        return new_list


if __name__ == '__main__':
    list1 = MyList()
    for i in range(4):
        list1.append(i)
    list2 = MyList()
    for i in range(4, 7):
        list2.append(i)
    print(repr(list1))
    print(list1 + list2)
    print(list1)
    list1 += list2
    print(list1)
    print(list1[-1])
    print(2 * list1)
    print(list1 * 2)
