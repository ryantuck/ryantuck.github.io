roundsInput = document.getElementById('rounds');
roundsInput.addEventListener('input', () => {
    // input = 2, take divs[6:]
    // input = 5, take divs[3:]
    // input = 8, take divs[0:]
    // nth-child display none
    var bracketDiv = document.getElementById('bracket');
    var roundElements = bracketDiv.querySelectorAll(":scope > div");
    console.log(roundElements);
    var startingIdx = 8 - roundsInput.value;
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
            const fontVar = (1 + 0.1 * (i));
            console.log(fontVar);
            roundElements[i].style.fontSize = fontVar.toString() + 'em';


            // i == startingIdx 8vh
            // i = startingIdx+1 16vh
            // 2^(3+i-startingIdx)
            var relIdx = i-startingIdx;
            // const h = Math.pow(2,4+relIdx);
            const h = (16 + startingIdx*2) * Math.pow(2,relIdx);
            console.log(h);
            console.log(h.toString()+'vh');
            console.log(roundElements[i]);
            const subdivs = roundElements[i].querySelectorAll('div');
            console.log(subdivs);
            subdivs.forEach(d => d.style.height = h.toString()+'vh');
            subdivs[0].style.height = (4 + h/2).toString()+ 'vh';

            subdivs.forEach(d => d.style.fontSize = fontVar.toString() + 'em');

        }
    }
    // rangeValueDisplay.textContent = rangeInput.value;
});
