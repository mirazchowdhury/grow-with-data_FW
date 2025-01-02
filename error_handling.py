import requests


def get_example():
    """
    Demonstrates a simple GET request using the `requests` library.
    Fetches a list of posts from a public API and prints the titles of all posts.
    Includes error handling for connection errors and timeouts.
    """
    url = 'https://jsonplaceholder.typicode.com/posts'
    try:
        response = requests.get(url, timeout=5)  # Timeout set to 5 seconds

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
            print(f"Failed to retrieve data. HTTP Status Code: {response.status_code}")

    except requests.exceptions.Timeout:
        print("Error: The request timed out.")
    except requests.exceptions.ConnectionError:
        print("Error: A connection error occurred.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


def post_example():
    """
    Demonstrates a simple POST request using the `requests` library.
    Sends JSON data to a public API and prints the response.
    Includes error handling for connection errors and timeouts.
    """
    url = 'https://jsonplaceholder.typicode.com/posts'
    data = {
        'title': 'foo',
        'body': 'bar',
        'userId': 10
    }
    try:
        response = requests.post(url, json=data, timeout=5)  # Timeout set to 5 seconds

        # Check if the request was successful
        if response.status_code == 201:
            print("POST request successful!")
            # Print response content
            print(response.json())
        else:
            print(f"Failed to post data. HTTP Status Code: {response.status_code}")

    except requests.exceptions.Timeout:
        print("Error: The request timed out.")
    except requests.exceptions.ConnectionError:
        print("Error: A connection error occurred.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


def main():
    """
    Main function to execute the examples.
    """
    print("Executing GET example...")
    get_example()
    print("\nExecuting POST example...")
    post_example()


if __name__ == "__main__":
    main()
