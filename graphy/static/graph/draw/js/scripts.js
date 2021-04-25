// create global vars and event listeners
let dataFetchBtn = document.getElementById('get-data-btn');
dataFetchBtn.addEventListener("click", dataFetcher);

let equationForm = document.getElementById('equation');
equationForm.addEventListener("keypress", dataFetcher);



function dataHandler(data){
    let dataDisplay = document.getElementById('data-display');
    
    if (dataDisplay.hasChildNodes() == true){
        let childNodes = dataDisplay.childNodes;
        
        for (let i = 0; i < childNodes.length; i++) {

            childNodes[i].style.display = "none";
            
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

function dataFetcher(e) {

    let equation = document.getElementById('equation');
    console.log(e)
    if (equation != null && e.key === 'Enter' || e.type === "click"){
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


