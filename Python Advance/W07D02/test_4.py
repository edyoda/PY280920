class TestClass:
    def utility(self):
        self.list1 = [1,2,3,4]
        return self.list1

    def utility2(self):
        self.list2 = [2,4,5]
        return self.list2

    def test_1(self):
        list1 = self.utility()
        assert 5 in list1

    def test_2(self):
        list1 = self.utility()
        assert 2 in list1
