
$(document).ready(function() {
    var table = document.getElementById("hafalan-table")

    $("#hafalan-table").DataTable({
        responsive: true,
        paging: false,
        searching: true,
        scrollCollapse: true,
        ordering: true,
        info: true,
        scrollY: '50vh',
        language: {
            search: "Cari data ",
            lengthMenu: "Menampilkan _MENU_ data per halaman",
            info: "Menampilkan _START_ - _END_ dari _TOTAL_ data",
            infoFiltered: "(Terfilter dari _MAX_ total data)",
            infoEmpty: "Tidak ada hafalan",
            zeroRecords: "Tidak ada hafalan yang sesuai",
        },
    });

    $('#toogle-btn').on('click', function (){
        setTimeout(() => {
            $("#hafalan-table").DataTable().columns.adjust().draw();
        }, 600);
    });

});
