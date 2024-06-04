from lexical_analyzer import Token
import time
import lexical_analyzer


class SLRParser:
    def __init__(self):
        self.table = table
        self.rule = rule

    def parse(self, input):
        stack = [1]
        input = input + [Token("$", "$")]
        i = 0
        string = []
        while True:
            time.sleep(2)
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
                return True
            elif action[0] == "S":
                stack.append(int(action[1:]))
                string.append(input[i].type)
                i += 1
            elif action[0] == "R":
                rule_index = int(action[1:])
                print(rule_index)
                stack.pop()
                for j in range(len(self.rule[rule_index][1])):
                    string.pop()
                string.append(Token(self.rule[rule_index][0], ""))
                state = stack[-1]
                token = string[-1].type
                stack.append(self.table[state]["GOTO"][token])
            else:
                return False
            

rule = [
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
    {"ACTION":{"vtype":"S2"}, "GOTO":{"VDECL":1}},
    {"ACTION":{"ϵ":"S5","vtype":"S6"}, "GOTO":{"CODE":3,"VDECL":1,"FDECL":4}},
    {"ACTION":{"id":"S7"}, "GOTO":{"ASSIGN":8}},
    {"ACTION":{"$":"ACC"}, "GOTO":{}},
    {"ACTION":{"ϵ":"S5","vtype":"S6"}, "GOTO":{"CODE":9,"VDECL":1,"FDECL":4}},
    {"ACTION":{"$":"R2"}, "GOTO":{}},
    {"ACTION":{"id":"S10"}, "GOTO":{"ASSIGN":8}},
    {"ACTION":{"semi":"S11","assign":"S12"}, "GOTO":{}},
    {"ACTION":{"semi":"S13"}, "GOTO":{}},
    {"ACTION":{"$":"R1"}, "GOTO":{}},
    {"ACTION":{"semi":"S11","assign":"S12","lparen":"S14"}, "GOTO":{}},
    {"ACTION":{"ϵ":"R3","vtype":"R3","id":"R3","if":"R3","while":"R3"}, "GOTO":{}},
    {"ACTION":{"id":"S23","literal":"S17","character":"S18","boolstr":"S19","lparen":"S22","num":"S24"}, "GOTO":{"RHS":15,"EXPR":16,"EXPR1":20,"EXPR2":21}},
    {"ACTION":{"ϵ":"R4","vtype":"R4","id":"R4","if":"R4","while":"R4"}, "GOTO":{}},
    {"ACTION":{"ϵ":"S27","vtype":"S26"}, "GOTO":{"ARG":25}},
    {"ACTION":{"semi":"R5"}, "GOTO":{}},
    {"ACTION":{"semi":"R6"}, "GOTO":{}},
    {"ACTION":{"semi":"R7"}, "GOTO":{}},
    {"ACTION":{"semi":"R8"}, "GOTO":{}},
    {"ACTION":{"semi":"R9"}, "GOTO":{}},
    {"ACTION":{"semi":"R11","addsub":"S28","rparen":"R11"}, "GOTO":{}},
    {"ACTION":{"semi":"R13","addsub":"R13","multdiv":"S29","rparen":"R13"}, "GOTO":{}},
    {"ACTION":{"id":"S23","lparen":"S22","num":"S24"}, "GOTO":{"EXPR":30,"EXPR1":20,"EXPR2":21}},
    {"ACTION":{"semi":"R15","addsub":"R15","multdiv":"R15","rparen":"R15"}, "GOTO":{}},
    {"ACTION":{"semi":"R16","addsub":"R16","multdiv":"R16","rparen":"R16"}, "GOTO":{}},
    {"ACTION":{"rparen":"S31"}, "GOTO":{}},
    {"ACTION":{"id":"S32"}, "GOTO":{}},
    {"ACTION":{"rparen":"R19"}, "GOTO":{}},
    {"ACTION":{"id":"S23","lparen":"S22","num":"S24"}, "GOTO":{"EXPR":33,"EXPR1":20,"EXPR2":21}},
    {"ACTION":{"id":"S23","lparen":"S22","num":"S24"}, "GOTO":{"EXPR1":34,"EXPR2":21}},
    {"ACTION":{"rparen":"S35"}, "GOTO":{}},
    {"ACTION":{"lbrace":"S36"}, "GOTO":{}},
    {"ACTION":{"ϵ":"S39","comma":"S38"}, "GOTO":{"MOREARGS":37}},
    {"ACTION":{"semi":"R10","rparen":"R10"}, "GOTO":{}},
    {"ACTION":{"semi":"R12","addsub":"R12","rparen":"R12"}, "GOTO":{}},
    {"ACTION":{"semi":"R14","addsub":"R14","multdiv":"R14","rparen":"R14"}, "GOTO":{}},
    {"ACTION":{"ϵ":"S42","vtype":"S2","id":"S47","if":"S45","while":"S46"}, "GOTO":{"VDECL":43,"ASSIGN":44,"BLOCK":40,"STMT":41}},
    {"ACTION":{"rparen":"R18"}, "GOTO":{}},
    {"ACTION":{"vtype":"S48"}, "GOTO":{}},
    {"ACTION":{"rparen":"R21"}, "GOTO":{}},
    {"ACTION":{"return":"S50"}, "GOTO":{"RETURN":49}},
    {"ACTION":{"ϵ":"S42","vtype":"S2","id":"S47","if":"S45","while":"S46"}, "GOTO":{"VDECL":43,"ASSIGN":44,"BLOCK":51,"STMT":41}},
    {"ACTION":{"rbrace":"R23","return":"R23"}, "GOTO":{}},
    {"ACTION":{"ϵ":"R24","vtype":"R24","id":"R24","if":"R24","while":"R24"}, "GOTO":{}},
    {"ACTION":{"semi":"S52"}, "GOTO":{}},
    {"ACTION":{"lparen":"S53"}, "GOTO":{}},
    {"ACTION":{"lparen":"S54"}, "GOTO":{}},
    {"ACTION":{"assign":"S12"}, "GOTO":{}},
    {"ACTION":{"id":"S55"}, "GOTO":{}},
    {"ACTION":{"rbrace":"S56"}, "GOTO":{}},
    {"ACTION":{"id":"S23","literal":"S17","character":"S18","boolstr":"S19","lparen":"S22","num":"S24"}, "GOTO":{"RHS":57,"EXPR":16,"EXPR1":20,"EXPR2":21}},
    {"ACTION":{"rbrace":"R22","return":"R22"}, "GOTO":{}},
    {"ACTION":{"ϵ":"R25","vtype":"R25","id":"R25","if":"R25","while":"R25"}, "GOTO":{}},
    {"ACTION":{"boolstr":"S60"}, "GOTO":{"COND":58,"COND1":59}},
    {"ACTION":{"boolstr":"S60"}, "GOTO":{"COND":61,"COND1":59}},
    {"ACTION":{"ϵ":"S39","comma":"S38"}, "GOTO":{"MOREARGS":62}},
    {"ACTION":{"ϵ":"R17","vtype":"R17"}, "GOTO":{}},
    {"ACTION":{"semi":"S63"}, "GOTO":{}},
    {"ACTION":{"rparen":"S64"}, "GOTO":{}},
    {"ACTION":{"comp":"S65"}, "GOTO":{}},
    {"ACTION":{"comp":"R29"}, "GOTO":{}},
    {"ACTION":{"rparen":"S66"}, "GOTO":{}},
    {"ACTION":{"rparen":"R20"}, "GOTO":{}},
    {"ACTION":{"rbrace":"R32"}, "GOTO":{}},
    {"ACTION":{"lbrace":"S67"}, "GOTO":{}},
    {"ACTION":{"boolstr":"S60"}, "GOTO":{"COND":68,"COND1":59}},
    {"ACTION":{"lbrace":"S69"}, "GOTO":{}},
    {"ACTION":{"ϵ":"S42","vtype":"S2","id":"S47","if":"S45","while":"S46"}, "GOTO":{"VDECL":43,"ASSIGN":44,"BLOCK":70,"STMT":41}},
    {"ACTION":{"rparen":"R28"}, "GOTO":{}},
    {"ACTION":{"ϵ":"S42","vtype":"S2","id":"S47","if":"S45","while":"S46"}, "GOTO":{"VDECL":43,"ASSIGN":44,"BLOCK":71,"STMT":41}},
    {"ACTION":{"rbrace":"S72"}, "GOTO":{}},
    {"ACTION":{"rbrace":"S73"}, "GOTO":{}},
    {"ACTION":{"ϵ":"S76","else":"S75"}, "GOTO":{"ELSE":74}},
    {"ACTION":{"ϵ":"R27","vtype":"R27","id":"R27","if":"R27","while":"R27"}, "GOTO":{}},
    {"ACTION":{"ϵ":"R26","vtype":"R26","id":"R26","if":"R26","while":"R26"}, "GOTO":{}},
    {"ACTION":{"lbrace":"S77"}, "GOTO":{}},
    {"ACTION":{"ϵ":"R31","vtype":"R31","id":"R31","if":"R31","while":"R31"}, "GOTO":{}},
    {"ACTION":{"ϵ":"S42","vtype":"S2","id":"S47","if":"S45","while":"S46"}, "GOTO":{"VDECL":43,"ASSIGN":44,"BLOCK":78,"STMT":41}},
    {"ACTION":{"rbrace":"S79"}, "GOTO":{}},
    {"ACTION":{"ϵ":"R30","vtype":"R30","id":"R30","if":"R30","while":"R30"}, "GOTO":{}}
    ]