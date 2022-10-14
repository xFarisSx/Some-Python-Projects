using System;

namespace guessing
{
    class Program
    {   
        //Entry Point
        static void Main(string[] args)
        {
            string appName = "Number Guesser";
            string appVersion = "1.0.0";
            string appAuthor = "Faris Sammour";

            Console.ForegroundColor = ConsoleColor.Green;

            Console.WriteLine("{0}: Version {1} by {2}", appName, appVersion, appAuthor);

            Console.ForegroundColor = ConsoleColor.White;

            Console.WriteLine("What is your name");

            string inputname = Console.ReadLine();

            Console.WriteLine("Hello {0}, let's play", inputname);
            bool yes = true;
            bool son = false;

            while (yes == true)
            {
                Random random = new Random();

                int correctNumber = random.Next(1, 11);

                int guess = 0;

                Console.WriteLine("Guess a  number between 1 and 10");

                int turns = 3;
                

                while (true)
                {

                    
                    if (turns == 0 && guess != correctNumber)
                    {
                        Console.ForegroundColor = ConsoleColor.Red;
                        Console.WriteLine("Lost The Game!");
                        Console.ForegroundColor = ConsoleColor.White;
                        son = true;
                        break;
                    }
                    else if (turns >= 0 && guess == correctNumber)
                    {
                        Console.ForegroundColor = ConsoleColor.Yellow;

                        Console.WriteLine("Won The Game!!");

                        Console.ForegroundColor = ConsoleColor.White;
                        son = true;

                        break;
                    }

                    if (son == true)
                    {
                        Console.WriteLine("Wanna play again?");
                        var ans = Console.ReadLine();
                        if (ans == "no")
                        {
                            yes = false;
                            son = false;
                            break;
                        }
                        else
                        {
                            yes = true;
                            Console.WriteLine("Enter your guess!");
                            son = false;
                        }
                    
                    }

                    turns--;


                    string input = Console.ReadLine();

                    if (!int.TryParse(input, out guess))
                    {
                        Console.ForegroundColor = ConsoleColor.Red;
                        Console.WriteLine("it is not a number!");
                        Console.ForegroundColor = ConsoleColor.White;
                        turns++;
                        continue;

                    }

                    guess = Int32.Parse(input);



                    if (guess != correctNumber)
                    {
                        Console.ForegroundColor = ConsoleColor.Red;

                        Console.WriteLine("Try Again!");

                        Console.ForegroundColor = ConsoleColor.White;
                    }
                }
            }
            

        }

    }
}