document.querySelectorAll('.b div').forEach(item => {
    item.addEventListener('click', function(event) {

        console.log('.b div clicked');
        console.log(event.target);

        let trackId = item.dataset.trackId;
        let url = 'https://open.spotify.com/embed/track/' + trackId;
        console.log('url', url);
        document.getElementById('player').setAttribute('src', url);
        console.log('player updated');

    });
});

document.querySelectorAll('li').forEach(item => {
    item.addEventListener('click', function(event) {

        console.log('li clicked');
        console.log(event.target);
        console.log(item);

        let trackId = item.querySelector('.track-li').dataset.trackId;
        console.log('id', trackId);
        let url = 'https://open.spotify.com/embed/track/' + trackId;
        console.log('url', url);
        document.getElementById('player').setAttribute('src', url);
        console.log('player updated');

    });
});
