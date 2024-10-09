PGDMP  #    4        
    	    |            minihospital    16.3    16.3 -    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    58108    minihospital    DATABASE     �   CREATE DATABASE minihospital WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.874';
    DROP DATABASE minihospital;
                postgres    false            �          0    58146 	   auth_user 
   TABLE DATA           �   COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
    public          postgres    false    226   @)       �          0    58256    authen_department 
   TABLE DATA           5   COPY public.authen_department (id, name) FROM stdin;
    public          postgres    false    235   �2       �          0    58272    authen_doctor 
   TABLE DATA           �   COPY public.authen_doctor (id, phone, address, doctor_image, shift_day, start_time, end_time, description, department_id, prefix, user_id) FROM stdin;
    public          postgres    false    239   A3       �          0    58262    authen_patient 
   TABLE DATA           �   COPY public.authen_patient (id, prefix, gender, nationality, "DOB", height, weight, blood_group, phone, address, allergy, "registrationDate", patient_image, user_id) FROM stdin;
    public          postgres    false    237   l9       �          0    58301    appoint_appointment 
   TABLE DATA           �   COPY public.appoint_appointment (id, appointment_date, appointment_time, created_at, symptom, "start_sympDate", temperature, note, doctor_id, patient_id) FROM stdin;
    public          postgres    false    243   �9       �          0    58132 
   auth_group 
   TABLE DATA           .   COPY public.auth_group (id, name) FROM stdin;
    public          postgres    false    222   :       �          0    58118    django_content_type 
   TABLE DATA           C   COPY public.django_content_type (id, app_label, model) FROM stdin;
    public          postgres    false    218   2:       �          0    58126    auth_permission 
   TABLE DATA           N   COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
    public          postgres    false    220   �:       �          0    58140    auth_group_permissions 
   TABLE DATA           M   COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
    public          postgres    false    224   �=       �          0    58154    auth_user_groups 
   TABLE DATA           A   COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
    public          postgres    false    228   �=       �          0    58160    auth_user_user_permissions 
   TABLE DATA           P   COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
    public          postgres    false    230   M>       �          0    58280    authen_staff 
   TABLE DATA           g   COPY public.authen_staff (id, first_name, last_name, phone, email, address, department_id) FROM stdin;
    public          postgres    false    241   j>       �          0    58321    bill_invoice 
   TABLE DATA           M   COPY public.bill_invoice (id, total, created_at, appointment_id) FROM stdin;
    public          postgres    false    245   �>       �          0    58218    django_admin_log 
   TABLE DATA           �   COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
    public          postgres    false    232   �>       �          0    58110    django_migrations 
   TABLE DATA           C   COPY public.django_migrations (id, app, name, applied) FROM stdin;
    public          postgres    false    216   /C       �          0    58246    django_session 
   TABLE DATA           P   COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
    public          postgres    false    233   sF       �          0    58333    prescribe_medicine 
   TABLE DATA           o   COPY public.prescribe_medicine (id, name, type, price, "stockQuantity", "expiryDate", instruction) FROM stdin;
    public          postgres    false    247   �G       �          0    58341    prescribe_prescription 
   TABLE DATA           n   COPY public.prescribe_prescription (id, "prescriptionDetail", "prescriptionDate", appointment_id) FROM stdin;
    public          postgres    false    249   H       �          0    58349    prescribe_prescriptionmedicines 
   TABLE DATA           o   COPY public.prescribe_prescriptionmedicines (id, quantity, duration, medicine_id, prescription_id) FROM stdin;
    public          postgres    false    251    H       �          0    58373    treat_treatmenttype 
   TABLE DATA           J   COPY public.treat_treatmenttype (id, name, description, cost) FROM stdin;
    public          postgres    false    253   =H       �          0    58381    treat_treatment 
   TABLE DATA           d   COPY public.treat_treatment (id, details, diagnose, appointment_id, "treatmentType_id") FROM stdin;
    public          postgres    false    255   ZH       �           0    0    appoint_appointment_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.appoint_appointment_id_seq', 1, false);
          public          postgres    false    242            �           0    0    auth_group_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.auth_group_id_seq', 2, true);
          public          postgres    false    221            �           0    0    auth_group_permissions_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 10, true);
          public          postgres    false    223            �           0    0    auth_permission_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.auth_permission_id_seq', 68, true);
          public          postgres    false    219            �           0    0    auth_user_groups_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 27, true);
          public          postgres    false    227            �           0    0    auth_user_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.auth_user_id_seq', 30, true);
          public          postgres    false    225            �           0    0 !   auth_user_user_permissions_id_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);
          public          postgres    false    229            �           0    0    authen_department_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.authen_department_id_seq', 6, true);
          public          postgres    false    234            �           0    0    authen_doctor_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.authen_doctor_id_seq', 23, true);
          public          postgres    false    238            �           0    0    authen_patient_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.authen_patient_id_seq', 1, true);
          public          postgres    false    236            �           0    0    authen_staff_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.authen_staff_id_seq', 1, false);
          public          postgres    false    240            �           0    0    bill_invoice_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.bill_invoice_id_seq', 1, false);
          public          postgres    false    244            �           0    0    django_admin_log_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.django_admin_log_id_seq', 61, true);
          public          postgres    false    231            �           0    0    django_content_type_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.django_content_type_id_seq', 17, true);
          public          postgres    false    217            �           0    0    django_migrations_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.django_migrations_id_seq', 38, true);
          public          postgres    false    215            �           0    0    prescribe_medicine_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.prescribe_medicine_id_seq', 1, false);
          public          postgres    false    246            �           0    0    prescribe_prescription_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.prescribe_prescription_id_seq', 1, false);
          public          postgres    false    248            �           0    0 &   prescribe_prescriptionmedicines_id_seq    SEQUENCE SET     U   SELECT pg_catalog.setval('public.prescribe_prescriptionmedicines_id_seq', 1, false);
          public          postgres    false    250            �           0    0    treat_treatment_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.treat_treatment_id_seq', 1, false);
          public          postgres    false    254            �           0    0    treat_treatmenttype_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.treat_treatmenttype_id_seq', 1, false);
          public          postgres    false    252            �   f	  x���k����_{?E^�ݐ�d(Ԗmٖl�7��"Ywْ��o��RHR($�&Bv��4e�I�~�>�l�l2�B�a遙�;��?�<F�B�y���)�U� �4�W1l���=D�Z2\���TW�ֶ�0�	�!w��Z��rd�>�(_uwM�Lǌ:��
ufA ��p��������������a��a��a����3x�]v�=|Ȏ�����8�-/R�?Zՙ�ς��I(�!>�Yƨ2B���?͢�L�nK!�iM]�eGhϋ�~(��H��mʚ�]����Qu��W�nX��#��#� E3��,��O�Û����E��u��";�8�>B&��V��08�<�4�'Vc;]��m<��H�6쮸$[h�-2k��_�("��	?se��bO�rg�I�3	�$����,�����dz��
kÈ�ۑC�,r����d�*+C&��ةJj��R�X�s73�e�v�\��m�u��S����H<�Y�['>G��:�@�%�囬�`�_�W=��wx��1�o�
q�a]�$� 3��	�p� ��$���^OV}��U{z�(ʡK����V"��9���*nbk+*�����>�
��#���a��|�W����3��Y!��h�S-}q|�)��`qS/#H�	�4�9�+��\4�5�ɔY$�4,�`��naŊx��v{��⒂��Z�i<��,q�����(�s"���5龾��"�$�4�yU��� �-^���b��Y}峠b`��Z÷VtkUѱ�(x�6:T7�'����M۝e$y��� �eP�T[�%�O��z���e��ߨ�3[���;�� +�+�n���-�"[�%�J�l�bٴ�%R1��0���t��RO����Wӑ�X��\,�,�@s��g�W��oY��ful�9�_`�]@�fY�LdM
OsT���GaOQQ6��	�'��N-Z%uXtN�Jc!"�҆�h���6�`e��fՉ�3�TVhVV��y�k��|�r���~�1B�Ϗm�s��Aok	p��2=��ܥYR� j���ۍVU.�*1�&��[��8�
�Ĝ��-p.Bu�\�����:� ���y܅#��.?e��U�Ka��+�+��#߹Ce����x].��/��0�Mus��^w�
f�& ��!Cpx-%�V�E���Y��*�'���y����Դ�e̬F7ښ2���.]C�c��Љ5���Re�-�bQ��$��&�VMt3��ٙ ?��� +<�x���>�:{�����P��0�ph���>o��uo�5��)�wRܲi��u�p%b�>��	�i�k�Z�˺0&w��s���<�@�p\������}���߂�H�۫
�HƂ\1���U�o����mz:ب
���MN�]%�Է���5�U�p��.WQ6��K�vd���s<�>~>��������#c�D�Y�PΌy��y���AW�Wt�J%�
�צ���Q��G���TI��i��~s�ʾ���j8��F9v�,��ʛL�O��H�ʗ�}�x��C�U#?x�p��r�OSl�Vrr���L��3��J�Y"v�1D-�+1��r�����ٟu�)��W��f��o=���g�|����s!�9��2�U���%��r���!��q4W$Q�n{�>w����H��:zѐj#�5ݐB��ȴc0_7��t�vW��aW
�5b���Qm��B^��i3��~��������!��	:#�"�<�Q��v��:�{�4�ϋ���K���Rw��L:��J#�M�I�kR�]=h������o.u����)����֕���pz��6Z�ZxerD���3V���z&^�J͢����KbT�r4�f$bV�v;@�yJ5�Iv)J��_�G�	��Sxڴ�JH�S&ϻ]+�������7�|�c��|��$�T:��|gIKMN�@��q1V��_u;L0�l72��+kX��k:�M7�^�V�=���;x(�� N�{�Ah��X�6H}kk�~\(|5I�������Q�ɻ6LA�m�����+֕U1/#K�Ee�3�˶A���%9ـ�R�r�X*��[��W��ﶲ;\�YX6F��G/u��L������~�,Cf�Ld=��B]���;�LEI�xk���x��f"2Lk
�[!f�t����DQ��褲m(&�-����|�-<y�~��ad0��i`��Vs���O\�0���Վ*L�+��eQA:�b���NWѸ"Y��%K�GA�ex~M��7]N/E �p
�ݗ���Uf9p�����"�efǮ���D�{ݰ�5�M�l��d��|��p�~���jY�P*u��D��Jʂ�(����A��И=�dK���*�˫/�K���;�#��a�m��I��>����ٳg�k��V      �   {   x�-�;
�PE��*\A@�Y��� ��H� ��XXH��wvs��}/V�ι��8/�K���O=D,�Ĳ#>2t.Ĥ��R�y+�N֍��`��������Fǅw����]���옛���a>      �     x��X�n�6��B0��l�R�a
tŰ�r���N�&�+I�]թQ%�:h�I���w��n��o�G���E�rl'� ]P�����P��hv�2�Cה0h�A=.���Q���:���35������Y4��]8�c���7k%�^�}��V�}��Z*U�����ٔf�+o��5�[�5:�A��	0��5�A5V�hΒ��G�s�������a0����:<�OA_i
/��@��1�:v��fb4��� ����=���5u�2@@|VP��VZ12ĠxfS�e�l�D�8�J9�8i��r��_���R�Ay����˯���{��ra�\�]�,y��[Ip���i}$0�ȭY���F&kZ9[�@$����X�^���ˋ�1���q�8��!�F����j������_�b��Lk�S�6~:# ̊>��$&���m?��7��8H���Q��2�_��@;���� ������ѫ�<g7"��m�q��`�r���C��-�P��<���fsf��=���V�x��bD��$�G�/Ĳ�K���k�hs"��!��O��/I]�;m����h]dӌ��NY�zX� t��L+6��@y�P}���pp:�u,��O�/�]g���j�q�="��	�A)1�9�{�\C U�S�d'��!6͔'��|�~ �A,����!z<�)�[�QN�ټŽ��3�Ɋg/'�á�p�ΰp��Jy�q�gy�Y��;��~e����_|ѷ���7.,�/]�����3��D%Ita�K�Q�u�*��%a��^4�c`�J���ӿ���M���BS>���#:b�@"�?��	re2պh���nN��D�1�ys��7�d���b�<��7�c}�$�s��b)�kl9@��=Z�-����g����8�;����a焞!T5�LN�]��c����y���	[%�pM�P��x��4����8]�0O���de�,ѩ�s$w)l�`���Ѿ-���ΐ�����>�10���s��C�S)~��ۛ�c�
���7c��e����]3`)VK��n�jys������:��m�0��Ɋ�V�b�b�������|�ɍy�b�D4j��؍�R'PXN�Y1#\rD��ӑ��\���>�I�hĆq�����7���8�����b죥�_[�8$`�bmw�=ah��H�A������Nݫ#�צ@e���.=��q5�_���#�݋�j����ռĦ�$Lѩ�u"����T�2Ʉ����[�sw��	w�9E+��9aA��_Q���@]��a�,�mehD�^���>H�by���Jaq)��Z�o�"r�Ң��K��ƄH��ALx��PW�G'���d�g�w���N�0���$�n�c���܋}���5�$�>�&{8��oy-#ez�����W(�� �߂��E��;.͡7�<��U��~�W0�9V�&q鳋�����u>VyW��6�K_\l�v�~�X�����Vw�������4Ͳ�^+��c����tL��%KoX��4!�?���      �   i   x�3�|�c�ރ�z@�j �`ǖ;�9�lx�����M`ѥvl�4200�"#NCCC=8���i`albjfnai�Y�R���V�	�`d�kh D���\1z\\\ S$(<      �      x������ � �      �       x�3�L�O.�/�2�,H,�L�+����� [m�      �   �   x�u�͊A���0˚���^:=&+Lw�:���ff�{ѪO� E*���5�HS���q�Vq����Iq����p��x����༤�<.I��)����<����n������&�2g� �6����7�)�Yz�~b���g�w�1���?�d��H������p�q��&���� e�v�      �   �  x�u�[��0E��Ud��W���FK#�� �{Ի�PW���b��rnAp����v��c|����.����kC_ r���h(����q� N	X����&����g�,�8��d�7Z΀d�؋�3,	*�*��G�ݒ�c?'W� ����x��	ډ�!�����d���U �������*�@�O'�G���i���K:�>��_;��St5��6��U�d0	���2��4_�E3�Aװ!Y/���i��wa�3a&킑^�T������k�u�9�|aC�N8c6�	�p3��� �5#��em���oh��K�j^��AĤ��DT��[�eIu7��qv7P��/M�A�t'�4R	O�0 )�����s��Wk�N��ɸE�K�&�fA�+�oˢ�"%��4��@$��Ք�L�3��o��lx��i�J�sla8�?�BW��;�>�d�c��J�6�^�o�:��}%.��_��������{cse_�iM}-�5�q����n/��=�k�j9ί ���]���Ff�j���/���g��{?�ŅzWGZ������JS��T�}�A���|\�}�����y�����7��5F
i:\�T����5�BIW�����_~�h���
"�ę�U�%N���@���_���*J��      �   8   x�ű� �XW�ǒ���7ٌ�vBQ�d�b��sb�j��$_�8�~�	�      �   V   x�̹�0�X[k}@/�_��_�zZS��V\�q�ģ'>zcޝ�����@� ! Ā\0�`z�����z�t|�9�着�
a      �      x������ � �      �      x������ � �      �      x������ � �      �   {  x��XMoG=���k�?�c�m/�nB�۰\�俗���%�nP���7��H> |���2b�O���'H��Ooϯ������x|8����o�><���$!GA�+s�{�4���p����������r�8{2
P"Hl�v".�ko�9`ΐ���O5������'��~����?/���3dt�#b�D��B�9�5��@	X�� ���/aG�Q5 G*x���t�����\<���A�J�l��t�8*�L�zy�<����ϭH��;�lrU�V� #@�Y�TV��H,�R��Ab�E����G�����m�t���y���p��/_��wv����T��C���h�)y:X}�[�Eʅ��Q�GƠ�����lOt��T�
�c�#q@����Mk�$�U;5���Y<�wD�N��ѭ�3K�Te*Ǽ�,	��%��1Kƛ3�;F� /A�1�;��iS�b��Z��:�9ue���v
j��%��
�<A��!Q�U(�����S��{�ٰ�Y��(Z~/�F�:�:�Be��eǗ<
�"4�sP �#��w��n�W�&#f����MM��ܺ�կBN3`%�t"�l�,Td	f�x<;�F�`���i��Jl�4Od- OO�Q�f�ag��<AIj��Ib�J�F+V>�J^��S�j� yg��<�m���#��b�	Ȫ_��ӵ�<�y��b�)-�l�WNu�`N����c�ni�d�F^�ԅ�)`�E��/u���1��L��\�k:'^D��Y7�E��"�� �ę�z�䉕Y|��ZD^$O{"��E���Ѕ����Z�i�~�kiW�6��zSL	1�A���,��=�:Y�"�X��L2{���H�8R�{L��v{��"ʽ'Q��3���;W�Z7��q�F`[d�m��p��H�{�FH��ꣽ���n�|�kڭ���A��?:��""�I���qb�m"6�|�"k+���1�4a���F�g���2�'Zl�<��v�Z)gB�)�za���b� 9�"�fya��e���2����Z{U/��)�^�&u�f]����n#���c�S-������趤H4	l�|���Q�{&�� ��jO���c����e=I����9�P��.��+�ǖ�E�?�����=�      �   4  x����n�0��O��U#���<�J�.���:�۾��N��	�8��g��@���v��=ر ��v���i
$�^���Vs^S^R��_D�`aN��c�s�0��uOH�� �v��n�cX���޶��ա~������T��/za�6����~o�Q�?z�l�P�-�v�y5�:~�;��m�aD��?Ԧ��׃��Ǹ��׭�ҍ��W�(��J�(��Ncx��q�C�d�H�V
�)�--��;�(�hj���sFc�)Z���N�v�E���)�RDp������从�mBd��rɧ\��iw0S���}�}�uk���4^�xJ;��6�y`��(U�T���)S���?��,���O�s�Dj;���4��|�����;�P.c3`��w�ݕB�xb�b�KՇ�B��,��k������,QR1�Ay��u�cUr�xs!ŏ%��eXb1x;�{��u�i� -&o��c���A�9����C�CK������Ë�@� )��3)]�֏}��������p~����}6��x���4T�L�6��*���mp6�e��ט�ro j��0W)��2�8�cl/�jG�UZ*��[���]f��\���ϛM� T!��>$H�I䃏Qq6$��Rs�(d u���$Lk:�1�W�V5�2^]Kaz��s]x�v��e��gPR	��P���Y��`����Қ����3Ey��i��0��m	�HXJ;�q���Cֶ��eMEY��&/Л�ߢos�]@oK�p�4�5���wK�Z	dGHMxl3	SN���,��ov�e�C8ii�H����]��������      �   c  x�E��r�0  е~E�wt���$���Z��8@(`A!y|}��=�p��C��^J`3��'+�$��gu���Xd20�����(��d�]��Ja�:�̄ʾs����V��P�����$��`%�o 24��`���2����>u�(T>��Q����>�b���ӝ��p��٭��O��Ʉ��K�lj�fzB=
��)���¦�.����E���j�~�W���[w�r��(	�˒��>�2����x����( S�Z��ʯ)Q9��f�s6���EAZ:>��m���fbTv��ҫ';�Q���k�
��OJ?�^|=z����I��HǊ���[/��ok���      �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �     