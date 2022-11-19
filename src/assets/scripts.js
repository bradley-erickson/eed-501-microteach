if (!window.dash_clientside) {
    window.dash_clientside = {};
}

window.dash_clientside.clientside = {

    change_pages: function(prev, next, hash) {
        const order = ['home', 'overview', 'while', 'for', 'do-while'];
        if (dash_clientside.callback_context.triggered.length > 0) {
            const trig = dash_clientside.callback_context.triggered[0].prop_id;
            let current_hash = order.indexOf(hash.replace('#', ''));
            if (current_hash === -1) {current_hash = 0;}
            if (trig.includes('next')) {
                return order[(current_hash+1) % order.length];
            } else if (trig.includes('prev')) {
                return order[(current_hash-1) % order.length];
            }
        }
        return window.dash_clientside.no_update;
    }
}