# -*- coding: utf-8 -*-
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
        'item':     'sloth.items.MyRectItem',
        'hotkey':   '1',
        'text':     'C1',
    },
    {
        'attributes': {
            'class':      'C2',
            # 'id'   :      int,
            # 'comment':    str
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

'''
设置类颜色和画刷样式,若是给出颜色,必须给出画刷样式：0,默认无画刷
0=Qt.NoBrush
12=Qt.BDiagPattern
13=Qt.FDiagPattern
'''
COLORS = {"C1": (QColor(255, 0, 255), 12), "C2": (Qt.blue, 0), "C3": (QColor(0xCD, 0x37, 0x00), 0)}
