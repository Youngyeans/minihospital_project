--
-- PostgreSQL database dump
--

-- Dumped from database version 16.3
-- Dumped by pg_dump version 16.3

-- Started on 2024-10-10 01:57:36


--
-- TOC entry 5042 (class 0 OID 58132)
-- Dependencies: 222
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.auth_group (id, name) VALUES (1, 'doctor');
INSERT INTO public.auth_group (id, name) VALUES (2, 'patient');


--
-- TOC entry 5044 (class 0 OID 58140)
-- Dependencies: 224
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (1, 1, 42);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (2, 1, 43);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (3, 1, 44);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (4, 2, 41);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (5, 2, 42);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (6, 2, 43);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (7, 2, 44);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (8, 2, 25);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (9, 2, 26);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (10, 2, 28);


--
-- TOC entry 5046 (class 0 OID 58146)
-- Dependencies: 226
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (13, 'pbkdf2_sha256$870000$pHI9uJT2gDtTq6ZftBvBIy$mepzV3LOSFPe+Qrgw+hVrgsnC2e2KBjzHOfuW9aSL9I=', NULL, false, '1103201234560', 'สงกรานต์', 'วงศ์กุล', 'songkran@gmail.com', false, true, '2024-10-08 16:37:15+07');
INSERT INTO public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (14, 'pbkdf2_sha256$870000$ZC9RhJPxC16JuDamEViLJl$TRpVOErVdRJ7gXLn+oJyK5kkfrBcJdvjzT/bJUPCE10=', NULL, false, '1103304567893', 'ธวัช', 'อินทรพิทักษ์', 'thawat@gmail.com', false, true, '2024-10-08 16:40:37+07');
INSERT INTO public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (15, 'pbkdf2_sha256$870000$C4tgFyYqDVysTND6ZKoxCz$yLPhLJKSy1cH2un/UU75ughXKcjVaGB3SkPTdVMybPM=', NULL, false, '1609801234566', 'วีระ', 'ทองทวี', 'weera@gmail.com', false, true, '2024-10-08 16:47:19+07');
INSERT INTO public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (16, 'pbkdf2_sha256$870000$mZPgcAveV6HtOMELZue25Z$PCOkjxcbjCHhF6wUuyR6pdjNQahEWgSn1sYhC0KLyis=', NULL, false, '1306704567897', 'สุภาพร', 'คำแก้ว', 'supaporn@gmail.com', false, true, '2024-10-09 00:31:56+07');
INSERT INTO public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (6, 'pbkdf2_sha256$870000$uMefPPRHVdEtvRiANaQdBe$Vpj5sKq6GbItLaKfULG/ZjZjthbv7rKSx/W1SJ3v4l8=', NULL, false, '1109801234567', 'ภูมิ', 'ประเสริฐศักดิ์', 'phoom@gmail.com', false, true, '2024-10-08 16:14:11+07');
INSERT INTO public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (18, 'pbkdf2_sha256$870000$fX4AWrfwSb0bHGXY9mtaPT$j0w3e5zmgsZO+dChJxzN4PZ3WnDRiFSk8h3gOqbpbG4=', NULL, false, '1701201234564', 'ก้องภพ', 'สุทธิชัย', 'kongpop@gmail.com', false, true, '2024-10-09 00:34:39+07');
INSERT INTO public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (19, 'pbkdf2_sha256$870000$sCdvnC0Ae3eenjbFngv8Iv$O2We9Z4EGTFM7I4fe1n6SGLmN+YJMqrPkG7tR8mZ92Y=', NULL, false, '1102604567895', 'สุชาติ', 'ธนศักดิ์', 'suchart@gmail.com', false, true, '2024-10-09 00:37:06+07');
INSERT INTO public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (5, 'pbkdf2_sha256$870000$Fuo4algk75F7CAQtdvPxxL$Q1Uh8nGe/6Ze1M7t9PfqxMicqdt9sFwlBuUdRoC4QZs=', NULL, false, '1209804567892', 'สมชาย', 'จันทร์สุข', 'somchai@gmail.com', false, true, '2024-10-08 16:06:57+07');
INSERT INTO public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (20, 'pbkdf2_sha256$870000$AT3T3BTUpQZa2CtEOt0RtD$zLOg8a6dX4AisvusLr5+uFVFJvPFGRox7SvgvbHBisk=', NULL, false, '1505501234562', 'กิตติตยา', 'จินดามณี', 'kitti2@gmail.com', false, true, '2024-10-09 00:39:50+07');
INSERT INTO public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (4, 'pbkdf2_sha256$870000$BOlj8C6Lb02fzi0tWJFIBV$vAe5YGXrVsjynCWQGZgp9uJXWCy0jiGr2d0bSjjR1eY=', NULL, false, '100701234561', 'มิจิ', 'ย้าวยาว', 'miji@gmail.com', false, true, '2024-10-08 16:03:59+07');
INSERT INTO public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (7, 'pbkdf2_sha256$870000$zjTZwaUVQWwBoFAGpc56U4$pPTpSVH0oTdfz2skNmuLfoCt0psRp95G4Du5qgtswO4=', NULL, false, '1104501234569', 'กิตติ', 'จินดามณี', 'kitti@gmail.com', false, true, '2024-10-08 16:16:39+07');
INSERT INTO public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (8, 'pbkdf2_sha256$870000$HgsS7ecgFNryfV4zBdj8D1$g9enpTisb6HbdPAlN/DsOakZK/PuL07Xr8jBf2xTndc=', NULL, false, '1406701234563', 'มณี', 'สุวรรณรักษ์', 'mani@gmail.com', false, true, '2024-10-08 16:18:40+07');
INSERT INTO public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (9, 'pbkdf2_sha256$870000$RKgDwEkXNpb7IpK7fLdAjX$yCuQRowdZ5jP5lrjnCC+LwYoqODCwZlVdLW5ZjWbOl0=', NULL, false, '1508704567890', 'อรพินท์', 'ศรีสุวรรณ', 'arapin@gmail.com', false, true, '2024-10-08 16:20:10+07');
INSERT INTO public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (10, 'pbkdf2_sha256$870000$XKQOB6KHjRSjNHkd0xaZ1i$qkh6YjzAtXEyFuCdbfIAXGPKp8JNGAZxxCIztSmJre0=', NULL, false, '1201204567894', 'วิรัชญา', 'กิตติชัย', 'wirat@gmail.com', false, true, '2024-10-08 16:22:34+07');
INSERT INTO public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (11, 'pbkdf2_sha256$870000$9ckaYikqoNdEAdysTtFA8k$wfbIkErQhKUkhHpVuLO64jd80iOnHXjVnitOJBpYYo8=', NULL, false, '1103701234568', 'อรอนงค์', 'ธำรงสุข', 'arnon@gmail.com', false, true, '2024-10-08 16:24:30+07');
INSERT INTO public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (12, 'pbkdf2_sha256$870000$ydItpGVp2652nIf9RzeHJA$iq1hDFT15br+/9VfIjpUTkNsr6RcN3YGydv1kwCncng=', NULL, false, '1405501234565', 'ปวีณา', 'ภิรมย์รักษ์', 'pavina@gmail.com', false, true, '2024-10-08 16:32:42+07');
INSERT INTO public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (21, 'pbkdf2_sha256$870000$Z8NsskidUWN5TVZQ6iJjid$ePDUijfjp728EUfhs0lwF6WYywjvsfn6pNPo0gUCEjc=', NULL, false, '1201704567896', 'สมพร', 'รัตนสกุล', 'somporn@gmail.com', false, true, '2024-10-09 00:40:58+07');
INSERT INTO public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (22, 'pbkdf2_sha256$870000$lrn2j8bzX0Kz18osQuPlll$0K7wq8eUaD/NxiV9ulKdAFrcXVXEGH7JzEoInOdinzE=', NULL, false, '1104501234570', 'อัญชลี', 'จินดามณี', 'anchalee@gmail.com', false, true, '2024-10-09 00:42:01+07');
INSERT INTO public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (17, 'pbkdf2_sha256$870000$r4jQMj39WaR9aRLQf4EYPH$O4uKY6WPF5zoBSGqUXSzc61fAJhJo15lu65DKH6N7Oc=', '2024-10-09 04:32:51.407318+07', false, '1102404567891', 'จารุวรรณ', 'พรชัย', 'jaruwan@gmail.com', false, true, '2024-10-09 00:33:40+07');
INSERT INTO public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (1, 'pbkdf2_sha256$870000$PP6ZMWDlzgPqbVuroPXLxW$saZJnBjM9oSMyxG1SlhvgTBrWmgYlDYxcQAhZRQiGK0=', '2024-10-09 23:50:03.291841+07', true, 'youngyeans', '', '', 'nattanicha.suw@gmail.com', true, true, '2024-10-08 09:12:15.975027+07');
INSERT INTO public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (25, 'pbkdf2_sha256$870000$tWqrgOVOZliuc9NCJ0QjUQ$/Vtx0xqPbL6w9ga5zKIthKAfI6dzyVZsiGtxmgh36Uk=', NULL, false, '1102701234569', 'dcdz', 'dvdv', 'miji@gmail.com', false, true, '2024-10-09 03:57:54+07');
INSERT INTO public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (23, 'pbkdf2_sha256$870000$EaWfg8jhzG6uOPPPKgyQWs$swbccO1TuDZKzv1frHjEoqCMrr/GSv8tAyFZf4GqiZk=', NULL, false, '1102701234568', 'ปรีชา', 'พิทักษ์สกุล', 'preecha@gmail.com', false, true, '2024-10-09 03:56:26+07');
INSERT INTO public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (26, 'pbkdf2_sha256$870000$OmecpoQiGVBMaLX7FCVaRq$Z1MPZgInUGjYvrWI0rVV32qC7wUo/IeknDLkiVQYqY8=', NULL, false, '1219900847472', 'ภูมิ', 'ประเสริฐศักดิ์', 'kitti@gmail.com', false, true, '2024-10-09 04:07:19.809831+07');
INSERT INTO public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (30, 'pbkdf2_sha256$870000$mXdKQNpINeqHO6JuUtl9VK$NmjTnE/baasrgPTP/NgYv/7JnAuC0DUunR0Ax1nRLFc=', NULL, false, '1219900847471', 'ยองยีน', 'ยอดยาหยี', '', false, true, '2024-10-10 00:10:20.246595+07');


--
-- TOC entry 5048 (class 0 OID 58154)
-- Dependencies: 228
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.auth_user_groups (id, user_id, group_id) VALUES (3, 4, 1);
INSERT INTO public.auth_user_groups (id, user_id, group_id) VALUES (4, 5, 1);
INSERT INTO public.auth_user_groups (id, user_id, group_id) VALUES (5, 6, 1);
INSERT INTO public.auth_user_groups (id, user_id, group_id) VALUES (6, 7, 1);
INSERT INTO public.auth_user_groups (id, user_id, group_id) VALUES (7, 8, 1);
INSERT INTO public.auth_user_groups (id, user_id, group_id) VALUES (8, 9, 1);
INSERT INTO public.auth_user_groups (id, user_id, group_id) VALUES (9, 10, 1);
INSERT INTO public.auth_user_groups (id, user_id, group_id) VALUES (10, 11, 1);
INSERT INTO public.auth_user_groups (id, user_id, group_id) VALUES (11, 12, 1);
INSERT INTO public.auth_user_groups (id, user_id, group_id) VALUES (12, 13, 1);
INSERT INTO public.auth_user_groups (id, user_id, group_id) VALUES (13, 14, 1);
INSERT INTO public.auth_user_groups (id, user_id, group_id) VALUES (14, 15, 1);
INSERT INTO public.auth_user_groups (id, user_id, group_id) VALUES (15, 16, 1);
INSERT INTO public.auth_user_groups (id, user_id, group_id) VALUES (16, 17, 1);
INSERT INTO public.auth_user_groups (id, user_id, group_id) VALUES (17, 18, 1);
INSERT INTO public.auth_user_groups (id, user_id, group_id) VALUES (18, 19, 1);
INSERT INTO public.auth_user_groups (id, user_id, group_id) VALUES (19, 20, 1);
INSERT INTO public.auth_user_groups (id, user_id, group_id) VALUES (20, 21, 1);
INSERT INTO public.auth_user_groups (id, user_id, group_id) VALUES (21, 22, 1);
INSERT INTO public.auth_user_groups (id, user_id, group_id) VALUES (22, 25, 1);
INSERT INTO public.auth_user_groups (id, user_id, group_id) VALUES (23, 23, 1);
INSERT INTO public.auth_user_groups (id, user_id, group_id) VALUES (24, 26, 1);
INSERT INTO public.auth_user_groups (id, user_id, group_id) VALUES (27, 30, 2);


--
-- TOC entry 5050 (class 0 OID 58160)
-- Dependencies: 230
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 5055 (class 0 OID 58256)
-- Dependencies: 235
-- Data for Name: authen_department; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.authen_department (id, name) VALUES (1, 'กระดูก');
INSERT INTO public.authen_department (id, name) VALUES (2, 'เด็ก');
INSERT INTO public.authen_department (id, name) VALUES (3, 'ตา หู คอ จมูก');
INSERT INTO public.authen_department (id, name) VALUES (4, 'ผิวหนัง');
INSERT INTO public.authen_department (id, name) VALUES (5, 'โรคทั่วไป');
INSERT INTO public.authen_department (id, name) VALUES (6, 'ผู้หญิง');


--
-- TOC entry 5059 (class 0 OID 58272)
-- Dependencies: 239
-- Data for Name: authen_doctor; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.authen_doctor (id, phone, address, doctor_image, shift_day, start_time, end_time, description, department_id, prefix, user_id) VALUES (21, '0876543210', 'นครราชสีมา, ประเทศไทย', 'images/doctor/Screenshot_2024-05-26_225842.png', 'จันทร์ - ศุกร์', '09:00:00', '17:00:00', 'แพทย์ผู้เชี่ยวชาญด้านโรคผิวหนังและการรักษาความงาม', 4, 'นพ.', 23);
INSERT INTO public.authen_doctor (id, phone, address, doctor_image, shift_day, start_time, end_time, description, department_id, prefix, user_id) VALUES (2, '084-562-8080', 'มิจิ จังหวัดมิจิ', 'images/doctor/College_Life_As_Told_By_20_Gavin_Memes.jpg', 'จันทร์-ศุกร์', '09:00:00', '16:00:00', 'แพทย์ผู้เชี่ยวชาญด้านมิจิ', 6, 'นพ.', 4);
INSERT INTO public.authen_doctor (id, phone, address, doctor_image, shift_day, start_time, end_time, description, department_id, prefix, user_id) VALUES (3, '0812345678', 'กรุงเทพฯ', 'images/doctor/s.PNG', 'จันทร์-ศุกร์', '09:00:00', '17:00:00', 'ผู้เชี่ยวชาญด้านกระดูกและข้อ และการออกกำลังกายขั้นปรมาจารย์', 1, 'นพ.', 5);
INSERT INTO public.authen_doctor (id, phone, address, doctor_image, shift_day, start_time, end_time, description, department_id, prefix, user_id) VALUES (5, '0834567890', 'นครปฐม', 'images/doctor/dk.PNG', 'จันทร์-ศุกร์', '08:30:00', '17:30:00', 'ให้คำปรึกษาเกี่ยวกับกระดูกและกล้ามเนื้อ', 1, 'นพ.', 7);
INSERT INTO public.authen_doctor (id, phone, address, doctor_image, shift_day, start_time, end_time, description, department_id, prefix, user_id) VALUES (22, '0898341682', 'dvsdvsd', 'images/doctor/p.jpg', 'จันทร์-ศุกร์', '03:57:00', '23:16:00', 'vsdvsdvs', 2, 'นพ.', 25);
INSERT INTO public.authen_doctor (id, phone, address, doctor_image, shift_day, start_time, end_time, description, department_id, prefix, user_id) VALUES (6, '0845678901', 'ขอนแก่น', 'images/doctor/p.PNG', 'จันทร์-ศุกร์', '08:00:00', '16:00:00', 'เชี่ยวชาญด้านการรักษาเด็กทุกช่วงวัย และความสวย', 2, 'พญ.', 8);
INSERT INTO public.authen_doctor (id, phone, address, doctor_image, shift_day, start_time, end_time, description, department_id, prefix, user_id) VALUES (7, '0856789012', 'ชลบุรี', 'images/doctor/ru.PNG', 'อังคาร-อาทิตย์', '10:00:00', '18:00:00', 'เชี่ยวชาญด้านโรคในเด็กและทารก และมิจิ', 2, 'พญ.', 9);
INSERT INTO public.authen_doctor (id, phone, address, doctor_image, shift_day, start_time, end_time, description, department_id, prefix, user_id) VALUES (8, '0867890123', 'เชียงใหม่', 'images/doctor/a.PNG', 'จันทร์-เสาร์', '09:00:00', '17:00:00', 'รักษาโรคเด็กและภูมิแพ้ในเด็ก และสกิบบิดี้', 2, 'พญ.', 10);
INSERT INTO public.authen_doctor (id, phone, address, doctor_image, shift_day, start_time, end_time, description, department_id, prefix, user_id) VALUES (9, '0878901234', 'สุราษฎร์ธานี', 'images/doctor/tang.PNG', 'จันทร์-ศุกร์', '09:30:00', '17:30:00', 'ผู้เชี่ยวชาญด้านหู คอ จมูก และการเล่นต้อกๆ', 3, 'พญ.', 11);
INSERT INTO public.authen_doctor (id, phone, address, doctor_image, shift_day, start_time, end_time, description, department_id, prefix, user_id) VALUES (10, '0889012345', 'นครศรีธรรมราช', 'images/doctor/jn.PNG', 'พุธ-เสาร์', '09:00:00', '17:00:00', 'แพทย์เฉพาะทางด้านตาและการได้ยิน และการเต้นขั้นดาวต้อกๆ', 3, 'พญ.', 12);
INSERT INTO public.authen_doctor (id, phone, address, doctor_image, shift_day, start_time, end_time, description, department_id, prefix, user_id) VALUES (11, '0890123456', 'อุดรธานี', 'images/doctor/tk.PNG', 'อังคาร-ศุกร์', '10:00:00', '18:00:00', 'เชี่ยวชาญด้านการผ่าตัดหู คอ จมูก และการทำเซิร์ฟมายคราฟ', 3, 'นพ.', 13);
INSERT INTO public.authen_doctor (id, phone, address, doctor_image, shift_day, start_time, end_time, description, department_id, prefix, user_id) VALUES (12, '0901234567', 'ระยอง', 'images/doctor/ex.PNG', 'พุธ-อาทิตย์', '09:30:00', '17:30:00', 'แพทย์ผิวหนังที่เชี่ยวชาญด้านการรักษาสิว และการร้องเพลง', 4, 'นพ.', 14);
INSERT INTO public.authen_doctor (id, phone, address, doctor_image, shift_day, start_time, end_time, description, department_id, prefix, user_id) VALUES (13, '0912345678', 'ลำปาง', 'images/doctor/m.PNG', 'จันทร์-ศุกร์', '09:00:00', '17:00:00', 'ผู้เชี่ยวชาญด้านโรคผิวหนังและการแพ้ และการเล่น roblox', 4, 'นพ.', 15);
INSERT INTO public.authen_doctor (id, phone, address, doctor_image, shift_day, start_time, end_time, description, department_id, prefix, user_id) VALUES (14, '0923456789', 'เชียงราย', 'images/doctor/yy.PNG', 'อังคาร-เสาร์', '09:00:00', '16:00:00', 'เชี่ยวชาญด้านการรักษาผิวหนังและเลเซอร์ และการเล่น dress to impress', 4, 'พญ.', 16);
INSERT INTO public.authen_doctor (id, phone, address, doctor_image, shift_day, start_time, end_time, description, department_id, prefix, user_id) VALUES (15, '0934567890', 'พัทลุง', 'images/doctor/Toon.PNG', 'จันทร์-ศุกร์', '08:00:00', '16:00:00', 'แพทย์ทั่วไปให้คำปรึกษาทางการแพทย์ และการแต่งตัวคุมธีม', 5, 'พญ.', 17);
INSERT INTO public.authen_doctor (id, phone, address, doctor_image, shift_day, start_time, end_time, description, department_id, prefix, user_id) VALUES (16, '0945678901', 'กรุงเทพฯ', 'images/doctor/z.PNG', 'จันทร์-เสาร์', '09:00:00', '17:00:00', 'รักษาโรคทั่วไปและให้คำแนะนำในการดูแลสุขภาพ และการเล่น ทาวเวอร์ดีเฟ้น', 5, 'นพ.', 18);
INSERT INTO public.authen_doctor (id, phone, address, doctor_image, shift_day, start_time, end_time, description, department_id, prefix, user_id) VALUES (17, '0956789012', 'นนทบุรี', 'images/doctor/tew.PNG', 'อังคาร-ศุกร์', '10:00:00', '18:00:00', 'แพทย์ทั่วไปที่เชี่ยวชาญด้านโรคเรื้อรัง และการเล่น วาโลแง้น', 5, 'นพ.', 19);
INSERT INTO public.authen_doctor (id, phone, address, doctor_image, shift_day, start_time, end_time, description, department_id, prefix, user_id) VALUES (18, '0967890123', 'สมุทรปราการ', 'images/doctor/wonyoung.PNG', 'จันทร์-ศุกร์', '08:30:00', '17:30:00', 'เชี่ยวชาญด้านสุขภาพสตรี และ IT GIRL GEN4', 6, 'พญ.', 20);
INSERT INTO public.authen_doctor (id, phone, address, doctor_image, shift_day, start_time, end_time, description, department_id, prefix, user_id) VALUES (19, '0978901234', 'สงขลา', 'images/doctor/karina.PNG', 'อังคาร-เสาร์', '09:00:00', '17:00:00', 'เชี่ยวชาญด้านการดูแลสุขภาพสตรีและตั้งครรภ์ และความเหมียว', 6, 'พญ.', 21);
INSERT INTO public.authen_doctor (id, phone, address, doctor_image, shift_day, start_time, end_time, description, department_id, prefix, user_id) VALUES (20, '0989012345', 'ขอนแก่น', 'images/doctor/sakura.PNG', 'พุธ-อาทิตย์', '10:00:00', '18:00:00', 'เชี่ยวชาญด้านการผ่าตัดเฉพาะทางในสตรี และไอดอลประสบการณ์ 10 ปี', 6, 'พญ.', 22);
INSERT INTO public.authen_doctor (id, phone, address, doctor_image, shift_day, start_time, end_time, description, department_id, prefix, user_id) VALUES (4, '0823456789', 'พิษณุโลก', 'images/doctor/tae.PNG', 'พฤหัส-เสาร์', '09:00:00', '17:00:00', 'ผู้เชี่ยวชาญด้านการรักษากระดูกและข้อ และการเปลี่ยน อินโทรเวิร์ด เป็น เอ็กโทรเวิร์ด', 1, 'นพ.', 6);
INSERT INTO public.authen_doctor (id, phone, address, doctor_image, shift_day, start_time, end_time, description, department_id, prefix, user_id) VALUES (23, '0834567890', 'fvsfv', 'images/doctor/65070066_05.gif', 'พุธ-อาทิตย์', '09:07:00', '17:07:00', 'sfvsdsd', 3, 'นพ.', 26);


--
-- TOC entry 5057 (class 0 OID 58262)
-- Dependencies: 237
-- Data for Name: authen_patient; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.authen_patient (id, prefix, gender, nationality, "DOB", height, weight, blood_group, phone, address, allergy, "registrationDate", patient_image, user_id) VALUES (1, 'ด.ญ.', 'หญิง', 'เกาหลี', '2002-02-20', 111.00, 111.00, 'AB-', '0834567890', 'sdsdffs', '', '2024-10-10', '', 30);


--
-- TOC entry 5061 (class 0 OID 58280)
-- Dependencies: 241
-- Data for Name: authen_staff; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 5065 (class 0 OID 58321)
-- Dependencies: 245
-- Data for Name: bill_invoice; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 5052 (class 0 OID 58218)
-- Dependencies: 232
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (1, '2024-10-08 09:16:16.627102+07', '1', 'doctor', 1, '[{"added": {}}]', 3, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (2, '2024-10-08 09:16:24.864103+07', '1', 'doctor', 2, '[]', 3, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (3, '2024-10-08 09:17:36.650713+07', '2', 'patient', 1, '[{"added": {}}]', 3, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (4, '2024-10-08 09:29:12.096046+07', '2', 'doc1', 1, '[{"added": {}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (5, '2024-10-08 09:29:38.188072+07', '2', 'doc1', 2, '[{"changed": {"fields": ["Groups"]}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (6, '2024-10-08 09:30:11.272057+07', '3', 'patient1', 1, '[{"added": {}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (7, '2024-10-08 09:30:19.120247+07', '3', 'patient1', 2, '[{"changed": {"fields": ["Groups"]}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (8, '2024-10-08 11:32:55.036291+07', '3', 'patient1', 2, '[{"changed": {"fields": ["password"]}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (9, '2024-10-08 11:34:23.402209+07', '3', 'patient1', 2, '[]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (10, '2024-10-08 15:56:51.824352+07', '2', 'doc1', 3, '', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (11, '2024-10-08 15:56:56.613016+07', '3', 'patient1', 3, '', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (12, '2024-10-08 16:04:00.88593+07', '4', '100701234561', 1, '[{"added": {}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (13, '2024-10-08 16:06:19.980302+07', '4', '100701234561', 2, '[{"changed": {"fields": ["First name", "Last name", "Email address", "Groups"]}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (14, '2024-10-08 16:06:57.705921+07', '5', '1209804567892', 1, '[{"added": {}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (15, '2024-10-08 16:08:31.517309+07', '5', '1209804567892', 2, '[{"changed": {"fields": ["First name", "Last name", "Email address", "Groups"]}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (16, '2024-10-08 16:14:12.416789+07', '6', '1109801234567', 1, '[{"added": {}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (17, '2024-10-08 16:15:36.115898+07', '6', '1109801234567', 2, '[{"changed": {"fields": ["First name", "Last name", "Email address", "Groups"]}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (18, '2024-10-08 16:15:49.950712+07', '5', '1209804567892', 2, '[{"changed": {"fields": ["password"]}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (19, '2024-10-08 16:15:52.188868+07', '5', '1209804567892', 2, '[]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (20, '2024-10-08 16:16:02.084819+07', '5', '1209804567892', 2, '[{"changed": {"fields": ["password"]}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (21, '2024-10-08 16:16:04.503176+07', '5', '1209804567892', 2, '[]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (22, '2024-10-08 16:16:40.409271+07', '7', '1104501234569', 1, '[{"added": {}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (23, '2024-10-08 16:17:32.53024+07', '7', '1104501234569', 2, '[{"changed": {"fields": ["First name", "Last name", "Email address", "Groups"]}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (24, '2024-10-08 16:17:58.727412+07', '4', '100701234561', 2, '[{"changed": {"fields": ["password"]}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (25, '2024-10-08 16:18:01.231721+07', '4', '100701234561', 2, '[]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (26, '2024-10-08 16:18:11.60311+07', '7', '1104501234569', 2, '[{"changed": {"fields": ["password"]}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (27, '2024-10-08 16:18:13.929072+07', '7', '1104501234569', 2, '[]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (28, '2024-10-08 16:18:41.049423+07', '8', '1406701234563', 1, '[{"added": {}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (29, '2024-10-08 16:19:22.554089+07', '8', '1406701234563', 2, '[{"changed": {"fields": ["First name", "Last name", "Email address", "Groups"]}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (30, '2024-10-08 16:20:11.670193+07', '9', '1508704567890', 1, '[{"added": {}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (31, '2024-10-08 16:21:02.384294+07', '9', '1508704567890', 2, '[{"changed": {"fields": ["First name", "Last name", "Email address", "Groups"]}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (32, '2024-10-08 16:22:35.592036+07', '10', '1201204567894', 1, '[{"added": {}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (33, '2024-10-08 16:23:45.126606+07', '10', '1201204567894', 2, '[{"changed": {"fields": ["First name", "Last name", "Email address", "Groups"]}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (34, '2024-10-08 16:24:31.874679+07', '11', '1103701234568', 1, '[{"added": {}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (35, '2024-10-08 16:26:18.930589+07', '11', '1103701234568', 2, '[{"changed": {"fields": ["First name", "Last name", "Email address", "Groups"]}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (36, '2024-10-08 16:32:42.954834+07', '12', '1405501234565', 1, '[{"added": {}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (37, '2024-10-08 16:36:04.940577+07', '12', '1405501234565', 2, '[{"changed": {"fields": ["First name", "Last name", "Email address", "Groups"]}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (38, '2024-10-08 16:37:16.337824+07', '13', '1103201234560', 1, '[{"added": {}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (39, '2024-10-08 16:38:43.53181+07', '13', '1103201234560', 2, '[{"changed": {"fields": ["First name", "Last name", "Email address", "Groups"]}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (40, '2024-10-08 16:40:38.473685+07', '14', '1103304567893', 1, '[{"added": {}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (41, '2024-10-08 16:45:22.819304+07', '14', '1103304567893', 2, '[{"changed": {"fields": ["First name", "Last name", "Email address", "Groups"]}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (42, '2024-10-08 16:47:19.821317+07', '15', '1609801234566', 1, '[{"added": {}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (43, '2024-10-08 16:48:24.80358+07', '15', '1609801234566', 2, '[{"changed": {"fields": ["First name", "Last name", "Email address", "Groups"]}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (44, '2024-10-09 00:31:57.453277+07', '16', '1306704567897', 1, '[{"added": {}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (45, '2024-10-09 00:32:34.361719+07', '16', '1306704567897', 2, '[{"changed": {"fields": ["First name", "Last name", "Email address", "Groups"]}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (46, '2024-10-09 00:33:40.923944+07', '17', '1102404567891', 1, '[{"added": {}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (47, '2024-10-09 00:34:13.673506+07', '17', '1102404567891', 2, '[{"changed": {"fields": ["First name", "Last name", "Email address", "Groups"]}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (48, '2024-10-09 00:34:40.780617+07', '18', '1701201234564', 1, '[{"added": {}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (49, '2024-10-09 00:35:20.616623+07', '18', '1701201234564', 2, '[{"changed": {"fields": ["First name", "Last name", "Email address", "Groups"]}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (50, '2024-10-09 00:37:07.326702+07', '19', '1102604567895', 1, '[{"added": {}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (51, '2024-10-09 00:37:43.080946+07', '19', '1102604567895', 2, '[{"changed": {"fields": ["First name", "Last name", "Email address", "Groups"]}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (52, '2024-10-09 00:39:51.453118+07', '20', '1505501234562', 1, '[{"added": {}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (53, '2024-10-09 00:40:24.161211+07', '20', '1505501234562', 2, '[{"changed": {"fields": ["First name", "Last name", "Email address", "Groups"]}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (54, '2024-10-09 00:40:59.59484+07', '21', '1201704567896', 1, '[{"added": {}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (55, '2024-10-09 00:41:32.364882+07', '21', '1201704567896', 2, '[{"changed": {"fields": ["First name", "Last name", "Email address", "Groups"]}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (56, '2024-10-09 00:42:02.494246+07', '22', '1104501234570', 1, '[{"added": {}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (57, '2024-10-09 00:42:37.277619+07', '22', '1104501234570', 2, '[{"changed": {"fields": ["First name", "Last name", "Email address", "Groups"]}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (58, '2024-10-09 04:03:32.633593+07', '25', '1102701234569', 2, '[{"changed": {"fields": ["Groups"]}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (59, '2024-10-09 04:03:41.466733+07', '23', '1102701234568', 2, '[{"changed": {"fields": ["Groups"]}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (60, '2024-10-09 23:50:22.403572+07', '27', '1219900847471', 3, '', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (61, '2024-10-10 00:10:01.980089+07', '28', '1219900847471', 3, '', 4, 1);



--
-- TOC entry 5053 (class 0 OID 58246)
-- Dependencies: 233
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('d7814pru2b1pz6noditbglmxudmp5ibs', 'e30:1syHoF:hHeVCWLLltisGrmSAzDE3NKRNUq_bDq8S7uRixv_9mU', '2024-10-23 04:31:59.140998+07');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('gypr4nzw4gkuex89nh6ryvzx736hodfr', '.eJxVjDsOwjAQBe_iGlnrb2xKes5grXcdHECOFCcV4u4QKQW0b2beSyTc1pq2XpY0sTgLJU6_W0Z6lLYDvmO7zZLmti5TlrsiD9rldebyvBzu30HFXr-19yajt7aQNz4E0DyUSJqNGkgZcD6rEUE7ChwKWQAVgrOsmU1EiKN4fwDHGDc9:1syaCb:lHSdIEZM3KDdEsaqpyu7dlShCGtwM3s5uxxMaTSMESM', '2024-10-24 00:10:21.489556+07');



-- Completed on 2024-10-10 01:57:36

--
-- PostgreSQL database dump complete
--

