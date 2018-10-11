import ctypes  # provides low-level arrays


def make_array(n):
    return (n * ctypes.py_object)()
    #create a simple array of references?


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
        if(-self.n <= ind < 0):
            ind = self.n + ind
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
                str_lst.append(f'{self.data[i]}')
            else:
                str_lst.append(f'{self.data[i]}, ')

        str_lst.append("]")
        return "".join(str_lst)

    def __add__(self, other):
        new_list = MyList()
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

    def insert(self, index, val):
        if not(-self.n <= index < self.n - 1):
            raise IndexError(str(index) + " is out of range")
        if(self.n == self.capacity):
            self.resize(2 * self.capacity)
        else:
            self.n += 1
            for i in range(self.n - 1, index - 1, -1):
                self.data[i] = self.data[i - 1]
            self.data[index] = val
        return self

    def pop(self, index=None):
        if(self.n == 0):
            raise IndexError("List cannot be empty")

        if not(index == None):
            if not(-self.n <= index < self.n - 1):
                raise IndexError(str(index) + " is out of range")

            for i in range(index, self.n - 1):
                self.data[i] = self.data[i + 1]
        else:
            index = self.n - 1

        val = self.data[index]
        self.data[self.n - 1] = None

        self.n -= 1

        if(self.n < self.capacity // 4):
            self.resize(self.capacity // 2)
        return val


'''
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
    print(list1)
    list1.insert(1, 30)
    print(list1)
    print(list1.pop())
    list1.pop(2)
    print(list1)
    list1.pop(3)
    print(list1, "capacity", list1.capacity)
    list1.pop()
    print(list1)
'''
