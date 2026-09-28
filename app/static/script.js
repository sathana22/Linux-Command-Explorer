async function searchCommand() {

    const command = document.getElementById("searchInput").value;

    const response = await fetch("/api/commands/" + command);

    const result = document.getElementById("result");

    if (!response.ok) {
        result.innerHTML = "<h2>Command not found</h2>";
        return;
    }

    const data = await response.json();

    let flags = "";

    for (const flag in data.flags) {
        flags += `<p><b>${flag}</b> - ${data.flags[flag]}</p>`;
    }

    result.innerHTML = `
        <h2>${command}</h2>

        <p>${data.description}</p>

        <h3>Usage</h3>
        <p>${data.usage}</p>

        <h3>Flags</h3>
        ${flags}

        <h3>Example</h3>
        <p>${data.example}</p>
    `;
}