let clicks = 0;

function onCookieClick() {
    clicks += 1;
    document.getElementById("nClicks").innerHTML = clicks;
}
function getFlag() {
    let encoded = btoa(clicks);
    document.cookie = 'clicks=' + encoded;
    fetch('/flag.php', {
    
        method: 'POST', 
        headers: {
        'Content-Type': 'text/plain',
        },
        credentials: 'include'
    })
    .then(response => {
        return response.text()
    })
    .then(body => {
        document.getElementById("flagStatus").innerHTML = body;
    })
}