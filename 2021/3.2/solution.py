class Node:

    def __init__(self, bit_index, leaf_value):
        self.bit_index = bit_index
        self.count = 1
        
        self.one_count = 0
        self.one_node = None
        
        self.zero_count = 0
        self.zero_node = None
        
        self.leaf_value = None
        if bit_index >= len(leaf_value): # This is a terminal node. There are no more bits
            self.leaf_value = leaf_value
            return

        # Parse the remaining bits of the value
        child = Node(bit_index + 1, leaf_value)
        if leaf_value[bit_index] == '1':
            self.one_count += 1
            self.one_node = child
        else:
            self.zero_count += 1
            self.zero_node = child

    
    def __str__(self):
        if self.leaf_value:
            return "Leaf node: " + self.leaf_value
        else:
            return "Inner node: " + str(self.count) + " children. " + str(self.one_count) + " ones, " + str(self.zero_count) + " zeros."

    def insert(self, line):
        self.count += 1
        if line[self.bit_index] == '1':
            self.one_count += 1
            if self.one_node is None:
                self.one_node = Node(self.bit_index + 1, line)
            else:
                self.one_node.insert(line)
        else:
            self.zero_count += 1
            if self.zero_node is None:
                self.zero_node = Node(self.bit_index + 1, line)
            else:
                self.zero_node.insert(line)
                
    def oxygen_generator_rating(self):
        if self.leaf_value:
            return ''
        if self.one_count >= self.zero_count:
            return '1' + self.one_node.oxygen_generator_rating()
        else:
            return '0' + self.zero_node.oxygen_generator_rating()

    def co2_scrubber_rating(self):
        if self.leaf_value:
            return ''
        if self.zero_count != 0 and self.zero_count <= self.one_count or self.one_count == 0:
            return '0' + self.zero_node.co2_scrubber_rating()
        else:
            return '1' + self.one_node.co2_scrubber_rating()

root = None
with open('input.txt') as input:
    for line in input.readlines():
        line = line.strip()
        if root == None:
            root = Node(0, line)
        else:
            root.insert(line)
print("Life support rating: " + str(int(root.oxygen_generator_rating(), 2)*int(root.co2_scrubber_rating(), 2)))
