# Tính tổng các số chẵn từ 0 đến 100
using System;

class Program
{
    static void Main()
    {
        int tong = 0;
        for (int i = 0; i <= 100; i += 2) // duyệt từ 0 đến 100, bước nhảy 2
        {
            tong += i;
        }
        Console.WriteLine("Tổng các số chẵn từ 0 đến 100 là: " + tong);
    }
}
