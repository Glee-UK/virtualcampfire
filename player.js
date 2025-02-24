function debug(str) { 
  //   alert(str);
}
var playlist = [];
var player;

function filenameFromUrl(url) {
  var parts = url.split('/');
  return parts[parts.length - 1];
}
function initPlayer(){
  player = document.getElementById('player');
  if (typeof player === 'undefined') {
    alert('your browser does not like audio.');
  } else {
    debug('adding ended event');
    player.addEventListener('ended', function() {
        debug('ended'
             +'\npaused: ' + player.paused
             +'\nsrc: ' + player.src
             +'\ntime: ' + player.currentTime
             +'\nplaylist: ' + playlist
        );

	  if (playlist.length > 1) {
  	  	    play(playlist.shift());
      }
      play(playlist[0])
    });
  }
}

function choose(url) {
  playlist.push(url);
  debug("Adding to playlist: " + url);
  if (player.paused) {
    play(url);
  }
}

function play(url) {
    debug('paused:' + player.paused
         +'\nsrc:' + player.src
         +'\ntime:' + player.currentTime
         +'\nplaylist:' + playlist
    );
    player.src = url;
    player.play();
}
  

