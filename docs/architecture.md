# System Architecture

```text
                    USER
                      |
                      v
          +-----------------------+
          | Streamlit Dashboard   |
          |       app.py          |
          +-----------+-----------+
                      |
                      | HTTP Request
                      v
          +-----------------------+
          | FastAPI Backend       |
          |     backend/main.py   |
          +-----------+-----------+
                      |
                      v
              +---------------+
              | Risk Engine   |
              +-------+-------+
                      |
        +-------------+-------------+
        |             |             |
        v             v             v
   Sender         Content          URL
   Analyzer       Analyzer       Analyzer
        |             |             |
        +-------------+-------------+
                      |
                      v
              Attachment Analyzer
                      |
                      v
              Rule-Based Score
                      |
                      +-------------+
                                    |
                                    v
                          Machine Learning
                              Prediction
                                    |
                                    v
                         Combined Risk Score
                                    |
                                    v
                            Analysis Result
                                    |
                                    v
                         Streamlit Dashboard