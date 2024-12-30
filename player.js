function debug(str) { 
  //   alert(str);
}
function filenameFromUrl(url) {
  var parts = url.split('/');
  return parts[parts.length - 1];
}
var currentTimeVar = 0;
function choose(url) {
  window.currentAudioElement = document.getElementById('player');
  if (typeof window.currentAudioElement === 'undefined') {
    alert('your browser does not like audio.');
  } else {
    debug('paused:' + window.currentAudioElement.paused
         +'\nsrc:' + window.currentAudioElement.src
         +'\ntime:' + window.currentAudioElement.currentTime
    );
    if (window.currentAudioElement.paused) {
      if(window.currentAudioElement.src.endsWith(filenameFromUrl(url))) {
        window.currentAudioElement.currentTime = currentTimeVar;
        debug('window.currentAudioElement.currentTime:' + window.currentAudioElement.currentTime);
      } else {
         debug('Setting url from :' + window.currentAudioElement.src + ' to:' + url);
         window.currentAudioElement.src = url;
      }
      window.currentAudioElement.play();
    } else {
      debug('Not Paused **\n' + 'paused:' + window.currentAudioElement.paused
         +'\nsrc:' + window.currentAudioElement.src
         +'\ntime:' + window.currentAudioElement.currentTime
         );
  
      if(window.currentAudioElement.src.endsWith(filenameFromUrl(url))) {
        currentTimeVar = window.currentAudioElement.currentTime;
        debug('window.currentAudioElement.currentTime:' + window.currentAudioElement.currentTime);
        window.currentAudioElement.pause();
      } else {
         debug('Setting url from :' + window.currentAudioElement.src + ' to:' + url);
         window.currentAudioElement.src = url;
         window.currentAudioElement.play();
      }

    }
  
  }

}
  

