
car_number = input("차량번호를 입력하세요: ")
a = [
    7768 ,	2580 ,	2596 ,	5794 ,	2260 ,	1212 ,	1828 ,	8183 ,	8057 ,	8201 ,	3431 ,	8164 ,	6129 ,	6422 ,	8204 ,	5371 ,	2515 ,	5567 ,	7018 ,
    3437 ,	3398 ,	4966 ,	2519 ,	2690 ,	3475 ,	3406 ,	5152 ,	5637 ,	2517 ,	2629 ,	2589 ,	3488 ,	3092 ,	3812 ,	2527 ,	5796 ,	1858 ,	9409 ,	
    3166 ,	2040 ,	1542 ,	5217 ,	2565 ,	8134 ,	8299 ,	8059 ,	5505 ,	5550 ,	4784 ,	8210 ,	1310 ,	7051 ,	8171 ,	7573 ,	9616 ,	2716 ,	6838 ,	
    5093 ,	6435 ,	5795 ,	5309 ,	6587 ,	3204 ,	6595 ,	6947 ,	3483 ,	7428 ,	6432 ,	9501 ,	2501 ,	5111 ,	3449 ,	8615 ,	8072 ,	8553 ,	2526 ,	
    2063 ,	8383 ,	5557 ,	3442 ,	6252 ,	3066 ,	9622 ,	2572 ,	5447 ,	1463 ,	3444 ,	4295 ,	9663 ,	3678 ,	2512 ,	9222 ,	2287 ,	6818 ,	3531 ,	
    5221 ,	3837 ,	5321 ,	7822 ,	8282 ,	5471 ,	4489 ,	7001 ,	9171 ,	1730 ,	1289 ,	8277 ,	2516 ,	3173 ,	7987 ,	9599 ,	9303 ,	4262 ,	4863 ,	
    1336 ,	6637 ,	8658 ,	6550 ,	7706 ,	2975 ,	3882 ,	2740 ,	8531 ,	5924 ,	2503 ,	3326 ,	5734 ,	7545 ,	6932 ,	2219 ,	8430 ,	7801 ,	5448 ,	
    5095 ,	2547 ,	9398 ,	5903 ,	4826 ,	4239 ,	1270 ,	2006 ,	1047 ,	1826 ,	9966 ,	6017 ,	3548 ,	5564 ,	2158 ,	4501 ,	3402 ,	2857 ,	7482 ,	
    6618 ,	2044 ,	3036 ,	6052 ,	5538 ,	5071 ,	5330 ,	7252 ,	2522 ,	5507 ,	8253 ,	2954 ,	7254 ,	5232 ,	6647 ,	7158 ,	6297 ,	1964 ,	5808 ,	
    2546 ,	2700 ,	4226 ,	2459 ,	1294 ,	6688 ,	1057 ,	5052 ,	7962 ,	7767 ,	5107 ,	3980 ,	4127 ,	4620 ,	9338 ,	9612 ,	8655 ,	1077 ,	6732 ,	
    5325 ,	1407 ,	4129 ,	7794 ,	4527 ,	3170 ,	2534 ,	9046 ,	9582 ,	4672 ,	7336 ,	8372 ,	9566 ,	4263 ,	3787 ,	7547 ,	5592 ,	7319 ,	8593 ,	
    8361 ,	2056 ,	1279 ,	8493 ,	7939 ,	8722 ,	7103 ,	5200 ,	2506 ,	1798 ,	2751 ,	6702 ,	5868 ,	3908 ,	9972 ,	2593 ,	5097 ,	4256 ,	2509 ,	
    4914 ,	3630 ,	7718 ,	4311 ,	5354 ,	9092 ,	5401 ,	8014 ,	6614 ,	9036 ,	2848 ,	2498 ,	2552 ,	4931 ,	7496 ,	3782 ,	4251 ,	7629 ,	4974 ,	
    6212 ,	9770 ,	8880 ,	6085 ,	6411 ,	5044 ,	1695 ,	6979 ,	1797 ,	6251 ,	9896 ,	5092 ,	4180 ,	9563 ,	6347 ,	2620 ,	9268 ,	8527 ,	5207 ,	
    7467 ,	9455 ,	4632 ,	4923 ,	3807 ,	2562 ,	3190 ,	3750 ,	6629 ,	5024 ,	3171 ,	2656 ,	7830 ,	2211 ,	7635 ,	2007 ,	7237 ,	1264 ,	2507 ,	
    3410 ,	9310 ,	2633 ,	7993 ,	6878 ,	7025 ,	3244 ,	4306 ,	1075 ,	2771 ,	8107 ,	4221 ,	8165 ,	6700 ,	4568 ,	8494 ,	6510 ,	9263 ,	6955 ,	
    4702 ,	4561 ,	7879 ,	8184 ,	2523 ,	8154 ,	4145 ,	2710 ,	6953 ,	2374 ,	6117 ,	6241 ,	8083 ,	4055 ,	8209 ,	8511 ,	8323 ,	7189 ,	8255 ,	
    8359 ,	6969 ,	3846 ,	5482 ,	2236 ,	2972 ,	1700 ,	2945 ,	1992 ,	7014 ,	7073 ,	5841 ,	1273 ,	2625 ,	9472 ,	8800 ,	6480 ,	5839 ,	4368 ,	
    1006 ,	7313 ,	1540 ,	4505 ,	4498 ,	5622 ,	4559 ,	3322 ,	4592 ,	8076 ,	2940 ,	1497 ,	2632 ,	3675 ,	1541 ,	3698 ,	2035 ,	8196 ,	9746 ,	
    3509 ,	2325 ,	4319 ,	9038 ,	7889 ,	8012 ,	5913 ,	6792 ,	2554 ,	4434 ,	9510 ,	3937 ,	6182 ,	6416 ,	6077 ,	7481 ,	6497 ,	4738 ,	4397 ,	
    7891 ,	1600 ,	6493 ,	8156 ,	7391 ,	7582 ,	2194 ,	2680 ,	3621 ,	3450 ,	5344 ,	9587 ,	9517 ,	2524 ,	8708 ,	6934 ,	7201 ,	8964 ,	5105 ,	
    8893 ,	8969 ,	2161 ,	8618 ,	8168 ,	8813 ,	8816 ,	2542 ,	4790 ,	6872 ,	8757 ,	9493 ,	3855 ,	2579 ,	4092 ,	2392 ,	8248 ,	2819 ,	2544 ,	
    6753 ,	5357 ,	1759 ,	8985 ,	1196 ,	3104 ,	7552 ,	5283 ,	5815 ,	4815 ,	9350 ,	3210 ,	6705 ,	9820 ,	5518 ,	4714 ,	4810 ,	1444 ,	8921 ,	
    3259 ,	9002 ,	5113 ,	3499 ,	2092 ,	7828 ,	8759 ,	2559 ,	9697 ,	8113 ,	8504 ,	2543 ,	6317 ,	2784 ,	8807 ,	7134 ,	6507 ,	7058 ,	8275 ,	
    2154 ,	8185 ,	2570 ,	2298 ,	6350 ,	2375 ,	1135 ,	8590 ,	8829 ,	8595 ,	2705 ,	2582 ,	1103 ,	2537 ,	6164 ,	9080 ,	1015 ,	4950 ,	4916 ,	
    2594 ,	3051 ,	5719 ,	8367 ,	8914 ,	8471 ,	5594 ,	1500 ,	9148 ,	8391 ,	9945 ,	7344 ,	4608 ,	1232 ,	6307 ,	8928 ,	4131 ,	3682 ,	1961 ,	
    4011 ,	9924 ,	6494 ,	3428 ,	1567 ,	6871 ,	8197 ,	7328 ,	8436 ,	1425 ,	2224 ,	8765 ,	4670 ,	4748 ,	8269 ,	2894 ,	7292 ,	6404 ,	7541 ,	
    6089 ,	2642 ,	4861 ,	4528 ,	4291 ,	5536 ,	5586 ,	4170 ,	2873 ,	9960 ,	4152 ,	8140 ,	5264 ,	6825 ,	7847 ,	9326 ,	7601 ,	3556 ,	2142 ,	
    1278 ,	4745 ,	6282 ,	5897 ,	2768 ,	6845 ,	8261 ,	1947 ,	6173 ,	3852 ,	7072 ,	1067 ,	8544 ,	9296 ,	8123 ,	1643 ,	5910 ,	1251 ,	3813 ,	
    2555 ,	3695 ,	6646 ,	4029 ,	6356 ,	3486 ,	5553 ,	2760 ,	6579 ,	8160 ,	7605 ,	8736 ,	2921 ,	7945 ,	9137 ,	5225 ,	6261 ,	6162 ,	9562 ,	
    1522 ,	3794 ,	9680 ,	6180 ,	1503 ,	7520 ,	5269 ,	7421 ,	4634 ,	8363 ,	3373 ,	4860 ,	1303 ,	9892 ,	8819 ,	2429 ,	1467 ,	3064 ,	9318 ,	
    9684 ,	2583 ,	4805 ,	9201 ,	2232 ,	5651 ,	7927 ,	1975 ,	8456 ,	5235 ,	6623 ,	7150 ,	4963 ,	8542 ,	6687 ,	1300 ,	8375 ,	3971 ,	1837 ,	
    2595 ,	1191 ,	2465 ,	2145 ,	1579 ,	2301 ,	2432 ,	6220 ,	8254 ,	6738 ,	2802 ,	4294 ,	6276 ,	5000 ,	6834 ,	3012 ,	7888 ,	4774 ,	4484 ,	
    2739 ,	4849 ,	7084 ,	2129 ,	1040 ,	1911 ,	3260 ,	2192 ,	8149 ,	5438 ,	5206 ,	3757 ,	5369 ,	9174 ,	1661 ,	4794 ,	5696 ,	7967 ,	1082 ,	
    8054 ,	6941 ,	6135 ,	3984 ,	5895 ,	6796 ,	4511 ,	3329 ,	3199 ,	4812 ,	1200 ,	6904 ,	9170 ,	4037 ,	1280 ,	9335 ,	5413 ,	2312 ,	5299 ,	
    1388 ,	5838 ,	2563 ,	9329 ,	4257 ,	8200 ,	4593 ,	6392 ,	3502 ,	3661 ,	6445 ,	9169 ,	3538 ,	9440 ,	6716 ,	7376 ,	7633 ,	6627 ,	8051 ,	
    4509 ,	7965 ,	1152 ,	1853 ,	2404 ,	7338 ,	8335 ,	7161 ,	8963 ,	5628 ,	1105 ,	2321 ,	6155 ,	1100 ,	1966 ,	2783 ,	3067 ,	4449 ,	7523 ,	
    2493 ,	2576 ,	2190 ,	9467 ,	4919 ,	8142 ,	9403 ,	5353 ,	8392 ,	4732 ,	5634 ,	8606 ,	5911 ,	3078 ,	8224 ,	7990 ,	9498 ,	8480 ,	1029 ,	
    5880 ,	1059 ,	5007 ,	8257 ,	7959 ,	1236 ,	5560 ,	7941 ,	9731 ,	5384 ,	5328 ,	2535 ,	6120 ,	1050 ,	2772 ,	4816 ,	8295 ,	5701 ,	9390 ,	
    5698 ,	9332 ,	9832 ,	2977 ,	4953 ,	9494 ,	5522 ,	4172 ,	2106 ,	1038 ,	2741 ,	8838 ,	7643 ,	4113 ,	5926 ,	5675 ,	9304 ,	5046 ,	6891 ,	
    4687 ,	3893 ,	2722 ,	2965 ,	6434 ,	3270 ,	8378 ,	5197 ,	6926 ,	8351 ,	9432 ,	2774 ,	6770 ,	9889 ,	7261 ,	6506 ,	3989 ,	2744 ,	2615 ,	
    8176 ,	2982 ,	4866 ,	1157 ,	4985 ,	2569 ,	4352 ,	2969 ,	7207 ,	6030 ,	1334 ,	5546 ,	7488 ,	7543 ,	7480 ,	2877 ,	7580 ,	3348 ,	8075 ,	
    4913 ,	7301 ,	1980 ,	6851 ,	9670 ,	9906 ,	5939 ,	4900 ,	5671 ,	9609 ,	8579 ,	4058 ,	6537 ,	9803 ,	4551 ,	6278 ,	5406 ,	7066 ,	5573 ,	
    4258 ,	1171 ,	8516 ,	8305 ,	5135 ,	8252 ,	7454 ,	4751 ,	1480 ,	8522 ,	4114 ,	9693 ,	7297 ,	7914 ,	2467 ,	7406 ,	1348 ,	3026 ,	5064 ,	
    1710 ,	8649 ,	8900 ,	6453 ,	6720 ,	1204 ,	8018 ,	3440 ,	1995 ,	4064 ,	8723 ,	5823 ,	6467 ,	4869 ,	3551 ,	5502 ,	2561 ,	3278 ,	3576 ,	
    6572 ,	7937 ,	6857 ,	3520 ,	8671 ,	9358 ,	3304 ,	1323 ,	3174 ,	9843 ,	2584 ,	2597 ,	1557 ,	5068 ,	2550 ,	6396 ,	2520 ,	8212 ,	3588 ,	
    7913 ,	6253 ,	3947 ,	6113 ,	5931 ,	1779 ,	2047 ,	6975 ,	1606 ,	8353 ,	2607 ,	6771 ,	6665 ,	4771 ,	1907 ,	4005 ,	4542 ,	5169 ,	2504 ,	
    4302 ,	1672 ,	7385 ,	8929 ,	2592 ,	7865 ,	9007 ,	8572 ,	1401 ,	8189 ,	9367 ,	1938 ,	2051 ,	6094 ,	8833 ,	4143 ,	5467 ,	3467 ,	1471 ,	
    8050 ,	2122 ,	3013 ,	9138 ,	2638 ,	7090 ,	9121 ,	9347 ,	2672 ,	3448 ,	5099 ,	9270 ,	6812 ,	9141 ,	6149 ,	6775 ,	3496 ,	5022 ,	2791 ,	
    1597 ,	4009 ,	6586 ,	8406 ,	7584 ,	5476 ,	1305 ,	8096 ,	5439 ,	7574 ,	3741 ,	2486 ,	6988 ,	5153 ,	8605 ,	2531 ,	8639 ,	2518 ,	5211 ,	
    2074 ,	6295 ,	1046 ,	8001 ,	1687 ,	8048 ,	2867 ,	7265 ,	5665 ,	5191 ,	9292 ,	6424 ,	8272 ,	5394 ,	3624 ,	5730 ,	4342 ,	4344 ,	1479 ,	
    9082 ,	8073 ,	7123 ,	6292 ,	6195 ,	6150 ,	4153 ,	9690 ,	5736 ,	2571 ,	7739 ,	1749 ,	5530 ,	2505 ,	8942 ,	4833 ,	4050 ,	5688 ,	6781 ,	
    4385 ,	8178 ,	7233 ,	5804 ,	6337 ,	7039 ,	7312 ,	5544 ,	9090 ,	8652 ,	2581 ,	4715 ,  9219 ,	4093 ,	6436 ,	9651 ,	3979 ,	7668 ,	8508 ,	
    4825 ,	6420 ,	9487 ,	3969 ,	5690 ,	9313 ,	9754 ,	6243 ,	3567 ,	3086 ,	9100 ,	4167 ,	2176 ,	5185 ,	8619 ,	7362 ,	1969 ,	2564 ,	4426 ,	
    2529 ,	7550 ,	8219 ,	8139 ,	5554 ,	5485 ,	8325 ,	9763 ,	9724 ,	9402 ,	8611 ,	7976 ,	7827 ,	3359 ,	2306 ,	2648 ,	3730 ,	9529 ,	3420 ,	
    8648 ,	2833 ,	2586 ,	5458 ,	5424 ,	1464 ,	6895 ,	1120 ,	3186 ,	7245 ,	2189 ,	4515 ,	4665 ,	9882 ,	1189 ,	4793 ,	1183 ,	9040 ,	8864 ,	
    4888 ,	3257 ,	7820 ,	5327 ,	7340 ,	7223 ,	1178 ,	4904 ,	2574 ,	4329 ,	8371 ,	8161 ,	3494 ,	6997 ,	5908 ,	6717 ,	1682 ,	5756 ,	4712 ,	
    9314 ,	4580 ,	3696 ,	3382 ,	5844 ,	5781 ,	4466 ,	4803 ,	4878 ,	4628 ,	7429 ,	6421 ,	3545 ,	3172 ,	3416 ,	5223 ,	8238 ,	8281 ,	1272 ,	
    1698 ,	3455 ,	3946 ,	7248 ,	5228 ,	6567 ,	1017 ,	8292 ,	1179 ,	4718 ,	5026 ,	2796 ,	2870 ,	2623 ,	4627 ,	1269 ,	7236 ,	1446 ,	7534 ,	
    7743 ,	8693 ,	5975 ,	8412 ,	6279 ,	8019 ,	4410 ,	2502 ,	8787 ,	7572 ,	3891 ,	1766 ,	3470 ,	8698 ,	1048 ,	9328 ,	3163 ,	7725 ,	8428 ,	
    1776 ,	8633 ,	5890 ,	4827 ,	9022 ,	2822 ,	3345 ,	8302 ,	9120 ,	2567 ,	7360 ,	3138 ,	5523 ,	4412 ,	3834 ,	1149 ,	5430 ,	5248 ,	3998 ,	
    2573 ,	1089 ,	8592 ,	7045 ,	3424 ,	2269 ,	9235 ,	2419 ,	9765 ,	7138 ,	4734 ,	4331 ,	1596 ,	9389 ,	6654 ,	6489 ,	5319 ,	4536 ,	2540 ,	
    2177 ,	7274 ,	1293 ,	2889 ,	5526 ,	6357 ,	2231 ,	8366 ,	5198 ,	4224 ,	2521 ,	3655 ,	2974 ,	9116 ,	1150 ,	2640 ,	9951 ,	4640 ,	3701 ,	
    8195 ,	8534 ,	2475 ,	4567 ,	7640 ,	3958 ,	8399 ,	7185 ,	7638 ,	7311 ,	2443 ,	8356 ,	6367 ,	6466 ,	8206 ,	3724 ,	1190 ,	7052 ,	4807 ,	
    4836 ,	2895 ,	5580 ,	8387 ,	9341 ,	3053 ,	4297 ,	1063 ,	8884 ,	6151 ,	6847 ,	2829 ,	8114 ,	2033 ,	9660 ,	3665 ,	7893 ,	1486 ,	1229 ,	
    4123 ,	6442 ,	4345 ,	7645 ,	3760 ,	5073 ,	8924 ,	4796 ,	4414 ,	2346 ,	1418 ,	1243 ,	7286 ,	1268 ,	6360 ,	1901 ,	2167 ,	7175 ,	5541 ,	
    1009 ,	1865 ,	9108 ,	2553 ,	9214 ,	7664 ,	6635 ,	5520 ,	8098 ,	6362 ,	8033 ,	9107 ,	1742 ,	6301 ,	3361 ,	8270 ,	8713 ,	9914 ,	5016 ,	
    1084 ,	4697 ,	3219 ,	2568 ,	4304 ,	5575 ,	6735 ,	6669 ,	3169 ,	8686 ,	5393 ,	8218 ,	1060 ,	9639 ,	8229 ,	1368 ,	4961 ,	1640 ,	4150 ,	
    5862 ,	6265 ,	4619 ,	4300 ,	2721 ,	4951 ,	2313 ,	7349 ,	3578 ,	8768 ,	1781 ,	1845 ,	5314 ,	4845 ,	9543 ,	2675 ,	5504 ,	4104 ,	2073 ,	
    6005 ,	6128 ,	4731 ,	8327 ,	5387 ,	3490 ,	7764 ,	8035 ,	5760 ,	8396 ,	7615 ,	3723 ,	1465 ,	8373 ,	8435 ,	1999 ,	3435 ,	9312 ,	5635 ,	
    5864 ,	1743 ,	2545 ,	1866 ,	6224 ,	7364 ,	3708 ,	8148 ,	8477 ,	3968 ,	1860 ,	4023 ,	2609 ,	5370 ,	4277 ,	9787 ,	4347 ,	6136 ,	7998 ,	
    8443 ,	3209 ,	2341 ,	2538 ,	3124 ,	6206 ,	1466 ,	7335 ,	3758 ,	9598 ,	5515 ,	5933 ,	7575 ,	1815 ,	1397 ,	7930 ,	8461 ,	5532 ,	3785 ,	
    1162 ,	8153 ,	7323 ,	4894 ,	6769 ,	5434 ,	1221 ,	1125 ,	4765 ,	2706 ,	5647 ,	3022 ,	9533 ,	1143 ,	2604 ,	8808 ,	2876 ,	3443 ,	8024 ,	
    3015 ,	9919 ,	7013 ,	9815 ,	6433 ,	5953 ,	3149 ,	1341 ,	4219 ,	1492 ,	5317 ,	6248 ,	7597 ,	9447 ,	4577 ,	8466 ,	5322 ,	8479 ,	8397 ,	
    7226 ,	1869 ,	9225 ,	8174 ,	9804 ,	4453 ,	5435 ,	8901 ,	6885 ,	5265 ,	7966 ,	5980 ,	7868 ,	3756 ,	9561 ,	8268 ,	9287 ,	6864 ,	2095 ,	
    8202 ,	6933 ,	9008 ,	2598 ,	9479 ,	8556 ,	7118 ,	6906 ,	5230 ,	3810 ,	3156 ,	3094 ,	2418 ,	2291 ,	1839 ,	1631 ,	1591 ,	2925 ,	8145 ,	
    1842 ,	3784 ,	9992 ,	9981 ,	3748 ,	1481 ,	9833 ,	8101 ,	2015 ,	7714 ,	3477 ,	7540 ,	3986 ,	8541 ,	3076 ,	3438 ,	4582 ,	7558 ,	4333 ,	
    1757 ,	2400 ,	4095 ,	2402 ,	3690 ,	6209 ,	2468 ,	8023 ,	2533 ,	5043 ,	1358 ,	7625 ,	8017 ,	4530 ,	5179 ,	6547 ,	1584 ,	9017 ,	1131 ,	
    6983 ,	8922 ,	8810 ,	7135 ,	5644 ,	1665 ,	1728 ,	1578 ,	1793 ,	2990 ,	7637 ,	4003 ,	1042 ,	1662 ,	8737 ,	3168 ,	2826 ,	7015 ,	4588 ,	
    1531 ,	2790 ,	8678 ,	9033 ,	8080 ,	8491 ,	2097 ,	7618 ,	5716 ,	2899 ,	1510 ,	6576 ,	4270 ,	5678 ,	4992 ,	3808 ,	7471 ,	2659 ,	8105 ,	
    2365 ,	8684 ,	6344 ,	3943 ,	8026 ,	4614 ,	7339 ,	6811 ,	4015 ,	3907 ,	5994 ,	5877 ,	5292 ,	3121 ,	3447 ,	7817 ,	8664 ,	2936 ,	6502 ,	
    2405 ,	2683 ,	5941 ,	9637 ,	7909 ,	7262 ,	6010 ,	4265 ,	3982 ,	2170 ,	1511 ,	1194 ,	3734 ,	2773 ,	2578 ,	1172 ,	3472 ,	5148 ,	9267 ,	
    8220 ,	5623 ,	7803 ,	7180 ,	8173 ,	4840 ,	6168 ,	5983 ,	5130 ,	2842 ,	3631 ,	3940 ,	6255 ,	8047 ,	2893 ,	9378 ,	4879 ,	5652 ,	9515 ,	
    7448 ,	1601 ,	6596 ,	6779 ,	8839 ,	4202 ,	7964 ,	3133 ,	9976 ,	5778 ,	4266 ,	2556 ,	7507 ,	8950 ,	9930 ,	6123 ,	3714 ,	8941 ,	6713 ,	
    2834 ,	3043 ,	5263 ,	4124 ,	9938 ,	4617 ,	3924 ,	8770 ,	1483 ,	6053 ,	2851 ,	5295 ,	3603 ,	1408 ,	9842 ,	8519 ,	8885 ,	9793 ,	8039 ,	
    9261 ,	3093 ,	7197 ,	7810 ,	4767 ,	5758 ,	8357 ,	4688 ,	8742 ,	5400 ,	5313 ,	5825 ,	6788 ,	6984 ,	4824 ,	7275 ,	3037 ,	2588 ,	1553 ,	
    4760 ,	3638 ,	8037 ,	7062 ,	9688 ,	9935 ,	3550 ,	3468 ,	2508 ,	1691 ,	5812 ,	7836 ,	4625 ,	9217 ,	2767 ,	8182 ,	5081 ,	4273 ,	9983 ,	
    9202 ,	9115 ,	7556 ,	7446 ,	7318 ,	7164 ,	7107 ,	7093 ,	6739 ,	5418 ,	4323 ,	4290 ,	4204 ,	2386 ,	2037 ,	1836 ,	1263 ,	1926 ,	3025 ,	
    2852 ,	8250 ,	4168 ,	9114 ,	7948 ,	1594 ,	5966 ,	2793 ,	8604 ,	9163 ,	6455 ,	6144 ,	8136 ,	3606 ,	3196 ,	1092 ,	5255 ,	7902 ,	3072 ,	
    9025 ,	2902 ,	5149 ,	3353 ,	9084 ,	8289 ,	2944 ,	6269 ,	3863 ,	4560 ,	1620 ,	3241 ,	8879 ,	3368 ,	3790 ,	6020 ,	8380 ,	3602 ,	9620 ,	
    7923 ,	2302 ,	6921 ,	8151 ,	1287 ,	9782 ,	8823 ,	8701 ,	2268 ,	5128 ,	1260 ,	2536 ,	8982 ,	4785 ,	4195 ,	4209 ,	5657 ,	2251 ,	5168 ,	
    3777 ,	8071 ,	3214 ,	7293 ,	3075 ,	5121 ,	8934 ,	8382 ,	9985 ,	9507 ,	7227 ,	1274 ,	8760 ,	4080 ,	2230 ,	4259 ,	7650 ,	9841 ,	6054 ,	
    7740 ,	2855 ,	3295 ,	1219 ,	1337 ,	2541 ,	2661 ,	4646 ,	1321 ,	2191 ,	6708 ,	3123 ,	1902 ,	2549 ,	7355 ,	4828 ,	9524 ,	7525 ,	3993 ,	
    3581 ,	9144 ,	6004 ,	7823 ,	1987 ,	8971 ,	2490 ,	9918 ,	7816 ,	6516 ,	6504 ,	6193 ,	6110 ,	4729 ,	4578 ,	4032 ,	3850 ,	2370 ,	2137 ,	
    1133 ,	4467 ,	9371 ,	2497 ,	7546 ,	8246 ,	1390 ,	1787 ,	7493 ,	9102 ,	7451 ,	5231 ,	6163 ,	1013 ,	3414 ,	8146 ,	3155 ,	4857 ,	6804 ,	
    9273 ,	4630 ,	4392 ,	6481 ,	3029 ,	1713 ,	5660 ,	2827 ,	1343 ,	5593 ,	4823 ,	9586 ,	1008 ,	3000 ,	1571 ,	7960 ,	1630 ,	5451 ,	5379 ,	
    6616 ,	9469 ,	7631 ,	1072 ,	4977 ,	5561 ,	1011 ,	2723 ,	3245 ,	9451 ,	9650 ,	6689 ,	8342 ,	9042 ,	8385 ,	4184 ,	7789 ,	5865 ,	5938 ,	
    3931 ,	2590 ,	2369 ,	7531 ,	5837 ,	5620 ,	9112 ,	6589 ,	4839 ,	2836 ,	1384 ,	4905 ,	9307 ,	4599 ,	9788 ,	3463 ,	3495 ,	5713 ,	7483 ,	
    5267 ,	3498 ,	9822 ,	8828 ,	8795 ,	8612 ,	8518 ,	7935 ,	7855 ,	7555 ,	7455 ,	7213 ,	7085 ,	6874 ,	6214 ,	6189 ,	5489 ,	5138 ,	4896 ,	
    4678 ,	4151 ,	3985 ,	2991 ,	2492 ,	2461 ,	2354 ,	2307 ,	1723 ,	1607 ,	1412 ,	8103 ,	1708 ,	5547 ,	6605 ,	1426 ,	7148 ,	4031 ,	5470 ,	
    7266 ,	3135 ,	4161 ,	1142 ,	8286 ,	9970 ,	4890 ,	2273 ,	4004 ,	3479 ,	9857 ,	5348 ,	5711 ,	6833 ,	6544 ,	5608 ,	2815 ,	1093 ,	8010 ,	
    3315 ,	1916 ,	3507 ,	1443 ,	1953 ,	9538 ,	9753 ,	6577 ,	7869 ,	5445 ,	2862 ,	9276 ,	2907 ,	5452 ,	2239 ,	5172 ,	5220 ,	4348 ,	6152 ,	
    8697 ,	5529 ,	3532 ,	8175 ,	6375 ,	6727 ,	7177 ,	4725 ,	9624 ,	8904 ,	5949 ,	8411 ,	1538 ,	2859 ,	8187 ,	3687 ,	6890 ,	1250 ,	3547 ,	
    2261 ,	6476 ,	1849 ,	8951 ,	1295 ,	8207 ,	5359 ,	9419 ,	9255 ,	8873 ,	8409 ,	7792 ,	7208 ,	6690 ,	6107 ,	6101 ,	5810 ,	3636 ,	2948 ,	
    2897 ,	2204 ,	1298 ,	4156 ,	6242 ,	6797 ,	7152 ,	7678 ,	5902 ,	1393 ,	4674 ,	9768 ,	5641 ,	2532 ,	2548 ,	8624 ,	9260 ,	7153 ,	4800 ,	
    2124 ,	8478 ,	3779 ,	2250 ,	4390 ,  8732 ,	8259 ,	8395 ,	4801 ,	3601 ,	3355 ,	1616 ,	8492 ,	7839 ,	5456 ,	7281 ,	1524 ,	6311 ,	7630 ,	
    3021 ,	5041 ,	5215 ,	1128 ,	8694 ,	9725 ,	1297 ,	9925 ,	9473 ,	9073 ,	8811 ,	8719 ,	8712 ,	8549 ,	8530 ,	8291 ,	7843 ,	7710 ,	7663 ,	
    7081 ,	6601 ,	6546 ,	5399 ,	5275 ,	5246 ,	5240 ,	5233 ,	4856 ,	4737 ,	4691 ,	4525 ,	4469 ,	4054 ,	3883 ,	3754 ,	3335 ,	3071 ,	3063 ,	
    2932 ,	5305 ,	6098 ,	5699 ,	6027 ,	4362 ,	5012 ,	4428 ,	3597 ,	7026 ,	6171 ,	8573 ,	7685 ,	1238 ,	9595 ,	5038 ,	5055 ,	7953 ,	1226 ,	
    2103 ,	8093 ,	4327 ,	2511 ,	9711 ,	6842 ,	5404 ,	4531 ,	9534 ,	6131 ,	6050 ,	5900 ,	3710 ,	2227 ,	1197 ,	5177 ,	5579 ,	9373 ,	4115 ,	
    9825 ,	6598 ,	6016 ,	4169 ,	7133 ,	4545 ,	5245 ,	4572 ,	3454 ,	2233 ,	8069 ,	4162 ,	5462 ,	4099 ,	9743 ,	7151 ,	6661 ,	6561 ,	6099 ,	
    6064 ,	5595 ,	5542 ,	5258 ,	4730 ,	4106 ,	1215 ,	1044 ,	9016 ,	5661 ,	2396 ,	2066 ,	6585 ,	4128 ,	2809 ,	4576 
 ]
'''
# 입력값을 정수로 변환하여 리스트에 있는지 확인
if int(car_number) in a:
    print("방문번호입니다")
else:
    print("아닙니다")
'''

ranks = []
    
for i in range(2124):
      ranks.append((str(i+1)+"등"))

  # 입력값을 정수로 변환하여 리스트에 있는지 확인
if int(car_number) in a:
      print(ranks[a.index(int(car_number))])
else:
      print("없음")


