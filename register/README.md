# Register Machines!

Implemented as detailed in MC Chapter 7(?) or something...

3. Make a file with instructions for your machine! You don't need to count the lines off before the command, since the line number in the file works as the program counter location. If you don't want to reread the chapter for reference, here it is:

A register machine has addressable registers $R_0, R_1, R_2, \ldots$ that you can modify with two commands. Importantly, the first register, $R_0$, works as **program counter**, or **PC**, to tell the machine what instruction in the instruction file to look at in that moment.

|command|form|example|
|-------|----|-------|
|increment| `I {register to increment} {new PC}`| `I 1 2` increments $R_1$ and goes to instruction 2 |
|decrement| `D {register to TRY to decrement} {new PC if possible} {new PC if not possible}` | `D 1 2 3` tries to decrement $R_1$ and go to instruction 2, BUT if $R_1$ is 0 (not decrementable), it will jump to instruction 3|

Refer to the textbook, or me(?) if you have any more questions. **Remember, on the test we will presumably NEED to be able to write programs AND notice that each of these instructions is preceded by a number that is essential the line number... we did away with that here because it's unnecessary but MC is nothing if not OD lol**

4. Name your file something, and save it in the same directory as `main.py`. For the sake of demonstration, we'll go about this as if you just wrote `add.txt`. Importantly, this file must just be a textfile, so write it in notepad if you're on windows, or (i think) also notepad if you're on macos.

You'll run the file by running:

```sh
python main.py {instruction file name}
```

or, for example `python main.py add.txt`.

The program will prompt you with a setup for registers. **IMPORTANT:** the first register you set IS $R_0$, or the PC as we defined earlier. If you want your program to run normally, you should probably set that to $1$.

5. Check your calculations! This is only useful if you're trying to work out problems by yourself and using this to verify your work.

## Other Considerations

If you ever need to read this, consider that you might be doing too much for this method. I'm keeping track of all of this because I'm inordinately passionate about theoretical computer science, and you really don't need to be... BUT if you have the energy or capacity to mess around with this please consider theoretical CS classes because it does get SO much cooler than this:

The script has two constant variables, the ones in all CAPS, that limit what this program can do. That is to say that I don't want y'all's computers to blow up, or for us to not catch an error with your program or code that might make it work infinitely (i haven't solved the halting problem but you should tell me if you do). Those variables are ITER_LIMIT and OVERFLOW_LIMIT, which do what they sound like. ITER limits the amount of times the program can apply instructions. OVERFLOW limits the amount of registers you can address. I think the ones I set are MORE than reasonable limits, and most programs converge within a second (i write good code like that), and I'd rather someone set them larger if they want to rather than setting them high earlier. If you do need to change these variables, first check if your program is actually like... really working... there's no reasonable reason that you should be changing it. BUT if you actually are reasonably changing it (which is probably for a cool reason) reach out to me if your program works.

