#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUF_SIZE 50

int cal(int a, int b, int c)
{
    int i, j, k;
    int total = 0;

    for(i = 0; i < a; i++)
    {
        for(j = 0; j < b; j++)
        {
            for(k = 0; k < c; k++)
            {
                if(i > k && j < i)
                    return cal(a-1, b-1, c-1);
                return total + cal(a-1, b-1, c-1);
            }
        }
    }

    return 1;
}

int main(int argc, char** argv)
{
    char FLAG[BUF_SIZE];
    scanf("%s", FLAG);

    int pass1 = 0;
    int pass2 = 0;
    int pass3 = 0;
    int pass4 = 0;

    int i, j, k;

    int len = strlen(FLAG);

    if(argc == 1)
    {
        if(len < 30)
        {
            int a = (FLAG[10] ^ FLAG[15]) + (FLAG[12] ^ FLAG[21]) + (FLAG[19] ^ FLAG[8]);

            if(a < 100)
            {
                int b = ((a ^ 257193) - 244285) ^ 8284913;
                if(b == 84829144)
                {   
                    if((((len * len) ^ 218452) + 14810) == 5885213)
                    {
                        pass3 = (len + b) - 3851246 + 128596;
                    }
                    if((FLAG[0] ^ FLAG[1] ^ FLAG[2] ^ FLAG[3] ^ FLAG[4] ^ FLAG[5]) == 41)
                    {
                        if(((FLAG[1] ^ FLAG[2]) + 1) == (FLAG[0] ^ FLAG[2]))
                        {
                            if(((FLAG[4] ^ FLAG[1]) - 1) == (FLAG[0] ^ FLAG[2]))
                            {
                                if(((FLAG[5] ^ FLAG[1]) - (FLAG[2] ^ FLAG[5])) == (FLAG[1] ^ FLAG[0]))
                                {
                                    if(((FLAG[1] ^ FLAG[3]) - (FLAG[0] ^ FLAG[1]) - (FLAG[4] ^ FLAG[2])) == ((FLAG[5] ^ FLAG[4]) - (FLAG[3] ^ FLAG[5])))
                                    {
                                        if(FLAG[2] == 76 && FLAG[1] == 65)
                                        {
                                            pass4 = FLAG[2] * FLAG[5] * FLAG[4] * FLAG[1];
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
            else
            {
                int b = ((a ^ 882123) - 18453) ^ 82851;
                if(b == 28175233)
                {   
                    if((((len * len) ^ 2185852) + 11850) == 2185123)
                    {
                        pass3 = (len + b) - 18516 + 8299452;
                    }
                    if((FLAG[0] ^ FLAG[1] ^ FLAG[2] ^ FLAG[3] ^ FLAG[4] ^ FLAG[5]) == 41)
                    {
                        if(((FLAG[1] ^ FLAG[2]) + 1) == (FLAG[0] ^ FLAG[2]))
                        {
                            if(((FLAG[4] ^ FLAG[1]) - 1) == (FLAG[0] ^ FLAG[2]))
                            {
                                if(((FLAG[5] ^ FLAG[1]) - (FLAG[2] ^ FLAG[5])) == (FLAG[1] ^ FLAG[0]))
                                {
                                    if(((FLAG[1] ^ FLAG[3]) - (FLAG[0] ^ FLAG[1]) - (FLAG[4] ^ FLAG[2])) == ((FLAG[5] ^ FLAG[4]) - (FLAG[3] ^ FLAG[5])))
                                    {
                                        if(FLAG[3] == 83 && FLAG[0] == 66)
                                        {
                                            pass4 = FLAG[0] * FLAG[2] * FLAG[1] * FLAG[3];
                                        }
                                    }
                                }
                            }
                        }
                    }
                    if(pass3 == 81751928)
                    {
                        if((FLAG[9] ^ FLAG[10]) == (FLAG[13] ^ FLAG[12]))
                        {
                            if((FLAG[12] ^ FLAG[8]) == (FLAG[10] ^ FLAG[11]))
                            {
                                if(((FLAG[9] ^ FLAG[6]) - (FLAG[8] ^ FLAG[13])) == (FLAG[7] ^ FLAG[10]))
                                {
                                    if(((FLAG[14] ^ FLAG[11]) + (FLAG[13] ^ FLAG[8])) == ((FLAG[6] ^ FLAG[10]) + (FLAG[13] ^ FLAG[14])))
                                    {
                                        if(((FLAG[11] ^ FLAG[10]) - (FLAG[7] ^ FLAG[6])) == ((FLAG[10] ^ FLAG[12]) + (FLAG[8] ^ FLAG[9])))
                                        {
                                            if(FLAG[11] == 108 && FLAG[12] == 49)
                                            {
                                                pass3 = FLAG[6] * FLAG[8] * FLAG[10] * FLAG[12] * FLAG[14];
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                    if(pass4 == 15782934)
                    {
                        if((FLAG[15] ^ FLAG[20]) == (FLAG[23] ^ FLAG[24]))
                        {
                            if((FLAG[19] ^ FLAG[22]) == (FLAG[21] ^ FLAG[20]))
                            {
                                if(((FLAG[21] ^ FLAG[16]) - (FLAG[19] ^ FLAG[17])) == (FLAG[17] ^ FLAG[22]))
                                {
                                    if(((FLAG[24] ^ FLAG[18]) - (FLAG[15] ^ FLAG[19])) == (FLAG[20] ^ FLAG[16]))
                                    {
                                        if(((FLAG[15] ^ FLAG[19]) - (FLAG[24] ^ FLAG[20])) == ((FLAG[17] ^ FLAG[16]) - (FLAG[19] ^ FLAG[17])))
                                        {
                                            if(((FLAG[18] ^ FLAG[16]) + (FLAG[23] ^ FLAG[24])) == ((FLAG[16] ^ FLAG[17]) + (FLAG[22] ^ FLAG[21])))
                                            {
                                                if(FLAG[20] == 116 && FLAG[22] == 48)
                                                {
                                                    pass4 = FLAG[21] * FLAG[17] * FLAG[23] * FLAG[15];
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                    if(pass3 == 1857293)
                    {
                        if(((FLAG[25] ^ FLAG[28]) + (FLAG[26] ^ FLAG[30])) == (FLAG[27] ^ FLAG[29]))
                        {
                            if(((FLAG[29] ^ FLAG[28]) - (FLAG[27] ^ FLAG[25])) == (FLAG[30] ^ FLAG[26]))
                            {
                                if(((FLAG[28] ^ FLAG[30]) - (FLAG[31] ^ FLAG[26])) == ((FLAG[29] ^ FLAG[32]) - (FLAG[30] ^ FLAG[25])))
                                { 
                                    if(((FLAG[27] ^ FLAG[29]) - (FLAG[29] ^ FLAG[28])) == ((FLAG[27] ^ FLAG[28]) + (FLAG[28] ^ FLAG[27])))
                                    { 
                                        if(FLAG[26] == 117 && FLAG[30] == 121)
                                        {
                                            pass3 = FLAG[28] * FLAG[30] * FLAG[29] * FLAG[31];
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
                else
                {
                    for(i = 0; i < 158174; i++)
                    {
                        for(j = 0; j < 183751; j++)
                        {
                            for(k = 0; k < 91658; k++)
                            {
                                pass4 = cal(FLAG[(i*k)%30], FLAG[(i*j)%30], FLAG[(j*k)%30]);
                            }
                        }
                    }
                }
            }
        }
        else if(len < 40)
        {
            int a = (FLAG[10] ^ FLAG[15]) + (FLAG[12] ^ FLAG[21]) + (FLAG[19] ^ FLAG[8]);

            if(a < 100)
            {
                int b = ((a ^ 8589273) - 24473) ^ 8175013;
                if(b == 847194)
                {   
                    if((((len * len) ^ 242852) + 11860) == 218588)
                    {
                        pass1 = (len + b) - 32581246 + 158296;
                    }
                    if((FLAG[0] ^ FLAG[1] ^ FLAG[2] ^ FLAG[3] ^ FLAG[4] ^ FLAG[5]) == 41)
                    {
                        if(((FLAG[1] ^ FLAG[2]) + 1) == (FLAG[0] ^ FLAG[2]))
                        {
                            if(((FLAG[4] ^ FLAG[1]) - 1) == (FLAG[0] ^ FLAG[2]))
                            {
                                if(((FLAG[5] ^ FLAG[1]) - (FLAG[2] ^ FLAG[5])) == (FLAG[1] ^ FLAG[0]))
                                {
                                    if(((FLAG[1] ^ FLAG[3]) - (FLAG[0] ^ FLAG[1]) - (FLAG[4] ^ FLAG[2])) == ((FLAG[5] ^ FLAG[4]) - (FLAG[3] ^ FLAG[5])))
                                    {
                                        if(FLAG[2] == 76 && FLAG[1] == 65)
                                        {
                                            pass2 = FLAG[2] * FLAG[5] * FLAG[4] * FLAG[1];
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
            else
            {
                int b = ((a ^ 88539183) - 241863) ^ 884193;
                if(b == 89010746)
                {   
                    if((((len * len) ^ 24691852) + 195260) == 24886088)
                    {
                        pass1 = (len + b) - 3275216 + 88296;
                    }
                    if((FLAG[0] ^ FLAG[1] ^ FLAG[2] ^ FLAG[3] ^ FLAG[4] ^ FLAG[5]) == 41)
                    {
                        pass3 = cal(FLAG[0], FLAG[1], FLAG[2]);
                        if(((FLAG[1] ^ FLAG[2]) + 1) == (FLAG[0] ^ FLAG[2]))
                        {
                            pass3 += cal(FLAG[1], FLAG[2], FLAG[0]);
                            if(((FLAG[4] ^ FLAG[1]) - 1) == (FLAG[0] ^ FLAG[2]))
                            {
                                pass3 += cal(FLAG[4], FLAG[1], FLAG[0]);
                                if(((FLAG[5] ^ FLAG[1]) - (FLAG[2] ^ FLAG[5])) == (FLAG[1] ^ FLAG[0]))
                                {
                                    pass3 += cal(FLAG[5], FLAG[1], FLAG[2]);
                                    if(((FLAG[1] ^ FLAG[3]) - (FLAG[0] ^ FLAG[1]) - (FLAG[4] ^ FLAG[2])) == ((FLAG[5] ^ FLAG[4]) - (FLAG[3] ^ FLAG[5])))
                                    {
                                        pass3 += cal(FLAG[1], FLAG[3], FLAG[0]);
                                        if(FLAG[3] == 83 && FLAG[0] == 66)
                                        {
                                            pass2 = FLAG[0] * FLAG[2] * FLAG[1] * FLAG[3];
                                            pass3 += cal(FLAG[0], FLAG[1], FLAG[2]);
                                        }
                                    }
                                }
                            }
                        }
                    }
                    if(pass1 == 85823858)
                    {
                        if((FLAG[9] ^ FLAG[10]) == (FLAG[13] ^ FLAG[12]))
                        {
                            pass4 = cal(FLAG[9], FLAG[10], FLAG[13]);
                            if((FLAG[12] ^ FLAG[8]) == (FLAG[10] ^ FLAG[11]))
                            {
                                pass4 += cal(FLAG[12], FLAG[8], FLAG[10]);
                                if(((FLAG[9] ^ FLAG[6]) - (FLAG[8] ^ FLAG[13])) == (FLAG[7] ^ FLAG[10]))
                                {
                                    pass4 += cal(FLAG[9], FLAG[6], FLAG[8]);
                                    if(((FLAG[14] ^ FLAG[11]) + (FLAG[13] ^ FLAG[8])) == ((FLAG[6] ^ FLAG[10]) + (FLAG[13] ^ FLAG[14])))
                                    {
                                        pass4 += cal(FLAG[14], FLAG[13], FLAG[11]);
                                        if(((FLAG[11] ^ FLAG[10]) - (FLAG[7] ^ FLAG[6])) == ((FLAG[10] ^ FLAG[12]) + (FLAG[8] ^ FLAG[9])))
                                        {
                                            pass4 += cal(FLAG[11], FLAG[10], FLAG[7]);
                                            if(FLAG[11] == 108 && FLAG[12] == 49)
                                            {
                                                pass1 = FLAG[6] * FLAG[8] * FLAG[10] * FLAG[12] * FLAG[14];
                                                pass4 += cal(FLAG[7], FLAG[13], FLAG[11]);
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                    if(pass2 == 27061320)
                    {
                        if((FLAG[15] ^ FLAG[20]) == (FLAG[23] ^ FLAG[24]))
                        {
                            pass3 = cal(FLAG[15], FLAG[20], FLAG[23]);
                            if((FLAG[19] ^ FLAG[22]) == (FLAG[21] ^ FLAG[20]))
                            {
                                pass3 += cal(FLAG[19], FLAG[22], FLAG[21]);
                                if(((FLAG[21] ^ FLAG[16]) - (FLAG[19] ^ FLAG[17])) == (FLAG[17] ^ FLAG[22]))
                                {
                                    pass3 += cal(FLAG[21], FLAG[16], FLAG[19]);
                                    if(((FLAG[24] ^ FLAG[18]) - (FLAG[15] ^ FLAG[19])) == (FLAG[20] ^ FLAG[16]))
                                    {
                                        pass3 += cal(FLAG[24], FLAG[18], FLAG[15]);
                                        if(((FLAG[15] ^ FLAG[19]) - (FLAG[24] ^ FLAG[20])) == ((FLAG[17] ^ FLAG[16]) - (FLAG[19] ^ FLAG[17])))
                                        {
                                            pass3 += cal(FLAG[15], FLAG[19], FLAG[24]);
                                            if(((FLAG[18] ^ FLAG[16]) + (FLAG[23] ^ FLAG[24])) == ((FLAG[16] ^ FLAG[17]) + (FLAG[22] ^ FLAG[21])))
                                            {
                                                pass3 += cal(FLAG[18], FLAG[16], FLAG[23]);
                                                if(FLAG[20] == 116 && FLAG[22] == 48)
                                                {
                                                    pass2 = FLAG[21] * FLAG[17] * FLAG[23] * FLAG[15];
                                                    pass3 += cal(FLAG[20], FLAG[17], FLAG[23]);
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                    if(pass1 == 1290812880)
                    {
                        if(((FLAG[25] ^ FLAG[28]) + (FLAG[26] ^ FLAG[30])) == (FLAG[27] ^ FLAG[29]))
                        {
                            pass4 = cal(FLAG[25], FLAG[28], FLAG[26]);
                            if(((FLAG[29] ^ FLAG[28]) - (FLAG[27] ^ FLAG[25])) == (FLAG[30] ^ FLAG[26]))
                            {
                                pass4 += cal(FLAG[29], FLAG[28], FLAG[27]);
                                if(((FLAG[28] ^ FLAG[30]) - (FLAG[31] ^ FLAG[26])) == ((FLAG[29] ^ FLAG[32]) - (FLAG[30] ^ FLAG[25])))
                                {
                                    pass4 += cal(FLAG[28], FLAG[30], FLAG[31]); 
                                    if(((FLAG[27] ^ FLAG[29]) - (FLAG[29] ^ FLAG[28])) == ((FLAG[27] ^ FLAG[28]) + (FLAG[28] ^ FLAG[27])))
                                    { 
                                        pass4 += cal(FLAG[27], FLAG[29], FLAG[29]);
                                        if(FLAG[26] == 117 && FLAG[30] == 121)
                                        {
                                            pass1 = FLAG[28] * FLAG[30] * FLAG[29] * FLAG[31];
                                            pass4 += cal(FLAG[30], FLAG[27], FLAG[31]);
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        else if (len < 50)
        {
            for(i = 0; i < 28571; i++)
            {
                for(j = 0; j < 285392; j++)
                {
                    for(k = 0; k < 18758; k++)
                    {
                        pass3 = cal(FLAG[(i*k)%50], FLAG[(i*j)%50], FLAG[(j*k)%50]);
                    }
                }
            }
        }
        else
        {
            printf("Input size too large!\n");
        }

        if(pass1 == 89661000 && pass2 == 18967410)
        {
            printf("Congratulation! Now you got the FLAG!\n");
        }
        else
        {
            printf("Too bad! You don't have the FLAG!\n");
        }
    }

    return 0;
}