const ctx = document.getElementById('chart_tahfidz').getContext('2d');
const ctx_tahunan = document.getElementById('chart_tahfidz_tahunan').getContext('2d');

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
                position: "right",
            },
            title: {
                display: true,
                text: "Jumlah Setoran Perminggu"
            },
        },
        scales: {
            x: {
                title: {
                    display: false,
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

// Chart Setoran Tahunan
new Chart(ctx_tahunan, {
    type: "line",
    data: {
        labels: chart_data_tahunan.labels,
        datasets: chart_data_tahunan.datasets
    },
    options: {
        indexAxis: 'y',
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                position: "right",
            },
            title: {
                display: true,
                text: "Jumlah Setoran Tahunan"
            },
        },
        scales: {
            x: {
                beginAtZero: true,
                title: {
                    display: true,
                    text: "Jumlah Setoran (ayat)"
                },
            },
            y: {
                title: {
                    display: true,
                    text: "Bulan"
                }
            }
        }
    }
});
