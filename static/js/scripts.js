let count = 0;

function decrement() {
    if(count > 0) {
        count--;
        document.getElementById('dayCount').innerText = count;
        document.getElementById('dayInput').value = count;
    }
}

function increment() {
    if(count < 4) {
        count++;
        document.getElementById('dayCount').innerText = count;
        document.getElementById('dayInput').value = count;
    }
}
