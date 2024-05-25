
import pandas as pd
import string
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud


# Load the dataset
reviews_df = pd.read_excel('user_review.xls')


# Define a function for basic text preprocessing
def preprocess_text(text):
    # Lowercase the text
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

# 
# Apply the preprocessing function to the 'review' column
reviews_df['review'] = reviews_df['review'].apply(preprocess_text)




# Define a function to get the sentiment of a review
def get_sentiment(review):
    analysis = TextBlob(review)
    # Classify the sentiment
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity < 0:
        return 'negative'
    else:
        return 'neutral'


# Apply the function to the 'review' column
reviews_df['sentiment'] = reviews_df['review'].apply(get_sentiment)
output_file = 'user_reviews_with_sentiment.xlsx'
reviews_df.to_excel(output_file, index=False)
# Count the number of each sentiment
sentiment_counts = reviews_df['sentiment'].value_counts()


# Plot the distribution of sentiments
plt.figure(figsize=(8, 6))
sentiment_counts.plot(kind='bar', color=['green', 'red', 'blue'])
plt.title('Distribution of Sentiments')
plt.xlabel('Sentiment')
plt.ylabel('Number of Reviews')
plt.xticks(rotation=0)
plt.show()

# 
# Plot 1: Pie Chart of Sentiment Distribution
plt.figure(figsize=(8, 6))
sentiment_counts.plot(kind='pie', autopct='%1.1f', colors=['green', 'red', 'blue'])
plt.title('Proportion of Sentiments')
plt.ylabel('')
plt.show()



# 
# Function to generate word cloud
def generate_wordcloud(text, title):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title)
    plt.show()


# Plot 2: Word Cloud of Positive Reviews
positive_reviews = ' '.join(reviews_df[reviews_df['sentiment'] == 'positive']['review'])
generate_wordcloud(positive_reviews, 'Word Cloud of Positive Reviews')

# Plot 3: Word Cloud of Negative Reviews
negative_reviews = ' '.join(reviews_df[reviews_df['sentiment'] == 'negative']['review'])
generate_wordcloud(negative_reviews, 'Word Cloud of Negative Reviews')


