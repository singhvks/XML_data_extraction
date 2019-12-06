# XML_feature_extraction

This provides a fast and easy way to process and extract information from XML server responses

# Introduction

I was presented with a problem where an internal team at my project required some sort of arrangement to get structured information from server responses.
The XML response was very challenging to process manually and required more effort hours.

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
