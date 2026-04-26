// Shuffle children of any .randomize-rows container (tbody or div)
document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.randomize-rows').forEach(function (container) {
        var items = Array.from(container.children);
        for (var i = items.length - 1; i > 0; i--) {
            var j = Math.floor(Math.random() * (i + 1));
            container.appendChild(items[j]);
            items.splice(j, 1);
        }
        container.appendChild(items[0]);
    });
});
