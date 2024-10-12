// ฟังก์ชันในการเปิด date picker เมื่อกดที่รูปภาพ
function openDatePicker(inputId) {
    const dateInput = document.getElementById(inputId);
    if (dateInput) {
        dateInput._flatpickr.open();
    }
}

// ฟังก์ชันแปลงวันที่เป็นรูปแบบไทย (สำหรับแสดงผล)
function formatThaiDate(date) {
    const months = [
        "มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", 
        "พฤษภาคม", "มิถุนายน", "กรกฎาคม", "สิงหาคม", 
        "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"
    ];
    const day = date.getDate();
    const month = months[date.getMonth()];
    const year = date.getFullYear() + 543; // แปลงปีค.ศ.เป็นปีพ.ศ.สำหรับแสดงผล
    return `วันที่ ${day} ${month} ${year}`;
}

document.addEventListener('DOMContentLoaded', function() {
    // ตรวจสอบว่าค่าใน input ถูกต้อง
    const startDateValue = document.getElementById('startDate').value;

    // อัปเดต formattedDate ทันทีเมื่อ DOM โหลดเสร็จ โดยใช้ค่าเริ่มต้นจาก startDate
    if (startDateValue !== "") {
        const parsedDate = flatpickr.parseDate(startDateValue, "d/m/Y");  // แปลงวันที่จาก input เป็น date object
        const formattedDate = formatThaiDate(parsedDate);  // แปลงเป็นรูปแบบไทย
        document.getElementById("formattedDate").textContent = formattedDate;  // อัปเดตค่าใน #formattedDate
    }

    // Initialize flatpickr สำหรับ #startDate พร้อมกับการเชื่อมต่อฟังก์ชัน onChange
    flatpickr("#startDate", {
        dateFormat: "d/m/Y",
        allowInput: true,
        defaultDate: startDateValue !== "" ? startDateValue : null,  // ใช้ค่าเริ่มต้นจาก input
        locale: "th",  // ใช้ภาษาไทยใน date picker
        onChange: function(selectedDates) {
            if (selectedDates.length > 0) {
                // แปลงวันที่ที่เลือกเป็นรูปแบบไทยและอัปเดต #formattedDate
                const formattedDate = formatThaiDate(selectedDates[0]);
                document.getElementById("formattedDate").textContent = formattedDate;
                
                // เรียกใช้ฟังก์ชัน updateDates เพื่ออัปเดตข้อมูลวันที่ในกริด
                updateDates();
            }
        }
    });

    // Initialize flatpickr สำหรับ #sympDate (ไม่มีการเชื่อมต่อ onChange)
    flatpickr("#sympDate", {
        dateFormat: "d/m/Y",
        locale: "th"  // ใช้ภาษาไทยใน date picker
    });

    // เรียกใช้ updateDates ทันทีเมื่อโหลดหน้า
    updateDates();
});

// ฟังก์ชัน updateDates สำหรับการอัปเดตวันที่ในกริด
function updateDates() {
    console.log("Date selected");

    // รับค่าจาก input (วันที่ที่ถูกเลือก)
    const input = document.getElementById('startDate').value;
    
    // แยกวันที่จากรูปแบบ dd/mm/yyyy
    const parts = input.split('/');
    const day = parseInt(parts[0], 10);
    const month = parseInt(parts[1], 10) - 1; // เดือนใน JS เริ่มจาก 0
    const year = parseInt(parts[2], 10);

    // สร้าง Date object จากวันที่ที่เลือก
    const startDate = new Date(year, month, day);

    // รับข้อมูล doc.day ที่ส่งมาจาก Django ผ่าน JSON
    const docDays = JSON.parse(document.getElementById('docDaysData').textContent);

    // รับ element ที่จะแสดงผล (dateGrid และช่องของวันที่และชื่อวัน)
    const dateGrid = document.getElementById('dateGrid');

    for (let i = 1; i <= 7; i++) {
        const dateElement = document.getElementById('date' + i);
        const dayElement = document.getElementById('day' + i);
        const containerElement = dayElement.parentElement;
    
        // เพิ่มจำนวนวันไปทีละวันจาก startDate
        const currentDate = new Date(startDate); // เริ่มจาก startDate
        currentDate.setDate(startDate.getDate() + i - 1); // เพิ่มวันตามรอบของลูป
    
        // อัปเดตวันที่ในช่องกริด
        dateElement.textContent = currentDate.getDate();
    
        // อัปเดตชื่อวัน (เช่น Mon, Tue)
        const dayName = currentDate.toLocaleDateString('th-TH', { weekday: 'short' });  // ใช้ชื่อวันเป็นภาษาไทย
        dayElement.textContent = dayName;

        // ตรวจสอบว่า textContent ของวันนั้นอยู่ใน doc.day หรือไม่
        if (!docDays.includes(dayName)) {
            // ถ้าไม่อยู่ในช่วง doc.day, เปลี่ยนสีพื้นหลังของกล่อง
            containerElement.style.backgroundColor = '#EBEBEB';  // เปลี่ยนเป็นสีแดงอ่อน
            containerElement.style.color = '#C8C8C8';  // เปลี่ยนสีข้อความ
        } else {
            // ถ้าอยู่ใน doc.day, ทำให้เป็นสีปกติ
            containerElement.style.backgroundColor = '#E1F6F5';  // เปลี่ยนกลับเป็นสีปกติ
            containerElement.style.color = '#3E5279';  // เปลี่ยนสีข้อความกลับเป็นปกติ
        }
    }
}
