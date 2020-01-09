let PRIME = 7;
const cvs = document.getElementById('square7x7');
const c = cvs.getContext('2d');
let myFrame = cvs.getBoundingClientRect();

let mouse = {
    x: undefined,
    y: undefined,
    held: false
};

let direction = {x: 1, y: 0};
let directionVector = [undefined, undefined];

function applyWindowSize() {
    myFrame = cvs.getBoundingClientRect();
    cvs.width = 40 * (PRIME+2);
    cvs.height = 40 * (PRIME+0.5);
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
            drawALine(this.x, this.y);
        }
    }

}

const dots = [];
var hoveredDot = undefined;

function initializeDots() {
    dots.length = 0; // clear the array
    for (let y = 0; y < PRIME; y++) {
        for (let x = 0; x < PRIME; x++) {
            dots.push(new MatrixDot(x,y));
        }
    }
}

function drawALine(x,y) {
    dots.forEach( (dot) => {
        dot.onLine = false;
    });
    var xi=x;
    var yi=y;
    for (let i=0; i<PRIME; i++) {
        dots[PRIME*yi + xi].onLine = true;
        xi = (xi+direction.x + PRIME) % PRIME;
        yi = (yi+direction.y + PRIME) % PRIME;
    }
} 

const areWeOnDot = () => (hoveredDot && hoveredDot.dot.underMouse);

function onMouseDown(event) {
    directionVector[0] = areWeOnDot() ? {x: hoveredDot.x, y: hoveredDot.y} : undefined;
}

function onMouseUp(event) {
    if (directionVector[0] && areWeOnDot()) {
        directionVector[1] = {x: hoveredDot.x, y: hoveredDot.y};
        let newDirection = {x: directionVector[1].x - directionVector[0].x,
                        y: directionVector[1].y - directionVector[0].y};
        if (newDirection.x || newDirection.y) {
            direction = newDirection;
        }
    }
}

function animate() {
  requestAnimationFrame(animate);
  c.clearRect(0, 0, cvs.width, cvs.height);
  dots.forEach(dot => dot.draw())
};

initializeDots();
applyWindowSize();
animate();