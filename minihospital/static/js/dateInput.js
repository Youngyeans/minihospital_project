const datepicker = flatpickr("#startDate", {
    dateFormat: "d/m/Y",
    allowInput: true,
    onChange: function(selectedDates) {
        if (selectedDates.length > 0) {
            const formattedDate = formatThaiDate(selectedDates[0]);
            document.getElementById("formattedDate").textContent = formattedDate;
        }
    }
});

// ฟังก์ชันในการเปิด date picker เมื่อกดที่รูปภาพ
function openDatePicker() {
    datepicker.open();
}

// ฟังก์ชันแปลงวันที่เป็นรูปแบบไทย
function formatThaiDate(date) {
    const months = [
        "มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", 
        "พฤษภาคม", "มิถุนายน", "กรกฎาคม", "สิงหาคม", 
        "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"
    ];
    const day = date.getDate();
    const month = months[date.getMonth()];
    const year = date.getFullYear() + 543; // แปลงปีค.ศ.เป็นปีพ.ศ.
    return `วันที่ ${day} ${month} ${year}`;
}

window.onload = function() {
    const today = document.getElementById("startDate").value;
    // const today = {{ today|safe }};
    console.log(today)
    if (today) {
        const parsedToday = flatpickr.parseDate(today, "d/m/Y"); // ใช้ flatpickr ในการแปลงวันที่จาก input
        if (parsedToday) {
            const formattedDate = formatThaiDate(parsedToday);
            console.log(formattedDate)
            document.getElementById("formattedDate").textContent = formattedDate;
        }
    }
};
