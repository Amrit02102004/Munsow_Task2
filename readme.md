## API

### Filter Questions Endpoint

This Flask application provides a single endpoint for filtering mock interview questions.

#### Endpoint

- **URL:** `/filter-questions`
- **HTTP Method:** POST
- **Content-Type:** application/json

#### Request Body

The request body should be a JSON object with the following fields:

- `input_filename`: The filename of the JSON file containing the mock interview questions to be filtered.
- `output_filename`: The filename where the filtered questions will be saved.
- `difficulty_level` (optional): The difficulty level of the questions to filter. If provided, only questions with the specified difficulty level will be included in the filtered results.
- `tags` (optional): A list of tags to filter questions by. If provided, only questions that contain at least one of the specified tags will be included in the filtered results.

Example Request Body:
```json
{
  "input_filename": "questions.json",
  "output_filename": "filtered_questions.json",
  "difficulty_level": "Medium",
  "tags": ["Programming", "Python"]
}
```

#### Response

- **Success Response (200 OK):**
  - **Content-Type:** application/json
  - **Body:** A JSON object with a message indicating the success of the operation.
  ```json
  {
    "message": "Filtered questions saved to 'filtered_questions.json'"
  }
  ```

- **Error Responses:**
  - **404 Not Found:** If no questions match the filter criteria.
    - **Content-Type:** application/json
    - **Body:** A JSON object with an error message.
    ```json
    {
      "error": "No questions found matching the filter criteria."
    }
    ```

  - **500 Internal Server Error:** If an error occurs during the processing or saving of the filtered questions.
    - **Content-Type:** application/json
    - **Body:** A JSON object with an error message.
    ```json
    {
      "error": "Failed to save filtered questions to 'filtered_questions.json'"
    }
    ```
Sample request body images:
![Screenshot 2024-04-29 201054](https://github.com/Amrit02102004/Munsow_Task2/assets/114827768/5b5c6e24-0bd7-42c0-a8fe-4c1ddc45f285)
![Screenshot 2024-04-29 201045](https://github.com/Amrit02102004/Munsow_Task2/assets/114827768/b8f26a49-2fae-4fb8-b355-8f1f2fe332bb)


