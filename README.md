# hack-the-talk-exotel
This is a skeleton repository indicating the directory structure for the code submission.

Refer to the challenge here - https://www.hackerearth.com/sprints/hack-the-talk/

### Rules for Submission

The submission must be in a tar.gz format. It should have a run.sh in the top
directory that will take care of compilation, creating the executable and
running your code. Your code must read an input file - input.txt.
The Input File will have a list of audio files like:

 - one.mp3
 - two.mp3
 - three.mp3
 - four.mp3... and So on.

These files one.mp3, two.mp3 etc will be files in the current directory. Your program would need to output the emotion detected for each file (one.mp3, two.mp3 etc) as happy, unhappy, angry, or neutral in separate lines:

happy  
unhappy  
neutral  
neutral  

The above output means one.mp3 was a "happy" conversation, two.mp3 was a "unhappy" conversation etc.


### Trainig dataset

This repo also contains the training data in training_dataset directoy.
