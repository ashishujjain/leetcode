""" 2365. Task Scheduler II

Youtube link : https://www.youtube.com/watch?v=yoGLupCpItw

Medium
Topics
Companies
Hint
You are given a 0-indexed array of positive integers tasks, representing tasks that need to be completed in order, where tasks[i] represents the type of the ith task.

You are also given a positive integer space, which represents the minimum number of days that must pass after the completion of a task before another task of the same type can be performed.

Each day, until all tasks have been completed, you must either:

Complete the next task from tasks, or
Take a break.
Return the minimum number of days needed to complete all tasks.

 

Example 1:

Input: tasks = [1,2,1,2,3,1], space = 3
Output: 9
Explanation:
One way to complete all tasks in 9 days is as follows:
Day 1: Complete the 0th task.
Day 2: Complete the 1st task.
Day 3: Take a break.
Day 4: Take a break.
Day 5: Complete the 2nd task.
Day 6: Complete the 3rd task.
Day 7: Take a break.
Day 8: Complete the 4th task.
Day 9: Complete the 5th task.
It can be shown that the tasks cannot be completed in less than 9 days.
Example 2:

Input: tasks = [5,8,8,5], space = 2
Output: 6
Explanation:
One way to complete all tasks in 6 days is as follows:
Day 1: Complete the 0th task.
Day 2: Complete the 1st task.
Day 3: Take a break.
Day 4: Take a break.
Day 5: Complete the 2nd task.
Day 6: Complete the 3rd task.
It can be shown that the tasks cannot be completed in less than 6 days.

"""


from collections import deque
import heapq
from typing import Counter, List
import time
from memory_profiler import profile

class Leet_2365_TaskScheduler2:
    #@profile
    def taskScheduler2(self, tasks: List[int], space: int) -> int:
        current_day = 1
        memo = {}
        for task in tasks:
            #print ("------------------------------")
            #print ("current_day : ", current_day)
            if task in memo:
                #print ("Task in memo:", task)
                lastday_task_was_done = memo[task]
                #print ("lastday_task_was_done : ", lastday_task_was_done)
                next_day_task_can_done = lastday_task_was_done + space + 1
                #print ("next_day_task_can_done :", next_day_task_can_done)
                current_day = max (current_day, next_day_task_can_done)
                #current_day = next_day_task_can_done
            #print ("Adding/updating Task in memo with new date it can be executed:", task)
            #print ("Updating the current day for the task : ",current_day )
            memo[task] = current_day
            #print (memo)
            current_day +=1
        #print ("current day : ", memo[task])
        current_day -= 1
        #return current_day
        return memo[task]

if __name__=="__main__":
    leet_2365 = Leet_2365_TaskScheduler2()
    a = [1,2,1,2,3,1]
    space = 3
    print (leet_2365.taskScheduler2(a, space))
    print ("================================================")
    a = [5,8,8,5]
    space = 3
    print (leet_2365.taskScheduler2(a, space))
    print ("================================================")
    a = [4116863,4645716,2404704,6239358,4206673,4876827,3633062,7584625,1277744,1573232,4889817,8841891,9349888,5805984,306410,9424969,6373703,2404704,6309448,4715876,3297559,4863708,887812,9672912,9214444,8427478,9259440,1362133,4037376,1022884,2513268,226698,8769517,6741789,9023873,1263547,510398,3056057,4483131,3555787,2937934,7482449,7572159,9623242,5701146,7100702,6247132,4445729,3722760,7808637,223547,1135487,2199054,6548608,4058809,1534041,5719253,5615236,9146904,5459497,1099539,3917066,7676098,1652454,9907641,5111076,4439977,2341111,8397497,6494362,4850937,2143249,9555430,8711625,3869979,9846247,7737572,4739490,9403301,1003296,3090932,9664175,1250563,543919,8735111,6434820,1752599,1696989,3341892,4844988,7869983,9214444,9146904,1087406,5087295,2590292,1516864,5467025,6458303,6490030,584038,2666857,1409434,5307113,5143647,261588,3261483,9833242,8564958,4834315,952222,463203,342187,5942993,2544609,1627743,9065803,1246745,9094770,9937018,275124,9745660,4923969,1955869,219837,7028504,1902941,938493,226698,9380615,4859560,6491674,1744986,413196,5187467,4123942,7185760,8429576,1738600,5691985,9266990,9998509,3731864,2588238,2517615,2735968,9138348,1425328,3442451,1268745,2819841,3790308,5025096,9301947,3052084,9023873,4430885,1258197,4448882,6447145,9623523,9197335,8939923,3090932,4178344,3489644,8560728,5158494,3056057,9241350,306410,4876827,3714828,4923969,3756452,438449,5056214,6102940,5609750,5546670,2360980,4620288,8772604,6990592,1250563,1377971,1312469,6893741,5826225,1303539,6103394,564118,761930,6550838,3515226,6412164,3958238,4222165,4072629,8015472,3101459,1212896,9046784,367306,2341111,4119971,2360980,89674,6587837,5899589,4667338,7940381,899357,3210112,3063120,8303687,8875833,7572159,6785481,4206673,8087322,1990173,9065803,3741282,3902257,8728069,9950883,4803488,6285028,1867954,5111076,835275,5464873,116007,3200443,4092517,2015670,7589058,6228336,5766853,6434820,5630962,9166476,1503290,362718,1532197,5931265,9146904,686114,7515743,1168417,666194,782598,1612829,552694,1457514,991992,9429757,7482449,5389805,708510,6851513,931833,7667960,7426789,6309448,931833,9768987,1540365,403656,314148,9997297,1573796,761930,5899589,636318,3918488,2426918,6370725,7736240,6031354,8728069,5718578,1310424,8916403,6947776,4715876,7231439,3815363,8955760,3911548,2123693,8769517,5691985,8929556,8048209,9301270,251081,726845,5137149,8303687,5137408,7659720,8189207,5076668,387761,5230060,2093635,1115818,7110095,8469093,6925800,6079995,5316497,67442,2341111,563262,5921652,1990173,7152643,6309448,8625014,3717053,2206594,9933413,8466767,4829429,9510860,1721696,1463724,9062761,5630962,1439733,5222900,3393640,9250691,613698,4669049,8533283,839591,8270416,2244710,7324399,8528143,8022295,5569681,4513233,8233343,2437803,4311472,9749056,5569681,4800056,9242599,9577338,6031354,1872653,2274337,3912410,3445301,1532197,8696634,9320109,8597918,7238069,8625014,4437090,9803105,6274062,6548608,6582678,9221298,6463758,8199065,1409434,5143647,6144710,6247132,686835,9850461,4945951,9979978,6528369,1867954,5851730,5691985,6528369,933134,2404560,8734408,6505261,8048209,5733325,4607032,572228,779814,792542,8240416,3484842,3617742,9023873,2200274,6253936,1653294,3763998,4201289,835275,9768987,9724885,810350,6079141,5805984,2621737,9914779,4758730,6517242,5025096,3735625,9242599,5899155,7792221,8063876,7104089,4217142,7823506,5831881,3771466,3633961,7897248,8787938,709183,3762371,6385638,2715035,2052532,2762079,4349147,255730,5110846,4923969,942641,5409693,3918488,5087295,7869983,3911548,933854,4423983,4501742,7869983,5137149,5163943,626404,6680165,2601112,5144075,3957945,224685,189500,4437090,3618194,1691604,8545580,7047828,6610758,8822241,685765,3698404,1513160,7188852,7192845,6144710,4923969,1532197,3811716,3853093,4911292,4430885,4871742,9661923,4937485,6168942,7524789,7475218,9108501,5144075,3502763,1790996,9945506,8022295,2596592,189500,4092517,6168942,4403216,6144710,2574562,839591,2548290,8905879,9155690,3550335,2259517,7329099,8905879,589722,5134115,1511046,1744986,710418,8716975,584038,9501216,8712007,1542831,839591,8112859,4423983,5227876,1542831,626404,7622710,1865741,836753,1685587,8872079,8469093,7920717,3321154,2896320,1848916,4585880,5615236,2733898,1848916,3831868,4064988,1849885,7568630,1208037,9764142,6197386,3912410,5625876,4923969,709183,4906655,9214444,6769652,1448527,5753546,8822566,4667338,6886132,292051,6438907,8924130,4119971,1575154,6038312,6990592,592855,8557830,7104089,1751005,5571418,9146728,8944781,8739281,7092398,9085158,2360980,1638749,3530393,4806386,3902257,9764142,1168417,3022258,6285028,9266990,219837,3510756,4739237,9378325,6544612,2340702,4037376,1584567,6334955,9836067,3258984,7568630,9660000,5137408,2215412,7421434,6851962,5785155,238077,6447145,5632388,7396416,67442,5116026,1448527,8560728,359599,8108486,466315,1277744,5471657,7869983,6031354,1066343,4228913,5617936,25562,5899589,779814,9513963,845816,5615236,3137724,3618194,1310424,1653294,6236439,6484589,907907,7825578,5952486,4251433,836753,3438712,4669049,4739490,8278566,7946187,886343,2922054,2090618,6407363,6040028,5025096,7240154,9749056,5701146,4241787,5025096,5830899,7159261,69953,6851513,7167525,8138220,3361719,413196,7323758,8716975,8939923,2587096,835031,5510870,9203731,1982032,5517640,8364839,1375306,3651056,510398,1540365,3257254,4042460,948895,8528143,1503290,9378659,100906,8871208,8822566,5830899,7736240,3489644,4534404,2987310,3771466,2511151,7589952,6436987,6552797,4790076,1751005,907907,2621737,4728631,2084453,5475091,3194527,1053127,8503794,3206227,686114,46960,67442,5718578,3815363,5899155,8762582,951290,9661923,4859842,1919759,8427478,4877867,220634,3052281,1087406,9764142,426165,445441,886343,4806386,1573232,4064988,1631629,792907,7367715,3559050,1263547,2206594,3300756,5087295,6454819,726845,5733325,7028504,808542,9155690,8483380,7549497,3920364,7021783,2437803,5680122,6484589,4241787,3396623,1921777,2274337,907907,4439977,3987470,2621737,2485492,1981536,2810409,6373703,1375263,145525,5917422,60881,6893741,1584567,726570,4097695,6844968,238077,4545077,223547,8537113,7329099,9119755,9146728,4149208,249806,6079141,7192845,8669750,5571418,5222580,238077,4963960,8108278,6669689,7950449,308910,359599,5716653,2810409,839591,5716653,7188852,7064859,6463758,403656,9210653,6196693,6505261,1250563,7421321,7045895,5276923,1575154,2904204,5893850,3735625,9879756,899357,8649217,8533283,613698,674140,8772604,2275746,1376362,8711625,2363599,8409953,3617742,6463758,3673524,359599,7659720,4611227,9210653,8601394,3266086,5952486,8108486,7033936,1935239,7977319,9160669,4311472,2898662,9979978,5546670,1112475,1025427,3555787,6034687,4923969,5780505,3396623,3714828,2200274,1656732,3442451,7618617,6334955,5632388,8370536,3475251,6754369,7935663,8503794,2850220,1976760,2928299,5588354,8855451,607676,2162190,238077,3555787,4945951,8087322,8108278,3557478,8466767,4052043,9669589,5229839,2640715,5388528,5917422,9979978,4898536,7451611,3537617,1813475,8564958,7803764,3746702,3510756,1594770,5782726,7475218,1526585,314148,7896848,8667234,5475091,1733630,9998509,1803821,5534409,1472834,6458303,9466990,8519443,8833281,6996410,1955869,2954303,3762371,8551194,6353914,8762582,3915290,48921,9796577,7021783,2900950,2120600,8875833,8233343,7324399,8205384,8867865,9998509,140334,6285028,8464418,8916403,2093635,4654751,6095966,1872653,875271,6922478,8734408,7825578,2400734,6579233,7823506,3617742,2548290,950127,5087295,1956767,6485302,66111,1302434,7041561,3917698,3771466,7863886,2934102,5744686,7867355,4149208,3811716,3261483,6852624,2874209,4341172,1503290,9166476,6769652,2492692,3629263,5137408,7306924,9669589,6683981,5248750,1252963,9203731,3068607,7897248,2215412,875247,3337455,9812783,4123942,8882104,761930,6197386,9963317,2532936,9567679,1653294,3673524,2184578,8469093,3510756,7104089,1653294,5389805,4669049,5265315,7045895,3386555,4774222,5187511,2015670,8625014,2228773,1113377,552694,6228336,4439284,3112521,4729165,6197386,7240154,4850659,636318,377773,942641,6467375,7092398,4673018,5720926,6741789,7936552,5743413,844147,3869979,459765,2256166,5977973,2404488,1976760,7946187,7791062,7028504,4898536,8742818,2605357,1824684,3530393,1574890,413077,5615236,1918996,5785155,8617424,9549729,6208636,9003004,9669589,6309448,9644466,5097619,8728069,5931265,1685587,2428210,1855612,459765,931833,9174507,9241350,1087406,2275746,7475218,8787938,75589,6557361,7361895,4859560,2184578,6353895,7152643,6587837,6344683,8712007,224685,7383962,282698,3090932,2510715,931833,1956767,9146904,5976126,7257190,9203731,6458303,5388528,9316059,5316497,1089732,7107322,9003004,3922675,8819193,1572852,9091895,4844988,5743413,7033936,219837,3902257,6168942,2874209,7104089,1721696,6491674,579449,639312,741202,4898536,7064859,7448900,7524789,8871891,7799902,4589826,1865741,1573796,792907,7552538,7475218,6240622,6852624,7499069,1929036,8205384,2616381,5831881,8529356,921946,8370087,7676098,4800056,7271222,764787,8939923,7946187,6996410,9241350,7920504,2896320,4755153,5062721,4923969,5614507,4430885,6531704,2733898,2518714,552992,3632680,7028504,4773800,4939309,146388,876593,9320231,1605643,1083559,3475251,1099539,9293454,8246106,8718675,6454819,8303687,4510025,9210653,445441,7631394,9945506,4051132,3265577,6412164,5588354,1267870,6142953,4430885,8293821,1439733,2762079,3442451,275124,5868848,907907,7522009,7390329,1263547,66111,6754369,6912806,8560728,4439977,7185760,5036506,7552538,761046,6197492,6616558,9501216,4439977,7631394,8871208,6454819,3540877,3112521,8303687,5388528,8465175,7482449,2517615,6285028,2428210,7667960,1575154,9203731,261588,2055807,7549497,5541121,5611218,8669750,4673018,7920504,5921652,3673524,6886132,5805984,6625308,1267870,92632,5364193,2244710,4766074,7575605,2343611,2184578,7863886,1813475,8024689,3618194,782598,659011,7823791,1542831,7868696,7719370,5001430,7240154,8681400,9155690,75589,2922054,5588354,9103364,6437548,1526585,5733325,4488952,2199054,6485302,2898780,792542,5155526,3629263,6649724,6366804,4551138,5351408,9577338,3200443,9119755,3078489,6437548,4963960,8841891,899357,3257254,8337526,8551194,8124603,3076489,8649217,7389406,9486294,2471094,7910083,579449,310017,1022659,116007,9486294,9846247,8294717,4802245,5134115,6886132,7867355,9501216,8015472,7572884,6996410,8037032,310093,9316059,9724885,636318,6447145,5102381,4871742,835031,4445729,6353895,2383539,1790996,3341892,4090357,2726547,362718,674140,6886132,3724008,7396416,6616558,6253936,4439977,8524314,2200274,4149208,5720926,3210112,5718578,4331208,5899589,3618194,1008056,2244710,4803488,8687137,6218583,2428210,5215372,9797363,7448900,626404,1534041,9266990,4673018,2896320,5625876,6102261,25562,9724885,4795969,6906767,3010630,1955869,6381664,9380615,899357,2272771,1189991,3920364,5097946,4513770,7312239,1277744,9208373,5025096,4728506,8924130,8557858,3654494,5475091,8400180,1542831,5868848,8240416,2922054,2548290,6852624,6197492,8597918,3943844,4739490,9745660,2052040,8564958,907907,3122238,145525,7104089,710418,5036399,9745660,7792221,4667338,8944781,3502763,69953,2341111,1751005,8026230,3337455,5614507,607676,6218583,726845,8755598,5189995,3194527,1267870,7946187,3815363,6491674,7802593,8519443,7312239,3257254,7520576,9407829,2601005,8564958,2655767,4376996,1078251,1612829,8905879,9046784,2400734,6316311,2200274,1733630,1874883,9510860,835275,2780350,4513233,2303022,4552116,8048209,4513233,7584625,7659720,7353375,8087322,8601441,466315,4607032,7421434,6464927,8845669,3853093,4859560,6544612,738471,9797363,7823506,6557361,6642684,5976126,6353895,8617424,5415589,3876935,8961643,2272771,6467375,6680165,8670345,1375306,6485302,3722760,5617936,6366804,7910083,7306924,6528369,4510025,3300756,584038,4790076,1463724,89674,5155526,5912930,9678108,7706355,8233166,6095966,5562116,3396623,7825578,5143647,3514804,8667234,6401559,5230887,7041561,5657200,5868848,933134,7896848,2650139,2590292,6844968,2780350,3245338,4698013,3979590,7823791,2733898,8197400,9301947,5766589,7033936,3445521,165300,9242599,7575605,9950883,4923969,9386629,832889,9998509,8841891,9963317,2303022,4304314,5931265,9203731,7791062,5056214,4970046,6544612,2787113,6353895,1022884,7014728,7600150,2666985,5087295,6316311,2681753,4363577,2780350,5560163,336815,5171708,626404,2343611,3484842,1377971,856735,8996648,1848916,1652454,2476339,1235874,5598724,1001651,6210780,3869979,2505308,7033936,6528369,7104089,4850659,7367604,261588,8880346,8696634,1197293,4611227,9380615,2143249,792542,5625876,6437548,9166476,5076668,8882104,3722760,2640715,5001430,6316427,4941625,8550678,8040401,1362133,3078489,1573796,6377766,1252963,2720669,8158767,6248345,4690539,2762079,9396726,1189991,4911292,145525,3820511,5363672,1546349,4090357,7159093,6494362,3437663,5492752,5893850,1857485,9997297,7920504,711197,6315594,8755598,9963317,1738600,4251433,4265404,6851962,907907,7600150,592855,1098902,7869983,1189991,6517337,1375263,4728506,6874075,6197492,1668325,6353914,6505261,251081,9178677,2476965,2434409,8557858,5163943,4119971,4787581,9939084,6103394,8758898,4311472,1574890,2476965,2492692,1099539,3265577,5116026,2548290,2296715,6748835,6922478,6103394,5611218,8108486,8867865,3166615,4132502,1409434,1848916,6454819,3943844,3918488,875271,8597918,7524789,8138220,5701146,8497920,6200849,5826225,5229437,639312,1342528,2844246,6912806,2228773,6505261,7367715,4405670,189500,1982032,7706355,6990592,5126309,6344683,9371948,3651056,2898780,5868848,145525,3056057,116007,792542,7367715,2780350,3068607,2720669,4945971,1080879,7092398,8529356,5744686,4863708,2862875,9644466,3773444,7935663,1112475,520187,3629263,6505261,832889,7719370,1110886,3876935,303255,1584567,2735968,5415589,23441,9724885,2020428,9166476,165300,1540365,4483131,5189995,9320231,3682604,5116026,2443111,8900473,3790308,5753546,3735625,224685,9780430,8037032,9814871,3445521,2275746,2476965,5562116,2400734,4790076,397985,1874883,1993791,6494362,6528369,2404704,8617424,9803105,2510715,1902941,7522009,5701146,3756452,7451611,3793805,4862825,1457514,7706355,6680542,6205048,5363672,3831868,6436987,7975377,4669049,4057283,7737572,6491674,9644466,9203731,8111467,8124603,4862825,7626638,6256232,1573796,8762582,9623523,3945051,387761,224685,761930,3557478,4871742,7188852,3922675,1849885,314148,3122238,2443111,8529356,1656732,1268745,1053127,674140,1003296,1546349,761046,9357111,5534409,2274337,2340702,7896848,1908757,2934102,7936552,5388528,1375263,4945951,4090357,703239,5517640,3762371,2602333,5171708,665730,9749056,4842255,7367715,1739116,4058809,9351410,4439284,8660759,7104089,1040143,278812,4020102,9850461,4081033,4611227,8625014,2532936,738471,6847164,161309,7329099,2898780,4363577,3397290,5782726,2272771,8009482,1981536,4862825,2244710,9467039,4541227,6200849,3858873,911010,2143249,796097,9665019,5265315,128730,4201289,220634,2456786,6268633,2505308,377773,3334975,2383539,7667960,8996648,2274337,5505195,8718675,4939309,8597918,6769652,6217949,796097,2093635,8427478,782598,6484589,9660000,2862875,7192922,3443606,1257009,9320231,5691985,1087406,1751005,1261918,4739237,796097,8649217,438449,1066343,552992,5464873,7367715,9221298,8900473,8855451,5892566,8875833,3123153,6534247,1652454,6852624,3437663,707872,5808632,8240416,921946,7823506,9242599,4970046,1409434,9846247,3475251,7545780,6256232,9513963,8819193,826113,8040401,579449,4607032,5230060,1573232,9424969,2588238,6047351,116007,1194377,7743136,5110928,8867865,6412164,4403216,8693925,5036399,5680122,8370087,8464418,2550669,755832,1278274,8087322,2733898,4384835,2532936,4599028,9823648,4734014,6430907,1671017,3820511,2476965,2404488,9836067,4057283,1849885,3917066,9241350,3651056,4274271,4589826,5952486,3711406,7792221,8762582,2360980,9403301,2404560,2055807,3915290,4911292,3258984,9320231,8028155,8028155,6624840,2199054,6594548,7104089,342187,2884941,9293454,3245338,8233166,8435222,4655495,9138348,8111467,8435363,4634832,1546349,8900473,6505261,875271,227308,909817,6334955,4655495,2735968,3510756,2900950,1235874,1668325,5766853,6103394,7383962,9549729,336815,1573796,1929036,4510025,7383962,5110846,7646853,1277744,7482449,1546349,8370087,1212896,639312,4333586,9320109,9221298,8464418,411795,4206673,5614507,5351408,5965944,4877867,8662818,5097619,8670345,3052084,377773,2850220,9108501,3831868,9620814,5534409,757092,3038452,6051959,8625014,3791179,2084453,2780350,3987470,5609750,8845669,836753,782598,1025427,1935239,1189991,4669049,6748835,4341172,6447334,4607032,9812783,7867355,8551194,5163943,3057098,219837,5388528,3445301,835031,2141169,2434409,2052040,1425328,6197386,4645716,6240622,3258984,3443606,5785155,5571418,9197335,7033936,7396416,2404704,6102261,8867865,792542,3194527,7014728,5076668,6268633,8108486,8956583,6505261,8464418,9197335,607676,4669049,5227759,4898536,1824684,8630379,3816127,6940832,6467375,2565042,2131384,6868446,6625308,3047503,9190566,4551138,8370087,2341111,9091895,4384835,278812,6315594,238077,3519958,9138348,392866,3831868,835275,8898584,4673018,6420785,2601112,5110928,4138509,9907641,1981536,9661923,6385638,7257190,933134,8669750,6893741,7674559,6437548,8483380,9484636,4042460,826232,7717129,5899155,4064117,9403301,6454819,8015472,8158767,5475091,6344896,5222900,5276923,9403301,9094770,8872079,6868446,9371948,521612,1235874,4812558,4132502,1751005,5733325,1702167,4674577,8464418,1212896,7271222,7240154,9378325,9103364,8631458,6840175,7572884,2532936,3882502,7167525,2084453,359599,2819841,6144710,1194775,1008056,5720926,8822566,5307113,7499069,8484673,6680542,9155690,7535284,3687640,6851962,1638749,4585880,6937441,8138220,9484636,1612829,2272771,1022884,4790076,3321154,1981536,3958238,9918387,1337419,8597918,1022884,4241787,7946187,2123693,9764142,5143647,9708543,6434185,6426321,7421321,3397290,4222165,4430885,8181264,5381003,5189995,4069888,9918387,6060172,4765976,9240252,1671017,2596592,3869979,8347233,145525,1115818,413077,2476965,7238069,342187,2650139,4037278,6481455,5780505,6485302,1448527,666194,4717134,4599028,2363599,1956767,5701146,5921652,6912806,9371948,5220115,1040394,4439977,7238069,1115818,8028155,1060859,7920717,1553104,2666857,5569681,4739237,2499278,8755598,4765976,1212896,6893741,6040028,3762371,1574890,7946187,6517337,8397497,5830899,3731864,8435222,7359223,6642684,5541121,7802593,5341051,6491674,5331716,2532936,2052040,4446329,8755598,726570,6625308,4790076,844147,8368841,2844246,23441,6031354,4937485,7561634,2565042,7737572,6844968,1586072,8240416,2394219,4713061,6315594,7803764,5222580,5222580,1189991,8608366,1115818,2787113,3530393,6037552,3030298,1003296,5505195,552992,7395206,6643481,1799971,9814871,7383962,7028504,4673018,6649724,8832819,1981536,3205927,6534247,3831868,7482449,292051,8189207,7235773,1244958,3038452,4119971,6587837,1481174,909817,9380615,3030298,7324399,5097619,3897310,2681753,9021919,7631330,1733630,9361958,6309448,9480163,8063876,5158494,8503794,1921777,4206673,5899589,8456307,9825313,1738600,7325450,3166615,7706355,2517615,9062761,8880346,8832819,238077,6344896,8270416,8550678,9797363,2844246,6947776,4241787,5297784,7823791,7589058,8246106,8415064,543919,6370725,921946,3711406,1887914,2510150,6925800,9396726,764787,9549729,9407829,9945506,665730,5782726,4945951,9349888,703239,8278566,2426918,7736240,909817,9644466,5363672,4589826,8158767,6925800,7977319,4877867,8909552,9246522,3443606,205815,154087,255730,4534404,3633961,367306,5409693,270703,9062761,5039881,933134,7047828,7110095,3090932,2428210,4713061,8456307,8278566,205815,9094770,1268745,1140532,2614088,7021783,4963960,2206594,5143647,445441,1197293,2476965,3341892,6627005,7237234,7367604,8503794,1757415,6552797,1849921,3065989,4765976,2456786,7110095,4726243,5219925,763910,1268745,6583850,8026230,7159093,3987470,5785155,4687683,9174507,584038,5227759,6430907,4403216,4012253,3508532,8497821,8028155,741202,3897310,8670345,4081033,5363672,4576444,1627743,4064117,1656732,8466767,4513233,145525,9916443,1302434,685765,2443111,6875371,5116026,2884941,8718675,4717134,1834154,7713152,6040028,2762079,1993791,3687640,9386629,2055807,4437090,4911292,3300756,1594770,8465175,7306924,4765976,2305724,1001651,4020102,3920364,3771466,310093,1377971,1503941,8270416,6350517,7667960,5569681,2275746,223547,5912930,8519443,5409693,5931265,1908757,9641537,7231439,7760311,6625308,9661923,5976126,6548608,4227938,2269522,4251433,413077,3038452,8557830,1982032,4265404,3651056,4303744,6579233,779814,710418,2508213,764787,4303744,6470532,686114,2787113,1066343,145525,9210653,6274062,7946187,9708543,8822241,3811716,9065803,9138348,8519443,8794059,251081,741202,6730866,3205927,6217949,249806,2090618,2404488,255730,5230060,9724885,5892566,8762582,8360348,5187467,7482449,4051132,832889,8882104,6407363,8465175,6344896,5351408,2574562,8370536,6852624,9046784,4844988,7499069,1990173,8524314,5617936,8024689,9094770,1087406,7192922,6467375,4081033,4437090,1572852,6047351,8597918,310017,6947776,5899589,66111,6925800,3617742,9349888,7605097,2206594,6680542,3888524,9657532,4674577,8930753,3987470,6353895,8728069,9197335,7584625,1375263,2303022,1918996,1671017,9122404,1448527,5229437,5918155,4333586,9054770,8822241,3166615,4690539,9647571,4090357,1310424,1511046,9214444,5517640,9122933,6947776,3245338,2904204,1008056,7324399,6065866,2532566,7823506,2199054,331338,1956767,2596592,9998509,8303465,1273047,6256232,738471,8875833,3979590,8364839,8711625,7329293,1302434,9897893,4405670,9178677,7448900,887812,8755598,5475091,4227938,392866,9647571,1813475,552694]
    space = 2250
    print (leet_2365.taskScheduler2(a, space))
    
        
