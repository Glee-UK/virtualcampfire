function debug(str) { 
  //   alert(str);
}
var playlist = [];
var player;

function idFromUrl(url) {
  if (url == null) {
    alert('url is null');
  }
  var parts = url.split('/');
  return  parts[parts.length - 1].replaceAll("'", "").replaceAll(".mp3", "").replaceAll("(", "").replaceAll(")", "")
}

function initPlayer(){
  player = document.getElementById('player');
  player.addEventListener('ended', function() {
    debug('ended: ' + player.src
         +'\nplaylist: \n   ' + playlist.join('\n   ')
    );

    ended_song_id = idFromUrl(player.src);
    checkbox = document.getElementById(ended_song_id);
    if (checkbox == null) {
      alert('checkbox is null: ' + ended_song_id);
    }
    checkbox.checked = false;
    checkbox.style.accentColor = null;
	if (playlist.length > 0) {
        next_url = playlist.shift()
     	play(next_url);
    } else {
        play(player.src)
    }
  });
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
	} else {
      checkbox.style.accentColor = null;
      player.pause();
      player.src = null;
      next_url = playlist.shift()
      if (next_url != null ){
        play(next_url);
      }
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
	  alert('checkbox is null: ' + id);
	} else {
      checkbox.style.accentColor = 'orange';
    }
    player.src = url;
    player.play();
}
  

