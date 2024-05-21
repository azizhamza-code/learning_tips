class StrDefaultDict(dict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]
        
    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default
        
    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()
    

if __name__ == "__main__":
    str_dict = StrDefaultDict()
    str_dict[1] = 'one'
    print(str_dict[1])
    print(str_dict['1'])
    print(str_dict.get(1))
    print(str_dict.get('1'))
    print(str_dict.get(2)) 