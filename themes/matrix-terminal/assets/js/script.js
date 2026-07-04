const canvas = document.getElementById('code-rain');
const context = canvas?.getContext('2d');

if (canvas && context) {
  const glyphs = '01アイウエオカキクケコサシスセソ0123456789{}[]<>/';
  const fontSize = 15;
  let drops = [];

  function resize() {
    canvas.width = window.innerWidth * devicePixelRatio;
    canvas.height = window.innerHeight * devicePixelRatio;
    canvas.style.width = `${window.innerWidth}px`;
    canvas.style.height = `${window.innerHeight}px`;
    context.setTransform(devicePixelRatio, 0, 0, devicePixelRatio, 0, 0);
    drops = Array.from({ length: Math.ceil(window.innerWidth / fontSize) }, () => Math.random() * -40);
  }

  function draw() {
    context.fillStyle = 'rgba(3, 8, 6, 0.12)';
    context.fillRect(0, 0, window.innerWidth, window.innerHeight);
    context.fillStyle = '#66ff86';
    context.font = `${fontSize}px monospace`;

    drops.forEach((drop, index) => {
      const glyph = glyphs[Math.floor(Math.random() * glyphs.length)];
      context.fillText(glyph, index * fontSize, drop * fontSize);
      drops[index] = drop * fontSize > window.innerHeight && Math.random() > 0.975 ? 0 : drop + 1;
    });
    requestAnimationFrame(draw);
  }

  resize();
  window.addEventListener('resize', resize);
  draw();
}
