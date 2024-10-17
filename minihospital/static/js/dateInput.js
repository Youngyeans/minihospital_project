
function openDatePicker(inputId) {
    const dateInput = document.getElementById(inputId);
    if (dateInput) {
        dateInput._flatpickr.open();
    }
}

function formatThaiDate(date) {
    const months = [
        "มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", 
        "พฤษภาคม", "มิถุนายน", "กรกฎาคม", "สิงหาคม", 
        "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"
    ];
    const day = date.getDate();
    const month = months[date.getMonth()];
    const year = date.getFullYear() + 543;
    return `วันที่ ${day} ${month} ${year}`;
}


document.addEventListener('DOMContentLoaded', function() {
    const startDateValue = document.getElementById('startDate').value;

    if (startDateValue !== "") {
        const parsedDate = flatpickr.parseDate(startDateValue, "d/m/Y");
        const formattedDate = formatThaiDate(parsedDate);
        document.getElementById("formattedDate").textContent = formattedDate;
    }

    flatpickr("#startDate", {
        dateFormat: "d/m/Y",
        allowInput: true,
        defaultDate: startDateValue !== "" ? startDateValue : null,
        locale: "th",
        onChange: function(selectedDates) {
            if (selectedDates.length > 0) {
                const formattedDate = formatThaiDate(selectedDates[0]);
                document.getElementById("formattedDate").textContent = formattedDate;
                
                updateDates(startDateValue);
            }
        }
    });


    flatpickr("#sympdate", {
        dateFormat: "d/m/Y",
        locale: "th"
    });


    updateDates(startDateValue);
});


function updateDates(startDateValue) {
    console.log("Date selected");


    const input = startDateValue
    
    const parts = input.split('/');
    const day = parseInt(parts[0], 10);
    const month = parseInt(parts[1], 10) - 1;
    const year = parseInt(parts[2], 10);

    const startDate = new Date(year, month, day);
    const docDays = JSON.parse(document.getElementById('docDaysData').textContent);


    for (let i = 1; i <= 7; i++) {
        const dateElement = document.getElementById('date' + i);
        const dayElement = document.getElementById('day' + i);
        const containerElement = dayElement.parentElement;
    
        const currentDate = new Date(startDate);
        currentDate.setDate(startDate.getDate() + i - 1);
    
        dateElement.textContent = currentDate.getDate();
    

        const dayName = currentDate.toLocaleDateString('th-TH', { weekday: 'short' });
        dayElement.textContent = dayName;

        if (!docDays.includes(dayName)) {
            containerElement.style.backgroundColor = '#EBEBEB';
            containerElement.style.color = '#C8C8C8';
        } else {
            containerElement.style.backgroundColor = '#E1F6F5';
            containerElement.style.color = '#3E5279';
        }
    }
}
