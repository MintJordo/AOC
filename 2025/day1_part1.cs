using System.IO;

string[] lines = File.ReadAllLines("./inputs/day1.txt");
int dial = 50;
int times = 0;

foreach (string line in lines)
{
  if(line[0] == 'L')
  {
    dial -= int.Parse(line[1..]) % 100;
    dial = dial < 0 ? dial + 100 : dial;
  }
  else
  {
    dial += int.Parse(line[1..]) % 100;
    dial = dial >= 100 ? dial - 100 : dial;
  }

  if(dial == 0)
  {
    times++;
  }
}

Console.WriteLine(times);
