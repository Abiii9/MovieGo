Feature: editing product in basket

Scenario: deleting a product  added in basket
    Given we want to delete the product in basket
    When we click on delete
    Then we can see the product removed from the basket