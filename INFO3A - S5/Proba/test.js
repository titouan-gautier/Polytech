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