# Created by iberb at 16/01/2021
Feature: Verify if books are added or deleted using API Library
  # Enter feature description here
  @library
  Scenario: Verify AddBook API Functionality
    Given the book details which needs to be added to Library
    When we execute the AddBook PostAPI method
    Then Book is successfully added
    And status code response should be 200
  @library
  Scenario Outline: Verify AddBook API Functionality
    Given Book details <isbn> and <aisle>
    When we execute the AddBook PostAPI method
    Then Book is successfully added
      Examples:
        |isbn    |  aisle |
        | lesson | 3131   |
        | access | 1381   |