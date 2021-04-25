// create global vars and event listeners
let dataFetchBtn = document.getElementById('get-data-btn');
dataFetchBtn.addEventListener("click", dataFetcher);

function dataHandler(data){
    let dataDisplay = document.getElementById('data-display');
    
    if (dataDisplay.hasChildNodes == true){
        let childNodes = dataDisplay.children

        for (let child in childNodes) {
            child.display = None
        }
    }
    
    let points = data.data;
    let header = document.createElement('li');
    header.innerText = 'X  |  Y'


    points.forEach(point => {
        let temp = document.createElement('li')
        
        temp.innerText = point[0] + '   ' + point[1]
        dataDisplay.appendChild(temp);
    });

    
}

function dataFetcher() {

    let equation = document.getElementById('equation');

    if (equation != null){
        let url = equation.getAttribute('name-space');
        let equationString = {"equation" : equation.value}


        fetch(url, {
            method : 'POST',
            cache: 'no-cache',
            body : JSON.stringify(equationString),
            headers: {
                'Content-Type': 'application/json'
            }

            
            })
            .then(response => response.json())
            .then(data => dataHandler(data));
            
    }


}


