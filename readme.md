Introduction
=
This is a website which uses flask to run python and javascript both, its main purpose is to teach you french's pronunciation.


To Run the project,
=
 - run, python3 app.py (running it the first time will take time as it will download the wav2vec2 speech-to-phoneme model  in listen.py)
 - (it has only been tested on macos, it technically should run on windows/linux but idk)
Requirements,
=
- Download imports from requirements.txt
- Download a local llm model (must be ollama)
- Change the version of local llm set in config.py to yours(by default it is llama3.1:8b)

What is it?
=
- when you run app.py,
- you get a website in terminal,
- opening that website you get options,
- clicking generates, generates your sentence
- clicking listen, makes it speak out loud
- clicking record, records you attempting to say that sentence
- after your attempt you get a result with wrong pronounced words as red and righly pronunced as green


INCONSISTENCIES!
= 
- it a very real possibilty for this code to flag different accents which are considered to be right pronunciation as wrong pronunciation so beaware it is a fairly inconsistent code which needs more improvement to be helpfull for real students as for the same word many phonemes could be considered as correct in different accent and it only ignores  common incosistencies rather than most of them.

AI USED?
=
AI has been used in the following ways,

- The Levenshtein code in compare.py has been assissted by ai, no agent has been used in the entirety of this project but that specific code has been assissted but the idea was original and the I did specifically learn the method from youtube while only the code itself was assissted as it was just taking too much time.
- Ai has been used to learn way of shortcut functions, shortcut for the loops, and for the if else shortcut of the red and green of the result throughout the code
- Ai has been used in the setup of flask's basic code.
- Ai has been used in javascript, the asking for permission and adding errors which may occur 
- Ai has helped in making or telling of the specific codes to achieve specific css advancements.(keep in mind it has NOT been used to generate the idea or ask for its advice only for the ways to achieve a certain task)

I would like to add even though the above part of the code has been assissted by AI, the idea was original and AI has only either corrected an error ,taught the method or in very specific cases only wrote the codes for the for example levenshtien mentioned explicitly.









