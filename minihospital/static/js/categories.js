const count = 6;

    // วนลูปตามจำนวนที่ต้องการ
    for (let i = 1; i <= count; i++) {
        const hoverArea = document.getElementById("cat" + i);
        const targetImage = document.getElementById("img" + i);

        // ตรวจสอบว่า hoverArea และ targetImage มีอยู่ก่อนที่จะเพิ่ม event listener
        if (hoverArea && targetImage) {
            // เพิ่ม transition ให้ภาพตั้งแต่แรก
            targetImage.classList.add('transition', 'duration-300', 'ease-in-out', 'delay-150');

            // เมื่อเมาส์เข้าไปใน hover-area
            hoverArea.addEventListener('mouseenter', function() {
                targetImage.classList.add('brightness-200');  // เพิ่มคลาส brightness-200
            });

            // เมื่อเมาส์ออกจาก hover-area
            hoverArea.addEventListener('mouseleave', function() {
                targetImage.classList.remove('brightness-200');  // ลบคลาส brightness-200
            });
        }
    }

    const border = document.getElementById('search1');
    const bg = document.getElementById('search2');

    border.addEventListener('mouseenter', function() {
        bg.classList.add('bg-[#15CDCB]');
        bg.classList.add('text-white');
        bg.classList.remove('bg-white');
        bg.classList.remove('text-[#494949]');
    });

    border.addEventListener('mouseleave', function() {
        bg.classList.remove('bg-[#15CDCB]');
        bg.classList.remove('text-white');
        bg.classList.add('bg-white');
        bg.classList.add('text-[#494949]');
    });

