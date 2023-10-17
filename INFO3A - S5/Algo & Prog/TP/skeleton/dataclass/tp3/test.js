
'use strict';

(() => {
    function* quickSort(tab) {
        tab = tab.slice();
        yield {tab};
        for (const state of quickSortRec(tab, 0, tab.length - 1)) {
            yield state;
        }
        yield {tab, f: tab.length}; // f marks the ordered part of tab
        function* quickSortRec(tab, f, t) {
            yield {tab, f, t, h: [[f, t]]};
            if (f < t) {
                const pivot = tab[f];
                let [i, j] = [f, t];
                yield {tab, f, t, i, j, pivot, h: [[f, t]]};
                while (i < j) {
                    while (tab[i] < pivot) {
                        i += 1;
                        yield {tab, f, t, i, j, pivot, h: [[f, t]]};
                    }
                    while (tab[j] > pivot) {
                        j -= 1;
                        yield {tab, f, t, i, j, pivot, h: [[f, t]]};
                    }
                    if (i < j) {
                        [tab[i], tab[j]] = [tab[j], tab[i]];
                        //i += 1;
                        //j -= 1;
                        yield {tab, f, t, i, j, pivot, h: [[f, t]]};
                    }
                }
                [tab[i], tab[j]] = [tab[j], tab[i]];
                yield {tab, f, t, i, j, h: [[f, t]]};
                for (const state of quickSortRec(tab, f, j)) {
                    yield {...state, h: [[f, t], ...state.h]};
                }
                for (const state of quickSortRec(tab, j + 1, t)) {
                    yield {...state, h: [[f, t], ...state.h]};
                }
            }
        }
    }
    function* algo(n) {
        for (;;) {
            const tab = sample([...range(10)], 10);
            for (const state of quickSort(tab)) {
                const action = yield state;
                if (action === 'shuffle') {
                    break;
                }
            }
        }
    }
    function sample(tab, n) {
        const res = [];
        for (; n > 0 && tab.length; n--) {
            res.push(tab.splice(Math.random() * tab.length | 0, 1)[0]);
        }
        return res;
    }
    function stateToJSONML({tab, i, j, f, t, h, pivot}) {
        console.log(h);
        const dict1 = {[f]: 'f', [t]: 't'};
        const dict2 = {[i]: 'i', [j]: 'j'};
        return ['table', {onmousedown, onclick: (event) => execute(event, 'step')},
            ['tr.small', ['th', ' '], h !== undefined && ['td', {colspan: tab.length}, h.map(([a, b]) => `${a}→${b}`).join()]],
            ['tr.square',
                ['th', 't'],
                ...[...tab].map((v, ii) => ['td',
                    {style: `${ii >= f && ii <= t ? 'background-color: grey;' : ''}`},
                    f === undefined ? {} : ii < f ? {class: 'ordered'} : {class: 'unordered'},
                    v,
                ]),
                ['th', {onclick: (event) => execute(event, 'shuffle')}, '🔀'],
            ],
            ['tr.small', ['th', ' '], ...[...tab].map((_, ii) => ['td', dict1[ii]])],
            ['tr.small', ['th', ' '], ...[...tab].map((_, ii) => ['td', dict2[ii]])],
            ['tr.small', ['th', ' '], pivot !== undefined && ['td', {colspan: tab.length}, `pivot : ${pivot}`]],
        ];
    }
    function onmousedown(event) {
        // Prevent selection of surrounding text when double-clicking
        event.preventDefault();
        return false;
    }
    const state = algo();
    let where;
    where = stateToJSONML(state.next().value).toDOM();
    function execute(event, action) {
        event.stopPropagation();
        try {
            const jsonml = stateToJSONML(state.next(action).value);
            where = resyncDOM(jsonml, where);
        }
        catch (e) {
            console.error(e.message);
        }
    }
})();
