# XML_feature_extraction

This provides a fast and easy way to process and extract information from XML server responses. The data collected in this section can be used as a starting point for predicting that customers stay with the company for insurance. We can also predict the most likely addons that a new customer would take.

# Introduction

Working with XML responses can be very challenging sometimes especially if the data is not structured properly. This solution works for specific data that I was using. You can use this approach to read data from XMLs in a directory and create results in CSV format. The tabular output makes sense and is more readable.

# Requirements

1. Fast solution as hundreds of XMLs were to be used for analysis
2. Offline running method required - ruling out need for any web app solution
3. Each response should be uniquely identified in the output
4. Solution should simple so that anybody can execute
5. Shouldn't require any installation - run without admin rights
6. Should be executable from non admin user accounts
7. There are only two possible types of XML responses from server
8. Solution should get all XML and produce output likewise from them

# Solution

- Reading input files directly from the Solution Directory
- Reading data from XML using ElementTree Package
- Iterating over the XMLs present in the directory to fetch input
- Sending data to CSV file with Policy Number and DataTime Stamp (unique values)
- Making portable executable using Pyinstaller Module

# Limitation
- Prone to failure if the server response structure changes
- Cannot share data as it is confidential

# Improvement Points

- Can use tree traversal for searching the nodes (computation intensive)
- Using tree structure can prevent errors that might come up due to server response structure change

# CONCLUSION

- I am able to achieve all the objectives for this project
- A better version could be using tree traversal which I might work on I future
