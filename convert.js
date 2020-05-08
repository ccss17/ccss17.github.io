const path = require('path'),
    fs = require('fs'),
    kt = require('katex'),
    tm = require('markdown-it-texmath').use(kt),
    md = require('markdown-it')({
        html: true,
        linkify: true,
        typographer: true
    }).use(tm);

const htmlTmpl = (html) => `<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/4.0.0/github-markdown.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.18.1/styles/atom-one-dark.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.11.1/dist/katex.min.css" integrity="sha384-zB1R0rpPzHqg7Kpt0Aljp8JPLqbXI3bhnPWROx27a9N0Ll6ZP/+DiW/UqRcLbRjq" crossorigin="anonymous">
<link rel="stylesheet" href="https://gitcdn.xyz/repo/goessner/mdmath/master/css/texmath.css">
<link rel="stylesheet" href="https://gitcdn.xyz/repo/goessner/mdmath/master/css/vscode-texmath.css">
<link rel="stylesheet" href="https://raw.githubusercontent.com/sindresorhus/github-markdown-css/gh-pages/github-markdown.css">
<style>
body {
  box-sizing: border-box;
  min-width: 200px;
  max-width: 980px;
  margin: 0 auto;
  padding: 45px;
}
</style>
</head><body><article class="markdown-body">
${html}
</article></body></html>`

const directoryPath = path.join(__dirname, 'memos');
fs.readdir(directoryPath, function (err, files) {
  if (err) 
    return console.log('Unable to scan directory: ' + err);
  files.forEach(function (file) {
    let content = fs.readFileSync(path.join(directoryPath, file), {encoding: 'utf8', flag: 'r'});
    let htmlfn = file.split('.')[0]+'.html';
    fs.writeFileSync(path.join(__dirname, htmlfn), htmlTmpl(md.render(content)), 'utf8');
  });
});