from PyQt4.Qt import *
LABELS = (
    {
        'attributes': {
            'class':      'C1',
            # 'type':       'rect',
            # 'comment':    ["Martin", "Mika"]
            'comment':    str
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     'sloth.items.RectItem',
        'hotkey':   '1',
        'text':     'C1',
    },
    {
        'attributes': {
            'class':      'C2',
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     'sloth.items.RectItem',
        'hotkey':   '2',
        'text':     'C2',
    },
    {
        'attributes': {
            'class':      'C3',
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     'sloth.items.RectItem',
        'hotkey':   '3',
        'text':     'C3',
    },
    {
        'attributes': {
            'class':      'C4',
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     'sloth.items.RectItem',
        'hotkey':   '4',
        'text':     'C4',
    },
    
)
COLORS = {"C1": QColor(255, 0, 255), "C2": Qt.blue}
