if (!window.dash_clientside) {
    window.dash_clientside = {};
}

window.dash_clientside.clientside = {

    change_pages: function(prev, next, home, what, types, examples, end, hash) {
        const order = ['home', 'section-1', 'overview', 'activity-1', 'section-2', 'types', 'while', 'for', 'section-3', 'while-examples', 'for-examples', 'activity-2', 'end'];
        if (dash_clientside.callback_context.triggered.length > 0) {
            const trig = dash_clientside.callback_context.triggered[0].prop_id;
            let current_hash = order.indexOf(hash.replace('#', ''));
            if (current_hash === -1) {current_hash = 0;}
            if (trig.includes('next')) {
                return order[(current_hash+1) % order.length];
            } else if (trig.includes('prev')) {
                return order[(current_hash-1) % order.length];
            } else if (trig.includes('home')) {
                return 'home';
            } else if (trig.includes('what-is')) {
                return 'section-1';
            } else if (trig.includes('types')) {
                return 'section-2';
            } else if (trig.includes('examples')) {
                return 'section-3';
            } else if (trig.includes('end')) {
                return 'end';
            }
        }
        return window.dash_clientside.no_update;
    },

    update_icons: function(hash) {
        const current_hash = hash.replace('#', '');
        const s1 = ['section-1', 'overview', 'activity-1'];
        const s2 = ['section-2', 'types', 'while', 'for'];
        const s3 = ['section-3', 'while-examples', 'for-examples', 'activity-2'];
        let output = Array(5).fill('far fa-circle')
        if (current_hash === 'home') {
            output[0] = 'fas fa-circle';
        } else if (current_hash === 'end') {
            output[4] = 'fas fa-circle';
        } else if (s1.includes(current_hash)) {
            output[1] = 'fas fa-circle';
        } else if (s2.includes(current_hash)) {
            output[2] = 'fas fa-circle';
        } else if (s3.includes(current_hash)) {
            output[3] = 'fas fa-circle';
        }
        return output;
    }
}