# Created by iberb at 23/01/2021
Feature: GitHub API Validation
  # Enter feature description here

  Scenario: Session management check
    Given I have github auth credentials
    When I hit getRepo API of github
    Then status code response should be 200