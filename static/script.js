document.addEventListener("DOMContentLoaded", () => {
  const passwordInput = document.getElementById("password");
  const strengthMeter = document.getElementById("strengthMeter");
  const strengthText = document.getElementById("strengthText");
  const feedbackList = document.getElementById("feedbackList");

  passwordInput.addEventListener("input", async () => {
    const password = passwordInput.value;

    console.log("Typing:", password);

    try {
      const res = await fetch("http://127.0.0.1:5000/check", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ password })
      });

      if (!res.ok) throw new Error("Network error");

      const data = await res.json();

      strengthMeter.className = "meter " + data.strength.toLowerCase();
      strengthText.textContent = `Strength: ${data.strength}`;

      feedbackList.innerHTML = "";
      data.feedback.forEach(msg => {
        const li = document.createElement("li");
        li.textContent = msg;
        feedbackList.appendChild(li);
      });
    } catch (error) {
      console.error("Error:", error);
    }
  });
});
