
function debug(str) {
  //alert(str);
}
function log(str) {
  //alert(str);
}
var playlist = [];
var player;
var currentHref = new URL(window.location.href);

// Note the checkbox id and song url are tightly coupled, same logic repeated in jinja_site.py
function idFromUrl(url) {
  if (url == null) {
    alert('url is null');
  }
  var parts = url.split('/');
  return  parts[parts.length - 1].replaceAll("'", "").replaceAll(".mp3", "").replaceAll("(", "").replaceAll(")", "")
}
function loadFromQueryString() {
  const params = new URLSearchParams(window.location.search);
  if (!params.has('playlist')) {
	return;
  }
  playlistIds = params.get('playlist').split(',');
  first = 0;
  for (i=0; i<playlistIds.length; i++)  {
    id=playlistIds[i];
    checkbox = document.getElementById(id);
    checkbox.checked = true;
    if (first == 0) {
      first = 1;
      player.src=checkbox.value;
      checkbox.style.accentColor = 'orange';
    } else {
      playlist.push(checkbox.value);
    }
  }
}
function initPlayer(){
  player = document.getElementById('player');
  player.addEventListener('ended', function() {
    debug('ended: ' + player.src
         +'\nplaylist: \n   ' + playlist.join('\n   ')
    );

    uncheck(player.src);
	if (playlist.length > 0) {
      next_url = playlist.shift()
      debug('choosing next: ' + next_url );
      play(next_url);
    } else {
      debug('choosing this: ' + player.src );
      play(player.src);
    }
  });
  loadFromQueryString();
}

function uncheck(url) {
    id = idFromUrl(url);
    checkbox = document.getElementById(id);
    checkbox.checked = false;
    checkbox.style.accentColor = null;
}
function updatePlaylist() {
    var playlistIds = '';
    if (player.src != null && player.src != '') {
	  playlistIds = idFromUrl(player.src) + ',';
	}
	playlistIds += playlist.map(idFromUrl).join(',');
    currentHref.searchParams.set('playlist', playlistIds);
    window.history.pushState({}, '', currentHref);
}
function choose(url,add) {
  if (add) {
    debug("Adding to playlist: " + url);
    playlist.push(url);
    updatePlaylist();

    if (player.paused) {
      next_url = playlist.shift()
  	  play(next_url);
    }
  } else {
    uncheck(url);
	var index = playlist.indexOf(url);
	if (index > -1) {
	  debug("Removing from playlist: " + url);
	  playlist.splice(index, 1);
	} else { // already playing
      next_url = playlist.shift()
      if (next_url != null ){
        play(next_url);
      } else {
        player.pause();
        player.src = '';
      }
	}
    updatePlaylist();
  }
}

function play(url) {
    log('play: ' + url
        +'\nplaylist: \n   ' + playlist.join('\n   ')
    );
    checkbox = document.getElementById(idFromUrl(url));
    checkbox.checked = true;
    checkbox.style.accentColor = 'orange';
    player.src = url;
    player.play();
}
  

