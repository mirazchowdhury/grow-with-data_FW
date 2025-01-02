import requests


def get_example():
    """
    Demonstrates a simple GET request using the `requests` library.
    Fetches a list of posts from a public API and prints the titles of all posts.
    """
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        print("GET request successful!")
        # Parse response content as JSON
        posts = response.json()

        # Print the titles of all posts
        print("Titles of all posts:")
        for post in posts:
            print(f"Post ID {post['id']}: {post['title']}")
    else:
        print("Failed to retrieve data")


def post_example():
    """
    Demonstrates a simple POST request using the `requests` library.
    Sends JSON data to a public API and prints the response.
    """
    url = 'https://jsonplaceholder.typicode.com/posts'
    data = {
        'title': 'foo',
        'body': 'bar',
        'userId': 10
    }
    response = requests.post(url, json=data)

    # Check if the request was successful
    if response.status_code == 201:
        print("POST request successful!")
        # Print response content
        print(response.json())
    else:
        print("Failed to post data")


def main():
    """
    Main function to execute the examples.
    """
    print("Executing GET example...")
    get_example()
   # print("\nExecuting POST example...")
   # post_example()


if __name__ == "__main__":
    main()
