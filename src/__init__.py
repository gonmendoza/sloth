class sldataframe:
    def __init__(self, data, index=None, columns=None): 
        self._data = data
        if index is None:
            for colname in data.keys():
                last = len(data[colname])
                for colname in data.keys():
                    if len(data[colname]) != last:
                        raise ValueError("FOOL! Your arrays must have the same size")
                    else:
                        self._index = np.array(range(len(data[colname])))
        else:
            self._index = index
        if columns is None:
            self._columns = self._data.keys()
        else:
            self._columns = columns
    
    @property
    def data(self):
        return self._data
    @property
    def index(self):
        return self._index
    @property
    def columns(self):
        return self._columns
    def __repr__(self):
        return f"Index(Index='{self.index}', columns='{self.columns}')"