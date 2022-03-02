// ---------------------------------------------
// Refactor
// - Support relative placement and movement.
// - Is one div per scene the right approach?
// - A face could contain an entities list similar to 
//    how a scene does it.
// - All config values should be relative

// Notes
// - draw() defines the DOM element and its 
//    immutable characteristics, whereas update()
//    grabs the element and updates its variable attributes.
// ---------------------------------------------
var randomItem = function (inputArray) {
  return inputArray[Math.floor(Math.random() * inputArray.length)];
}

var noise = function (minVal, maxVal) {
  return randomItem(_.range(minVal, maxVal));
}

// ----------------------------------------------
// Objects
// ----------------------------------------------

var Point = function (x, y) {
  return { x: x, y: y }
};

var Scene = function (id, width, height, bgColor) {

  this.id = id;
  this.width = width;
  this.height = height;
  this.bgColor = bgColor;
  this.entities = [];

  this.centerPoint = function () {
    return Point(this.width / 2, this.height / 2);
  };

  this.addEntity = function (entity, entityCenterPoint) {
    this.entities.push({ entity: entity, centerPoint: entityCenterPoint });
  };

  this.draw = function () {
    var svg = d3.select('#' + this.id)
      .append("svg")
      .attr("width", this.width)
      .attr("height", this.height);

    svg.append('rect')
      .attr('id', this.id + 'Background')
      .attr('width', this.width)
      .attr('height', this.height);

    this.update();

    for (var i = 0; i < this.entities.length; i++) {
      var entityEntry = this.entities[i];
      entityEntry.entity.draw(svg, entityEntry.centerPoint);
    }
  };

  this.updateBackground = function() {
    d3.select('#' + this.id + 'Background')
      .attr('fill', this.bgColor);
  }

  this.update = function () {

    this.updateBackground();

    for (var i = 0; i < this.entities.length; i++) {
      var entityEntry = this.entities[i];
      entityEntry.entity.update();
    }
  };
};

var Eye = function (id, radius, pupilRadius) {

  this.id = id;
  this.radius = radius;
  this.pupilRadius = pupilRadius;

  this.draw = function (svg, centerPoint) {
    svg.append('circle')
      .attr('id', this.id)
      .attr('cx', centerPoint.x)
      .attr('cy', centerPoint.y);

    svg.append('circle')
      .attr('id', this.id + 'Pupil')
      .attr('cx', centerPoint.x)
      .attr('cy', centerPoint.y);

    this.update();
  };

  this.updatePupil = function () {
    d3.select('#' + this.id + 'Pupil')
      .attr('r', this.pupilRadius)
      .attr('fill', 'black');
  }

  this.updateEyeball = function () {
    d3.select('#' + this.id)
      .attr('r', this.radius)
      .attr('fill', 'white');
  }

  this.update = function () {
    this.updateEyeball();
    this.updatePupil();
  }
}

var Smile = function (id, rads) {

  this.id = id;
  this.rads = rads;

  this.smileArc = function () {
    return d3.arc()  // starts at North, deg in rads
      .innerRadius(80) // TODO make dynamic
      .outerRadius(85)
      .startAngle(this.rads)
      .endAngle(Math.PI * 2 - this.rads);
  };

  this.draw = function (svg, centerPoint) {
    svg.append("path")
      .attr('id', this.id)
      .attr('transform', 'translate(' + centerPoint.x + ',' + centerPoint.y + ')')
      .attr("class", "arc")
      .attr("fill", "black");

    this.update();
  }

  this.update = function () {
    d3.select('#' + this.id)
      .attr('d', this.smileArc());
  }

};

var Face = function (
  id,
  radius,
  color,
  pd,
  eyeHeight,
  eyeRadius,
  eyeNoise,
  pupilRadius,
) {
  this.id = id;
  this.radius = radius;
  this.color = color;
  this.pd = pd; // %
  this.eyeHeight = eyeHeight; // %
  this.eyeRadius = eyeRadius; // %
  this.eyeNoise = eyeNoise; // % ?
  this.pupilRadius = pupilRadius; // %

  this.leftEye = new Eye(this.id + 'LeftEye', this.eyeRadius, this.pupilRadius);
  this.rightEye = new Eye(this.id + 'RightEye', this.eyeRadius, this.pupilRadius);

  this.smile = new Smile(this.id + 'Smile', 2);

  // TODO abstract these?
  this.leftEyePoint = function (eyesCenterPoint) {
    return new Point(
      eyesCenterPoint.x - this.pd / 2 + noise(0 - this.eyeNoise, this.eyeNoise),
      this.eyeHeight + noise(0 - this.eyeNoise, this.eyeNoise),
    )
  };
  this.rightEyePoint = function (eyesCenterPoint) {
    return new Point(
      eyesCenterPoint.x + this.pd / 2 + noise(0 - this.eyeNoise, this.eyeNoise),
      this.eyeHeight + noise(0 - this.eyeNoise, this.eyeNoise),
    )
  };

  this.drawEyes = function (svg, centerPoint) {

    var eyesCenterPoint = new Point(centerPoint.x, centerPoint.y - eyeHeight);

    this.leftEye.draw(svg, this.leftEyePoint(eyesCenterPoint));
    this.rightEye.draw(svg, this.rightEyePoint(eyesCenterPoint));

  };

  this.drawSmile = function (svg, centerPoint) {
    this.smile.draw(svg, centerPoint);
  };


  this.draw = function (svg, centerPoint) {
    svg.append('circle')
      .attr('id', this.id)
      .attr('cx', centerPoint.x)
      .attr('cy', centerPoint.y);

    this.drawEyes(svg, centerPoint);
    this.drawSmile(svg, centerPoint);

    this.update();
  };

  this.update = function () {
    d3.select('#' + this.id)
      .attr('r', this.radius)
      .attr('fill', this.color);

    this.leftEye.update();
    this.rightEye.update();
    this.smile.update();
  };
}

// -------------------------------------------
// Scene
// -------------------------------------------
var sceneId = 'scene1';
var sceneWidth = 400;
var sceneHeight = 400;

var bgColors = ['#111', '#333', '#555', '#777', '#999', '#aaa', '#ccc'];
var faceColors = ['hotpink', '#0f0', 'cyan', 'magenta', 'yellow', 'red', 'blue'];
var smileAngles = [1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8];

sc = new Scene(
  sceneId,
  sceneWidth,
  sceneHeight,
  bgColor = randomItem(bgColors),
);

let face = new Face(
  id = sceneId + 'Face',
  radius = sceneWidth / 4,
  color = randomItem(faceColors),
  pd = sceneWidth / 4, // 100%
  eyeHeight = sceneHeight * 7 / 16,
  eyeRadius = sceneWidth / 16,
  eyeNoise = 20,
  pupilRadius = sceneWidth / 64,
);
face.smile.rads = randomItem(smileAngles);

sc.addEntity(face, sc.centerPoint());
sc.draw();


// Interactivity!
d3.select('#' + sceneId)
  .on('mousemove', function () {

    // NOTE should this be:
    // face.rightEye.update(radius=...)?
    mouseX = d3.mouse(this)[0];
    mouseY = d3.mouse(this)[1];

    maxEyeRadius = sceneWidth / 16;

    face.rightEye.radius = mouseX / sceneWidth * maxEyeRadius;
    face.leftEye.radius = mouseY / sceneHeight * maxEyeRadius;

    sc.update();
  })
  .on('click', function () {

    console.log('clicked');

    face.color = randomItem(faceColors);
    sc.bgColor = randomItem(bgColors);
    face.smile.rads = randomItem(smileAngles);

    sc.update();
  });