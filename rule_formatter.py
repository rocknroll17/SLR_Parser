#This code is used to convert the rules of the syntax analyzer to the python code format.
rule = [
    ["CODE", "VDECL CODE"],
    ["CODE", "FDECL CODE"],
    ["CODE", "ϵ"],
    ["VDECL", "vtype id semi"],
    ["VDECL", "vtype ASSIGN semi"],
    ["ASSIGN", "id assign RHS"],
    ["RHS", "EXPR"],
    ["RHS", "literal"],
    ["RHS", "character"],
    ["RHS", "boolstr"],
    ["EXPR", "EXPR1 addsub EXPR"],
    ["EXPR", "EXPR1"],
    ["EXPR1", "EXPR2 multdiv EXPR1"],
    ["EXPR1", "EXPR2"],
    ["EXPR2", "lparen EXPR rparen"],
    ["EXPR2", "id"],
    ["EXPR2", "num"],
    ["FDECL", "vtype id lparen ARG rparen lbrace BLOCK RETURN rbrace"],
    ["ARG", "vtype id MOREARGS"],
    ["ARG", "ϵ"],
    ["MOREARGS", "comma vtype id MOREARGS"],
    ["MOREARGS", "ϵ"],
    ["BLOCK", "STMT BLOCK"],
    ["BLOCK", "ϵ"],
    ["STMT", "VDECL"],
    ["STMT", "ASSIGN semi"],
    ["STMT", "if lparen COND rparen lbrace BLOCK rbrace ELSE"],
    ["STMT", "while lparen COND rparen lbrace BLOCK rbrace"],
    ["COND", "COND1 comp COND"],
    ["COND1", "boolstr"],
    ["ELSE", "else lbrace BLOCK rbrace"],
    ["ELSE", "ϵ"],
    ["RETURN", "return RHS semi"]

]

formatted_rules = []
for left, right in rule:
    right_str = f'["{left}", {right.split(" ")}]'
    formatted_rules.append(right_str)


#Make rules to python format codes
final_output = '[' + ',\n'.join(formatted_rules) + ']'
print(final_output)