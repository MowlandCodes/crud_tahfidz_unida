const setoran_perminggu = document.getElementById('chart-setoran-mingguan');
const setoran_perbulan = document.getElementById('chart-setoran-bulanan');

// Chart Setoran Perminggu
new Chart(setoran_perminggu, {
    type: "doughnut",
    data: {
        labels: label_mingguan,
        datasets: [{
            label: "Rata-Rata Setoran Perminggu",
            data: data_mingguan, 
            backgroundColor: [
                "rgba(18, 53, 36, 0.5)", 
                "rgba(62, 123, 39, 0.5)",
                "rgba(133, 169, 71, 0.5)", 
                "rgba(225, 255, 187, 0.5)", 
                "rgba(255, 244, 183, 0.5)", 
                "rgba(239, 227, 194, 0.5)"
            ],
            borderColor: [
                "rgba(18, 53, 36, 1)", 
                "rgba(62, 123, 39, 1)",
                "rgba(133, 169, 71, 1)", 
                "rgba(225, 255, 187, 1)", 
                "rgba(255, 244, 183, 1)", 
                "rgba(239, 227, 194, 1)"
            ],
            hoverOffset: 4,
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                position: "right",
            }
        }
    }
})

// Chart Setoran Perbulan
new Chart(setoran_perbulan, {
    type: "bar",
    data: {
        labels: label_bulanan,
        datasets: [{
            label: "Rata-Rata Setoran Perbulan",
            data: data_bulanan,
            backgroundColor: [
                "rgba(18, 53, 36, 0.9)", 
                "rgba(62, 123, 39, 0.9)",
                "rgba(133, 169, 71, 0.9)", 
                "rgba(225, 255, 187, 0.9)", 
                "rgba(255, 244, 183, 0.9)", 
                "rgba(239, 227, 194, 0.9)"
            ],
            borderColor: [
                "rgba(18, 53, 36, 1)", 
                "rgba(62, 123, 39, 1)",
                "rgba(133, 169, 71, 1)", 
                "rgba(225, 255, 187, 1)", 
                "rgba(255, 244, 183, 1)", 
                "rgba(239, 227, 194, 1)"
            ],
            hoverOffset: 4,
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                position: "right",
            }
        }
    }
})
