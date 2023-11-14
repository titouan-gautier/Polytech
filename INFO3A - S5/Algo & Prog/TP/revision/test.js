
'use strict';
(() => {
    const tree =
    ['+',
        ['×', [3], [2]],
        [1],
    ];
    const treeSize = tree => tree ? 1 + treeSize(tree[1]) + treeSize(tree[2]) : 0;
    function* walk(tree) {
        //const style = () => ({style: 'fill: red'});
        const style = () => ({});
        function* rec_walk(tree) {
            if (!tree) {
                return;
            }
            yield tree;
            for (const node of rec_walk(tree[1])) {
                yield node;
            }
            for (const node of rec_walk(tree[2])) {
                yield node;
            }
        }
        yield {tree, visited: [...rec_walk(tree)].map(([value]) => value), style: () => ({})};
        for (;;) {
            const visited = [];
            yield {tree, visited, style};
            for (const node of rec_walk(tree)) {
                visited.push(node[0]);
                yield {tree, visited, style: (aNode) => (aNode === node && {style: 'fill: red'})};
            }
        }
    }

    function stateToJSONML({tree, visited, style}) {
        return ['div', {style: 'display: flex; align-items: center'}, {onclick, onmousedown},
            ['div', {style: 'flex: 1'},
                treeToJSONML(tree, {cellWidth: 50, margin: 40, style}),
            ],
            ['svg.figure', {xmlns: 'http://www.w3.org/2000/svg'},
                {width: (50 + 40) * treeSize(tree), height: 60},
                {style: 'flex: 1; stroke: currentcolor; stroke-width: 2; fill: none; font-size: 80%'},
                    ...visited.flatMap((v, i) => [
                        ['circle', {cx: 30 + (50 + 40) * i, cy: 30, r: 25}],
                        ['text', {x: 30 + (50 + 40) * i, y: 30}, v],
                    ]),
            ],
        ];
    }

    const state = walk(tree);
    let where = stateToJSONML(state.next().value).toDOM();
    function onclick() {
        where = resyncDOM(stateToJSONML(state.next(event).value), where);
    }
    function onmousedown(event) {
        // Prevent selection of surrounding text when double-clicking
        event.preventDefault();
        return false;
    }
})();
