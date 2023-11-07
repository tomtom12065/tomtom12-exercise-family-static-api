
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {
                "id": self._generateId(),
                "first_name": "John",
                "age": 33,
                "lucky_numbers": [7,13,22],
                
            },{
                "id": self._generateId(),
                "first_name": "Jane",
                "age": 35,
                "lucky_numbers": [10,14,3]
            },
            {
                "id": self._generateId(),
                "first_name": "Jimmy",
                "age": 5,
                "lucky_numbers": [1]
            }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        self._members.append(member)
        return True

    def delete_member(self, id):
        for i in range(len(self._members)):
            # self.members[i] standard for loop ["id"] to choose a specific id
            if self._members[i]["id"] == id:
                self._members.pop(i)  # pop removes from the inde
                return True

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member

    # this method is done, it returns a list with all the family members

    def get_all_members(self):
        return self._members
