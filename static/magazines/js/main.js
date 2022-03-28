var book = ePub("https://s3.amazonaws.com/moby-dick/");

    var rendition = book.renderTo("viewer", {
      width: "100%",
      height: 600,
      ignoreClass: 'annotator-hl',
      manager: "continuous"
    });

    var displayed = rendition.display(6);

    // Navigation loaded
    book.loaded.navigation.then(function(toc){
      // console.log(toc);
    });

    var next = document.getElementById("next");
    next.addEventListener("click", function(){
      rendition.next();
    }, false);

    var prev = document.getElementById("prev");
    prev.addEventListener("click", function(){
      rendition.prev();
    }, false);

    var keyListener = function(e){

      // Left Key
      if ((e.keyCode || e.which) == 37) {
        rendition.prev();
      }

      // Right Key
      if ((e.keyCode || e.which) == 39) {
        rendition.next();
      }

    };

    rendition.on("keyup", keyListener);
    document.addEventListener("keyup", keyListener, false);

    rendition.on("relocated", function(location){
      // console.log(location);
    });


    // Apply a class to selected text
    rendition.on("selected", function(cfiRange, contents) {
      rendition.annotations.highlight(cfiRange, {}, (e) => {
        console.log("highlight clicked", e.target);
      });
      contents.window.getSelection().removeAllRanges();

    });

    this.rendition.themes.default({
      '::selection': {
        'background': 'rgba(255,255,0, 0.3)'
      },
      '.epubjs-hl' : {
        'fill': 'yellow', 'fill-opacity': '0.3', 'mix-blend-mode': 'multiply'
      }
    });

    // Illustration of how to get text from a saved cfiRange
    var highlights = document.getElementById('highlights');

    rendition.on("selected", function(cfiRange) {

      book.getRange(cfiRange).then(function (range) {
        var text;
        var li = document.createElement('li');
        var a = document.createElement('a');
        var remove = document.createElement('a');
        var textNode;

        if (range) {
          text = range.toString();
          textNode = document.createTextNode(text);

          a.textContent = cfiRange;
          a.href = "#" + cfiRange;
          a.onclick = function () {
            rendition.display(cfiRange);
          };

          remove.textContent = "remove";
          remove.href = "#" + cfiRange;
          remove.onclick = function () {
            rendition.annotations.remove(cfiRange);
            return false;
          };

          li.appendChild(a);
          li.appendChild(textNode);
          li.appendChild(remove);
          highlights.appendChild(li);
        }

      })

    });