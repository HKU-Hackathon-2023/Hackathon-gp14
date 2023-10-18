document.addEventListener('DOMContentLoaded', function() {
  const microphoneButton = document.getElementById('microphone-button');
  const microphoneStatus = document.getElementById('microphone-status');
  let isRecording = false;
  let mediaRecorder;
  let chunks = [];

  function startRecording() {
    navigator.mediaDevices.getUserMedia({ audio: true })
      .then(function(stream) {
        mediaRecorder = new MediaRecorder(stream);

        mediaRecorder.addEventListener('dataavailable', function(e) {
          chunks.push(e.data);
        });

        mediaRecorder.addEventListener('stop', function() {
          const audioBlob = new Blob(chunks, { type: 'audio/webm' });
          const audioUrl = URL.createObjectURL(audioBlob);
          // You can do something with the recorded audio here, like sending it to a server or playing it back.
          console.log(audioUrl);

          chunks = [];
        });

        mediaRecorder.start();
      })
      .catch(function(error) {
        console.error('Error accessing microphone:', error);
      });
  }

  function stopRecording() {
    mediaRecorder.stop();
  }

  microphoneButton.addEventListener('click', function() {
    console.log('hi')
    microphoneButton.classList.toggle('listening');
    if (microphoneButton.classList.contains('listening')) {
      microphoneButton.querySelector('i').style.display = 'none';
      microphoneStatus.classList.remove('d-none');
      // startRecording();
    } else {
      console.log('hi')
      microphoneStatus.classList.add('d-none');
      // Add the following line to hide the microphone icon
      microphoneButton.querySelector('i').style.display = 'block';
  
      // stopRecording();
    }
  });
});