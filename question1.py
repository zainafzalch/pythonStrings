# Task 1: Keyword Highlighter

# Write a program that searches through reviews list and looks for keywords such as "good", "excellent", "bad", "poor", and "average". We want you to capitalize those keywords then print out each review. Print out each review with the keywords in uppercase so they stand out.

#     reviews = [
#         "This product is really good. I'm impressed with its quality.",
#         "The performance of this product is excellent. Highly recommended!",
#         "I had a bad experience with this product. It didn't meet my expectations.",
#         "Poor quality product. Wouldn't recommend it to anyone.",
#         "The product was average. Nothing extraordinary about it."
#     ]

# So for the first string in the reviews list, we want it to say: "This product is really GOOD. I'm impressed with its quality."

reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

keywords = ["good", "excellent", "bad", "poor", "average"]

for review in reviews:
    for keyword in keywords:
        if keyword.lower() in review.lower():
            review_capitilized = review.replace(keyword, keyword.upper())
            print(review_capitilized)

# Task 2: Sentiment Tally

# Develop a function that tallies the number of positive and negative words in each review.  The function should return the total count of positive and negative words.

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]



def pos_neg_word_count(positive_words, negative_words):

    positive_word_count = 0
    negative_word_count = 0
   
    for review in reviews:
        for positive_word in positive_words:
            if positive_word.lower() in review.lower():
                positive_word_count += 1

        for negative_word in negative_words:
            if negative_word.lower() in review.lower():
                negative_word_count += 1

    print("Positive word count: " + str(positive_word_count))
    print("Negative word count: " + str(negative_word_count))

pos_neg_word_count(positive_words, negative_words)

# Task 3: Review Summary

# Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. Ensure that the summary does not cut off in the middle of a word.

# Example: "This product is really good. I'm...",

def review_summary(review):
    if len(review) <= 30:
        return review + "..."
    else:
        words = review.split()
        if len(" ".join(words[:30])) <= 30:
            return " ".join(words[:30]) + "..."
        else:
            return " ".join(words[:30 - 3]) + "..."

for review in reviews:
    print(review_summary(review))