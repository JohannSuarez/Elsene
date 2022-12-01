form_func = () => {
  var button = document.getElementById("submit-button");
  var response_text = document.getElementById("request-response");


  const data = {
    yt_url: document.getElementById("input_yt_url").value,
    recipient: document.getElementById("input_recipient").value
  };

  fetch('/convert', {
    method: 'POST', // or 'PUT'
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })
    .then((response) => {

      // Check if the response is 200 or not.
      // Hide the button when the response is good. That means 
      // a subprocess has been created and the conversion is underway.
      console.log(response)

      if (response.status == 200) {

        button.style.display = 'none';
        response_text.classList.add("request-response-good");
        response_text.innerText = "Submitted! Please check your e-mail after a few minutes.";

      } else {
        response_text.innerText = "Error: Issue with server or request.";
      }
    })
    .catch((error) => {
      console.error('Fetch Error:', error);
    });
}
