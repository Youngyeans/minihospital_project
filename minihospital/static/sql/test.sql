PGDMP                   	    |            minihospital    16.3    16.3 -    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    58108    minihospital    DATABASE     �   CREATE DATABASE minihospital WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.874';
    DROP DATABASE minihospital;
                postgres    false            �          0    58301    appoint_appointment 
   TABLE DATA                 public          postgres    false    243   !       �          0    58132 
   auth_group 
   TABLE DATA                 public          postgres    false    222   9!       �          0    58140    auth_group_permissions 
   TABLE DATA                 public          postgres    false    224   �!       �          0    58126    auth_permission 
   TABLE DATA                 public          postgres    false    220   G"       �          0    58146 	   auth_user 
   TABLE DATA                 public          postgres    false    226   �%       �          0    58154    auth_user_groups 
   TABLE DATA                 public          postgres    false    228   �/       �          0    58160    auth_user_user_permissions 
   TABLE DATA                 public          postgres    false    230   �0       �          0    58256    authen_department 
   TABLE DATA                 public          postgres    false    235   �0       �          0    58272    authen_doctor 
   TABLE DATA                 public          postgres    false    239   �1       �          0    58262    authen_patient 
   TABLE DATA                 public          postgres    false    237   �8       �          0    58280    authen_staff 
   TABLE DATA                 public          postgres    false    241   �9       �          0    58321    bill_invoice 
   TABLE DATA                 public          postgres    false    245   �9       �          0    58218    django_admin_log 
   TABLE DATA                 public          postgres    false    232   �9       �          0    58118    django_content_type 
   TABLE DATA                 public          postgres    false    218   j?       �          0    58110    django_migrations 
   TABLE DATA                 public          postgres    false    216   �@       �          0    58246    django_session 
   TABLE DATA                 public          postgres    false    233   ^D       �          0    58333    prescribe_medicine 
   TABLE DATA                 public          postgres    false    247   F       �          0    58341    prescribe_prescription 
   TABLE DATA                 public          postgres    false    249   4F       �          0    58349    prescribe_prescriptionmedicines 
   TABLE DATA                 public          postgres    false    251   NF       �          0    58381    treat_treatment 
   TABLE DATA                 public          postgres    false    255   hF       �          0    58373    treat_treatmenttype 
   TABLE DATA                 public          postgres    false    253   �F       �           0    0    appoint_appointment_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.appoint_appointment_id_seq', 1, false);
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
          public          postgres    false    252            �   
   x���          �   X   x���v
Q���W((M��L�K,-ɈO/�/-P��L�Q�K�M�Ts�	uV�0�QPO�O.�/R״��$U�P{AbIfj^	H? O'B      �   �   x���v
Q���W((M��L�K,-ɈO/�/-�/H-��,.���+V��L�Q��X) WS!��'�5XA�PG�L�4��<�l��hcm1ڄF��( nbH�M!F�"�� F�"��!F�"�-�F���hK��f40�� b��l.. r',�      �   @  x���Mk�@���{K�X�6=��C��Ф�E�$�X���_i5k�̮o}}�X�y`^9�����ݯ's����ԇ��"����]m�}ѶEU��"��2�ۉɪ��e��>k��Y���[��ۏ�w��&����ii�<7�ի�o>�'f���]?G�_���7|F��--_m��X�9)���v��8�*,Hᣰ�a��/YN���(l��dJ�b-sXP����el�eixm�Cݳ���3��Le8���'r�Nk�g|����٦�mz��>B��gƥ5��K�e��%��+�cv+�a�l������K�4��Ⱁ�h���&[���	� m2��8D<\,�������YQ0��V�O�)P��� � * :�Ļ�C��]�?߳׾����eO�}�C
�'|�C
Ȋ'�c�C�y�k���'o��>C�X��q��qp��8ܿ�8�hw=��80owy�u��9��j@���	6-�W-O�i�H�hz��D��:m�����Wn��)�@u�P��졚^�Ⴠ�X��Z�� ;��uU�G���U�"���}��D���܂7����C��H�/ ���#��.��訖ס�\@GtƸ���T���s�e��LP����"9�o�����Ec�d"0�e֍m�����(���D1�X���GK���1ʄ��23�p������͋�(m;-#y9= ۜN��Xo{>K�^$UX���\�B� h`5�z=jp������� aT��������E����(?�"st��G�*�
O���( PQ[߭�ѯ������      �   K
  x��Z[���}ϯ�i����ݦ�T0`�����l|�l�����4i�J���$�ef%M�I��7��ș	����޶�����^�i�{�n?�h���+�9���h�$� ���>��r.� 9r�0z�x��>Ι�0��`����Օg��n�M�qzv��d�ɞ�d]O��Id.��*G��3]M� '��A��{B������p*��'	����z���}بD�9.�QyQn��3�߈��j�v�	���T�Хaf�֦���{����ǹ���o+;a�A@` ��� �>�m��m�����v۟v�/w�g�ןf�o��w�yz�v��f=װ�����k�'����#� �`�C|���aw�x����k�*�%"$��N���f\�gU��N���E��j�I#ν�k�m=(O�����Js �U�'	I!�_�x���~���������<����yzG��?$ESy)GW3����[g���FFm=�W�u�oWp��V�&��)�d{khR�c�0XlLG��e���l�����"��0��<�~Z�����+;���4=���W����Þ$ u��`�I�1)-4�G|��I�cR^�y�ZM��Ok�r����Z�<�����)Xnm�g`G N�8)Q�0_�2���W��?��޽�h��_�%�?�ؗ}/�J��H�<T��[�����K�a���\��F�j�e�閭��Z�����藃��;��j�)M�n�d�TN�@ A�Q�� �H�9��b�Xk��:��rɮ9���a�|���.{@!8��{�� |�sq��-M�n]T�Ѣk��rG-kyѷ����҈8��S�,Ɋ�ʂ�ު0�zMd�:�Y�?i�a�'���n�"���� �^�1M�W���m_�������Sϛ]�EZ��g"/ѡ���0З=(uf4�f�,��X"����ߩ���ڴQAB�n�k�z69E~��
����H�8Ёf�gb��~B�W�yZ�:>I�x���IK�{������/�%BZ]�4(i����Rs��X�yx�QZe���@ur����w�fk6CD]r&Q��lN��� `��$-�N��E��˃0N�)���H ��֫��^�{��6���ԉԅ�Zq�4��.�pI�ZDD	�|�2's5����)����hG:W��.e�'^9x�]�8��ؘ�g���?e��,!��Z� ^�n�6��	�>�G���ߑd���|�Q%��x��q5�*3\�!`wqM�5B��z+��0J�l��0�a5��j���gY��/BNldc��)G	Y�ZTی"�>�"n���3Z�w,��9���ѰYk�����acf���v�a��?�GCz,�	`(=��B�9E�8� eX�H���$E/�*�S:�����i�C E��+q	��՗��@��e�Vb�	�м/���X^_�7ph�g1�{t���S�VblnD�?W��D��Sg��U���n��B|��a��&F��uݔU��@y��\�o�
^WT�����m�-1�Q@Ze^�]ur~t?�e�#�e���ߦ-�4��mOb�L
�@�[����P�5*˪=j�
��YB�Ԓ5ʯ������Y��K�w�r���
��Q冘d�9ga�<N��d��������/�ee��7�7�`P�n��b%����u�۳�u[+Y���ܞ�ckS�F�u-�UEo�F���d�͔�Պnl�ެh��&Г5��q�'M�_Oe���`4X��;t0�����E�����ش�^[���u؏j%��/u�aW�Δ�Ӻ/����J�w�#Kt͈o����;?,#GA"��i2<�[D�|�bo�cO�hJ����!�����D�ZmD>#�0��nC����,��94����wJ��?���0���62f�����;q��5�Ԓb'"�I?;�����x�vF�����0��mS.���3_L�l��m��a�R7����5�20-��	���i�e��Kk�.��j��Ή$��pB��0�@�&��o�����5EA#o����.l��f�Dza'���X�Im W
�)R�ê�Z0��*S'����py�t7��ڛ����B�H�7�.�r{*��|�h��,�Ep�~��	!@�N�B��ܥ�.����X��y4f��P�a��c�Qo3�!�Ԝ6=sb��u�M�7��=$�^0���y��EB����)͊�4HYּQ�-9����lfC3r��+|�C�����E^r�xB��&�X�N� F+��
�/)C�6l#��%�����(�&�f���싄����N�M��P�2'�&�1Q�n��/n�W�n��t��1/k�;�0.�Ʉ��qEb7H�V՛ӭ (0���5IG��)�|ɇ{�d6�ia��[�v5�MK��z*�����R��6?�&��1�ܒ�Q�E�;�KPK���;`��"6@ �<����+44ۭp�)v�����(
 %P���q�6.R�-�{P$r���8��F*�i���6��x3D%�����Ղ"�a`}��6Ƌ�tK1*����
r�\�l��++�ѧ;l�L��ˇW??Zw�����C`/�H��{�1��_-���j��      �   �   x��ӽ
�P���\E�bs���C�R�V��� XZ�����-dx��uS�[�u{�1�?�cqK�w������7�3e�ӓ-t��L9]�K�P<�<y�"@j�ӄ��4��8M�Nj�ӔZ�8�
��=��S�Y�,��a0��q��C-���P��}����c郁�����f���7Ϲ?�?�      �   
   x���          �   �   x���v
Q���W((M��L�K,-�H͋OI-H,*�M�+Q��L�Q�K�M�Ts�	uV�0�QP������vlx�cʃ;�\uMk.O2M4���d��v
�2�n���Xt�jy�c-��x�c!�5[0���-v,[1����v�Sb�)8��a
t�t��;;@�rgSb�̽;�����v�{�� ���2      �   �  x�͚�O�F�����;Z�P�I����
!ulj��Z)1�qZ����B�:M*(�h	C阢�)ݜ�����s��I0P�R^������y~���/<�{Q�_X�N(o>\7�f
��U��ͥ�Yn�i��j��i�P,Vt˚�=��(��nk�X�j��6iV��V56H�^*���n-U�r�0K��L�l襪��+���dZشt2a���{?�} ܔ�iaJ��l&-K��r�c����c�9��cv�cr9-8�k�����:vӱ�;�:m�8�k�f���`���%kլj�(gRb6%+�,g�y�\Za/�u�xm����UH	tZ�v���DuVɏ��ܠ��ɠ#�2Ա�8v��?�����������%���ާh���w��:<ǰ����&?���K�q�|������`������ӷ��1�\5�dRYEN�ż���ݹ�5 ����a�ߘ������3�u펥-��E��m��\a�(i���5�<B	R�T@�>nD	��$�\�$9��*�<�$F%��&JD�w��5����%�﷿�Ү���P�^�lúB��u���	w�F�m�0�Ϸ��:ƭ]>C�mE
 �&p�^u�A�M������ZL��ٴ�mz`XϨ�S��!t&��2�����ñ��p5��������MHf�S%�$%/S��,�s)��w��l�E!�g��h�M�e���3�Vf��������ݨA�ZQr���#���=TT����a��4�[�0[���ƶ���3��7�_Pn�Dc�A�.5�a���!"��af���.��u&��z"	��k��D�||t^6G=W+@l�������I@���h>y�q�Ң�j�n�z��0��8���⚔�G"��;�Ȝeo4�f��s��ϡt�h�C��hIb�q����he��θ!� �ߘ���HV-�Vb�p�a>v
G��/����pp�B|T�F�<e���:b<t�g��t���hr�t.��P6��yB@;��{��{T�;�W��m��C�|�����5��`�a@u>��j��x��k�����h�d�e����-<�`�kcC]�������-;�ǱL�%���_ ��������M�o=�<ה�]Ӑ��s�9/B}���F���$�&Ge*#�iD1"TV�wA��)�t�H�'� Y!��└�����q���h/���Tڈ[K�τ�)Ṫ��0�d��d�S�S׻D�������	���|�I�������	0A@����Q�M�*�dcEMJ֤� �&�mG��i���?�a�HGp�����e�A~4E>g$�r�]<��m/�0_��$�����򕄢�,�\����>:F��,/��������gA�F�}���vp%w�&�+W�z;����S�2!��{:م	�5X�iq��;U��u���l9n��;�xUe�c�ɸ;\O1�1
n��B�Bj�,Du�h����  ��ms3v�a����aE���@a~Q���O������q�+'�$����@�l���V�����U�qN��g`�P������P��U��P�t3�N�j�KD2JDj�Dt�oVam�R�q ��U�Q�$7�F�"�uJ�E��}�{�KJ_�I>��&�N�#M>p��K?G��"c�îEl� �?��D�g�K|o�<�\�;<}�ktz/�A��J��~�����J���(���E�������d��d����hy�Z�
+��s��(���Y1�/^ts>��m�
��/��"�L�u��<�      �     x�E��J�@��y�K7ia&iՊ��vQ�luR�f2'af��ӕ+w��+w�0��<��.��ܟs7���� ��aM{��m���D�5�(�#�(,����" ���y%�#��j�(Q����X�5˸�����D9c
��PU�xw��mT�����u&�r�Z�*l7�����	��ٷ���8��ã�_ξ�����gg?�����]7�4�|�Ի$IbJ�5\,�n�Χ��ӳ�y�j�YQ���Y�P_CgJ'A�ްm      �   
   x���          �   
   x���          �   [  x��Mo�F����.NPg1_�ŞzpA
4i/F (��*�%C�QA�{w)���4]�n	�L�����wߙ]]��p�������_����7��Z|���7���v���l��׫�y1��W��t��]���_���4^�_n�w��M_nf������9���r��]����~��O��-�[�w�mx���w�_|(^�yqF@��-�|�&<�!�@?�=o�������mxo��6�-�Ť,�}��)\���7?��u��(g�;��-WC��ǖK�ņ����l�
���hIBG�xb҅��'�d�h���B��R����|Y-o���j��vs��|.�I�JDE�@��dj^�i;��x�)����=�F,�J��!�/����vm��!c�[Jb%@�{�D'H�ԦԨ	�.9��Pa�&,�Ȁ��2Љk	��P�i�,�R9 H,��%��)����p�:������v�/ֳ��优��=���v��)Bl��ߌ���(]Q�VYО��U��91��S^��SHW2*��[y�U.�$L(��p�a2U�0��0el^�`SH�D���U.��*L�3����)���S;V�k���3�Y��rѩ'�]�B�������N=�^�Fk���ʅ�@�<�f������g�ڔ��ؕ"����>�1�6�f.DI;e�
���f1�S���Tfwkd�d,V�'s��e�j�N����vX���ʓ?v4��,W��r���BM��*.��*��ʗ[��D'�$�SKFU;F����*L��]	d��Z/��;�	y�U.�N��d��'�ơ"�5<q���!�rĥh�d�S�*R3G�VΊ���"��7
��ʆԶQ\�gЮ�rTِ�@�RHy-�	E��Sݘ!�W6�����$k{)G���dO�0[����ͬ�:N�ن�Br���~t�9�d��B
ăb�8��I�8q���UOH�!E�z���K9�lHM�ظ��[	=�9�q�����W��֮rT���C��.`���t\O�]��ä�kKOtJ�&Qlж�ݔ���Ɖ�N�'��Jh�P#��׹�)�Į�����e'娲�u�)d�u`�šCˮZC��6�O)�m eИ���M9�lА�ɖ`S�����of��gM^���.�PQ����U6P'o߀��+��c���yӜP��)�H4H��Z7娲!u�!N�+��5���i�6�*��B�&R���`"�9�U2�&R(��Ľ��7h���ͫ��S(٪P5����U6��H)��1�ǃ䤛���
��Zˊ]�"iB�Ѳ�)��[�g7'v����q��_6����=�+v�_�0�!B����wp<�@�y�W���4��      �   !  x����J1����m���Vœ����^�l2]G�IH�B��$��+�in3��>�������kv�f�N����\��FС'l��b��V�T�#A-�����v�u�J.�e,���;��Ǣ!��$�>݂�{4������Ό�}{�=8:�:���/�=�h��ʳd��wӎ ����$�~����t��\���s<X��@��:g�Z��z.�%)��ϊ\�wZ���
R��/vP�H�P��� Q����n~$�����Jx�_E��7�I"�      �   �  x���Mo7���{s�:9���)�)Ф���VX�W�����%e��R�f`H��Z?�y��3������ߊ�/�~+��C㷛�/��z��]��ﻱx����]���~m���~����_�w�������iz�x_B�񝟼m�k �?P����J���cZr�Q��?�ܣ�@�Wv?}_� B�"��P��[�P��rT�1�i�]lOx6���gb�zc�z	JR�D�{�� �n�}�ccwf����!]�

�k��T��{&�i�=ٸ�P��\�`l3�`Z?��h郦�O�q�����	 �˦�l�ȶ�k�o�`)^C�*�X�+=
�ӲĴ��PR2��P��t|l�Y�
Yj)���KF�����U��`��T��F�ʜ\���6��Sƃi��`Z7�v���h-p���9�����k_1P�������E�Z\��b�Fɑm����Kh��Tα��Qd��z>3�e�)��>��>>��?��p��|toEY3�h¹F�8���qK�V���ڀb9�������nZ����%��!9��I�U\(�<��ܸ����@��� ��]�^2����sy���m��h-��?�,���#6�HIpsD��^Y\�.%��c�׏O���jlW����WTT@*�"���t�̑�2�"9/@�\b��V�K*A+��
�q�t�$O4)1feA���"l����k�����[�%��|ٷs2�10pWs���8;�(�@ӬD��e�R#JFs"}�8�4/�(r��'$eE�&-�إaI��y�/������u`[F�R ���>��3c�VCV^1�\3����=?N�����X�v���O���r�T�䦌��ߘ�6OYf9kn'��:�s#4`�9,O �OB\d�"GJ
B*"�a&q.U����L�"+]��Dcj�!Nz�����      �   �  x���ɒ�@ D�~7�cԨ�b���A� �����.�*���g��9�L�2�o�x��綎���6)H��.�-�"�#Ս{�6�3�o��{<�p_���r��L�{�f�QM[>��(ݪ�ܓ�(�6+k�$l:�X dæZi_�G�.i�-G���M������H-�g�<�C0� M���. ��� ����d�?.I}7>�z�}J�N@8�k�W��JT=�-�/�w����#�.n4�{31��4ۘ�~��!j�k�G��	�?�uß�����Rtg��?�G��ǳ]މ��C�E����6�جNt�!����uFdc�]㬯�95$j��u��]�9ݳ2�&�������O �8֚�?P��[���H�e�����x�7��uS?w�_� ��P�����(ʼ*}�L~H���      �   
   x���          �   
   x���          �   
   x���          �   
   x���          �   
   x���         