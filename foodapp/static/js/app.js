//1. Department Name
//2. Subject Name
//3. Subject Code
//4. Name of Faculty
//5. Last date of submission
//Assignment Deatils
//1. Assignment No.
//2. No. of Sets
//3. Question

const dptName = document.querySelector('#dptName');
const subjectName = document.querySelector('#subjectName');
const subjectCode = document.querySelector('#subjectCode');
const facultyName = document.querySelector('#facultyName');
const lastDateOfSubmission = document.querySelector('#lastDateOfSubmission');
const AssignmentNo = document.querySelector('#AssignmentNo');
const numberOfSets = document.querySelector('#numberOfSets');
const QuestionOne = document.querySelector('#QuestionOne');
const QuestionTwo = document.querySelector('#QuestionTwo');
const set = document.querySelector('#set');
const submit = document.querySelector('#save');



function Set(data) {
  set.insertAdjacentHTML("beforeend", `
  <h6 class="text-capitalize text-center">Set-${data.setNumber}</h6>
        <h6 class="text-capitalize text-center">(Roll no. 1-15 and roll no. 62-78)</h6>
        <div class="d-flex flex-column bd-highlight mb-3 text-center">
          <div class="p-2 bd-highlight">1. ${data.QuestionOne} </div>
          <div class="p-2 bd-highlight">2. ${data.QuestionTwo} </div>
        </div>
  `);
}



function appendComment (event) {

  const data = {
    avatar: "user.jpg",
    comment: commentInput.value,
    author: "pradeepBhardwaj"
  };

  event.preventDefault();
  // If the value is nothing just return
  if (commentInput.value.length < 1) return;

  // Insert new template into DOM
  template(data);

  // Reset textrea value
  commentInput.value = "";

  // Save the list to localStorage
  localStorage.setItem('commentListing', commentList.innerHTML);
}



submit.addEventListener('click', appendComment, false)

// Check for saved wishlist items
const saved = localStorage.getItem('commentListing');

// If there are any saved items, update our list
if (saved) {
	commentList.innerHTML = saved;
}


