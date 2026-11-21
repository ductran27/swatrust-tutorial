/* Draw the equations of a page with the math renderer that is part of the site. */
document$.subscribe(function (page) {
  renderMathInElement(page.body, {
    delimiters: [
      { left: "\\(", right: "\\)", display: false },
      { left: "\\[", right: "\\]", display: true }
    ],
    throwOnError: true
  });
});
