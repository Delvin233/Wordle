# Wordle – A Python Implementation

A simple implementation of the popular Wordle game written in Python.

---

## How to Play

1. Clone this repository.  
2. Navigate into the `Wordle` directory.  
3. (Optional) Review the codebase.  
4. Run `play_wordle_x.py` to start the game.  

---

## Customization Options

### Change Word Length

You can modify the game to use words of a different length.

1. Navigate to the `data` directory.  
2. Open `six_letter_words.py`.  
3. Rename the output file to match your desired word length (recommended for clarity).  
4. Update the filtering logic:

```python
with open(input_file_path, "r") as f:
    for line in f.readlines():
        word = line.strip()
        if len(word) == <desired_word_length>:
            six_letter_word.append(word)
````

5. In `wordle_x.py`, update:

   * `WORD_LENGTH` to your desired word length.
   * `MAX_ATTEMPTS` if you would like to increase or decrease the number of guesses.

---

## Notes

* `word_bank.txt` contains words ranging from 5 to 8 letters.
* Ensure all related configurations match your chosen word length to avoid errors.

