# /!\ fragile: require an update each time a new question is added
# TODO: automate with a script
TP_STRUCTURE = {'tp3': ['e1q1', 'e1q2',
                        'e2q1',
                        'e3q1', 'e3q2',
                        'e4q1', 'e4q2', 'e4q3', 'e4q4',
                        'e5q1', 'e5q2', 'e5q3', 'e5q4', 'e5q5', 'e5q6', 'e5q7',
                        'e6q1', 'e6q2', 'e6q3',
                        'e7q1',
                        'e8q1',
                        'e9q1', 'e9q2',
                        'e11q1',
                        'e12q1',
                        'e13q1',
                        'e14q1', 'e14q2', 'e14q3',
                        'e15q1', 'e15q2', 'e15q3', 'e15q4', 'e15q5', 'e15q6',
                        'e16q1',
                        'e17q1',
                        ],
                'tp4': ['e1q1', 'e1q2', 'e1q3',
                        'e2q1', 'e2q2', 'e2q3', 'e2q4', 'e2q5', 'e2q6',
                        'e3q1', 'e3q2', 'e3q3', 'e3q4', 'e3q5',
                        'e4q1', 'e4q2',
                        'e5q1',
                        'e6q1',
                        'e7q1', 'e7q2', 'e7q3',
                        'e8q1', 'e8q2', 'e8q3',
                        'e9q1', 'e9q2',
                        'e10q1', 'e10q2',
                        'e11q1', 'e11q2', 'e11q3']

                }

TP_CLASS = {
    'arraylist': {
        'module': 'tp3.arraylist',
        'class': 'ArrayList',
        'test_dataclass': 'tp3/test_arraylist_dataclass.py',
        'test_class': 'tp3/test_arraylist_class.py',
    },
    'stack': {
        'module': 'tp3.stack',
        'class': 'Stack',
        'test_dataclass': 'tp3/test_stack_dataclass.py',
        'test_class': 'tp3/test_stack_class.py',
    },
    'queue': {
        'module': 'tp3.queue_',
        'class': 'Queue',
        'test_dataclass': 'tp3/test_queue_dataclass.py',
        'test_class': 'tp3/test_queue_class.py',
    },
    'llist': {
        'module': 'tp4.llist',
        'class': 'LinkedList',
        'test_dataclass': 'tp4/test_llist_dataclass.py',
        'test_class': 'tp4/test_llist_class.py',
    },
    'deque': {
        'module': 'tp4.deque',
        'class': 'Deque',
        'test_dataclass': 'tp4/test_deque_dataclass.py',
        'test_class': 'tp4/test_deque_class.py',
    },
    'stack_deque': {
        'module': 'tp4.stack',
        'class': 'Stack',
        'test_dataclass': 'tp4/test_stack_dataclass.py',
        'test_class': 'tp4/test_stack_class.py',
    },
    'queue_deque': {
        'module': 'tp4.queue_',
        'class': 'Queue',
        'test_dataclass': 'tp4/test_queue_dataclass.py',
        'test_class': 'tp4/test_queue_class.py',
    },
}

LINKEDLIST_STRUCT_NAMES = ['LinkedList', 'Cell']
LINKEDLIST_FUNCTION_NAMES = ['ll_new', 'll_is_empty',
                             'll_len', 'll_get', 'll_set', 'll_insert', 'll_remove', 'll_append', 'll_prepend',
                             'll_head', 'll_tail', 'll_iter_cells', 'll_reversed_iter_cells',
                             'll_str', 'll_lookup', 'll_cell_at',
                             'll_extend']
LINKEDLIST_NAMES = LINKEDLIST_STRUCT_NAMES + LINKEDLIST_FUNCTION_NAMES

DEQUE_STRUCT_NAMES = ['Deque']
DEQUE_FUNCTION_NAMES = ['d_new', 'd_is_empty','d_len', 'd_str', 'd_front', 'd_rear', 'd_push_front', 'd_push_rear',
                        'd_pop_front', 'd_pop_rear']
DEQUE_NAMES = DEQUE_STRUCT_NAMES + DEQUE_FUNCTION_NAMES

STACK_STRUCT_NAMES = ['Stack']
STACK_FUNCTION_NAMES = ['s_new', 's_is_empty', 's_size', 's_len', 's_str', 's_top', 's_push', 's_pop']
STACK_NAMES = STACK_STRUCT_NAMES + STACK_FUNCTION_NAMES

QUEUE_STRUCT_NAMES = ['Queue']
QUEUE_FUNCTION_NAMES = ['q_new', 'q_is_empty', 'q_size', 'q_is_full', 'q_str', 'q_front', 'q_rear', 'q_enqueue', 'q_dequeue']
QUEUE_NAMES = QUEUE_STRUCT_NAMES + QUEUE_FUNCTION_NAMES
