const ctx = document.getElementById('chart_tahfidz').getContext('2d');

// Chart Setoran Perminggu
new Chart(ctx, {
    type: "bar",
    data: {
        labels: chart_data.labels,
        datasets: chart_data.datasets
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                position: "top",
            },
            title: {
                display: true,
                text: "Rata-Rata Setoran Perminggu"
            },
        },
        scales: {
            x: {
                title: {
                    display: true,
                    text: "Pekan"
                },
            },
            y: {
                beginAtZero: true,
                title: {
                    display: true,
                    text: "Jumlah Setoran (ayat)"
                }
            }
        }
    }
});

