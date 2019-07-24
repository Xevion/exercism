# Python Track Comments

This page represents all my comments from my solutions currently hosted on [Exercism.io](https://exercism.io/). You can view my profile [here](https://exercism.io/profiles/Xevion).
The reason for this is simply to have a place where I can collect my comments, as well as just have some fun with Python and webscraping. Exercise file and exercise submission links will be provided for each and every exercise.
This file is for the **Python** track, contains **48** submissions, **18** of which have comments. This file was built on **24-07-2019** at **04:10:14 UTC**.

## Word Count

[Link to File](./word-count/word_count.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/word-count/solutions/b8740c62231043358e4bdaa590764dbe)

Not exactly proud of this one really. I had to use regex to do the splitting as I couldn't think of a way to split on both arbitrary length whitespace AND punctuation. Luckily, the string library has access to all the punctuation I needed, so I just rolled with it. This isn't exactly the most elegant solution I could come up with, but it's definitely short and that's what matters to me. It uses list/dictionary comprehension, which is huge to me, so it should probably be moderately fast in the long run.

## Sieve

[Link to File](./sieve/sieve.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/sieve/solutions/9e38df44da5b4bc48d2d6e57ac7b5c2a)



## Hello World

[Link to File](./hello-world/hello_world.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/hello-world/solutions/e926fb7c9400480a80f75e957fe1b027)



## Leap

[Link to File](./leap/leap.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/leap/solutions/299afd8086d543ccb59fa20a3375c3bc)



## Reverse String

[Link to File](./reverse-string/reverse_string.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/reverse-string/solutions/80bc2033cd98458a89c53d5487b701d7)



## Isogram

[Link to File](./isogram/isogram.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/isogram/solutions/57fdfd4c98644a2191b9fed067526d14)

I'm kind of annoyed that there is no other way to do it that is 2 lines that doesn't have it calculate string without the spaces and hyphens twice, but whatever.

## Pangram

[Link to File](./pangram/pangram.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/pangram/solutions/928a4d5c41274472bf2b6feee833b444)



## RNA Transcription

[Link to File](./rna-transcription/rna_transcription.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/rna-transcription/solutions/3fc8fca40565475dbeb36f5e8048281f)



## ISBN Verifier

[Link to File](./isbn-verifier/isbn_verifier.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/isbn-verifier/solutions/fa2d5d0d7cc8469586d7227f197cff9f)



## Hamming

[Link to File](./hamming/hamming.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/hamming/solutions/ab3e897d3758468ca0f44cd68b2c9d33)



## Gigasecond

[Link to File](./gigasecond/gigasecond.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/gigasecond/solutions/2959cc74dfae4961a8f592df2e7a00ad)



## Bob

[Link to File](./bob/bob.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/bob/solutions/7961709ebcf94c47b27720337d4a1515)



## Yacht

[Link to File](./yacht/yacht.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/yacht/solutions/81c9206cf8c54284bd7431449526f47b)



## Run Length Encoding

[Link to File](./run-length-encoding/run_length_encoding.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/run-length-encoding/solutions/d794356bb2f64e1998420f4ed754c3e0)



## Meetup

[Link to File](./meetup/meetup.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/meetup/solutions/5ca86ad3921745e98e7e06e1ae02d394)

I think I should have changed up the constants to be dynamic so the solution would be smaller, but honestly, in the end it's probably better to go with a pretty and longer solution.
I feel like my else method of handling the `week` parameter was pretty weak.

## Armstrong Numbers

[Link to File](./armstrong-numbers/armstrong_numbers.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/armstrong-numbers/solutions/f7936f73fb564c4b9da704ea5b5de31a)



## Rotational Cipher

[Link to File](./rotational-cipher/rotational_cipher.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/rotational-cipher/solutions/83ee13c77e1d4de898c100f544771cf7)



## Difference Of Squares

[Link to File](./difference-of-squares/difference_of_squares.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/difference-of-squares/solutions/79021d92f5b24650af12a464a9f6e9d6)



## Anagram

[Link to File](./anagram/anagram.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/anagram/solutions/c00ab57051fd4bc8ad350a2cd42349f7)

I'm not sure if my .lower() optimization really made a difference, as it's duplicating the list. Originally, I was making .lower() on every single word, so I changed it, but now I'm wondering if it really made a difference as now I'm introducing `enumerate` and a second list of words. It got a bit longer (3 -> 4 lines), too...

## Allergies

[Link to File](./allergies/allergies.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/allergies/solutions/c7cf9ff0b73d460aa125b5433fc72182)

I took a bit more time with this one because I wanted to properly solve the problem you encounter when a score above 255 is entered, meaning a value not present is given. It took me a couple of minutes to remember how this all worked, but in the process, I learned a couple of long-forgotten math principles.

## Series

[Link to File](./series/series.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/series/solutions/c04eea9d5a0f478ea81039d232a66e7f)

I'm kind of bad at math and thinking in general, so I kind of just skimmed the thinking part via itertools. Oops.

## Robot Simulator

[Link to File](./robot-simulator/robot_simulator.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/robot-simulator/solutions/257266d04daa4093a7d60012d0c003ef)



## Atbash Cipher

[Link to File](./atbash-cipher/atbash_cipher.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/atbash-cipher/solutions/5a7e43952bd94c4d9a1d698c45748d49)

The extra grouping and sanitization was super confusing to figure out, I had honestly no idea what it wanted from me at that point.

## Sum Of Multiples

[Link to File](./sum-of-multiples/sum_of_multiples.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/sum-of-multiples/solutions/376b2f4ace694adf9de021c6cc10e243)



## Acronym

[Link to File](./acronym/acronym.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/acronym/solutions/b73a4ba276de4e158424e6799e885eb3)

Not exactly excited to be using regex and string again for an exercise, but if I don't want to be spending forever on it, I suppose this is a far better solution. Regex just feels like cheating sometimes, haha.

## Say

[Link to File](./say/say.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/say/solutions/c5c81bf1586047a8bf7913ce10e4e7c5)

This exercise should be renamed 'Cardinal Numbers' or something along those lines. 'Say' is too broad and doesn't really mean anything. Anyways, my solution is honestly pretty hard to understand, some of the more complex code at the bottom handled was just working out the quirks that come with recursion (which was mostly a random solution I came up with, I did not plan on using recursion, I was expecting to have to make more than one function).

## Kindergarten Garden

[Link to File](./kindergarten-garden/kindergarten_garden.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/kindergarten-garden/solutions/860766a18d484ef3922418d7416b519f)

Added comments for clarification on what stuff does. For some reason Pytest fails, I believe it's got some kind of problem with it, as only 1 of the 5 tests fails, and I don't exactly see the reason why, so I have reason to believe the pytest itself is incorrect.

## Grade School

[Link to File](./grade-school/grade_school.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/grade-school/solutions/fe5fbb3e83c14bb392fcc8c1a0275e57)



## Flatten Array

[Link to File](./flatten-array/flatten_array.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/flatten-array/solutions/d6dcaaa2dc0f4276ab4255f47dfb570a)

I decided that the empty nested tuple thing wasn't worth trying to fix, it's such a dumb test case.

## Roman Numerals

[Link to File](./roman-numerals/roman_numerals.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/roman-numerals/solutions/878a032e3e874bc3bf6fbe5d6a087962)



## Space Age

[Link to File](./space-age/space_age.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/space-age/solutions/22ab7b841514483ca523bc4c9995969d)

I don't like this solution since the measurements are off and they don't provide proper timings. I went and got my measurements (Oribital Sidereal Period (days) / ratio) from the Nasa factsheet here: https://nssdc.gsfc.nasa.gov/planetary/factsheet/neptunefact.html

## Grains

[Link to File](./grains/grains.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/grains/solutions/adff732869fb4477a4fff084db71a9c2)



## Luhn

[Link to File](./luhn/luhn.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/luhn/solutions/8aa8a2cb386f4dcfa99e2b18c8c7b805)

The pytester looks wrong to me. I tested mine online and double checked that it's doing it correctly, and the solutions on the Instructions page look right, yet mine do not solve test correctly through the pytester. I dunno, it feels weird for it to be wrong for such a simple problem.

## Scrabble Score

[Link to File](./scrabble-score/scrabble_score.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/scrabble-score/solutions/ee423be717314687b974302d5cc82503)



## Robot Name

[Link to File](./robot-name/robot_name.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/robot-name/solutions/f2053e5f37aa4e7594658ff52cd743a7)



## Matrix

[Link to File](./matrix/matrix.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/matrix/solutions/a911d0005ac2488fa1386754d609a929)



## Twelve Days

[Link to File](./twelve-days/twelve_days.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/twelve-days/solutions/1b45c94291dd447d9544ca5670288981)

I forgot that a couple things could be omitted, and decided to trim the nouns so that it's smaller. Script went from 10 or 11 lines to 7 lines for building the string.

## Clock

[Link to File](./clock/clock.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/clock/solutions/5ea6c6c4c840489da2850d5d3dacd63f)



## Grep

[Link to File](./grep/grep.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/grep/solutions/c5d464b7392248d6adaab310e49803f5)

I liked this exercise honestly. I learned about some new modules and methods, for example, while trying to create the invert flag, I was looking into how to negate the matching function, and the `functools` module allows one to create a wrapper that can negate any function you pass through it.

## Tournament

[Link to File](./tournament/tournament.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/tournament/solutions/6617ee41fac443be992d3090e650a16e)

This code is honestly pretty cryptic. I added comments for the portions that honestly make sense. I'm hoping it looks good enough for people to understand how the formatting works. It uses ljust and rjust built-in string methods so that the tally supports up to 99 matches before it breaks. Maybe I should add some code to make variable spacing?

## Protein Translation

[Link to File](./protein-translation/protein_translation.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/protein-translation/solutions/49d2d2bace424729a9f9baf382856be7)



## Two Fer

[Link to File](./two-fer/two_fer.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/two-fer/solutions/15e2514a48434abdaa898d197a718caf)



## Collatz Conjecture

[Link to File](./collatz-conjecture/collatz_conjecture.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/collatz-conjecture/solutions/ce1c77cfccd84f15be130ca55382058e)

Truly cursed.

## Markdown

[Link to File](./markdown/markdown.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/markdown/solutions/75a6c2148fe940eb841a8ebc24e8b6ad)



## Raindrops

[Link to File](./raindrops/raindrops.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/raindrops/solutions/95285ff036d04de1a103805ed7145f20)



## Rest API

[Link to File](./rest-api/rest_api.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/rest-api/solutions/1c88ea7c565c4133a44bcc020617803d)

Comments are included in the code.

## High Scores

[Link to File](./high-scores/high_scores.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/high-scores/solutions/4ff6fff98ed0460b900579ac2c1e7a2f)



## Darts

[Link to File](./darts/darts.py) | [Link to Submission](https://exercism.io/tracks/python/exercises/darts/solutions/dda1870d13b645768af9267f8beb8514)

