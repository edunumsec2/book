function updateModuloTheme() {
    const theme = document.body.dataset.theme;
    if (!theme) {
        setTimeout(updateTheme, 100);
    }
    let is_dark_theme = theme === "dark";
    if (theme === "auto" && window.matchMedia("(prefers-color-scheme: dark)").matches) {
        is_dark_theme = true;
    }
    document.body.classList.toggle("modulo-dark", is_dark_theme);
}

document.addEventListener("DOMContentLoaded", updateModuloTheme);
window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', updateModuloTheme);


document.addEventListener("DOMContentLoaded", function() {
    const buttons = document.getElementsByClassName("theme-toggle");

    for (const button of buttons) {
        button.addEventListener("click", function() {
        updateModuloTheme();
        });
    }
});