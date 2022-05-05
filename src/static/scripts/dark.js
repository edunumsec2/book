function updateModuloTheme() {
    const theme = document.body.dataset.theme;
    if (!theme) {
        setTimeout(updateModuloTheme, 100);
        return;
    }
    let is_dark_theme = theme === "dark";
    if (theme === "auto" && window.matchMedia("(prefers-color-scheme: dark)").matches) {
        is_dark_theme = true;
    }
    const was_dark_theme = document.body.classList.contains("modulo-dark");
    document.body.classList.toggle("modulo-dark", is_dark_theme);
    if (was_dark_theme !== is_dark_theme) {
        document.body.dispatchEvent(new CustomEvent("themechanged", {
            detail: {
                is_dark_theme: is_dark_theme
            }
        }));
    }
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