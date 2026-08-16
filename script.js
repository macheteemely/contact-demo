const form = document.getElementById("contactForm");
const result = document.getElementById("result");

form.addEventListener("submit", async function (event) {
    event.preventDefault();

    const data = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        message: document.getElementById("message").value
    };

    try {
        const response = await fetch("http://127.0.0.1:8000/contact", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const resultData = await response.json();

        if (response.ok) {
            result.textContent = resultData.message;
            form.reset();
        } else {
            result.textContent = "Message could not be sent.";
        }

    } catch (error) {
        result.textContent = "Could not connect to the server.";
        console.error(error);
    }
});