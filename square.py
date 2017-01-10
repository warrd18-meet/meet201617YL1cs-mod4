from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, length):
        super(Square,self).__init__(length,length)

    def set_length(self,new_length):
        super(Square,self).set_length(new_length)
        super(Square,self).set_height(new_length)

    def set_height(self,new_height):
        super(Square,self).set_height(new_height)
        super(Square,self).set_length(new_height)

        
