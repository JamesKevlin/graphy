var equationLookup = new Vue({
    el: '#equation-input',
    methods: {
        lookup : function(){
            let url = equation.getAttribute('name-space');
            let equationString = {"equation" : equation.value};
            fetch(url, {
                    method : 'POST',
                    cache: 'no-cache',
                    body : JSON.stringify(equationString),
                    headers: {
                        'Content-Type': 'application/json'
                    }
                })
                .then(response => response.json())
                .then(data => graph.draw(data))

                
                // .then(data => dataHandler(data));
        }
    }
})

var graph =  new Vue({
    el: '#graph',
    methods: {
        draw : function(data){
            let context = this.$el.getContext("2d");
            context.clearRect(0, 0, this.$el.width, this.$el.height);
            // context.rotate(360 * Math.PI / 180);

            

            if (data.data != null){
                let points = data.data;
                
                points.forEach(point => {
                    setTimeout(this.plot(point), 2000);
                });

            }

        },
        plot : function(point){
            let context = this.$el.getContext("2d");
            
            let size = 400;
            let scale = window.devicePixelRatio;
            context.width = size * scale;
            context.height = size * scale;
            context.scale(scale,scale);
            context.fillRect(point[0],point[1],5,5);
        }
    }
})

let canvas = document.getElementById('graph');
canvas.getContext("2d").rotate(360 * Math.PI / 180);
  