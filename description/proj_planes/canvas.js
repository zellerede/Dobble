const planes = {
    2: plane2, 3: plane3, 4: plane4, 5: plane5, 7: plane7, 
    8: plane8, 9: plane9, '9a': plane9a, 11: plane11, 13: plane13
};
let plane = plane3;  // read from cache (localstorage)

var N, parallels, allLines, direction, directionVector;

function prepareAllLines() {
    N = plane.lines[0].length;

    let horizontals = [];
    for (let i=0; i<N; i++) {
        horizontals.push( Array(N).fill(i) );
    }
    var lineCodes = [...plane.lines];
    lineCodes.unshift(horizontals);

    parallels = lineCodes.map( (parCodes) => parCodes.map(
        (lineCode) => new Line(lineCode)
    ));
    
    let verticals = [];
    for (let i=0; i<N; i++) {
        verticals.push( new VerticalLine(i) );
    }
    parallels.push(verticals);
    allLines = parallels.flat();
}

class Line {
    constructor(lineCode) {
        this.lineCode = lineCode;
    }

    has = (dot) => (
        this.lineCode[dot.x] == dot.y
    );
}

class VerticalLine {
    constructor(x) {
        this.x = x;
    }

    has = (dot) => (this.x == dot.x);
}

prepareAllLines();

//
const cvs = document.getElementById('squareNxN');
const c = cvs.getContext('2d');
let myFrame = cvs.getBoundingClientRect();

let mouse = {
    x: undefined,
    y: undefined,
    held: false
};

function applyWindowSize() {
    myFrame = cvs.getBoundingClientRect();
    cvs.width = 40 * (N+2);
    cvs.height = 40 * (N+0.5);
}

window.addEventListener('resize', () => {
  applyWindowSize();
});

cvs.onmousemove = (event) => {
    mouse.x = event.x - myFrame.left;
    mouse.y = event.y - myFrame.top;
};

cvs.onmousedown = (event) => {
    mouse.held = true;
    onMouseDown(event);
};

cvs.onmouseup = (event) => {
    mouse.held = false;
    onMouseUp(event);
};


class Dot {
    constructor(x, y, radius=4, fillStyle='brown') {
        this.x = x;
        this.y = y;
        this.radius = radius;
        this.fillStyle = fillStyle;
        this.underMouse = false;
    }

    hovered = () => {
    }

    draw = (stroked=false) => {
        c.beginPath();
        c.fillStyle = this.fillStyle;
        if (stroked) {
            c.lineWidth = 5;
            c.strokeStyle = '#003300';
            c.stroke();
        }
        c.arc(this.x, this.y, this.radius, 0, 2*Math.PI, false);
        c.fill();
        // bigger circle to catch mouse
        var catchRadius = Math.min(32, Math.max(12, this.radius*2))
        c.arc(this.x, this.y, catchRadius, 0, 2*Math.PI, false); 
        c.closePath()
        this.underMouse = c.isPointInPath(mouse.x, mouse.y)
        if (this.underMouse) {
            this.hovered();
        }
    }

}

class MatrixDot {

    unit = 40;
    start = {x: 50, y: 50};

    constructor(x, y, onLine=false) {
        this.x = x;
        this.y = y;
        this.dot = new Dot(this.start.x + x*this.unit, this.start.y + y*this.unit);
        this.dot.hovered = this.hovered;
        this.onLine = onLine;
    }

    draw = () => {
        this.dot.radius = this.onLine ? 8 : 3;
        this.dot.fillStyle = this.onLine ? 'green' : 'brown';
        this.dot.draw(this.onLine);
    }

    hovered = () => {
        hoveredDot = this;
        if (! mouse.held) {
            drawALine(this);
        }
    }

}

const dots = [];
var hoveredDot = undefined;

function initializeDots() {
    dots.length = 0; // clear the array
    for (let y = 0; y < N; y++) {
        for (let x = 0; x < N; x++) {
            dots.push(new MatrixDot(x,y));
        }
    }
}

function clearDirection() {
    direction = 0;
    directionVector = [undefined, undefined];
}

function drawALine(matrixDot) {
    var myLine = parallels[direction].filter(line => line.has(matrixDot))[0];
    dots.forEach( (dot) => {
        dot.onLine = myLine.has(dot);
    });
}

const areWeOnDot = () => (hoveredDot && hoveredDot.dot.underMouse);

function onMouseDown(event) {
    directionVector[0] = areWeOnDot() ? {x: hoveredDot.x, y: hoveredDot.y} : undefined;
}

function onMouseUp(event) {
    if (directionVector[0] && areWeOnDot()) {
        directionVector[1] = {x: hoveredDot.x, y: hoveredDot.y};
        if ((directionVector[0].x != directionVector[1].x) || 
            (directionVector[0].y != directionVector[1].y)) {
                let myLine = allLines.filter( (line) => 
                    (line.has(directionVector[0]) && line.has(directionVector[1])) 
                )[0]; // assert filter returns an array with exactly 1 element
                direction = parallels.findIndex( (pars) => (pars.includes(myLine)) );
        }
    }
}

function planeSelected(planeId) {
    console.log(planeId);   
    plane = planes[planeId];
    prepareAllLines();
    runIt();
}

function animate() {
  requestAnimationFrame(animate);
  c.clearRect(0, 0, cvs.width, cvs.height);
  dots.forEach(dot => dot.draw())
};

function runIt() {
  initializeDots();
  clearDirection();
  applyWindowSize();
  animate();
}

runIt();
