def main():
    input_file_path = "data/word_bank.txt"
    output_file_path = "data/wordle_words_six.txt"
    six_letter_word = []

    with open(input_file_path, "r") as f:
        for line in f.readlines():
            word = line.strip()
            if len(word) == 6:
                six_letter_word.append(word)

    with open(output_file_path, "w") as f:
        for word in six_letter_word:
            f.write(word + "\n")

    print(f"Found {len(six_letter_word)} six-letter words")


if __name__ == "__main__":
    main()
