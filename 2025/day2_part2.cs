using System.IO;

string line = File.ReadAllText("./inputs/day2.txt");
string[] ranges = line.Split(",");
long total = 0;

foreach(string range in ranges)
{
  string[] bounds = range.Split("-");
  long lower = long.Parse(bounds[0]);
  long upper = long.Parse(bounds[1]);
  for(long i = lower; i <= upper; i++)
  {
    string s = i.ToString();
    bool isRepeating = false;
    for(int len = 1; len <= s.Length / 2; len++)
    {
      if(s.Length % len == 0)
      {
        bool match = true;
        for(int k = len; k < s.Length; k++)
        {
          if(s[k] != s[k % len])
          {
            match = false;
            break;
          }
        }
        if(match)
        {
          isRepeating = true;
          break;
        }
      }
    }

    if(isRepeating)
    {
      total += i;
    }
  }
}

Console.WriteLine(total);