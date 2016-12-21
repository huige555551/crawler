
        // 闭包实现私有
        //var c = function c(){}; 前c为对象
        function c(){
            // var private = 1;
            var pri = function(){
                return private;
            };
            this.private = 1;
            return {
                usepri : "hi",
                p : function(){
                    private++;
                    },
                s : function(){
                    return private;
                },
                change:function(){
                    // usepri +="hi";
                    this.usepri +="hi";
                }
                };
        };
        var t = c();// 相当于var t = new c();
        t.s();
        var m = c();
        t.p();
        t.change();
        console.log(m.s());
