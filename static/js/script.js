const showMessageButton = document.getElementById('showMessageButton');
const messageBox = document.getElementById('messageBox');
const closeMessageButton = document.getElementById('closeMessageButton');

showMessageButton.addEventListener('click', () => {
    messageBox.style.display = 'block';
});

closeMessageButton.addEventListener('click', () => {
    messageBox.style.display = 'none';
});