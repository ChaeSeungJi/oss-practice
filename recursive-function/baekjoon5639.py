import sys
sys.setrecursionlimit(10**6)

class Node: # 값들을 담기 위한 노드 클래스
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def preorder_traversal(node): # 전위순회 함수
    if node is not None:
        # 현재 노드의 값을 출력
        print(node.value)
        
        # 왼쪽 서브트리를 전위순회
        preorder_traversal(node.left)
        
        # 오른쪽 서브트리를 전위순회
        preorder_traversal(node.right)

def postorder_traversal(node):  # 후위순회 함수
    if node is not None:
        postorder_traversal(node.left) # 왼쪽 노드부터 시작 만약 왼쪽노드가 왼쪽자식노드를 가지고 있다면 내려가고 또 내려가고 끝까지 내려감. 맨 밑까지 갔다가, 맨밑 함수가 끝나고 n-1 노드에서 자식노드 오른쪽 재귀함수 실행
        postorder_traversal(node.right)
        print(node.value)




def make_binary_tree(preorder_traverse): # 이진트리 만들기 함수
    if not preorder_traverse :
        return None
    
    root_value = preorder_traverse[0]
    root = Node(root_value)

    i=1
    while i<len(preorder_traverse) and preorder_traverse[i] < root_value: # 왼쪽 서브트리의 노드는 항상 루트값보다 작은 성질을 활용
        i+=1
    

    left_subTree = make_binary_tree(preorder_traverse[1:i]) # 왼쪽 서브트리의 값을 저장
    right_subTree = make_binary_tree(preorder_traverse[i:]) # 오른쪽 서브트리의 값을 저장

    root.left = left_subTree
    root.right = right_subTree

    return root

# preorder_traverse = [50,30,24,5,28,45,98,52,60]

# tree = make_binary_tree(preorder_traverse)

# postorder_traversal(tree)


li = []


while True:
    value = sys.stdin.readline()
    if not value:
        break
    li.append(int(value))


tree = make_binary_tree(li)

postorder_traversal(tree)