from collections import deque


class DirectedGraph:
    def __init__(self, head_node_value):
        self.size = 1
        self.head_node = Node(head_node_value)

    def breadth_first_search(self, value):
        if len(self.head_node.childs) == 0:
            raise Exception('Graph is empty')
        elif self.head_node.value == value:
            return self.head_node
        else:
            searched = []
            search_queue = deque(self.head_node.childs)
            while search_queue:
                node = search_queue.popleft()
                if node not in searched:
                    searched.append(node)
                    if node.value == value:
                        return node
                    else:
                        search_queue += node.childs
            return None


class Node:
    def __init__(self, value, childs=None):
        self.value = value
        if childs:
            self.childs = childs
        else:
            self.childs = []

    def add_child(self, value):
        added_node = Node(value)
        self.childs.append(added_node)
        return self

    def add_child_node(self, child):
        self.childs.append(child)
        return self


graph = DirectedGraph('dsdf')
graph.head_node \
    .add_child('sdfsd') \
    .add_child('sdfs123d') \
    .add_child('sdf12312313123sd')

print(graph.breadth_first_search('sdfs123d'))
print(graph.breadth_first_search('222'))
