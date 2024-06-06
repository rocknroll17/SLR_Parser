from lexical_analyzer import Token
import time
import lexical_analyzer
from tree import Tree


class SLRParser:
    def __init__(self):
        self.table = table
        self.rule = rule

    def parse(self, input):
        stack = [0]
        input = input + [Token("$", "$")]
        i = 0
        string = []
        tree = []
        while True:
            time.sleep(0.07)
            state = stack[-1]
            token = input[i].type
            action = self.table[state]["ACTION"][token]
            print("input:",input)
            print("스택:",stack)
            print("LEFT:",string)
            print("현재 input:",input[i])
            print("남은 input:",input[i:])
            print("토큰:",token, "action:",action)
            print()
            if action == "ACC":
                tree_node = Tree(self.rule[0][0])
                for j in range(len(tree)):
                    tree_node.add_child(tree[j], 0)
                tree = tree_node
                tree.print_tree_by_level()
                return True
            elif action[0] == "S":
                stack.append(int(action[1:]))
                string.append(input[i].type)
                tree.append(Tree(input[i].type))
                i += 1
            elif action[0] == "R":
                rule_index = int(action[1:])
                if self.rule[rule_index][1][0] != "ϵ":
                    for j in range(len(self.rule[rule_index][1])):
                        string.pop()
                        stack.pop()
                    tree_node = Tree(self.rule[rule_index][0])
                    for j in range(len(self.rule[rule_index][1])):
                        tree_node.add_child(tree.pop(), 0)
                string.append(Token(self.rule[rule_index][0], ""))
                tree.append(tree_node)
                state = stack[-1]
                token = string[-1].type
                stack.append(self.table[state]["GOTO"][token])
            else:
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
    ["COND", ['COND1', 'comp', 'COND']],
    ["COND1", ['boolstr']],
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
    {"ACTION":{"boolstr":"S57"}, "GOTO":{"COND":55,"COND1":56}},
    {"ACTION":{"boolstr":"S57"}, "GOTO":{"COND":58,"COND1":56}},
    {"ACTION":{"semi":"S9","assign":"S11"}, "GOTO":{}},
    {"ACTION":{"rparen":"R22","comma":"S32"}, "GOTO":{"MOREARGS":59}},
    {"ACTION":{"vtype":"R18","$":"R18"}, "GOTO":{}},
    {"ACTION":{"semi":"S60"}, "GOTO":{}},
    {"ACTION":{"rparen":"S61"}, "GOTO":{}},
    {"ACTION":{"comp":"S62"}, "GOTO":{}},
    {"ACTION":{"comp":"R30"}, "GOTO":{}},
    {"ACTION":{"rparen":"S63"}, "GOTO":{}},
    {"ACTION":{"rparen":"R21"}, "GOTO":{}},
    {"ACTION":{"rbrace":"R33"}, "GOTO":{}},
    {"ACTION":{"lbrace":"S64"}, "GOTO":{}},
    {"ACTION":{"boolstr":"S57"}, "GOTO":{"COND":65,"COND1":56}},
    {"ACTION":{"lbrace":"S66"}, "GOTO":{}},
    {"ACTION":{"vtype":"S42","id":"S43","rbrace":"R24","if":"S40","while":"S41","return":"R24"}, "GOTO":{"VDECL":38,"ASSIGN":39,"BLOCK":67,"STMT":37}},
    {"ACTION":{"rparen":"R29"}, "GOTO":{}},
    {"ACTION":{"vtype":"S42","id":"S43","rbrace":"R24","if":"S40","while":"S41","return":"R24"}, "GOTO":{"VDECL":38,"ASSIGN":39,"BLOCK":68,"STMT":37}},
    {"ACTION":{"rbrace":"S69"}, "GOTO":{}},
    {"ACTION":{"rbrace":"S70"}, "GOTO":{}},
    {"ACTION":{"vtype":"R32","id":"R32","rbrace":"R32","if":"R32","while":"R32","else":"S72","return":"R32"}, "GOTO":{"ELSE":71}},
    {"ACTION":{"vtype":"R28","id":"R28","rbrace":"R28","if":"R28","while":"R28","return":"R28"}, "GOTO":{}},
    {"ACTION":{"vtype":"R27","id":"R27","rbrace":"R27","if":"R27","while":"R27","return":"R27"}, "GOTO":{}},
    {"ACTION":{"lbrace":"S73"}, "GOTO":{}},
    {"ACTION":{"vtype":"S42","id":"S43","rbrace":"R24","if":"S40","while":"S41","return":"R24"}, "GOTO":{"VDECL":38,"ASSIGN":39,"BLOCK":74,"STMT":37}},
    {"ACTION":{"rbrace":"S75"}, "GOTO":{}},
    {"ACTION":{"vtype":"R31","id":"R31","rbrace":"R31","if":"R31","while":"R31","return":"R31"}, "GOTO":{}}
]

if __name__ == "__main__":
    import main