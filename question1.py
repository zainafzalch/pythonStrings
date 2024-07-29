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

review_to_summarize = "This product is really good. I'm impressed with its quality."

def summary(full_review):
    if len(full_review) <= 30:
        new_string = full_review[:-1]
        if full_review.endswith("."):
            return new_string.rstrip() + "..."
        return full_review.rstrip() + "..."
    else:
        if full_review[:30 + 1].isspace():
            return full_review[:30].rstrip() + "..."
        else:
            words = full_review.split()
            joining_words = "" 
            for word in words:
                if len(joining_words) <= 30:
                    joining_words = joining_words + " " + "".join(word)
            return joining_words + "..."
                     
print(summary(review_to_summarize))