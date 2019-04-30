import numpy as np

class dataframe:
    def __init__(self, data, index=None, columns=None, dtype=None): #"dunder init" = double underscore init
        for colname in data.keys():
            data[colname] = np.array(data[colname])
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
        coltypes = []
        for colname in data.keys():
            coltypes.append(f"{colname}: {type(data[colname][0])}")
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
    def __repr__(self):
        """
        Returns the "official" string representation of an object.
       
        Parameters
        ----------
       
        """
        return f"[{self._data}]"
    def __len__(self):
        """
        Returns the length of the object
       
        Parameters
        ----------
       
        """
        return len(self.index)
    def __getitem__(self,item):
        """
        Returns the dictionary value of the item
       
        Parameters
        ----------
        item : single label
        
        """
        return self._data[item]
    def __iter__(self):
        """
        To go through all the columns one by one .
       
        Parameters
        ----------
        
        """
        self.n = 0
        return iter(self._columns)
    def __next__(self):
         """
        Returns the the next column.
       
        Parameters
        ----------
        
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
    def __setitem__(self, idx, value):
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
            raise ValueError("FOOL! Length of values does not match length of index, stop trying to brake my DF!")
    
    def sum(self, column = None):
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
    def mean(self, column = None):
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
                        result += self._data[key][number]/len(self.index)
                    meanlist.append(result)
                elif type(self._data[key][0]) == type(np.array([1.0])[0]): 
                    for number in range(len(self.index)):
                        result += self._data[key][number]/len(self.index)
                    meanlist.append(result)
                else:
                    meanlist.append("String col")
            return meanlist
        else:
            result = 0
            for number in range(len(self.index)):
                result += self._data[column][number]/len(self.index)
            return result
    def median(self, column = None):
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
                        result = (sortedcol[len(self.index)/2] + sortedcol[(len(self.index)/2)-1])/2
                    else:
                        result = sortedcol[int((len(self.index)/2)-0.5)]
                    medianlist.append(result)
                elif type(self._data[key][0]) == type(np.array([1.0])[0]): 
                    if len(self.index) % 2 == 0:
                        result = (sortedcol[len(self.index)/2] + sortedcol[(len(self.index)/2)-1])/2
                    else:
                        result = sortedcol[int((len(self.index)/2)-0.5)]
                    medianlist.append(result)
                else:
                    medianlist.append("String col")
            return medianlist
        else:
            sortedcol = self._data[column]
            sortedcol.sort()
            result = 0
            if len(self.index) % 2 == 0:
                result = (sortedcol[len(self.index)/2] + sortedcol[(len(self.index)/2)-1])/2
            else:
                result = sortedcol[int((len(self.index)/2)-0.5)]
            return result
 #MAX

   def max(self):
        """ Returns a list of dictionary’s with the max value of numeric columns"""
  
        max_list = []
        max_dictionary = dict()

        # Iterate over all the columns
        for key in self.keys:
        
        # Check if the column contains numeric values
           
         if all(
                isinstance(x, (int, float, np.int_, np.float_)) for x in self.data[key]
            ):
                max_dictionary[key] = np.max(self.data[key])
            else:
                # Ignore if not numeric

        max_list.append(max_dictionary)
   

#MIN

def min(self):
        """ Returns a list of dictionary’s with the min value of numeric columns"""
        
        min_list = []
        min_dictionary = dict()

        # Iterate over all the columns
        for key in self.keys:
        
        # Check if the column contains numeric values
           
        if all(
                isinstance(x, (int, float, np.int_, np.float_)) for x in self.data[key]
            ):
                min_dictionary[key] = np.min(self.data[key])
            else:
                # Ignore if not numeric

        min_list.append(min_dictionary)
