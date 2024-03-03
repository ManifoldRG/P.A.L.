document.addEventListener('DOMContentLoaded', function() {
    const feed = document.getElementById('feed');

    // Call fetchUpdate when the DOM is loaded
    fetchUpdate();

    // Set up a timer to fetch updates every 10 seconds
    setInterval(fetchUpdate, 10000);

    function fetchUpdate() {
        fetch('http://localhost:5328/api/updates')
            .then(response => response.json())
            .then(data => {
                console.log(data);
                // Directly add the update to the feed if its content is not 'None'
                if (data.content !== 'None') {
                    addUpdateToFeed(data);
                }
            })
            .catch(error => console.error('Error fetching update:', error));
    }

    function addUpdateToFeed(update) {
        const div = document.createElement('div');
        div.className = 'update';
        div.innerHTML = `<p>${update.content}</p>`;
        // Adds the new update at the top of the feed
        feed.insertBefore(div, feed.firstChild);
    }
});