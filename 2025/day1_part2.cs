using System.IO;

string[] lines = File.ReadAllLines("./inputs/day1.txt");
int dial = 50;
int original = dial;
int times = 0;

foreach (string line in lines)
{
  original = dial;
  if(line[0] == 'L')
  {
    dial -= int.Parse(line[1..]) % 100;
    times += int.Parse(line[1..]) / 100;
    if(dial <= 0)
    {
      dial += dial < 0 ? 100 : 0;
      times += original != 0 ? 1 : 0;
    }
  }
  else
  {
    dial += int.Parse(line[1..]) % 100;
    times += int.Parse(line[1..]) / 100;
    if(dial >= 100)
    {
      dial -= 100;
      times++;
    }
  }
}

Console.WriteLine(times);
