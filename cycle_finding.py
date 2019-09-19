
class Node: 
  
    # Constructor for a node in the Linked List 
    def __init__(self, data): 
        self.data = data 
        self.next = None

#Simple list that does not contain a cycle
def makeList1():
	node1 = Node(5)
	node2 = Node(12)
	node3 = Node(7)
	node4 = Node(34)
	node5 = Node(44)

	node1.next = node2
	node2.next = node3
	node3.next = node4
	node4.next = node5

	return node1	

#Second list which contains a cycle
def makeList2():
	node1 = Node(76)
        node2 = Node(39)
        node3 = Node(68)
        node4 = Node(4)
        node5 = Node(11)
	node6 = Node(99)
	node7 = Node(81)

        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
	node5.next = node6
	node6.next = node7
	node7.next = node4

	return node1

#Floyd's algorithm which finds a loop in a linked list	
def Floyd(startingNode):
	fastNode = startingNode.next
	slowNode = startingNode

	#Iterate over list and see if there is a loop
	while(fastNode is not None and fastNode.next is not None):

		if (fastNode is slowNode):
			return("There is a loop!")

		fastNode = fastNode.next.next
		slowNode = slowNode.next

	#If list ends there there must not be a loop
	return("There is no loop")
	

def main():
	#Test first list
	startingNode = makeList1()
	print(Floyd(startingNode))
	
	#Test second list
	startingNode = makeList2()
	print(Floyd(startingNode))


if __name__ == "__main__":
    main()
