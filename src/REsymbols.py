symbols = {
    "union": "∨",
    "intersect": "∧",
    "-" : "-",
    "select_" : "σ",
    "project_" : "π",
    "X": "⨯",
    "join_": "⨝",
    "join": "⨝",
    "*": "⨝"
}

setOpSymbols = {
    "∨",
    "∧",
    "-"
}

joinOpSymbols = {
    "⨝",
    "⨯"
}

singleOpSymbols = {
    "σ",
    "π"
}

allRelationSymbols = setOpSymbols | joinOpSymbols | singleOpSymbols

booleanSymbols = {
    "≤",
    "≥",
    "≠",
    ">",
    "<",
    "="
}

booleanSymbolMap = {
    "<=" : "≤",
    ">=" : "≥",
    "!=" : "≠",
    "==" : "="    
}