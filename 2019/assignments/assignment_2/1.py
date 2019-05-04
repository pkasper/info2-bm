class scheisse:
    @property
    def attribute(self):
        print("prop")
        return self._attribute

    @attribute.setter
    def attribute(self, new_value):
        print("setter")
        self._attribute = new_value

hi = scheisse()
print("hello")
hi.attribute = "opfa"


print(hi.attribute)