import numpy as np

class dataframe:
    def __init__(self, data, index=None, columns=None, dtype=None):
        if type(data) != dict:
            raise TypeError("Naaay, only dictionaries if it please ma'lord")
        for key in data.keys():
            data[key] = np.array(data[key])
        self._data = data
        if index is None:
            for key in data.keys():
                last = len(data[key])
                for colname in data.keys():
                    if len (data[key]) != last:
                        raise ValueError("FOOL! Your arrays must have the same size")
                    else:
                        self._index = np.array(range(len(data[key])))
        else:
            self._index = index
        if columns is None:
            self._columns = self._data.keys()
        else:
            self._columns = columns
        coltypes = []
        for key in data.keys():
            coltypes.append(f"{key}: {type(data[key][0])}")
        self._dtype = coltypes
    
   @property
    def data(self):
        return self._data

    @property
    def index(self):
        return self._index

    @property
    def columns(self):
        return self._columns

    def dtype(self):
        """
        Returns the type of the data.
       
        Parameters
        ----------
       
        """
        return self._dtype

    def _repr_(self):
        """
        Returns the "official" string representation of an object.
       
        """
        return f"[{self._data}]"

    def _len_(self):
        """
        Returns the length of the object
       
        """
        return len(self.index)

    def _getitem_(self, item):
        """
        Allowes us to index the columns by name
        
        """
        return self._data[item]

    def _iter_(self):
        """
        Iterate through the column names
       
        Parameters
        ----------
        
        """
        self.n = 0
        return iter(self._columns)

    def _next_(self):
        """
        Returns the the next element.
        
        """
        self.n += 1
        return next(iter(self._columns))
        
    def showrow(self, rowsee):
        """
        Returns the given row
       
        Parameters
        ----------
        rowsee : single label
    
        """
        xrow = []
        for col in self._data.keys():
            xrow.append(self._data[col][rowsee])
        return f"Row nº{rowsee}: {xrow}"

    def _setitem_(self, idx, value):
        """
        Returns a value for a specified index 
       
        Parameters
        ----------
        idx : single label
        value: single value
        
        """
        if type(value) == type(1):
            newarr = []
            for number in self.index:
                newarr.append(value)
            self.data[idx] = np.array(newarr)
        elif type(value) == type(1.0):
            newarr = []
            for number in self.index:
                newarr.append(value)
            self.data[idx] = np.array(newarr)
        elif type(value) == type("a"):
            newarr = []
            for number in self.index:
                newarr.append(value)
            self.data[idx] = np.array(newarr)
        elif len(value) == len(self.index):
            self.data[idx] = np.array(value)
        else:
            raise ValueError(
                "Hi! Length of values does not match length of index, stop trying to brake my DF!"
            )
    
    def sum(self, column=None):
        """
        Returns sum of each column or a single columns if a specified column argument is
        passed
        
        Parameters
        ----------
        Columns : single label
        
        """
        if column is None:
            sumlist = []
            for key in self._data.keys():
                result = 0
                if type(self._data[key][0]) == type(np.array([1])[0]):
                    for number in range(len(self.index)):
                        result += self._data[key][number]
                    sumlist.append(result)
                elif type(self._data[key][0]) == type(np.array([1.0])[0]):
                    for number in range(len(self.index)):
                        result += self._data[key][number]
                    sumlist.append(result)
                else:
                    sumlist.append("String col")
            return sumlist
         else:
            result = 0
            for number in range(len(self.index)):
                result += self._data[column][number]
            return result

     def mean(self, column=None):
        """
        Returns mean of each column or a single columns if a specified column argument is
        passed
        
        Parameters
        ----------
        Columns : single label
        """
        if column is None:
            meanlist = []
            for key in self._data.keys():
                result = 0
                if type(self._data[key][0]) == type(np.array([1])[0]):
                    for number in range(len(self.index)):
                        result += self._data[key][number] / len(self.index)
                    meanlist.append(result)
                elif type(self._data[key][0]) == type(np.array([1.0])[0]):
                    for number in range(len(self.index)):
                        result += self._data[key][number] / len(self.index)
                    meanlist.append(result)
                else:
                    meanlist.append("String col")
            return meanlist
        else:
            result = 0
            for number in range(len(self.index)):
                result += self._data[column][number] / len(self.index)
            return result

    def median(self, column=None):
        """
        Returns median of each column or a single columns if a specified column argument is
        passed
        
        Parameters
        ----------
        Columns : single label
        """
        if column is None:
            medianlist = []
            for key in self._data.keys():
                sortedcol = self._data[key]
                sortedcol.sort()
                result = 0
                if type(self._data[key][0]) == type(np.array([1])[0]):
                    if len(self.index) % 2 == 0:
                        result = (
                            sortedcol[len(self.index) / 2]
                            + sortedcol[(len(self.index) / 2) - 1]
                        ) / 2
                    else:
                        result = sortedcol[int((len(self.index) / 2) - 0.5)]
                    medianlist.append(result)
                elif type(self._data[key][0]) == type(np.array([1.0])[0]):
                    if len(self.index) % 2 == 0:
                        result = (
                            sortedcol[len(self.index) / 2]
                            + sortedcol[(len(self.index) / 2) - 1]
                        ) / 2
                    else:
                        result = sortedcol[int((len(self.index) / 2) - 0.5)]
                    medianlist.append(result)
                else:
                    medianlist.append("String col")
            return medianlist
        else:
            sortedcol = self._data[column]
            sortedcol.sort()
            result = 0
            if len(self.index) % 2 == 0:
                result = (
                    sortedcol[len(self.index) / 2]
                    + sortedcol[(len(self.index) / 2) - 1]
                ) / 2
            else:
                result = sortedcol[int((len(self.index) / 2) - 0.5)]
            return result
    
    def max(self, column=None):
        """ Returns a list of dictionary’s with the max value of the columns or
        the specific column if so called
        
        Parameters
        ----------
        Columns : single label
        """

        if column is None:
            maxlist = []
            for key in self._data.keys():
                result = max(self._data[key])
                maxlist.append(result)
            return maxlist
        else:
            result = max(self._data[column])
            return result
    
    def min(self, column=None):
        """ Returns a list of dictionary’s with the min value of the columns or
        the specific column if so called
        
        Parameters
        ----------
        Columns : single label
        """

        if column is None:
            minlist = []
            for key in self._data.keys():
                result = min(self._data[key])
                minlist.append(result)
            return minlist
        else:
            sortedcol = self._data[column]
            sortedcol.sort()
            result = min(self._data[column])
            return result