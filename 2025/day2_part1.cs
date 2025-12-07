using System.IO;

string line = File.ReadAllText("./inputs/day2.txt");
string[] ranges = line.Split(",");
long total = 0;

foreach (string range in ranges)
{
  string[] bounds = range.Split("-");
  long lower = long.Parse(bounds[0]);
  long upper = long.Parse(bounds[1]);
  for(long i = lower; i <= upper; i++)
  {
    int numDigits = (int)Math.Floor(Math.Log10(i)) + 1;
    if(numDigits % 2 == 0)
    {
      long part1 = i / (long)Math.Pow(10, numDigits / 2);
      long part2 = i % (long)Math.Pow(10, numDigits / 2);
      if(part1 == part2)
      {
        total += i;
      }
    }
  }
}

Console.WriteLine(total);