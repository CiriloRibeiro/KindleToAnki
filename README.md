# KindleToAnki
A Python-based solution for automating English Anki decks from the Kindle database.

You must copy the file `vocab.db` into the same folder of this program before you start.

## A example of Output 

In this example, I will create a deck for a book called Zen Mind, Beginner's Mind.
1) First of all, get the `vocab.db` in the same folder as `main.py`
2) Take your API Key and change the variable `API_KEY` in `main.py`
3) Run the script and select the `id` of the chosen title.
4) The script will take the words and the usage from the vocab database and send a `GET request` for the Merriam-Webster's Collegiate® Thesaurus API to fetch each word definition (It can take a couple of minutes, depending on how many words your book has.)
5) Finally, your Book's deck will be created and saved in the /Decks directory.
6) Open the new apkg file in Anki and enjoy your English learning.

```
Database connection opened and DataFrame created

                                                title
id                                                   
1   (New Directions Paperbook) Yukio Mishima - Con...
2             12 Rules for Life, An Antidote to Chaos
3   Can't Hurt Me: Master Your Mind and Defy the Odds
4   Chris Voss - Never Split the Difference_ Negot...
5   Daniel Gilbert - Stumbling on Happiness-Knopf ...
6   David Deida - The Way of the Superior Man_ A S...
7   David Finch - The Journal of Best Practices_ A...
8   DeMarco, M. J - The millionaire fastlane_ crac...
9                                           Deep Work
10  Dr Julie Smith - Why Has Nobody Told Me This B...
11                                               Dune
12  Four Thousand Weeks_ Time Management for M - O...
16  Stephen R. Covey - The 7 Habits of Highly Effe...
17                                    The Daily Stoic
18  The Four Pillars of Investing: Lessons for Bui...
19                               The Mind Illuminated
20                                 The Power of Habit
21  The Ten Equations that Rule the World: And How...
22                            Thinking, Fast and Slow
23  Tynan - Superhuman Social Skills_ A Guide to B...
24  Wait But Why Year One: We finally figured out ...
25                                              Women
26                          Zen Mind, Beginner's Mind

Select a valid Title ID, or q to quit: 26
Title set to Zen Mind, Beginner's Mind
Getting word definitions: Word 10 out of 65. This may take a while, please wait...
Getting word definitions: Word 20 out of 65. This may take a while, please wait...
Getting word definitions: Word 30 out of 65. This may take a while, please wait...
Getting word definitions: Word 40 out of 65. This may take a while, please wait...
Getting word definitions: Word 50 out of 65. This may take a while, please wait...
Getting word definitions: Word 60 out of 65. This may take a while, please wait...
Completed definition column
Deck saved successfully.
```
## Here is a glimpse of what you can achieve with the program.

<img
  src="https://i.imgur.com/XViIEoW.png"
  width="500" height="500"
  style="display: inline-block; margin: 0 auto; max-width: 500px">


This program uses the Merriam-Webster's Collegiate® Thesaurus API for fetching English word definitions.
Therefore, you must request a Merriam-Webster's Collegiate® Thesaurus API key to connect to the API.

<img
  src="https://i.imgur.com/2riGnLz.png"
  width="100" height="100"
  style="display: inline-block; max-width: 500px;text-align: center;">


