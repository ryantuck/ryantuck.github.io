// TODO - make face object cleaner to work with and update
// TODO - use lodash more

var randomItem = function (inputArray) {
  return inputArray[Math.floor(Math.random() * inputArray.length)];
}

var width = 200;
var height = 200;

var faceRadius = width / 4;

var faceCenterX = width / 2;
var faceCenterY = height / 2;

var eyeRadius = faceRadius / 4;
var eyeHeight = height / 2 - faceRadius / 4;
var eyePd = faceRadius;
var pupilRadius = eyeRadius / 4;

var eyeNoise = width / 15;

var bgColors = ['#111', '#333', '#555', '#777', '#999', '#aaa', '#ccc'];
var faceColors = ['hotpink', '#0f0', 'cyan', 'magenta', 'yellow', 'red', 'blue'];
var smileAngles = [1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8];

bgColor = randomItem(bgColors);
faceColor = randomItem(faceColors);
smileAngle = randomItem(smileAngles);


console.log(faceRadius);
console.log(eyeRadius);
console.log('erx2 ' + eyeRadius * 2);
console.log(eyeHeight);
console.log(eyePd);


// main svg div
var svg = d3.select("#ball")
  .append("svg")
  .attr("width", width)
  .attr("height", height)
  .on('mousemove', function () {
    var rightRadius = d3.mouse(this)[0] / width * eyeRadius;
    d3.select('#rightEye').attr('r', rightRadius);
    var leftRadius = d3.mouse(this)[1] / height * eyeRadius;
    d3.select('#leftEye').attr('r', leftRadius);
  })
  .on('click', function () {
    console.log('clicked');
    d3.select('#personBackground').attr('fill', randomItem(bgColors));
    d3.select('#smile').attr('d', smileArc(randomItem(smileAngles)));
    d3.select('#personFace').attr('fill', randomItem(faceColors));
    rightEyeCenter = rightEyeCoords();
    leftEyeCenter = leftEyeCoords();
    d3.select('#rightEye')
      .attr('cx', rightEyeCenter.cx)
      .attr('cy', rightEyeCenter.cy)
      ;
    d3.select('#rightPupil')
      .attr('cx', rightEyeCenter.cx)
      .attr('cy', rightEyeCenter.cy)
      ;
    d3.select('#leftEye')
      .attr('cx', leftEyeCenter.cx)
      .attr('cy', leftEyeCenter.cy)
      ;
    d3.select('#leftPupil')
      .attr('cx', leftEyeCenter.cx)
      .attr('cy', leftEyeCenter.cy)
      ;
  });

// append a full rectangle with a background color
svg.append('rect')
  .attr('id', 'personBackground')
  .attr('width', width)
  .attr('height', height)
  .attr("fill", bgColor);


// face
svg.append('circle')
  .attr('id', 'personFace')
  .attr('cx', faceCenterX)
  .attr('cy', faceCenterY)
  .attr('r', faceRadius)
  .attr('fill', faceColor);

// eyes
var leftEyeCoords = function() {
  return {
    cx: faceCenterX - eyePd/2 + randomItem(_.range(0-eyeNoise, eyeNoise)),
    cy: eyeHeight + randomItem(_.range(0-eyeNoise, eyeNoise)),
  }
}
var rightEyeCoords = function() {
  return {
    cx: faceCenterX + eyePd/2 + randomItem(_.range(0-eyeNoise, eyeNoise)),
    cy: eyeHeight + randomItem(_.range(0-eyeNoise, eyeNoise)),
  }
}
leftCenter = leftEyeCoords();
rightCenter = rightEyeCoords();
svg.append('circle')
  .attr('id', 'leftEye')
  .attr('cx', leftCenter.cx)
  .attr('cy', leftCenter.cy)
  .attr('r', eyeRadius)
  .attr('fill', 'white');

svg.append('circle')
  .attr('id', 'leftPupil')
  .attr('cx',  leftCenter.cx)
  .attr('cy', leftCenter.cy)
  .attr('r', pupilRadius)
  .attr('fill', 'black');

svg.append('circle')
  .attr('id', 'rightEye')
  .attr('cx',  rightCenter.cx)
  .attr('cy', rightCenter.cy)
  .attr('r', eyeRadius)
  .attr('fill', 'white');

svg.append('circle')
  .attr('id', 'rightPupil')
  .attr('cx',  rightCenter.cx)
  .attr('cy', rightCenter.cy)
  .attr('r', eyeRadius / 4)
  .attr('fill', 'black');

var smileArc = function (rads) {
  return d3.arc()  // starts at North, deg in rads
    .innerRadius(0.8 * faceRadius)
    .outerRadius(0.80 * faceRadius + 5)
    .startAngle(rads)
    .endAngle(Math.PI * 2 - rads);
}

svg.append("path")
  .attr('id', 'smile')
  .attr('transform', 'translate(' + faceCenterX + ',' + faceCenterY + ')')
  .attr("class", "arc")
  .attr("d", smileArc(smileAngle))
  .attr("fill", "black");
