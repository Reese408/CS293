function handleLogin(event) {
    event.preventDefault();

    const formData = new FormData(event.target);
    fetch(event.target.action, {
        method: 'POST',
        body: formData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
        },
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(data => {
                alert(data.error);
            });
        }
        return response.text(); 
    })
    .then(data => {
        window.location.href = "{% url 'index' %}"; 
    })
    .catch(error => {
        console.error('Error:', error);
    });
}