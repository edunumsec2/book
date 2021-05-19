// Courtesy of https://stackoverflow.com/questions/30106476/using-javascripts-atob-to-decode-base64-doesnt-properly-decode-utf-8-strings
function b64DecodeUnicode(str) {
    return decodeURIComponent(atob(str).split('').map(function(c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));
}

function references_ready() {
    const main_content = document.getElementById("main-content").children.item(0);
    const tooltip = document.createElement("div");
    tooltip.setAttribute("id", "tooltip");
    document.body.appendChild(tooltip);

    var popperInstance = null;
    function createTooltip(elem) {
        tooltip.style.display = "block";
        const definition = elem.dataset.definition;
        tooltip.innerHTML = b64DecodeUnicode(definition) +
            '<div id="tooltip-arrow" data-popper-arrow></div>';
        popperInstance = Popper.createPopper(elem, tooltip, {
        modifiers: [
            {
                name: 'offset',
                options: {
                    offset: [0, 8],
                },
            },
            {
                name: 'preventOverflow',
                options: {
                    boundary: main_content,
                    altBoundary: true,
                },
            },
        ],
        });
    }

    function hideTooltip() {
        tooltip.style.display = "none";
        popperInstance.destroy();
        popperInstance = null;
    }

    var refs = document.getElementsByClassName("glossary-ref");
    for (const ref of refs) {
        // ref.addEventListener("click", function () {
        //     if (popperInstance == null) {
        //         createTooltip(ref);
        //     }
        //     else {
        //         hideTooltip();
        //     }
        // });
        ref.addEventListener("mouseenter", function() { createTooltip(ref); });
        ref.addEventListener("focus", function() { createTooltip(ref); });
        ref.addEventListener("mouseleave", hideTooltip);
        ref.addEventListener("blur", hideTooltip);
    }
}
document.addEventListener("DOMContentLoaded", references_ready, false);