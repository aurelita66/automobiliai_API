// JAVASCRIPT KODAS DINAMIŠKAI GENERUOTI LENTELĘ SU DUOMENIMIS
document.addEventListener('DOMContentLoaded', function() {
    fetch('/api2/automobiliai')
        .then(response => response.json())
        .then(data => {
            const tbody = document.getElementById('automobiliai-body');
            tbody.innerHTML = '';

            data.forEach(automobilis => {
                const tr = document.createElement('tr');

                tr.innerHTML = `
                    <td>${automobilis.id}</td>
                    <td>${automobilis.gamintojas}</td>
                    <td>${automobilis.modelis}</td>
                    <td>${automobilis.spalva}</td>
                    <td>${automobilis.metai}</td>
                `;

                tbody.appendChild(tr);
            });
        })
        .catch(error => console.error('Error fetching data:', error));
});

