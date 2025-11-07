roundsInput = document.getElementById('rounds');
roundsInput.addEventListener('input', () => {
    // input = 2, take divs[6:]
    // input = 5, take divs[3:]
    // input = 8, take divs[0:]
    // nth-child display none
    //
    var bracketDiv = document.getElementById('bracket');
    var roundElements = bracketDiv.querySelectorAll(":scope > div");
    var startingIdx = 8 - roundsInput.value;

    console.log(roundElements);

    for (var i = 0; i < roundElements.length; i++) {

        if (i < startingIdx) {
            roundElements[i].classList.remove("b");
            roundElements[i].classList.add("c");
            roundElements[i].style.display = "none";

        }
        else {

            roundElements[i].classList.remove("c");
            roundElements[i].classList.add("b");
            roundElements[i].style.display = "flex";
            roundElements[i].style.setProperty('flex-basis', 1);
            //roundElements[i].style.minWidth = '130px';

            if (i == startingIdx) {
                //roundElements[i].style.minWidth = '200px';
            }

            var nCols = 8 - startingIdx;
            var relIdx = i-startingIdx;
            // var fontVar = (1.4 - (7-i)*0.7/(nCols)); // nice :)

            var fontSizes = [1, 1.1, 1.2, 1.3, 1.4, 1.4, 1.4, 1.4];
            var fontVar = fontSizes[relIdx];

            roundElements[i].style.fontSize = fontVar.toString() + 'rem';


            // i == startingIdx 8vh
            // i = startingIdx+1 16vh
            // 2^(3+i-startingIdx)
            //const h = (5 + startingIdx*2) * Math.pow(2,relIdx);
            // height doubles with relIdx, add scale based on startingIdx
            //const h = (16 + startingIdx*6) * Math.pow(2,relIdx);
            const h = 16 * Math.pow(2,relIdx);


            // console.log(h);
            // console.log(h.toString()+'vh');
            // console.log(fontVar);
            // console.log(roundElements[i]);
            // console.log(subdivs);

            const subdivs = roundElements[i].querySelectorAll('div');
            subdivs.forEach(d => d.style.height = h.toString()+'vh');
            subdivs[0].style.height = (4 + h/2).toString()+ 'vh';

            subdivs.forEach(d => d.style.fontSize = fontVar.toString() + 'em');

        }
    }
    document.getElementById('nRounds').innerText = Math.pow(2, roundsInput.value-1);
});
