class Block:
    def __init__(self,value):
        self._value = value
    
    @property
    def value(self):
        return (Block(self._value))
        
class SuperBlock(Block):
        def split(self):
            if self._value == 1:
                return ['+'+'-'+'+'+'\n'+'|'+'1'+'|'+'\n'+'+'+'-'+'+']
            else:
                small = self._value//2
                big = self._value - small
                ps = '+'+'-'*len(str(small))+'+'+'\n'+'|'+str(small)+'|'+'\n'+'+'+'-'*len(str(small))+'+'
                pb = '+'+'-'*len(str(big))+'+'+'\n'+'|'+str(big)+'|'+'\n'+'+'+'-'*len(str(big))+'+'
                return ps,pb


if __name__ == "__main__":
    super_block_value = int(input())

    super_block_one = SuperBlock(super_block_value)

    try:
        super_block_one._value
    except AttributeError:
        print("Missed protecting value")

    try:
        super_block_one.value = 1
        print("Missed setting safe access to value")
    except AttributeError:
        pass

    print(isinstance(super_block_one, SuperBlock))

    try:
        print(isinstance(super_block_one, Block))
    except:
        print("You should use Block class to build SuperBlock")
    
    blocks = super_block_one.split()
    if len(blocks) > 1:
        print(blocks[0])
        print(blocks[1])
    else:
        print(blocks[0])
