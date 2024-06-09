from lexical_analyzer import Token
import time
import lexical_analyzer
from tree import Tree
from anytree import Node, RenderTree


class SLRParser:
    def __init__(self):
        self.table = table
        self.rule = rule

    def parse(self, input, additional = None):
        stack = [0]
        input = input + [Token("$", "$")]
        i = 0
        string = []
        any_tree = []
        tree = []
        while True:
            try:
                state = stack[-1]
                token = input[i].type
                action = self.table[state]["ACTION"][token]
                print("input:",input)
                print("스택:",stack)
                print("LEFT:",string)
                print("TREE:",tree)
                print("현재 input:",input[i])
                print("남은 input:",input[i:])
                print("토큰:",token, "action:",action)
                print("AnyTree:", any_tree)
                print()
                if action == "ACC":
                    tree_node = Tree(self.rule[0][0])
                    any_tree_node = Node(self.rule[0][0])
                    for j in range(len(tree)):
                        tree_node.add_child(tree[j], 0)
                        any_tree_node.children = any_tree
                    tree = tree_node
                    tree.set_parent()
                    tree.set_level(1)
                    any_tree = any_tree_node
                    for pre, fill, node in RenderTree(any_tree):
                        print("%s%s" % (pre, node.name))
                    tree.print_tree()
                    print("Accept")
                    return True
                elif action[0] == "S":
                    stack.append(int(action[1:]))
                    string.append(input[i].type)
                    tree.append(Tree(input[i].type))
                    any_tree.append(Node(input[i].type))
                    i += 1
                elif action[0] == "R":
                    rule_index = int(action[1:])
                    if self.rule[rule_index][1][0] != "ϵ":
                        for j in range(len(self.rule[rule_index][1])):
                            string.pop()
                            stack.pop()
                        tree_node = Tree(self.rule[rule_index][0])
                        any_tree_node = Node(self.rule[rule_index][0])
                        for j in range(len(self.rule[rule_index][1])):
                            tree_node.children.insert(0, tree.pop())
                        any_tree_node.children = any_tree[-len(self.rule[rule_index][1]):]
                        any_tree = any_tree[:-len(self.rule[rule_index][1])]
                    else:
                        tree_node = Tree(self.rule[rule_index][0])
                        any_tree_node = Node(self.rule[rule_index][0])

                    string.append(Token(self.rule[rule_index][0], ""))
                    tree.append(tree_node)
                    any_tree.append(any_tree_node)
                    state = stack[-1]
                    token = string[-1].type
                    stack.append(self.table[state]["GOTO"][token])
                    for j in any_tree:
                        for pre, fill, node in RenderTree(j):
                            print("%s%s" % (pre, node.name))
                else:
                    print("Reject")
                    for i in range(len(string)):
                        print(string[i].type, end=" ")
                    return False
            except:
                print("Reject")
                index = 0
                print()
                if additional == None:
                    for j in range(len(input)):
                        print(input[j].type, end=" ")
                    for j in range(i):
                        index += len(input[j].type) + 1
                    print()
                    print(" "*index, end = "")
                    print("^"*len(input[i].type))
                    print("Syntax Error: Invalid Syntax at line \""+ input[i].type+"\"")
                else:
                    index = i
                    finder = 0
                    sum = 0
                    for i in range(len(additional)):
                        sum += len(additional[i])
                        if sum >= index:
                            finder = i
                            sum -= len(additional[i])
                            break

                    print(" ".join(additional[finder]))
                    print(" "*(len(" ".join(additional[finder][:index-sum]))+1), end = "")
                    print("^"*len(input[index].value))
                    print("\nSyntax Error: Invalid Syntax")
                return False

            

rule = [

    ["S", ["CODE"]],
    ["CODE", ['VDECL', 'CODE']],
    ["CODE", ['FDECL', 'CODE']],
    ["CODE", ['ϵ']],
    ["VDECL", ['vtype', 'id', 'semi']],
    ["VDECL", ['vtype', 'ASSIGN', 'semi']],
    ["ASSIGN", ['id', 'assign', 'RHS']],
    ["RHS", ['EXPR']],
    ["RHS", ['literal']],
    ["RHS", ['character']],
    ["RHS", ['boolstr']],
    ["EXPR", ['EXPR1', 'addsub', 'EXPR']],
    ["EXPR", ['EXPR1']],
    ["EXPR1", ['EXPR2', 'multdiv', 'EXPR1']],
    ["EXPR1", ['EXPR2']],
    ["EXPR2", ['lparen', 'EXPR', 'rparen']],
    ["EXPR2", ['id']],
    ["EXPR2", ['num']],
    ["FDECL", ['vtype', 'id', 'lparen', 'ARG', 'rparen', 'lbrace', 'BLOCK', 'RETURN', 'rbrace']],
    ["ARG", ['vtype', 'id', 'MOREARGS']],
    ["ARG", ['ϵ']],
    ["MOREARGS", ['comma', 'vtype', 'id', 'MOREARGS']],
    ["MOREARGS", ['ϵ']],
    ["BLOCK", ['STMT', 'BLOCK']],
    ["BLOCK", ['ϵ']],
    ["STMT", ['VDECL']],
    ["STMT", ['ASSIGN', 'semi']],
    ["STMT", ['if', 'lparen', 'COND', 'rparen', 'lbrace', 'BLOCK', 'rbrace', 'ELSE']],
    ["STMT", ['while', 'lparen', 'COND', 'rparen', 'lbrace', 'BLOCK', 'rbrace']],
    ["COND", ['boolstr ', 'comp', 'COND']],
    ["COND", ['boolstr']],
    ["ELSE", ['else', 'lbrace', 'BLOCK', 'rbrace']],
    ["ELSE", ['ϵ']],
    ["RETURN", ['return', 'RHS', 'semi']]
    ]

table = [
    {"ACTION":{"vtype":"S4","$":"R3"}, "GOTO":{"CODE":1,"VDECL":2,"FDECL":3}},
    {"ACTION":{"$":"ACC"}, "GOTO":{}},
    {"ACTION":{"vtype":"S4","$":"R3"}, "GOTO":{"CODE":5,"VDECL":2,"FDECL":3}},
    {"ACTION":{"vtype":"S4","$":"R3"}, "GOTO":{"CODE":6,"VDECL":2,"FDECL":3}},
    {"ACTION":{"id":"S7"}, "GOTO":{"ASSIGN":8}},
    {"ACTION":{"$":"R1"}, "GOTO":{}},
    {"ACTION":{"$":"R2"}, "GOTO":{}},
    {"ACTION":{"semi":"S9","assign":"S11","lparen":"S10"}, "GOTO":{}},
    {"ACTION":{"semi":"S12"}, "GOTO":{}},
    {"ACTION":{"vtype":"R4","id":"R4","rbrace":"R4","if":"R4","while":"R4","return":"R4","$":"R4"}, "GOTO":{}},
    {"ACTION":{"vtype":"S14","rparen":"R20"}, "GOTO":{"ARG":13}},
    {"ACTION":{"id":"S23","literal":"S17","character":"S18","boolstr":"S19","lparen":"S22","num":"S24"}, "GOTO":{"RHS":15,"EXPR":16,"EXPR1":20,"EXPR2":21}},
    {"ACTION":{"vtype":"R5","id":"R5","rbrace":"R5","if":"R5","while":"R5","return":"R5","$":"R5"}, "GOTO":{}},
    {"ACTION":{"rparen":"S25"}, "GOTO":{}},
    {"ACTION":{"id":"S26"}, "GOTO":{}},
    {"ACTION":{"semi":"R6"}, "GOTO":{}},
    {"ACTION":{"semi":"R7"}, "GOTO":{}},
    {"ACTION":{"semi":"R8"}, "GOTO":{}},
    {"ACTION":{"semi":"R9"}, "GOTO":{}},
    {"ACTION":{"semi":"R10"}, "GOTO":{}},
    {"ACTION":{"semi":"R12","addsub":"S27","rparen":"R12"}, "GOTO":{}},
    {"ACTION":{"semi":"R14","addsub":"R14","multdiv":"S28","rparen":"R14"}, "GOTO":{}},
    {"ACTION":{"id":"S23","lparen":"S22","num":"S24"}, "GOTO":{"EXPR":29,"EXPR1":20,"EXPR2":21}},
    {"ACTION":{"semi":"R16","addsub":"R16","multdiv":"R16","rparen":"R16"}, "GOTO":{}},
    {"ACTION":{"semi":"R17","addsub":"R17","multdiv":"R17","rparen":"R17"}, "GOTO":{}},
    {"ACTION":{"lbrace":"S30"}, "GOTO":{}},
    {"ACTION":{"rparen":"R22","comma":"S32"}, "GOTO":{"MOREARGS":31}},
    {"ACTION":{"id":"S23","lparen":"S22","num":"S24"}, "GOTO":{"EXPR":33,"EXPR1":20,"EXPR2":21}},
    {"ACTION":{"id":"S23","lparen":"S22","num":"S24"}, "GOTO":{"EXPR1":34,"EXPR2":21}},
    {"ACTION":{"rparen":"S35"}, "GOTO":{}},
    {"ACTION":{"vtype":"S42","id":"S43","rbrace":"R24","if":"S40","while":"S41","return":"R24"}, "GOTO":{"VDECL":38,"ASSIGN":39,"BLOCK":36,"STMT":37}},
    {"ACTION":{"rparen":"R19"}, "GOTO":{}},
    {"ACTION":{"vtype":"S44"}, "GOTO":{}},
    {"ACTION":{"semi":"R11","rparen":"R11"}, "GOTO":{}},
    {"ACTION":{"semi":"R13","addsub":"R13","rparen":"R13"}, "GOTO":{}},
    {"ACTION":{"semi":"R15","addsub":"R15","multdiv":"R15","rparen":"R15"}, "GOTO":{}},
    {"ACTION":{"return":"S46"}, "GOTO":{"RETURN":45}},
    {"ACTION":{"vtype":"S42","id":"S43","rbrace":"R24","if":"S40","while":"S41","return":"R24"}, "GOTO":{"VDECL":38,"ASSIGN":39,"BLOCK":47,"STMT":37}},
    {"ACTION":{"vtype":"R25","id":"R25","rbrace":"R25","if":"R25","while":"R25","return":"R25"}, "GOTO":{}},
    {"ACTION":{"semi":"S48"}, "GOTO":{}},
    {"ACTION":{"lparen":"S49"}, "GOTO":{}},
    {"ACTION":{"lparen":"S50"}, "GOTO":{}},
    {"ACTION":{"id":"S51"}, "GOTO":{"ASSIGN":8}},
    {"ACTION":{"assign":"S11"}, "GOTO":{}},
    {"ACTION":{"id":"S52"}, "GOTO":{}},
    {"ACTION":{"rbrace":"S53"}, "GOTO":{}},
    {"ACTION":{"id":"S23","literal":"S17","character":"S18","boolstr":"S19","lparen":"S22","num":"S24"}, "GOTO":{"RHS":54,"EXPR":16,"EXPR1":20,"EXPR2":21}},
    {"ACTION":{"rbrace":"R23","return":"R23"}, "GOTO":{}},
    {"ACTION":{"vtype":"R26","id":"R26","rbrace":"R26","if":"R26","while":"R26","return":"R26"}, "GOTO":{}},
    {"ACTION":{"boolstr":"S56"}, "GOTO":{"COND":55}},
    {"ACTION":{"boolstr":"S56"}, "GOTO":{"COND":57}},
    {"ACTION":{"semi":"S9","assign":"S11"}, "GOTO":{}},
    {"ACTION":{"rparen":"R22","comma":"S32"}, "GOTO":{"MOREARGS":58}},
    {"ACTION":{"vtype":"R18","$":"R18"}, "GOTO":{}},
    {"ACTION":{"semi":"S59"}, "GOTO":{}},
    {"ACTION":{"rparen":"S60"}, "GOTO":{}},
    {"ACTION":{"rparen":"R30","comp":"S61"}, "GOTO":{}},
    {"ACTION":{"rparen":"S62"}, "GOTO":{}},
    {"ACTION":{"rparen":"R21"}, "GOTO":{}},
    {"ACTION":{"rbrace":"R33"}, "GOTO":{}},
    {"ACTION":{"lbrace":"S63"}, "GOTO":{}},
    {"ACTION":{"boolstr":"S56"}, "GOTO":{"COND":64}},
    {"ACTION":{"lbrace":"S65"}, "GOTO":{}},
    {"ACTION":{"vtype":"S42","id":"S43","rbrace":"R24","if":"S40","while":"S41","return":"R24"}, "GOTO":{"VDECL":38,"ASSIGN":39,"BLOCK":66,"STMT":37}},
    {"ACTION":{"rparen":"R29"}, "GOTO":{}},
    {"ACTION":{"vtype":"S42","id":"S43","rbrace":"R24","if":"S40","while":"S41","return":"R24"}, "GOTO":{"VDECL":38,"ASSIGN":39,"BLOCK":67,"STMT":37}},
    {"ACTION":{"rbrace":"S68"}, "GOTO":{}},
    {"ACTION":{"rbrace":"S69"}, "GOTO":{}},
    {"ACTION":{"vtype":"R32","id":"R32","rbrace":"R32","if":"R32","while":"R32","else":"S71","return":"R32"}, "GOTO":{"ELSE":70}},
    {"ACTION":{"vtype":"R28","id":"R28","rbrace":"R28","if":"R28","while":"R28","return":"R28"}, "GOTO":{}},
    {"ACTION":{"vtype":"R27","id":"R27","rbrace":"R27","if":"R27","while":"R27","return":"R27"}, "GOTO":{}},
    {"ACTION":{"lbrace":"S72"}, "GOTO":{}},
    {"ACTION":{"vtype":"S42","id":"S43","rbrace":"R24","if":"S40","while":"S41","return":"R24"}, "GOTO":{"VDECL":38,"ASSIGN":39,"BLOCK":73,"STMT":37}},
    {"ACTION":{"rbrace":"S74"}, "GOTO":{}},
    {"ACTION":{"vtype":"R31","id":"R31","rbrace":"R31","if":"R31","while":"R31","return":"R31"}, "GOTO":{}}
    ]

if __name__ == "__main__":
    import main