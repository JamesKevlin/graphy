// create global vars and event listeners
// let dataFetchBtn = document.getElementById('get-data-btn');
// dataFetchBtn.addEventListener("click", dataFetcher);

// let equationForm = document.getElementById('equation');
// equationForm.addEventListener("keypress", dataFetcher);



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
        let temp = document.createElement('li');
        
        temp.innerText = '(' + point[0] + '  ,  ' + point[1] + ')';
        dataDisplay.appendChild(temp);
    });

    
}

