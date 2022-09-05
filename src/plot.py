import os
import sys
import re
import json
from datetime import *
from tkinter.tix import Tree
from tokenize import String
from typing import List
import matplotlib.pyplot as plt
import numpy as np

metricsTime = [
    "00:00",
    "00:05",
    "00:10",
    "00:15",
    "00:20",
    "00:25",
    "00:30",
    "00:35",
    "00:40",
    "00:45",
    "00:50",
    "00:55",
    "01:00",
    "01:05",
    "01:10",
    "01:15",
    "01:20",
    "01:25",
    "01:30",
    "01:35",
    "01:40",
    "01:45",
    "01:50",
    "01:55",
    "02:00",
    "02:05",
    "02:10",
    "02:15",
    "02:20",
    "02:25",
    "02:30",
    "02:35",
    "02:40",
    "02:45",
    "02:50",
    "02:55",
    "03:00",
    "03:05",
    "03:10",
    "03:15",
    "03:20",
    "03:25",
    "03:30",
    "03:35",
    "03:40",
    "03:45",
    "03:50",
    "03:55",
    "04:00",
    "04:05",
    "04:10",
    "04:15",
    "04:20",
    "04:25",
    "04:30",
    "04:35",
    "04:40",
    "04:45",
    "04:50",
    "04:55",
    "05:00",
    "05:05",
    "05:10",
    "05:15",
    "05:20",
    "05:25",
    "05:30",
    "05:35",
    "05:40",
    "05:45",
    "05:50",
    "05:55"]
user_count = [0,
              1,
              6,
              11,
              16,
              21,
              26,
              31,
              35,
              40,
              45,
              50,
              55,
              60,
              65,
              70,
              75,
              80,
              85,
              90,
              95,
              100,
              105,
              110,
              115,
              120,
              125,
              130,
              135,
              140,
              145,
              150,
              155,
              160,
              165,
              170,
              175,
              180,
              185,
              190,
              195,
              200,
              200,
              200,
              200,
              200,
              200,
              200,
              200,
              200,
              200,
              200,
              200,
              200,
              200,
              200,
              200,
              200,
              200,
              200,
              200,
              200,
              200,
              200,
              200,
              200,
              200,
              200,
              200,
              200,
              200,
              200]
zt = [
    0,
    2200.0,
    2200.0,
    86,
    78,
    89,
    100.0,
    150.0,
    150.0,
    95,
    90,
    95,
    140.0,
    100.0,
    78,
    99,
    110.0,
    110.0,
    170.0,
    150.0,
    150.0,
    130.0,
    90,
    110.0,
    120.0,
    120.0,
    130.0,
    110.0,
    100.0,
    260.0,
    260.0,
    180.0,
    150.0,
    150.0,
    420.0,
    510.0,
    420.0,
    220.0,
    140.0,
    320.0,
    560.0,
    720.0,
    1200.0,
    1200.0,
    990.0,
    570.0,
    200.0,
    160.0,
    160.0,
    180.0,
    180.0,
    170.0,
    340.0,
    350.0,
    180.0,
    170.0,
    210.0,
    210.0,
    170.0,
    150.0,
    140.0,
    140.0,
    630.0,
    950.0,
    960.0,
    390.0,
    200.0,
    410.0,
    410.0,
    2000.0,
    2800.0,
    2700.0
]
it = [
    0,
    79,
    79,
    96,
    91,
    84,
    88,
    92,
    86,
    97,
    100.0,
    100.0,
    92,
    94,
    95,
    120.0,
    150.0,
    180.0,
    110.0,
    110.0,
    110.0,
    110.0,
    120.0,
    140.0,
    180.0,
    130.0,
    120.0,
    120.0,
    120.0,
    110.0,
    120.0,
    150.0,
    160.0,
    130.0,
    130.0,
    150.0,
    140.0,
    130.0,
    300.0,
    380.0,
    280.0,
    160.0,
    140.0,
    160.0,
    210.0,
    200.0,
    170.0,
    190.0,
    220.0,
    220.0,
    160.0,
    170.0,
    190.0,
    170.0,
    150.0,
    150.0,
    140.0,
    160.0,
    150.0,
    130.0,
    170.0,
    170.0,
    150.0,
    150.0,
    160.0,
    160.0,
    300.0,
    280.0,
    140.0,
    270.0,
    270.0,
    290.0,
]
ipt = [
    0,
    76,
    76,
    77,
    81,
    86,
    81,
    82,
    82,
    80,
    85,
    94,
    93,
    91,
    90,
    90,
    110.0,
    110.0,
    110.0,
    100.0,
    92,
    99,
    120.0,
    150.0,
    250.0,
    250.0,
    140.0,
    120.0,
    140.0,
    120.0,
    130.0,
    160.0,
    130.0,
    120.0,
    170.0,
    170.0,
    110.0,
    130.0,
    170.0,
    210.0,
    220.0,
    1600.0,
    1600.0,
    940.0,
    1300.0,
    1300.0,
    360.0,
    290.0,
    220.0,
    160.0,
    150.0,
    160.0,
    160.0,
    150.0,
    170.0,
    370.0,
    370.0,
    260.0,
    240.0,
    190.0,
    200.0,
    170.0,
    130.0,
    150.0,
    160.0,
    160.0,
    150.0,
    140.0,
    150.0,
    230.0,
    200.0,
    200.0
]
kt = [
    0,
    1300.0,
    2100.0,
    1100.0,
    200.0,
    100.0,
    120.0,
    130.0,
    130.0,
    170.0,
    170.0,
    130.0,
    120.0,
    130.0,
    170.0,
    140.0,
    130.0,
    150.0,
    190.0,
    150.0,
    160.0,
    170.0,
    150.0,
    170.0,
    190.0,
    220.0,
    200.0,
    200.0,
    180.0,
    170.0,
    150.0,
    340.0,
    340.0,
    180.0,
    190.0,
    190.0,
    890.0,
    860.0,
    200.0,
    350.0,
    350.0,
    180.0,
    150.0,
    300.0,
    510.0,
    2100.0,
    2100.0,
    1300.0,
    2000.0,
    2200.0,
    2200.0,
    2200.0,
    1800.0,
    280.0,
    260.0,
    210.0,
    180.0,
    200.0,
    170.0,
    160.0,
    210.0,
    200.0,
    170.0,
    210.0,
    330.0,
    330.0,
    1200.0,
    1900.0,
    3700.0,
    3600.0,
    2200.0,
    760.0
]
kpt = [0,
       92,
       92,
       110.0,
       110.0,
       110.0,
       110.0,
       97,
       110.0,
       170.0,
       170.0,
       100.0,
       110.0,
       110.0,
       270.0,
       250.0,
       160.0,
       220.0,
       260.0,
       450.0,
       480.0,
       420.0,
       360.0,
       180.0,
       180.0,
       150.0,
       230.0,
       210.0,
       170.0,
       220.0,
       240.0,
       230.0,
       280.0,
       330.0,
       270.0,
       1300.0,
       1900.0,
       2300.0,
       2200.0,
       1100.0,
       530.0,
       300.0,
       330.0,
       380.0,
       300.0,
       370.0,
       370.0,
       180.0,
       700.0,
       700.0,
       520.0,
       480.0,
       270.0,
       390.0,
       390.0,
       440.0,
       430.0,
       360.0,
       480.0,
       310.0,
       270.0,
       240.0,
       310.0,
       320.0,
       260.0,
       220.0,
       220.0,
       320.0,
       370.0,
       310.0,
       240.0,
       230.0]


def plotUsers(xpoints, xpointlabels, nusers):
    plot2 = plt.subplot2grid((1, 1), (0, 0))

    plot2.set_title("Number of Users")
    plot2.set_xlabel("Time")
    plot2.set_ylabel("Users")
    plot2.plot(xpoints, nusers, label="users")
    plot2.set_xticks(xpointlabels)
    plot2.set_xticklabels(xpointlabels, rotation=45, fontsize="small")
    plot2.grid()
    plot2.legend(loc='upper left')

    # plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.95, wspace=0.2, hspace=0.5)
    # plt.tight_layout()
    plt.show()


def plotP956(xpoints, xpointlabels, fP95, sP95, tP95, l1, l2, l3):
    plot1 = plt.subplot2grid((1, 1), (0, 0))
    # plot2 = plt.subplot2grid((2, 1), (1, 0))

    plot1.set_title("Response Time (ms)")
    plot1.set_xlabel("Time")
    plot1.set_ylabel("ms")
    plot1.plot(xpoints, fP95, label=l1)
    plot1.plot(xpoints, sP95, label=l2)
    plot1.plot(xpoints, tP95, label=l3)
    plot1.set_xticks(xpointlabels)
    plot1.set_xticklabels(xpointlabels, rotation=45, fontsize="small")
    plot1.grid()
    plot1.legend(loc='upper left')

    # plot2.set_title("Number of Users")
    # plot2.set_xlabel("Time")
    # plot2.set_ylabel("Users")
    # plot2.plot(xpoints, nusers, label="users")
    # plot2.set_xticks(xpointlabels)
    # plot2.set_xticklabels(xpointlabels, rotation=45, fontsize="small")
    # plot2.grid()
    # plot2.legend(loc='upper left')

    # # plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.95, wspace=0.2, hspace=0.5)
    # # plt.tight_layout()
    plt.show()


if __name__ == "__main__":

    xpoints = np.array(metricsTime)
    metricsTimeLabel = metricsTime[0:len(metricsTime):12]
    xpointlabels = np.array(metricsTimeLabel)
    fP95 = np.array(zt)
    sP95 = np.array(it)
    tP95 = np.array(ipt)
    nusers = np.array(user_count)

    plotUsers(xpoints, xpointlabels, nusers)

    plotP956(xpoints, xpointlabels, fP95, sP95, tP95, "demo app",
             "demo app with OPSM", "demo app with OPSM and policies")

    sP95 = np.array(kt)
    tP95 = np.array(kpt)

    plotP956(xpoints, xpointlabels, fP95, sP95, tP95, "demo app",
             "demo app with Kuma", "demo app with Kuma and policies")

    sP95 = np.array(ipt)
    tP95 = np.array(kpt)

    plotP956(xpoints, xpointlabels, fP95, sP95, tP95, "demo app",
             "demo app with OPSM and policies", "demo app with Kuma and policies")
