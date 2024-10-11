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

function updateDates() {
    console.log("date select")
    // รับค่าจาก input
    const input = document.getElementById('startDate').value;
    // แยกวันที่จากรูปแบบ dd/mm/yyyy
    const parts = input.split('/');
    const day = parseInt(parts[0], 10);
    const month = parseInt(parts[1], 10) - 1; // เดือนเริ่มนับจาก 0 ใน JS
    const year = parseInt(parts[2], 10);

    const startDate = new Date(year, month, day);

    // รับ element ที่จะแสดงผล
    const dateGrid = document.getElementById('dateGrid');
    // const dateElements = dateGrid.getElementsByID('date'+i);
    // const dayElements = dateGrid.getElementsByID('day'+i);

    // อัปเดตวันที่และชื่อวันในแต่ละช่อง
    for (let i = 1; i < 8; i++) {
        const dateElements = dateGrid.getElementsByID('date'+i);
        const dayElements = dateGrid.getElementsByID('day'+i);
        const currentDate = new Date(startDate);
        currentDate.setDate(startDate.getDate() + i);

        // อัปเดตวันที่
        dateElements.textContent = currentDate.getDate();
        
        // อัปเดตชื่อวัน (เช่น Mon, Tue)
        const dayName = currentDate.toLocaleDateString('en-GB', { weekday: 'short' });
        dayElements.textContent = dayName;
    }
}