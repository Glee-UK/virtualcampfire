function debug(str) { 
  //   alert(str);
}
var playlist = [];
var player;

function idFromUrl(url) {
  var parts = url.split('/');
  return  parts[parts.length - 1].replaceAll("'", "\\'");
}

function initPlayer(){
  player = document.getElementById('player');
  if (typeof player === 'undefined') {
    alert('your browser does not like audio.');
  } else {
    debug('adding ended event');
    player.addEventListener('ended', function() {
      debug('ended: ' + player.src
             +'\nplaylist: \n   ' + playlist.join('\n   ')
      );

	  if (playlist.length > 0) {
        checkbox = document.getElementById(idFromUrl(player.src));
        checkbox.checked = false;
        checkbox.style.accentColor = null;

        next_url = playlist.shift()
  	  	play(next_url);
      } else {
        play(player.src)
      }
    });
  }
}

function choose(url,checkbox) {
  if (checkbox.checked) {
    debug("Adding to playlist: " + url);
    playlist.push(url);
    if (player.paused) {
        next_url = playlist.shift()
  	  	play(next_url);
   }
  } else {
	var index = playlist.indexOf(url);
	if (index > -1) {
	  debug("Removing from playlist: " + url);
	  playlist.splice(index, 1);
	}
  }
}

function play(url) {
    debug('playing: ' + url
        +'\nplaylist: \n   ' + playlist.join('\n   ')
    );
    id = idFromUrl(url);
    checkbox = document.getElementById(id);
    if (checkbox == null) {
	  debug('checkbox is null: ' + id);
	} else {
      checkbox.style.accentColor = 'orange';
    }
    player.src = url;
    player.play();
}
  

