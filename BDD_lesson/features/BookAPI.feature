# Created by iberb at 16/01/2021
Feature: Verify if books are added or deleted using API Library
  # Enter feature description here

  Scenario: Verify AddBook API Functionality
    Given the book details which needs to be added to Library
    When we execute the AddBook PostAPI method
    Then Book is successfully added

  Scenario Outline: Verify AddBook API Functionality
    Given Book details with <isbn> and <aisle>
    When we execute the AddBook PostAPI method
    Then Book is successfully added
      Examples:
        | isbn | aisle |
        | fdfee| 8948  |
        | power| 7633  |