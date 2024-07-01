// Sample array of users (replace this with your actual data)
const users = [
    { id: 1, name: "STUDENT" },
    { id: 2, name: "ADMIN" },
    { id: 3, name: "TUTOR" }
];

// Function to display selected user's name
function displaySelectedUserName(userId) {
    const selectedUserContainer = document.getElementById("selectedUser");
    const selectedUser = users.find(user => user.id === userId);
    if (selectedUser) {
        selectedUserContainer.textContent = `Selected User: ${selectedUser.name}`;
    } else {
        selectedUserContainer.textContent = "";
    }
}


displaySelectedUserName(selectedUserId);
