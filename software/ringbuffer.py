#code from https://forum.micropython.org/viewtopic.php?t=4939

class Ringbuffer:
    def __init__(self, size):
        self.data = bytearray(size)
        self.size = size
        self.index_put = 0
        self.index_get = 0
        self.full = 0
        
    def put(self, value):
        next_index = (self.index_put + 1) % self.size
        # check for overflow
        if self.index_get != next_index: 
            self.data[self.index_put] = value
            self.index_put = next_index
            self.full = 0
        else:
            self.full = 1
        
        return self.full
        
    def get(self):
        if self.index_get == self.index_put:
            return None  ## buffer empty
        else:
            value = self.data[self.index_get]
            self.index_get = (self.index_get + 1) % self.size
            return value