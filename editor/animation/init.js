//Dont change it
//Dont change it
requirejs(['ext_editor_io', 'jquery_190'],
    function (extIO, $) {
        
        var $tryit;

        var io = new extIO({
            multipleArguments: true,
            functions: {
                python: 'sum_light',
                js: 'sumLight'
            }
        });
        io.parseInputArguments = function(data) {
            var fname = '';
            if (this.getLanguage() == "python") {
                fname = 'datetime';
            } else {
                fname = 'new Date';
            }
            var els = data[0];
            els = els.map(function(ee) {
                if (ee.length === 2) {
                    return '[' + fname + '(' + ee[0].join(', ') + '), ' + ee[1] + ']'
                } else {
                    return fname + '(' + ee.join(', ') + ')'    
                }
                
            })

            var start_watching = '';
            var end_watching = '';
            if (data.length > 1) {
                start_watching = ',\n' + fname + '(' + data[1].join(', ') +')';
            }
            if (data.length > 2) {
                end_watching = ',\n' + fname + '(' + data[2].join(', ') +')';
            }

            return '[\n' + els.join(',\n') + '\n]' + start_watching + end_watching;
        }
        io.start();
    }
);
