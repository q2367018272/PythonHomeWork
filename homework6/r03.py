class dictclass(dict):
    def __init__(self):
        dict.__init__(self)

    def del_dict(self,key):
        del self[key]

    def get_dict(self,key):
        if key in self.keys():
            return self[key]
        else:
            return 'not found'

    def update_dict(self,dict2):
        self.update(dict2)
        return self.values()




dict2=dictclass()
dict2['1']=1
dict2['2']=2
dict2['3']=3

print(dict2)
dict2.del_dict('2')
print(dict2)
print(dict2.get_dict('1'))
print(dict2.get_dict('2'))

dict3={'4':4}
print(dict2.update_dict(dict3))

