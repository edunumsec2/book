// Courtesy of https://stackoverflow.com/questions/30106476/using-javascripts-atob-to-decode-base64-doesnt-properly-decode-utf-8-strings
function b64DecodeUnicode(str) {
    return decodeURIComponent(atob(str).split('').map(function(c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));
}

function references_ready() {
    const main_content = document.querySelector(".main");
    const tooltip = document.createElement("div");
    tooltip.setAttribute("id", "tooltip");
    tooltip.innerHTML =
        '<div id="tooltip-container">' +
        '<h1 id="tooltip-name"></h1>' +
        '<div id="tooltip-description"></div>' +
        '<div id="tooltip-link-div">' +
        '<a id="tooltip-link" href="#">Voir dans le glossaire</a>' +
        '</div>' +
        '<div id="tooltip-close"><div>&#215;</div></div>' +
        '</div>' +
        '<div id="tooltip-arrow" data-popper-arrow></div>';
    document.body.appendChild(tooltip);
    const tooltipName = document.getElementById("tooltip-name");
    const tooltipDesc = document.getElementById("tooltip-description");
    const tooltipLink = document.getElementById("tooltip-link");

    var popperInstance = null;
    var activeElement = null;

    function createTooltip(elem) {
        tooltipName.innerText = b64DecodeUnicode(elem.dataset.entryName);
        tooltipDesc.innerHTML = b64DecodeUnicode(elem.dataset.definition);
        if ("glossaryUri" in elem.dataset) {
            tooltipLink.style.display = 'inline';
            tooltipLink.setAttribute("href", elem.dataset.glossaryUri);
        }
        else {
            tooltipLink.style.display = 'none';
        }
        tooltip.style.display = "block";

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
        activeElement = elem;
    }

    function hideTooltip() {
        tooltip.style.display = "none";
        popperInstance.destroy();
        popperInstance = null;
        activeElement = null;
    }

    document.getElementById("tooltip-close").addEventListener("click", hideTooltip);
    tooltipLink.addEventListener("click", function() {
        hideTooltip();
        return true;
    });

    var refs = document.getElementsByClassName("glossary-ref");
    for (const ref of refs) {
        ref.addEventListener("click", function () {
            if (activeElement == null) {
                createTooltip(ref);
            }
            else if (activeElement.isSameNode(ref)) {
                hideTooltip();
            }
            else {
                hideTooltip();
                createTooltip(ref);
            }
        });
    }
}
document.addEventListener("DOMContentLoaded", references_ready, false);