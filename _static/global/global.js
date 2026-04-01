// Shuffle rows within all <tbody class="randomize-rows"> elements
document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('tbody.randomize-rows').forEach(function (tbody) {
        var rows = Array.from(tbody.children);
        for (var i = rows.length - 1; i > 0; i--) {
            var j = Math.floor(Math.random() * (i + 1));
            tbody.appendChild(rows[j]);
            rows.splice(j, 1);
        }
        // append the remaining first element
        tbody.appendChild(rows[0]);
    });
});
