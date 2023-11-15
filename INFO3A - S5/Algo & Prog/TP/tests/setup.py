# /!\ fragile: require an update each time a new question is added
# TODO: automate with a script
TP_QUESTIONS = {'tp3': ['e1q1', 'e1q2',
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
                        'e11q1', 'e11q2', 'e11q3'],
                'tp5': ['e1q1', 'e1q2', 'e1q3', 'e1q4', 'e1q5',
                        'e2q1', 'e2q2',
                        'e3q1', 'e3q2', 'e3q3', 'e3q4',
                        'e4q1',
                        'e5q1', 'e5q2', 'e5q3',
                        'e6q1', 'e6q2', 'e6q3',
                        'e7q1', 'e7q2', 'e7q3', 'e7q4',
                        'e8q1', 'e8q2', 'e8q3',
                        'e9q1',
                        'e10q1', 'e10q2', 'e10q3', 'e10q4'],
                'tp6': ['e1q1', 'e1q2', 'e2q1', 'e2q2', 'e2q3', 'e3q1', 'e4q1', 'e4q2',
                        'e5q1', 'e6q1', 'e7q1', 'e8q1', 'e8q2',
                        'e8q3', 'e8q4', 'e8q5', 'e9q1']
                }

TP_DATA_STRUCTURES = {
    'arraylist': {
        'module': 'tp3.arraylist',
        'test_dataclass': 'tp3/test_arraylist_dataclass.py',
        'test_class': 'tp3/test_arraylist_class.py',
        'classnames': ['ArrayList'],
        'funcnames': [],
    },
    'stack': {
        'module': 'tp3.stack',
        'test_dataclass': 'tp3/test_stack_dataclass.py',
        'test_class': 'tp3/test_stack_class.py',
        'classnames': ['Stack'],
        'funcnames': ['s_new', 's_is_empty', 's_size', 's_len', 's_str', 's_top', 's_push', 's_pop']
    },
    'queue': {
        'module': 'tp3.queue_',
        'test_dataclass': 'tp3/test_queue_dataclass.py',
        'test_class': 'tp3/test_queue_class.py',
        'classnames': ['Queue'],
        'funcnames': ['q_new', 'q_is_empty', 'q_size', 'q_is_full', 'q_str', 'q_front', 'q_rear', 'q_enqueue', 'q_dequeue']
    },
    'llist': {
        'module': 'tp4.llist',
        'test_dataclass': 'tp4/test_llist_dataclass.py',
        'test_class': 'tp4/test_llist_class.py',
        'classnames': ['LinkedList', 'Cell'],
        'funcnames': ['ll_new', 'll_is_empty',
                             'll_len', 'll_get', 'll_set', 'll_insert', 'll_remove', 'll_append', 'll_prepend',
                             'll_head', 'll_tail', 'll_iter_cells', 'll_reversed_iter_cells',
                             'll_str', 'll_lookup', 'll_cell_at',
                             'll_extend']
    },
    'deque': {
        'module': 'tp4.deque',
        'test_dataclass': 'tp4/test_deque_dataclass.py',
        'test_class': 'tp4/test_deque_class.py',
        'classnames': ['Deque'],
        'funcnames': ['d_new', 'd_is_empty','d_len', 'd_str', 'd_front', 'd_rear', 'd_push_front', 'd_push_rear',
                        'd_pop_front', 'd_pop_rear']
    },
    'stack_deque': {
        'module': 'tp4.stack',
        'test_dataclass': 'tp4/test_stack_dataclass.py',
        'test_class': 'tp4/test_stack_class.py',
        'classnames': ['Stack'],
        'funcnames': ['s_new', 's_is_empty', 's_size', 's_len', 's_str', 's_top', 's_push', 's_pop']
    },
    'queue_deque': {
        'module': 'tp4.queue_',
        'test_dataclass': 'tp4/test_queue_dataclass.py',
        'test_class': 'tp4/test_queue_class.py',
        'classnames': ['Queue'],
        'funcnames': ['q_new', 'q_is_empty', 'q_size', 'q_is_full', 'q_str', 'q_front', 'q_rear', 'q_enqueue', 'q_dequeue']
    },
    'btree': {
        'module': 'tp5.btree',
        'test_dataclass': 'tp5/test_btree_dataclass.py',
        'test_class': 'tp5/test_btree_class.py',
        'classnames': ['BinaryTree', 'Node'],
        'funcnames': ['bt_new', 'bt_root', 'bt_is_empty', 'bt_size', 'bt_height', 'bt_str',
                      'bt_is_equal','bt_is_heap', 'bt_lca',
                      'n_new', 'n_set', 'n_get', 'n_left', 'n_right', 'n_is_leaf']
    },
    'bstree': {
        'module': 'tp5.bstree',
        'test_dataclass': 'tp5/test_bstree_dataclass.py',
        'test_class': 'tp5/test_bstree_class.py',
        'classnames': ['BSTree'],
        'funcnames': ['bt_is_bst', 'bst_lookup', 'bst_insert', 'bst_remove', 'bst_to_list']
    },
    'hashmap': {
        'module': 'tp6.hashmap',
        'test_dataclass': 'tp6/test_hashmap_dataclass.py',
        'test_class': 'tp6/test_hashmap_class.py',
        'classnames': ['HashMap', 'Item'],
        'funcnames': ['hm_new', 'hm_is_empty', 'hm_size', 'hm_str', 'hm_get', 'hm_put', 'hm_delete']
    },
    'hashset': {
        'module': 'tp6.hashset',
        'test_dataclass': 'tp6/test_hashset_dataclass.py',
        'test_class': 'tp6/test_hashset_class.py',
        'classnames': ['HashSet'],
        'funcnames': ['hs_new', 'hs_is_empty', 'hs_size', 'hs_member', 'hs_iterate', 'hs_insert',
                      'hs_delete', 'hs_union', 'hs_intersection', 'hs_difference']
    },
    'bloomfilter': {
        'module': 'tp6.bloomfilter',
        'test_dataclass': 'tp6/test_bloomfilter_dataclass.py',
        'test_class': 'tp6/test_bloomfilter_class.py',
        'classnames': ['BloomFilter'],
        'funcnames': ['bf_new', 'bf_insert', 'bf_lookup']
    },
    'unionfind': {
        'module': 'tp6.unionfind',
        'test_dataclass': 'tp6/test_unionfind_dataclass.py',
        'test_class': 'tp6/test_unionfind_class.py',
        'classnames': ['UnionFind'],
        'funcnames': ['uf_new', 'uf_size', 'uf_find', 'uf_union']
    },
}